from pathlib import Path
import copy
import importlib.util
import json
import re
import sys
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
spec = importlib.util.spec_from_file_location('builder', ROOT / 'tools/build-site.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)
from scenario import authoring_example


class CatalogContracts(unittest.TestCase):
    def setUp(self):
        self.catalog, self.content = authoring_example(builder)

    def test_no_legacy_overwrite(self):
        self.catalog['lessons'][0]['output'] = 'materials/week-01/concepts.html'
        with self.assertRaises(ValueError):
            builder.validate_catalog(self.catalog, self.content)

    def test_source_and_output_cannot_escape(self):
        for field, path in [('source', '../secret.md'), ('output', '/index.html'), ('output', 'materials/x/../../index.html')]:
            bad = copy.deepcopy(self.catalog)
            bad['lessons'][0][field] = path
            with self.assertRaises(ValueError):
                builder.validate_catalog(bad, self.content)

    def test_duplicate_outputs_fail(self):
        self.catalog['lessons'][1]['output'] = self.catalog['lessons'][0]['output']
        with self.assertRaises(ValueError):
            builder.validate_catalog(self.catalog, self.content)

    def test_missing_page_and_document_mapping_fail(self):
        self.catalog['documents']['materials/missing.md'] = 'missing.html'
        with self.assertRaises(ValueError):
            builder.validate_catalog(self.catalog, self.content)

    def test_summary_and_review_ids(self):
        source = next(page['source'] for page in self.catalog['lessons'] if page['id'] == 'example-review')
        self.content[source] = ('# 복습\n\n요약: ' + '가' * 201 + '\n\n## Q1. 질문\n').encode()
        with self.assertRaises(ValueError):
            builder.validate_catalog(self.catalog, self.content)
        self.content[source] = '# 복습\n\n요약: 질문을 확인한다.\n\n## Q1. 하나\n\n## Q1. 둘\n'.encode()
        with self.assertRaises(ValueError):
            builder.validate_catalog(self.catalog, self.content)

    def test_invalid_or_missing_translation_pairs_fail(self):
        original = dict(self.catalog['translations'])
        for pairs in ({'index.html': 'en/missing.html'},
                      {'index.html': 'en/index.html', 'materials/week-01/index.html': 'en/index.html'},
                      {}):
            self.catalog['translations'] = pairs
            with self.assertRaises(ValueError):
                builder.validate_catalog(self.catalog, self.content)
        self.catalog['translations'] = original


class IntegratedAuthoring(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog, cls.content = authoring_example(builder)
        cls.payload = builder.make_payload(cls.catalog, cls.content)
        cls.pages = {name: builder.Page(data.decode()) for name, data in cls.payload.items() if name.endswith('.html')}

    def test_complete_site_links_and_anchors(self):
        page_count, link_count = builder.validate_links(self.payload)
        expected = {name for name in self.content if name.endswith('.html')}
        expected.add('index.html')
        expected.add('en/index.html')
        expected.update(page['output'] for page in self.catalog['lessons'])
        self.assertEqual(page_count, len(expected))
        self.assertGreater(link_count, 3471)

    def test_new_pages_in_home_sidebar_and_search(self):
        home = self.payload['index.html'].decode()
        old = self.payload['materials/week-01/concepts.html'].decode()
        self.assertIn('TCP 연결 비용 읽기', home)
        self.assertIn('후속 심화', old)
        for page in self.catalog['lessons']:
            if page['output'].startswith('en/'):
                self.assertNotIn('href="' + page['output'] + '"', home)
            else:
                self.assertIn(page['output'], home)
            self.assertIn('authoring-example', old)
        index = re.search(r'id="study-search-data">([\s\S]*?)</script>', home)[1]
        found = {item['href'] for item in json.loads(index)}
        self.assertTrue({page['output'] for page in self.catalog['lessons'] if not page['output'].startswith('en/')} <= found)
        self.assertFalse(any(path.startswith('en/') for path in found))

    def test_language_switch_keeps_the_corresponding_page(self):
        for ko, en in self.catalog['translations'].items():
            for current, target, lang in ((ko, en, 'en'), (en, ko, 'ko')):
                html = self.payload[current].decode()
                links = re.findall(r'<nav class="study-language"[\s\S]*?</nav>', html)
                self.assertEqual(len(links), 1, current)
                self.assertIn('hreflang="' + lang + '"', links[0])
                path = re.search(r'href="([^"]+)"', links[0])[1]
                self.assertEqual(builder.resolve(current, path), target)
                self.assertIn('<link rel="alternate" hreflang="' + lang + '"', html)
                alternate = re.search(r'<link rel="alternate" hreflang="' + lang + r'" href="([^"]+)"', html)[1]
                self.assertEqual(alternate, builder.SITE_URL + ('' if target == 'index.html' else target))
        fallback = self.payload['materials/week-02/index.html'].decode()
        control = re.search(r'<nav class="study-language"[\s\S]*?</nav>', fallback)[0]
        self.assertIn('English home', control)
        self.assertIn('this page is available in Korean', control)
        self.assertNotIn('en/materials/week-02', control)

    def test_english_search_and_downloads_stay_in_english(self):
        for name, data in self.payload.items():
            if not name.startswith('en/') or not name.endswith('.html'):
                continue
            html = data.decode()
            self.assertIn('<html lang="en">', html)
            self.assertIn('Find learning materials', html)
            index = json.loads(re.search(r'id="study-search-data">([\s\S]*?)</script>', html)[1])
            self.assertTrue(index)
            self.assertTrue(all(builder.resolve(name, item['href']).startswith('en/') for item in index))
            self.assertTrue(all(not re.search('[가-힣]', item['group']) for item in index))
        review = self.payload['en/materials/week-01/review.html'].decode()
        self.assertEqual(review.count('<textarea '), 10)
        self.assertIn('Download my answers (Markdown)', review)
        self.assertIn('download href="REVIEW.md"', review)
        self.assertIn('Write your answer and supporting evidence.', review)
        self.assertNotIn('내 답', review)

    def test_project_links_work_on_both_languages_and_deep_pages(self):
        repo = 'https://github.com/OstenHun/hands-on-computer-networks'
        for name, data in self.payload.items():
            if not name.endswith('.html') or 'http-equiv="refresh"' in data.decode():
                continue
            english = name.startswith('en/')
            nav = re.findall(r'<nav class="study-project-links"[^>]*>[\s\S]*?</nav>', data.decode())
            self.assertEqual(len(nav), 1, name)
            self.assertIn('aria-label="' + ('Project links' if english else '프로젝트 안내') + '"', nav[0])
            for target in ('', '/issues/new/choose', '/blob/main/LICENSE.md',
                           '/blob/main/CONTRIBUTING.md' + ('#english' if english else '')):
                self.assertIn('href="' + repo + target + '"', nav[0], name)
            if english:
                self.assertIn('Report an issue', nav[0])
                self.assertNotRegex(nav[0], '[가-힣]')

    def test_link_rewrite_and_download_are_distinct(self):
        review = self.payload['materials/authoring-example/review.html'].decode()
        self.assertIn('href="concepts.html#rtt"', review)
        self.assertIn('href="answers.html"', review)
        self.assertIn('download href="CONCEPTS.md"', review)
        self.assertIn('&lt;a href="ANSWERS.md"&gt;', review)
        self.assertIn('1~3', review)  # Literal lesson text, not the course count.

    def test_review_fields_tables_and_script(self):
        review = self.payload['materials/authoring-example/review.html'].decode()
        self.assertEqual(review.count('<textarea '), 2)
        self.assertLess(review.index('id="answer-Q2"'), review.index('class="save-bar"'))
        self.assertIn('class="table-scroll"', review)
        self.assertIn('../../assets/lesson-answers.js', review)
        self.assertIn('rtt', self.pages['materials/authoring-example/concepts.html'].ids)

    def test_nested_index_has_final_relative_links(self):
        index = self.payload['materials/authoring-example/index.html'].decode()
        self.assertIn('href="concepts.html"', index)
        self.assertIn('href="review.html"', index)
        self.assertIn('href="../../assets/lesson.css"', index)
        self.assertNotIn('example-index.html', self.payload)

    def test_official_brand_assets_on_deep_pages(self):
        for name in ('index.html', 'materials/week-01/concepts.html', 'materials/week-04/review.html'):
            html = self.payload[name].decode()
            self.assertNotIn('study-logo-mark', html)
            self.assertIn('aria-label="실습으로 배우는 네트워크 학습 홈"', html)
            self.assertEqual(html.count('rel="icon"'), 1)
            self.assertIn('assets/aolda-logo.svg', html)
            self.assertIn('assets/aolda-icon.svg', html)
        for name in ('aolda-logo.svg', 'aolda-icon.svg'):
            original = (ROOT / 'content/assets' / name).read_bytes()
            self.assertEqual(self.payload['assets/' + name], original)

    def test_old_sources_body_scripts_and_styles_unchanged(self):
        baseline = builder.collect_content()
        for name, raw in baseline.items():
            if not name.endswith('.html') or 'http-equiv="refresh"' in raw.decode():
                continue
            output = self.payload[name].decode()
            for tag in ('main', 'style'):
                for element in re.findall(r'<' + tag + r'\b[\s\S]*?</' + tag + '>', raw.decode()):
                    self.assertIn(element, output, name)
            for script in re.findall(r'<script\b[\s\S]*?</script>', raw.decode()):
                self.assertIn(script, output, name)

    def test_public_indexing_and_sitemap(self):
        expected_urls = set()
        for name in self.pages:
            html = self.payload[name].decode()
            if 'http-equiv="refresh"' in html:
                self.assertIn('noindex,nofollow', html)
                continue
            self.assertNotIn('noindex', html, name)
            self.assertNotIn('nofollow', html, name)
            self.assertEqual(html.count('name="robots"'), 1, name)
            url = builder.SITE_URL + ('' if name == 'index.html' else name)
            self.assertEqual(html.count('rel="canonical"'), 1, name)
            self.assertIn('rel="canonical" href="' + url + '"', html, name)
            expected_urls.add(url)
        sitemap = ET.fromstring(self.payload['sitemap.xml'])
        locations = [node.text for node in sitemap.findall('{*}url/{*}loc')]
        self.assertEqual(len(locations), len(set(locations)))
        self.assertEqual(set(locations), expected_urls)

    def test_missing_link_and_anchor_fail(self):
        for link in ('missing.html', 'concepts.html#missing-anchor'):
            bad = dict(self.payload)
            bad['materials/authoring-example/check.html'] = ('<a href="' + link + '">check</a>').encode()
            with self.assertRaises(ValueError):
                builder.validate_links(bad)


if __name__ == '__main__':
    unittest.main()
