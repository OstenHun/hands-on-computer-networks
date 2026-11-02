# Week 1 Linux lab — normal, missing, stopped and recovered

Summary: Run Python and curl on the same Linux host. Compare 200, 404, connection failure and recovery; match output with loopback packets and distinguish expected examples from your own observations.

## Prepare the execution environment

Read the [concepts](CONCEPTS.md) first. Allow 20–40 minutes for setup when needed. Keep detailed predictions, commands, output and packets once in your own evidence files; use them to explain the [shared question](WORKSHEET.md).

Use a Linux host you are allowed to access. This HTTP experiment does not require a new VM or a firewall change. Check that you can connect, Python 3.10+ and curl are present, packet capture is permitted, and you can transfer a capture to your PC. If preparation is blocked for more than five minutes, use the alternatives below and leave direct execution unfinished.

```text
Personal PC: reading, SSH terminals, later packet analysis
   └─ one Linux host
        shell A: Python server
        shell B: curl
        shell C: permitted capture on lo
        server.py and the capture file live on this Linux host
```

Download the shared <a download href="../../../labs/week-01/server.py">server.py</a> and transfer it to Linux through an approved method such as SFTP or scp. A PC download does not automatically appear on the VM. The [code walkthrough](CODE_READING.md) explains the script in English; the shared script's comments are Korean.

A **terminal** displays commands and output; a **shell** runs the commands. Enter one line at a time and do not copy the prompt, such as `$`. A, B and C label shells on the same VM, not different machines. Ctrl+C stops a foreground command; it is not the copy shortcut.

| Command | Purpose |
| --- | --- |
| `pwd` | Show the current directory's absolute path |
| `ls` | List files and directories |
| `cd directory-name` | Enter a directory; replace the name |
| `cd ..` | Move to the parent directory |
| `mkdir -p labs/week-01` | Create the lab directory if needed |

The following commands assume that `labs/week-01/server.py` exists below your current project directory. If you only downloaded the script, create that directory and put the file there. In both A and B, check the location and tools:

```sh
hostname
uname -s
pwd
ls labs/week-01/server.py
python3 --version
curl --version
command -v ss
command -v tcpdump
```

If `ls` reports a missing file, fix the location before starting the server. Each shell has its own current directory. Compare SSH destinations as well as hostnames; identical hostnames do not guarantee the same host. Have missing tools prepared for the approved environment and permissions. Node is optional and is not required for this lab.

## 1. Start the server in shell A

**Predict:** What changes when the file becomes a running process?

```sh
python3 labs/week-01/server.py
```

The shell stays occupied while the server waits. Keep A running and use B for curl. The **expected example** is:

```json
{"event": "listening", "address": ["127.0.0.1", 8080]}
```

Record the actual listening address and port. The log does not prove external PC access.

## 2. Send a normal request from shell B

Predict the result before running it. Find the listening port under Local Address:Port in `ss`.

```sh
ss -lnt
curl -v --http1.1 --noproxy '*' --max-time 5 'http://127.0.0.1:8080/echo?message=hello'
echo $?
```

| Option | Meaning here |
| --- | --- |
| `ss -lnt` | List listening TCP sockets using numeric addresses and ports |
| `-v` | Show connection information and request/response headers |
| `--http1.1` | Explicitly use HTTP/1.1 |
| `--noproxy '*'` | Bypass proxies; keep the quotes |
| `--max-time 5` | Limit the entire request to five seconds |
| Quoted URL | Prevent the shell from interpreting special characters |
| `echo $?` | Show the immediately preceding command's exit code |

Expect HTTP 200, a `{"message": "hello"}` body and a new `response` log in A with the matching `path` and `status`. A completed transfer should exit with 0. These are predictions from the code, not observations you have already made.

curl marks sent headers with `>`, received headers with `<` and tool information with `*`. The body uses stdout, while verbose information uses stderr; both can appear on one screen. The body has no final newline, so the next prompt may touch it.

For **E1**, keep the actual command, B's status/body/exit code, and A's new response log. `client` contains the requesting IP and temporary port. Use that port in your diagram; a short connection can disappear before `ss` is run.

Change only `hello` to `again`, compare the values that changed, then return to the baseline `hello`.

## 3. Change the path in shell B

For **E2**, predict whether there will be an HTTP response and a new server log. Leave the server running.

```sh
curl -v --http1.1 --noproxy '*' --max-time 5 'http://127.0.0.1:8080/missing'
echo $?
```

Expect HTTP 404, an error body and a new response log. Without `--fail`, a completed 404 transfer can still return curl exit code 0. Keep HTTP status and process exit code separate. The optional Node client's exit code 2 for 404 is that client's own policy.

## 4. Stop and recover

For **E3**, predict the result. In A, press Ctrl+C to stop only the server you started. In B, repeat E1's request:

```sh
curl -v --http1.1 --noproxy '*' --max-time 5 'http://127.0.0.1:8080/echo?message=hello'
echo $?
```

If no other listener has replaced it, expect connection failure and no HTTP response. Record the actual exit code: connection refusal is 7; a timeout is 28. The stopped process cannot write a new response log. Do not call this “HTTP 7.”

For **E4**, predict recovery. Restart `python3 labs/week-01/server.py` in A, then run exactly the same curl command in B. Check 200, the body and A's new log. Keep the message and port unchanged during recovery.

## 5. Capture on lo and analyze on the PC

Run this only in shell C on the same Linux host, with permission to capture. If you cannot use the required capture privileges, use the [supplied capture](SAMPLE_CAPTURE.md). Give each run a new filename instead of overwriting previous evidence.

```sh
sudo tcpdump -i lo -nn -s 0 -w week-01-linux-run-01.pcap 'host 127.0.0.1 and tcp port 8080'
```

`-i` selects the interface, `-nn` keeps addresses and ports numeric, `-s 0` avoids packet truncation, and `-w` saves a file. The quoted expression is a **capture filter**. Reading one normal request flow is required; comparing all four states in packets is optional.

1. Wait for capture to start, then send a request in B. Keep C running if you stop the server in A.
2. If comparing all four states, run normal → 404 → stop A and request the normal URL → restart A and repeat. Stop C with Ctrl+C.
3. Check the capture with `ls -l week-01-linux-run-01.pcap`. Resolve read permissions through the approved method.
4. Transfer the file to your PC using SFTP or scp. Find its remote absolute path using `pwd` in C. If an SSH alias is already configured, the PC-shell form is `scp lab-alias:/actual/Linux/path/week-01-linux-run-01.pcap .`; replace the alias and path.
5. Open it in Wireshark. Use display filter `tcp.port == 8080`. Display filters and capture filters have different syntax. If necessary, use Analyze → Decode As to interpret the port as HTTP.
6. Select a request and use Follow → TCP Stream to read messages. Use Statistics → Flow Graph for direction. Record actual packet numbers, addresses, ports, path and status.

The supplied Windows example uses port **59995**, not 8080. Do not merge its packets with your Linux output or count supplied-file analysis as your own capture. Linux `lo` does not demonstrate traversal of your PC's Wi-Fi, the VM's external NIC, a router, ARP or cloud security groups. Packet counts, numbers and ephemeral ports are not fixed answers.

You may also inspect packets in [WireSalmon](https://taerim0.github.io/WireSalmon/) or Wireshark. WireSalmon's public web application can open built-in samples and saved capture files, but does not perform live capture. Its generated samples are examples, not evidence that you ran the Linux experiment. The original lab's [WireSalmon sample walkthrough (Korean)](../../../materials/week-01/linux.html) describes the named samples and optional comparison of 404 with refusal.

## 6. Rerun with a changed condition

Allow about 15 minutes. With another learner or a small group, choose one condition; each person predicts, runs, explains and restores it on their own Linux host. Rotate who proposes and checks the condition. Keep unfinished work as follow-up rather than claiming everyone performed one person's run.

- **Message:** `hello` → `pair`, keeping path and port.
- **Path:** `/echo?message=hello` → `/missing?message=hello`, keeping query and port.
- **Service port:** stop your server, start `python3 labs/week-01/server.py --port 8081`, and use 8081 in both URL and filters. This is one variable applied consistently in three places.

Explain the prediction before copying commands. Keep each person's own output and restore the baseline port and URL. When studying alone, choose the condition yourself and record which help you used.

## If the environment blocks you

| Symptom | Check | Alternative after five minutes |
| --- | --- | --- |
| Cannot connect | Approved host, account and connection method | Ask the environment owner; use concept/example analysis and leave execution incomplete |
| File missing | `pwd`, `ls`, transfer destination | Transfer it; if delayed, observe and complete your run later |
| Python or curl missing | Tool versions and approved preparation | Use an authorized environment with the tools |
| Address already in use | `ss -lnt`, your existing server | Use 8081 consistently; do not kill another person's process |
| Unexpected connection failure | Same host, listening socket and URL | Recheck the baseline; do not disable a firewall |
| Empty capture | `lo`, capture timing, filter and privileges | Analyze the supplied example; leave direct capture unfinished |
| Cannot transfer capture | Approved transfer and read permissions | Analyze on Linux with an approved tool such as tshark, or use the example; distinguish it from PC analysis |

## Finish

Stop only your own server and capture with Ctrl+C. Keep actual output, packets and explanations. Before sharing, redact real connection details and identifiers. See [sources](SOURCES.md) for command documentation. Successful reading or example analysis alone does not prove direct execution.
