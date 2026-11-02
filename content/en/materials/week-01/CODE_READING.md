# Follow a request through the code

Summary: Read server.py through request parsing, response selection, body encoding, sending and logging. Connect unfamiliar Python syntax with observable output; the Node client remains optional.

## 1. Follow one question

**Where is my `hello` read, and how does it enter the response?** Run one [normal request](LINUX.md), then spend about 10–15 minutes on sections 2–4. Writing the program from scratch or memorizing all Python syntax is not this week's goal.

| File or tool | Role | Scope |
| --- | --- | --- |
| `server.py` | Receive requests and choose status/body | Required lab file; start with the five steps below |
| curl | Send a request and display the result | Connect commands/output with the server code |
| `client.mts` | Separate connection, headers and body into logs | Optional after the basic lab |

```text
shell B: curl → HTTP GET /echo?message=hello
                         ↓ TCP connection inside the same Linux host
shell A: server.py → inspect path → build data → HTTP 200 + JSON body
                         ↓
shell B: curl displays status, headers and body
```

Python's HTTP library receives requests; this kit decides which response to construct. `/echo` is a route chosen in the code, not a command to open a directory or file.

## 2. A small Python reading guide

| Syntax | Meaning in this file |
| --- | --- |
| `import json` | Load Python's JSON tools |
| `class Handler(BaseHTTPRequestHandler):` | Define our behavior using the base HTTP handler |
| `def do_GET(self):` | Define the method the library calls for a GET request |
| `self.path` | Current request path and query, such as `/echo?message=hello` |
| `status_code = 200` | Store a value under a variable name |
| `request_url.path == "/echo"` | Compare values; `==` differs from assignment `=` |
| `if ...:` / `else:` | Choose a block according to a condition |
| `{"message": message}` | A dictionary pairing a name with the variable's value |
| `["hello"]` / `[0]` | A list / its first item; positions start at zero |
| `.get("message", ["hello"])` | Read the value list or use the default list |

`self` means the object handling this request, which holds request details such as path and client address. Indentation groups statements; preserve it when editing. Text after `#` is a comment.

## 3. Trace hello through five steps

These values explain the code and are not measured results. Keep your actual run in your own evidence file.

| Step | Code to find | For the hello request |
| --- | --- | --- |
| Read request | `urlsplit(self.path)` | Separate `/echo` from `message=hello` |
| Decide response | `if request_url.path == "/echo":` | Choose 200 and message data, or 404 and error data for another path |
| Build body | `json.dumps(...)` and `.encode("utf-8")` | Convert Python data into JSON text, then bytes |
| Send response | `send_response` through `wfile.write` | Send status/headers, a blank line and body bytes |
| Write log | `response_event` and `print(...)` | Print client endpoint, path, status and body length in shell A |

`parse_qs` reads `message=hello` as `{"message": ["hello"]}` because a name can have multiple values. This kit skips blank values, uses the first remaining `message`, and defaults to `hello` if none remains. Thus `/echo`, `/echo?message=`, and `/echo?message=first&message=second` produce `hello`, `hello`, and `first`.

A dictionary, JSON text and encoded bytes are different forms. Non-ASCII characters can occupy more than one UTF-8 byte, so `Content-Length` uses **`len(body)` after encoding**. The kit's `{"message": "hello"}` body is 20 bytes including spaces.

## 4. Connect code with output

| Code | What curl can show |
| --- | --- |
| `send_response(status_code)` | HTTP 200 or HTTP 404 status line |
| `send_header("Content-Type", ...)` | JSON and UTF-8 body format |
| `send_header("Content-Length", str(len(body)))` | Body byte count, not total header size |
| `send_header("Connection", "close")` | This kit closes after the response |
| `end_headers()` | Finish headers with a blank line |
| `wfile.write(body)` | Message or error body |

`send_response` and `send_header` prepare headers; `end_headers` sends them. Write the body afterward. curl's `<` marker is not part of the HTTP message.

**`print` does not send the network response.** The `event`, `client`, `path`, `status` and `bytes` fields go to the server terminal. The JSON sent to the client comes from `response_data`. A server log is not proof that the client read every byte, so compare it with curl output. The overridden `log_message` suppresses the default access log in favor of the kit's JSON log.

## 5. Read the shared file

Download <a download href="../../../labs/week-01/server.py">server.py</a>. The shared code has Korean comments; match the identifiers with the English walkthrough above.

Definitions are read before the bottom `if __name__ == "__main__":` starts the server. Defining the class does not execute `do_GET`; the library calls that method when GET requests arrive. `--port` selects the server port and defaults to 8080. Binding `127.0.0.1` keeps this experiment on the same host. Leave `serve_forever()` running in A while using curl in B. Ctrl+C triggers shutdown; the `with` block cleans up the server resource.

## 6. Predict small changes

Keep the baseline code and use your own copy. If you edit the server file, stop and restart the process to load the changed code. Change one condition at a time.

1. Keep code unchanged and change `hello` to `again` in the URL. Which variable and response field change?
2. Keep code unchanged and request `/missing`. Why does `else` run, and does the common response-sending code still run?
3. Optional: change only the code's default message from `hello` to `hi`. Compare `/echo` with `/echo?message=hello`. Restore the code and restart afterward.

Check after predicting: (1) message and body change while server port stays; (2) a non-`/echo` path chooses 404/error data and still sends a response; (3) results are `hi`, then `hello`, because the explicit query overrides the default.

## 7. Optional Node client

curl is sufficient for the required lab. Use the shared <a download href="../../../labs/week-01/client.mts">client.mts</a> only if Node is already prepared and you want to understand programmatic response reading. Check the version requirements in the [kit guide (Korean)](../../../labs/week-01/README.md) before running it.

A **callback** is a function registered to run when an event happens. `response.on("data", ...)` registers work for arriving data. Events do not all print immediately in source-file order.

```text
Typical success:
request → connected → response headers → data (possibly repeated) → end → body log
```

The code accumulates `data` chunks and prints the body on `end`. A data chunk is not necessarily a TCP packet. `setEncoding("utf8")` reads body text; `socket.once("connect", ...)` records actual local/remote endpoints. The client uses a three-second timeout and clears its timer on completion/error. Its exit policy is 0 for success, 2 for HTTP status 400+, and 1 for connection/transfer errors.

`elapsed_ms` includes work from the program's request start; it is not pure network latency. A 404 is received before the client chooses exit code 2. Read actual logs to see how much arrived before a connection, transfer or timeout error. Type stripping removes annotations such as `: string`; it does not perform type checking.

Return to the [lab](LINUX.md) when you can point to where status is chosen, body is sent and logs are written. Socket implementation, threading and full TypeScript syntax are outside this week's required scope.

Sources: [Python HTTP server](https://docs.python.org/3/library/http.server.html), [Python query parsing](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.parse_qs), [Node HTTP](https://nodejs.org/api/http.html#httpgetoptions-callback). Check the documentation matching the Node version you run.
