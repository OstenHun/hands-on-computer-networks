"""Shared shell labels and explicit pairs of translated learning pages."""
from html import escape
import posixpath


def page_language(path):
    return 'en' if path.startswith('en/') else 'ko'


def language_links(name, pairs):
    counterpart = pairs.get(name)
    if counterpart is None:
        counterpart = next((ko for ko, en in pairs.items() if en == name), None)
    home = posixpath.relpath('en/index.html', posixpath.dirname(name) or '.')
    if counterpart is None:
        return '<nav class="study-language" aria-label="언어"><span lang="ko" aria-current="true">한국어</span><a lang="en" hreflang="en" href="' + home + '" aria-label="English home; this page is available in Korean">English home</a></nav>'
    other = posixpath.relpath(counterpart, posixpath.dirname(name) or '.')
    language = page_language(name)
    labels = [('ko', '한국어'), ('en', 'English')]
    links = ''.join('<span lang="' + code + '" aria-current="true">' + label + '</span>' if code == language else '<a lang="' + code + '" hreflang="' + code + '" href="' + escape(other, quote=True) + '">' + label + '</a>' for code, label in labels)
    return '<nav class="study-language" aria-label="' + ('Language' if language == 'en' else '언어') + '">' + links + '</nav>'


ENGLISH_UI = {
    '프로젝트 안내': 'Project links',
    '오류 제보': 'Report an issue',
    '기여 안내': 'Contribute',
    '라이선스': 'License',
    '실습으로 배우는 네트워크 학습 홈': 'Hands-on Computer Networks home',
    '실습으로 배우는 네트워크': 'Hands-on Computer Networks',
    '본문으로 건너뛰기': 'Skip to content',
    '공개 학습 자료 찾기': 'Find learning materials',
    '주차나 개념 이름으로 검색': 'Search by week or concept',
    '전체 학습 경로': 'Learning path',
    'VM·SSH 접속 준비': 'VM and SSH preparation',
    '시작하기 전에': 'Before you start',
    '후속 개념 · 본문 일부': 'More concepts',
    '후속 심화': 'Further study',
    '공통 과정': 'Core course',
    '다시 찾아보기': 'Reference',
    '전체 개념 색인': 'Concept index',
    '면접·개발 참고자료': 'Developer references',
    '질문→탐색→설명→확인': 'Ask → explore → explain → test',
    '자료 검색': 'Search',
    '학습 메뉴 열기': 'Expand learning menu',
    '학습 메뉴': 'Menu',
    '학습 홈': 'Learning home',
    '현재 위치': 'Breadcrumb',
    '닫기': 'Close',
    '아주대학교 클라우드 운영 소학회 아올다의 4기 네트워크 스터디에서 시작했습니다.': 'Started in the fourth network study group of Aolda, the cloud operations club at Ajou University.',
}


def english_shell(html):
    for original, translated in ENGLISH_UI.items():
        html = html.replace(original, translated)
    return html
