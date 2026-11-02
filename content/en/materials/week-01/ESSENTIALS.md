# Week 1 essentials — location, endpoints and responses

Summary: Distinguish where a command runs, what an IP address and port identify, and whether an HTTP response exists. Apply these distinctions to a developer scenario without adding required lab work.

Use this in the last five minutes of concept reading. Connect one existing question to a scenario below; no extra presentation, worksheet or mandatory record is required.

## Three concepts to remember

### W01-K1 — localhost belongs to the execution environment

**Remember:** The same `127.0.0.1:8080` can identify a different endpoint when curl runs on a different host.

curl in the remote SSH shell runs on the VM; curl in a local PC shell runs on the PC. Where the window appears is different from where the command runs. “localhost always means my laptop” is false in a remote shell. See [concepts 1–2](CONCEPTS.md).

### W01-K2 — IP address, port and process are different units

**Remember:** IP addresses identify communication locations; TCP/UDP ports distinguish endpoints for the corresponding transport protocol. A port is not a process ID.

A host can have multiple addresses, processes and sockets; one process can use multiple sockets. A port number alone does not establish the actual process or external reachability. This week, read address, server port, temporary port and direction. See [concepts 4](CONCEPTS.md).

### W01-K3 — an HTTP response and connection failure occur at different stages

**Remember:** HTTP 404 is a response; distinguish it from connection refusal or timeout.

Compare the meaning of the response with the actual server log. A proxy might generate 404 in a general service, so status alone does not prove origin-server reachability. Timeout alone does not prove a stopped server. See [concepts 5–7](CONCEPTS.md) and [RFC 9110 §15.5.5](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.5.5).

## Two common confusions

| Claim | Distinction |
| --- | --- |
| The same URL always means the same server | Check execution host, name resolution, port and path. In this loopback example, the host changes without DNS |
| Successful TCP delivery or HTTP 200 means the business operation completed | Transport, HTTP response and application state are separate. Check the API contract, response contents and state evidence |

## Explain a developer scenario

These are questions authored for the study, not verified interview questions from any company.

Inside a VM, `/echo` returns 200 and `/missing` returns 404. From the PC shell, `http://127.0.0.1:8080/echo` is refused. These are illustrative conditions, not participant observations.

1. **W01-D1 — explanation:** Explain each result using execution location and the stage that failed.
2. **W01-D2 — changed condition:** If the PC request uses the VM's IP, is success guaranteed? Which conditions remain unknown?
3. **W01-D3 — diagnosis:** Which two pieces of evidence would you compare before changing the server code?

Answer first, then open the [developer explanations](ANSWERS.md#developer-scenarios). Reading an explanation differs from running the experiment or explaining independently.

## Explain it again next week

How does localhost's target change if the same request runs on the PC rather than the remote shell? Use a changed condition during ordinary review. If you are stuck, return to the relevant concept and reduce optional reading.
