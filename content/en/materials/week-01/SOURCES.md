# Week 1 sources and reading

Summary: Read selected port and HTTP sections for ten minutes within the concept session. Other sources are optional; distinguish introductory explanations, official verification and your own lab evidence.

## Required reading — ten minutes within the 30-minute concept session

Use the [concepts](CONCEPTS.md) alongside the [reading guide](ARTICLE_LESSON.md). The guide maps roadmap terms to selected original sections and experiment questions. You do not need to read every external article or complete every external assignment.

| Source | Selected part | Time and question |
| --- | --- | --- |
| [Cloudflare: computer ports](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/) | Opening definition and port-number explanation | Five minutes: distinguish endpoints at one IP; default 80 versus this kit's 8080 |
| [AWS: HTTP and HTTPS](https://aws.amazon.com/compare/the-difference-between-https-and-http/) | Request, response and status in “How does HTTP protocol work?” | Five minutes: evidence for 404 versus connection failure; omit form-method examples and TLS details |

Calling an external assignment's website or changing browser settings is not required. This kit uses curl HTTP/1.1 on Linux `lo`; do not copy browser cache, VPN or QUIC preparation from unrelated exercises.

## Optional reading

| Source | Selected scope | Suggested use |
| --- | --- | --- |
| [Network Engineer Roadmap](https://roadmap.sh/network-engineer) | Eleven terms in the [reading guide](ARTICLE_LESSON.md#roadmap-terms-and-original-articles) | Read only what helps with a blocked concept |
| [Kurose/Ross HTTP lab v9.0](https://www-net.cs.umass.edu/wireshark-labs/Wireshark_HTTP_v9.0.pdf) | Section 1, printed pages 2–3 | Five minutes: locate version and status |
| [Wireshark Follow Stream](https://www.wireshark.org/docs/wsug_html_chunked/ChAdvFollowStreamSection.html) | Introduction and TCP Stream view | Five minutes: read both directions of one stream |
| [Kurose/Ross introduction v9.0](https://www-net.cs.umass.edu/wireshark-labs/Wireshark_Intro_v9.0.pdf) | Printed pages 5–6 on list, details, bytes and filters | Ten minutes for a first Wireshark session |
| [curl manual](https://curl.se/docs/manpage.html) | verbose, noproxy, http1.1, max-time, exit codes | Ten minutes: command options and status versus exit code |
| [Python http.server](https://docs.python.org/3/library/http.server.html) | BaseHTTPRequestHandler, protocol_version, send_response, send_header | Ten minutes: response construction |
| [Node TypeScript](https://nodejs.org/api/typescript.html) | Type stripping | Five minutes, optional client; check the installed version first |

[CCNA practice (Korean)](../../../materials/week-01/ccna-practice.html) identifies optional linked questions and their provenance. External questions stay at their original sources.

## Official checks for facilitators

- [RFC 9110 §15.3.1](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.3.1) and [§15.5.5](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.5.5): 200/404 semantics versus this kit's route branch, about five minutes.
- [tcpdump's official manual source](https://raw.githubusercontent.com/the-tcpdump-group/tcpdump/master/tcpdump.1.in): `-i`, `-nn`, `-s`, `-w`, filters and termination, about ten minutes. The original guide used this repository source when the rendered official manual could not be fetched. Check installed `man tcpdump` and local privileges separately.
- [Wireshark Flow Graph](https://www.wireshark.org/docs/wsug_html_chunked/ChStatFlowGraph.html): direction and time, about five minutes.
- [Full reference guide (Korean)](../../../materials/REFERENCE_GUIDE.md): roles of references across the 16-week course.

## Attribution and reuse

External sources are linked rather than reproduced at length. Sources whose bodies were not verified are identified in the [reading guide](ARTICLE_LESSON.md).

Kurose/Ross Wireshark Labs © 2005–2025 J. F. Kurose and K. W. Ross. Follow the [authors' attribution guidance](https://gaia.cs.umass.edu/kurose_ross/wireshark.php); publishing adaptations requires the original copyright and adaptation notice. This kit's code, diagrams, authored questions and explanations did not use external instructor solutions. The supplied pcap is the project's own earlier Windows development capture.

The [essentials](ESSENTIALS.md) and developer scenarios connect the kit's concepts with sources; they are authored study questions, not verified company interview questions or frequency claims. [Developer reference notes (Korean)](../../../materials/week-01/interview-references.html) give further selection context.
