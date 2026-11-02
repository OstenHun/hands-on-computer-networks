# 기여 안내 · Contributing

요약: 오타·내용 오류·실습 문제·번역 개선을 이슈나 PR로 제안할 수 있다. 작은 범위로 수정하고 관련 원문·화면·출처를 확인한다. 한국어와 영어 제안을 모두 받는다.

[English guide](#english) · [이슈 작성](https://github.com/OstenHun/hands-on-computer-networks/issues/new/choose) · [학습 사이트](https://ostenhun.github.io/hands-on-computer-networks/)

## 오류나 개선점 알리기

비슷한 [이슈](https://github.com/OstenHun/hands-on-computer-networks/issues)가 있는지 살핀 뒤 **내용 오류**, **실습 문제**, **개선 제안** 중 하나를 선택한다. 페이지 URL·절 제목, 기대한 내용과 실제 내용을 적으면 확인하기 쉽다. 개념 오류는 공식 출처를, 실습 문제는 실행 위치·명령·오류를 함께 남긴다. 아직 원인을 몰라도 제보할 수 있다.

이슈와 PR은 공개된다. 비밀번호·키·토큰, 실제 접속 주소, 참가자 정보와 가리지 않은 로그·스크린샷을 올리지 않는다. 주소는 `192.0.2.10` 같은 문서용 예시로 바꾼다.

## 작은 수정 보내기

저장소를 fork하고 작업 브랜치에서 수정한 뒤 `main`을 대상으로 PR을 연다. 오타·링크 수정은 바로 제안해도 된다. 새 주차·실습, 학습 범위나 구조 변경은 먼저 이슈에서 목적과 범위를 논의한다.

| 수정할 내용 | 시작할 위치 |
| --- | --- |
| 교재·문제·해설 | `content/materials/`, 영어판은 `content/en/materials/` |
| 실습 코드와 실행 안내 | 해당 주차 교재 또는 `content/labs/` |
| 홈의 주차 소개·메뉴·새 교재 등록 | `config/site.json` |
| 공통 탐색·디자인·동작 | `tools/study_site_theme.py`, `tools/study-site.css`, `tools/study-site.js` |

새 교재는 Markdown으로 작성한다. 기존 수동 HTML 교재는 대응 Markdown과 함께 수정한다. 어느 파일인지 모르면 페이지 URL을 이슈에 남겨도 된다. `dist/`와 `.astro-input/`·`.astro-output/`은 생성물이므로 직접 수정하거나 커밋하지 않는다. 자세한 작성 규칙과 원문 대응은 [교재 작성 안내](docs/AUTHORING.md)를 따른다.

## 로컬에서 확인하기

Python 3.12 이상과 Node.js 22.22 이상이 필요하다. CI는 Node.js 24를 사용한다. 저장소 루트에서 실행한다.

```sh
npm ci --ignore-scripts
npm test
npm run build
python -m http.server 8000 --directory dist
```

[로컬 미리보기](http://localhost:8000)에서 변경한 페이지와 관련 링크를 연다. 화면 변경은 데스크톱·모바일에서 줄바꿈·잘림·키보드 조작을 확인한다. 실습은 실행 조건과 예상·실제 결과를 구별하고, 실행하지 못한 환경은 PR에 밝힌다.

PR에는 **무엇이 잘못됐는지**, **어떻게 바꿨는지**, **무엇을 확인했는지**를 짧게 적는다. 출처·필수/선택 구분·예제와 실제 관찰의 차이를 보존한다. 번역에서는 원문의 조건·수치·명령·출처와 대응 링크를 대조한다. 배포·복구 기준은 [운영 안내](docs/OPERATIONS.md)를 따른다.

## 라이선스와 외부 자료

기여한 교재에는 CC BY 4.0, 코드에는 MIT가 적용된다. 본인이 이용 허락할 수 있는 내용만 제안하고 외부 코드·그림·인용은 출처와 원래 이용 조건을 명시한다. 로고·외부 자료의 예외와 전문은 [라이선스 안내](LICENSE.md)를 확인한다.

## English

Issues and PRs are welcome in Korean or English. Report a typo, unclear explanation, broken link or lab problem through the [issue chooser](https://github.com/OstenHun/hands-on-computer-networks/issues/new/choose). The templates have English prompts alongside Korean. Include the page URL and section, expected and actual behavior, and a source or reproduction steps when available. Keep credentials, real connection details, participant data and unredacted logs out of public reports.

For a small fix, fork the repository, create a branch and open a PR against `main`. Discuss new labs or larger curriculum changes in an issue first. Lessons are in `content/materials/`, translations in `content/en/materials/`, and lab files in the relevant lesson folder or `content/labs/`. New lessons use Markdown; existing hand-written HTML pages have matching Markdown that must be kept in sync. Never edit generated `dist/`, `.astro-input/` or `.astro-output/` files.

### Local development

Use Python 3.12+ and Node.js 22.22+ (CI uses Node.js 24). From the repository root, run:

```sh
npm ci --ignore-scripts
npm test
npm run build
python -m http.server 8000 --directory dist
```

Preview at [localhost:8000](http://localhost:8000). Check affected links and, for UI changes, desktop/mobile layout and keyboard access. Explain the problem, change and validation in your PR; name environments you could not test. Preserve technical conditions, source attribution, required/optional scope and the distinction between examples and direct observations. Detailed [authoring](docs/AUTHORING.md) and [operations](docs/OPERATIONS.md) guides are in Korean.

Contribute only material you can license under the applicable [content/code terms](LICENSE.md). Identify third-party sources and their original licenses; brand assets remain excluded.
