# Week 1 reading guide — five questions about one request

Summary: Connect Network Engineer Roadmap reading with the Linux HTTP experiment. The specified port and HTTP sections take ten required minutes; the other readings are optional.

## How to use this guide

Use the section that answers your question while reading the [concepts](CONCEPTS.md). Each section identifies original reading, explains the connection and asks what to inspect in the lab. Required external reading is **five minutes for ports in section 3 and five for HTTP in section 5**, included in the 30-minute concept session. Other original articles are optional.

If a source is difficult or unavailable, use the explanation here and do not record the original as read. These explanations, diagrams and questions are authored for the kit, not copies of external articles or instructor solutions. Expected behavior is not a new observed result. Keep your actual evidence once in personal files and use it to explain the [shared question](WORKSHEET.md).

## 1. Must network communication cross the Internet?

Optional, about three minutes: read IBM's opening definition of [computer networking](https://www.ibm.com/think/topics/networking) and MDN's introduction and Internet-versus-web discussion in [How does the Internet work?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/How_does_the_Internet_work). Detailed router, DNS and provider relationships come later.

Networks, the Internet and the web describe different scopes. The web is a service using the Internet; not every networking exchange crosses the Internet. This kit's curl/Python HTTP traffic stays in remote Linux loopback. The PC-to-VM SSH connection is a separate exchange.

**Predict and check:** If your PC loses Internet access, is that the same condition as stopping the Python server? Do not disconnect your actual SSH session to test this; identify the different paths in the diagram and existing evidence.

**Explain:** Draw SSH from PC to VM, then HTTP inside the VM. Compare [concepts 1–2](CONCEPTS.md).

## 2. Are client and server names for machines?

Optional, about three minutes: read the client definition at [TechTarget](https://www.techtarget.com/searchenterprisedesktop/definition/client) and the definition/request-handling discussion at [Splunk](https://www.splunk.com/en_us/blog/learn/computer-servers.html).

A host and a process are different units. The request-initiating process is the client; the responding process is the server in that exchange. A server calling another service can be a client in that second exchange. Both roles can exist on the same machine. Do not build an additional service for this question.

**Predict and check:** Does stopping Python remove the VM? Compare continued shell use with the absence of an HTTP response.

**Explain:** Draw the VM, shells, Python process and curl process. Compare [concepts 2–3](CONCEPTS.md).

## 3. How do we distinguish endpoints at the same IP?

**Required, five minutes:** Read the opening port definition and port-number explanation in [Cloudflare's port article](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/). Memorizing port lists, firewall explanations and ping is outside this reading's scope.

Read IP addresses and TCP ports together. IP headers contain addresses; TCP headers contain source and destination ports. In the illustrative request `127.0.0.1:51000 → 127.0.0.1:8080`, the IP addresses match but ports differ. Find the actual client port in logs/capture and compare the listening server port with `ss -lnt`. Reverse both endpoints for the response.

Port 80 is HTTP's default, not a requirement for all HTTP traffic. This URL explicitly uses 8080. A port number alone does not prove protocol or encryption. Check [RFC 9110 §4.2.1](https://www.rfc-editor.org/rfc/rfc9110.html#section-4.2.1).

**Predict and check:** With the wrong destination port, will the request reach this server's `/echo` branch? Use the existing four-state evidence before adding experiments.

**Explain:** Identify both IP addresses and both ports, labeling client and server. Compare [concepts 4](CONCEPTS.md).

## 4. What do HTTP, TCP and IP each do?

Optional, about five minutes: read the definition in [Cloudflare's protocol article](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-protocol/) and application/transport/network roles in its [OSI article](https://www.cloudflare.com/en-gb/learning/ddos/glossary/open-systems-interconnection-model-osi/). Seven-layer memorization and product material are not required. Compare TCP/IP responsibilities with [RFC 1122 §1.1.3](https://www.rfc-editor.org/rfc/rfc1122.html#section-1.1.3).

| Question | Evidence | Responsibility |
| --- | --- | --- |
| Which path and response? | curl lines; server path/status | HTTP, application |
| Which endpoints exchanged bytes? | TCP source/destination ports | TCP, transport |
| Which addresses? | IP source/destination fields | IP, Internet |
| Where did you observe it? | Capture interface `lo` | Local delivery path in this experiment |

Do not treat `lo` as an external Ethernet observation. This kit's HTTP/1.1 uses TCP; different HTTP versions can use different transports. See [RFC 9110 §2.5](https://www.rfc-editor.org/rfc/rfc9110.html#section-2.5).

**Explain:** After 404, distinguish “the application did not return what I wanted” from “message delivery failed.” Compare logs and [concepts 5](CONCEPTS.md).

## 5. Why is 404 different from connection failure?

**Required, five minutes:** Read the request/response/status explanation in “How does HTTP protocol work?” in [AWS's HTTP/HTTPS comparison](https://aws.amazon.com/compare/the-difference-between-https-and-http/). Certificate/key exchange and HTTP/2/3 details are outside Week 1.

HTTP clients send requests and servers return statuses and data. 200 indicates success under the request's semantics. 404 means the server did not find a current representation for the target or is unwilling to disclose one. This kit's simple `/echo` versus other-path branch illustrates only one implementation. Check [RFC 9110 §15.3.1](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.3.1) and [§15.5.5](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.5.5).

404 is an HTTP response. A refused connection after stop may have no HTTP response. Distinguish that status from the **curl exit code**: the lab does not use `--fail`, so a completed 404 transfer can exit with 0. See the [curl manual](https://curl.se/docs/manpage.html).

**Predict and check:** In each of normal, missing path, stopped and restarted states, inspect the HTTP status line, new server response log and curl exit code separately. Do not replace your observations with the expected table.

**Explain:** Which part of your output refutes “404 means the server is switched off”? Compare [concepts 6–7](CONCEPTS.md).

## Roadmap terms and original articles

The [Network Engineer Roadmap](https://roadmap.sh/network-engineer) is the organizing reference. Links can change. The original Korean reading guide recorded the Temok body as unverified; it was not used as the sole basis for the host explanation.

| Term | Reference | Use here |
| --- | --- | --- |
| Networks | [IBM](https://www.ibm.com/think/topics/networking) | Optional opening definition |
| Internet | [roadmap guide](https://roadmap.sh/guides/what-is-internet), [Cloudflare](https://www.cloudflare.com/en-gb/learning/network-layer/how-does-the-internet-work/), [MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/How_does_the_Internet_work) | MDN selected; others alternatives |
| Client | [TechTarget](https://www.techtarget.com/searchenterprisedesktop/definition/client) | Optional definition, including same-machine roles |
| Server | [Splunk](https://www.splunk.com/en_us/blog/learn/computer-servers.html) | Optional definition/request handling |
| Host | [Temok](https://www.temok.com/blog/what-is-a-host) | Body unverified; use RFC 1122 for the explanation |
| IP address | [Coursera](https://www.coursera.org/articles/ip-address) | Optional supplement; detailed addressing/subnetting belongs to Week 2 |
| Port | [Cloudflare](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/) | Required selected sections; clarify default versus explicit port |
| Protocol | [Cloudflare](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-protocol/) | Optional opening definition |
| OSI | [Cloudflare](https://www.cloudflare.com/en-gb/learning/ddos/glossary/open-systems-interconnection-model-osi/), [Imperva](https://www.imperva.com/learn/application-security/osi-model/) | Selected layer roles; Imperva an alternative |
| TCP/IP | [Wikipedia](https://en.wikipedia.org/wiki/Internet_protocol_suite), [ThePower](https://thepower.education/en/blog/what-are-the-four-layers-that-make-up-tcp-ip) | Optional model comparisons; validate responsibilities with RFC 1122 |
| HTTP/HTTPS | [AWS](https://aws.amazon.com/compare/the-difference-between-https-and-http/) | Required request/response section only |

## Limits of introductory sources

Introductory analogies can simplify too much. Do not copy AWS's form-method example or TLS handshake details into this week's explanation. Use RFC 9110 for method semantics and the relevant TLS specification when studying TLS later. Do not use Coursera's `224.128.240.8` as an ordinary unicast host example. RFC 1122 supports the foundational host, loopback and layering distinctions; it is not a description of every current implementation.

Use [sources](SOURCES.md) for the specified sections. Reading original sources and completing direct lab work are separate achievements.
