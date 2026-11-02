# Week 1 concepts — where does communication happen?

Summary: Follow HTTP between two programs on one Linux host. Connect execution location, IP addresses, ports and layers to the evidence that distinguishes HTTP 200, HTTP 404 and a connection failure.

## Reading order and goal

Follow a request between two programs inside one Linux host. The goal is to distinguish a 404 response from a connection failure. Allow about 30 minutes for seven concepts, including five minutes each for the required port and HTTP readings in the [reading guide](ARTICLE_LESSON.md). Other external reading is optional.

Read each explanation, predict an answer, then compare it with the diagram. Finish by drawing the host and programs yourself. Use [essentials](ESSENTIALS.md) for the last five minutes. All output and temporary ports below are illustrative, not your measured results. Continue with the [Linux lab](LINUX.md) and keep your own evidence once in personal notes or files.

## 1. Networks — what is connected?

**Predict:** Can two programs on one computer communicate without an Internet connection?

A network connects devices so they can exchange data. The Internet connects many networks. Network communication does not always travel over the Internet.

This experiment uses the operating system's networking functions within one Linux host. The **loopback** path carries traffic inside that host, without an external cable or Wi-Fi connection. **curl** sends the request and a **Python server** responds. The request and response follow **HTTP**, introduced below.

```text
External communication: local host → links and intermediate devices → remote host
This experiment:        [ Linux host: curl → loopback → Python server ]
```

A capture tool records **packets**. A packet is not necessarily one line on screen or one HTTP message. One HTTP message can span multiple TCP segments and be reassembled by the receiver. Linux calls the loopback interface `lo`; an interface is a place through which networking data is sent or received.

**Observe:** Capture on `lo` and inspect the request and response addresses. Missing traffic on Wi-Fi does not prove that no communication occurred.

**Explain:** Why does this experiment alone say nothing about Internet connectivity?

## 2. Hosts and processes — computers and programs are different units

**Predict:** Do two terminal windows mean two computers?

A **host** is a computer participating in communication. A **virtual machine (VM)** has its own operating system and network environment and can act as a host. A **process** is a running program. `server.py` is a file on disk; running `python3 server.py` starts a Python process. Running curl also starts a process.

A **terminal** is the window where you enter commands and read output. A **shell** interprets and runs commands. Through **SSH**, a terminal on your PC can show a shell running on remote Linux.

```text
Personal PC                       One remote Linux VM
SSH terminal A ── commands ──────> shell A → Python server process
SSH terminal B ── commands ──────> shell B → curl process
                                  HTTP stays inside the VM
```

After SSH login, the command runs on Linux even though the window appears on your PC. Compare the SSH destination, `hostname` and `uname -s` in A and B. Matching hostnames alone do not guarantee the same VM. `pwd` shows the current directory and `ls` shows its files.

Files must also exist on the Linux host where you run them. Downloading a file to your PC does not copy it to the VM. You may capture packets on Linux and transfer the capture to Wireshark on your PC.

**Check the distinction:** A Python file on disk cannot receive requests until its server process runs.

**Explain:** Why does the file remain after Ctrl+C stops the server?

## 3. Client and server — roles in a particular exchange

**Predict:** Must a client and server run on different computers?

Here curl initiates the request, so it is the **client**. The Python program receives the request and responds, so it is the **server**. “Server” can also refer to a machine, but here it means a process. Both roles can run on the same host; a program can be a client in another exchange.

```text
curl                                  Python server
start request ── GET /echo?message=hello ──> inspect path
read body <──────── 200 + JSON body ────── build response
```

Start the server first. Its `listening` log says that it is waiting at a particular address and port; it does not prove that an external PC can reach it.

**Observe:** Match curl's request line to the server's `path` log.

**Explain:** What evidence identifies the client and server when both run inside one VM?

## 4. IP, ports and loopback — which endpoint?

**Predict:** Does the same IP address imply the same program?

An **IP address** identifies a location for network communication. A host may have multiple IP addresses, so one address does not always mean one computer. A **TCP port** distinguishes a communication endpoint at an address. It is neither a physical socket for a cable nor a process ID. One program can use multiple ports.

```text
http://127.0.0.1:8080/echo?message=hello
       address   port path  query parameter
```

The destination is `127.0.0.1`, the server TCP port is `8080`, the path is `/echo`, and the query supplies `hello` as `message`. The path tells this server what operation to perform; it need not name a file on disk.

```text
Illustrative temporary client port inside the same Linux host:
request   127.0.0.1:51000 ─────> 127.0.0.1:8080
response  127.0.0.1:51000 <───── 127.0.0.1:8080
```

The operating system usually chooses the client's temporary, or **ephemeral**, port. It can differ between requests. Find its actual value in the server's `client` log or capture. Addresses, ports and direction distinguish the endpoints even when the IP addresses match.

Use `ss -lnt` to find listening TCP sockets: `-l` means listening, `-n` numeric addresses and ports, and `-t` TCP. A short curl connection may end before you query it, so find its temporary port in logs or packets.

Loopback `127.0.0.1` points to the **network environment where the command runs**. curl on your PC and curl inside the SSH session point to different loopbacks. This week's experiment does not use containers or separate network namespaces.

**Explain:** Why does entering the same loopback URL on your PC fail to test the VM's server?

## 5. Protocols and layers — ask separate questions

**Predict:** What exactly succeeded when you say “communication succeeded”?

A **protocol** defines message formats and processing rules shared by participants. **Layers** help separate responsibilities.

| Role | This experiment | Question |
| --- | --- | --- |
| Application | HTTP | What request, status and body were exchanged? |
| Transport | TCP | Did the endpoints establish a connection and exchange data? |
| Internet | IP | Which addresses were used? |
| Local delivery path | Linux loopback, `lo` | Where did you observe the traffic? |

The application creates an HTTP message. TCP carries bytes using IP addressing; here the path stays inside Linux loopback. The receiving application interprets the message.

A working TCP connection does not imply that the requested HTTP path exists. A 404 is an HTTP response delivered over the connection. A refused connection may produce no HTTP status for the request. **This kit uses HTTP/1.1 over TCP**; do not generalize that transport to every HTTP version.

The OSI model describes seven layers. The TCP/IP model groups responsibilities around Internet protocols. Memorizing every layer name is unnecessary here; detailed boundaries and retransmission come later. Observing `lo` is not observing an external Ethernet link.

**Explain:** Why is HTTP 404 insufficient evidence that TCP is broken?

## 6. HTTP requests and responses — read the lines

Separate the request/status line, headers, blank line and body. **Headers** carry metadata; the **body** carries content.

**Predict:** If `hello` becomes `again`, which part of the URL and response changes?

This simplified example illustrates curl's display; it is not a measured result. `>` and `<` are curl's direction markers, not HTTP message characters. Dates, versions and header order can vary.

```text
> GET /echo?message=hello HTTP/1.1
> Host: 127.0.0.1:8080
>
< HTTP/1.1 200 OK
< Content-Type: application/json; charset=utf-8
< Content-Length: 20
< Connection: close
<
{"message": "hello"}
```

`GET` is the request **method**. This server's code returns 200 and a message for `/echo`, or 404 and an error body for other paths. **JSON** represents data using names and values, such as `"message": "hello"`. `Content-Length` counts body bytes, which can differ from character count. This kit closes the connection after each response.

Illustrative server log:

```json
{"event":"response","client":["127.0.0.1",51000],"path":"/echo?message=hello","status":200,"bytes":20}
```

Match the `client` port with the capture's request source port, and match `path` and `status` with curl. Logs come from the application; captures come from the selected interface. They are distinct evidence.

Read curl's `*` connection information, `>` request, `<` response and body. Verbose information and headers normally use stderr while the body uses stdout, so they can appear together. The number printed by `echo $?` is curl's process exit code, not the HTTP status.

Changing only `hello` to `again` should change the query value and body while keeping the server port. Observe the actual ephemeral port and timestamp after execution. HTTP 200 for this request does not establish that every function of another service works.

## 7. Compare four states

The following table contains **expected behavior from the supplied code and commands**. Record your own observations separately.

| Condition | HTTP status | New server response log | Expected curl exit code |
| --- | --- | --- | --- |
| Running, `/echo` | 200 | Yes | 0 if transfer completes |
| Running, `/missing` | 404 | Yes | 0 if transfer completes without `--fail` |
| Stopped, same URL | No response | A stopped process cannot log it | 7 for connection refusal; 28 for timeout |
| Restarted on the same port, `/echo` | 200 | Yes | 0 if transfer completes |

```text
Missing path:  < HTTP/1.1 404 Not Found        HTTP response from the server
After stop:    curl: (7) Failed to connect...  curl error, not an HTTP status line
```

For 404, find the response body and new server log. After stopping the server, do not expect a new response log or an HTTP status line from it. A connection error alone does not prove that the server was stopped: compare host, address and port, then retry the same command after restart.

HTTP status comes from an HTTP response. The exit code is the tool's result reported to the shell. Run `echo $?` immediately after curl; another intervening command replaces it. The optional Node client has its own policy: 0 for success, 2 for HTTP errors, and 1 for connection/transfer errors. Different tools can report different exit codes for the same HTTP response.

Change one condition at a time and compare results. You do not need to disable a firewall or stop someone else's processes.

## Close the text and explain

1. Draw two processes inside one host and label both directions with IP addresses and ports.
2. Place the PC terminal, Linux shell, capture interface `lo` and Wireshark analysis in the diagram.
3. Name two pieces of evidence for a 404 response and two for connection failure.
4. Explain the missing check in “The server is listening, so my external PC can reach it.”

Reread only the relevant section if needed. Continue with the [lab](LINUX.md), [review](REVIEW.md) and [sources](SOURCES.md). Diagrams, questions and annotated examples are authored for this learning project.
