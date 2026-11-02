# 실습으로 배우는 네트워크

요약: 개념을 읽고 Linux·패킷·로그로 확인하는 컴퓨터 네트워크 공개 학습 자료다. 기초 원리부터 클라우드 네트워크·장애 진단까지, 혼자 또는 스터디에서 공부할 수 있다.

**[학습 시작하기](https://ostenhun.github.io/hands-on-computer-networks/)** · [English](README.en.md) · [오류 제보·제안](https://github.com/OstenHun/hands-on-computer-networks/issues/new/choose) · [기여 안내](CONTRIBUTING.md)

“IP가 비슷하면 같은 망일까?”, “경로가 있는데 왜 접속이 막힐까?” 같은 질문에서 시작한다. 먼저 예상하고, 직접 실행한 출력과 패킷을 읽고, 조건 하나를 바꿔 설명을 확인한다.

네트워크를 처음 배우는 학생, 통신 문제를 이해하고 싶은 개발자, 각자 실험한 근거를 비교하는 스터디를 위한 자료다. 아주대학교 클라우드 운영 소학회 [아올다](https://www.aoldacloud.com/)의 4기 네트워크 스터디에서 시작했다.

## 시작하기

1. **처음 공부한다면:** [VM·SSH 준비](https://ostenhun.github.io/hands-on-computer-networks/materials/ssh-top-down/index.html)를 읽고 [1주차: 요청 하나 따라가기](https://ostenhun.github.io/hands-on-computer-networks/materials/week-01/index.html)에서 시작한다. 직접 실습에는 본인이 사용할 수 있는 Linux 환경이 필요하다.
2. **특정 개념을 찾는다면:** [전체 개념 색인](https://ostenhun.github.io/hands-on-computer-networks/materials/week-01/concept-index.html)이나 사이트의 **자료 검색**을 사용한다.
3. **영어로 읽는다면:** [English learning site](https://ostenhun.github.io/hands-on-computer-networks/en/)로 이동한다. 홈과 1주차 기본 교재를 제공하며, 2~16주차와 일부 선택 자료는 한국어로 제공한다.

## 무엇을 배우나

| 과정 | 다루는 내용 |
| --- | --- |
| [1~4주: 요청과 전달](https://ostenhun.github.io/hands-on-computer-networks/materials/week-01/index.html) | 요청·응답, IPv4·서브넷, LAN·ARP, TCP·UDP |
| [5~8주: 응용과 경로](https://ostenhun.github.io/hands-on-computer-networks/materials/week-05/index.html) | DNS·DHCP, HTTP·TLS·SSH, 정적 경로, 중간 진단·IPv6 |
| [9~12주: 망의 구성과 정책](https://ostenhun.github.io/hands-on-computer-networks/materials/week-09/index.html) | VLAN·STP·LACP, OSPF, NAT·접근 정책, 무선·VPN |
| [13~16주: 운영과 장애 진단](https://ostenhun.github.io/hands-on-computer-networks/materials/week-13/index.html) | 클라우드 네트워크, 성능·트래픽 분산, 소켓·자동화, 종합 진단 |

주차별 교재·공식 출처, Linux 실습 코드, 브라우저 실습 모형, 복습 문제와 분리 해설을 제공한다. 모형·제공 캡처 분석과 직접 실습을 구분하고, 필수·선택 범위는 각 실습 안내에서 확인한다.

혼자 예상·실행·관찰·조건 변경·복구를 시도한 뒤 자기 말로 설명한다. 스터디에서는 각자의 근거와 막힌 이유를 비교한다. 자세한 방법은 [학습 안내](https://ostenhun.github.io/hands-on-computer-networks/materials/week-01/concept-index.html#personal-study)를 따른다. 복습 답안은 서버에 제출하거나 자동 저장하지 않으므로, 페이지를 떠나기 전에 Markdown으로 내려받는다.

## 함께 개선하기

오타, 설명이 모호한 부분, 끊어진 링크, 실습 오류를 알려 주는 것도 기여다. [이슈 유형을 골라 제보](https://github.com/OstenHun/hands-on-computer-networks/issues/new/choose)하거나 작은 수정 PR을 보낼 수 있다. 큰 교재 개편이나 새 실습은 먼저 이슈에서 범위를 논의한다.

[기여 안내](CONTRIBUTING.md)에서 수정할 파일과 확인 방법을 찾을 수 있다. 교재 원문과 실습 코드는 [content/](content/)에 있고, 새 교재는 Markdown으로 작성해 Astro로 생성한다. 로컬 실행은 [기여 안내의 개발 환경](CONTRIBUTING.md#로컬에서-확인하기), 세부 절차는 [교재 작성 안내](docs/AUTHORING.md)와 [사이트 운영 안내](docs/OPERATIONS.md)를 참고한다.

## 라이선스

교재·문서는 [CC BY 4.0](LICENSES/CC-BY-4.0.txt), 실습·사이트 코드는 [MIT](LICENSES/MIT.txt)로 제공한다. 아올다 로고·아이콘과 외부 인용·의존성은 제외한다. 재사용할 때는 [적용 범위와 출처 표시 예시](LICENSE.md)를 확인한다.
