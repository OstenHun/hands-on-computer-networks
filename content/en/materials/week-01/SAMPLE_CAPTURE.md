# Week 1 supplied capture — find the four states

Summary: Read a Windows loopback example of 200, 404, refusal and recovery. Keep its packet numbers and port 59995 separate from your own Linux run and distinguish analysis from direct capture.

## When to use it

If direct capture on Linux `lo` is blocked, you can still practice packet analysis. Download <a download href="../../../materials/qa/week-01-local.pcapng">week-01-local.pcapng</a> and open it in Wireshark. Identify it as supplied-example analysis in your own evidence file. Reading the table below without opening the capture does not complete packet analysis.

The example was captured on Windows loopback using the Python server and optional Node client. Its server port is **59995**, unlike the Linux lab default 8080. Your Linux curl output and this Windows capture are separate runs.

## Find the packets

1. Open the saved file and apply display filter `tcp.port == 59995`. The Linux filter `tcp.port == 8080` finds nothing in this example.
2. Use the No. column to find packet numbers below. Both IP addresses are `127.0.0.1`; distinguish endpoints using ports and direction. The four client ports are 59996, 59997, 59998 and 59999.
3. If HTTP is not decoded, use Analyze → Decode As → HTTP for TCP port 59995. Select a request and choose Follow → TCP Stream. Use the packet list for numbers and the stream/details for content.
4. Compare 4→8, 17→21, 27→28 and 32→36. Headers and bodies can appear in different packets; one listed response packet need not contain every byte of the response.

| State | Request side | Other side | Evidence |
| --- | --- | --- | --- |
| Normal | 4: `59996 → 59995`, `GET /echo?message=hello` | 6: HTTP 200 headers; 8: 200 and JSON body | Request and response share the same endpoint pair |
| Missing path | 17: `59997 → 59995`, `GET /missing` | 19: HTTP 404 headers; 21: 404 and error body | An HTTP response exists; this is not connection failure |
| After server stop | 27: `59998 → 59995`, TCP SYN | 28: `59995 → 59998`, TCP RST/ACK | Refused connection; no HTTP status line for this attempt |
| After restart | 32: `59999 → 59995`, `GET /echo?message=again` | 34: HTTP 200 headers; 36: 200 and JSON body | The same server port responds again |

RST alone does not identify who stopped which process. Stop and restart are the example's known execution conditions; diagnose real incidents with process state and logs too.

## Answer before checking

1. Which temporary ports belong to normal and 404? Find a response-body packet for each.
2. How do directions differ between 17 and 21? Is “cannot connect to server” a correct description of 404 here?
3. Which TCP flags appear in 28? Is there HTTP 200 or 404 for the attempt beginning at 27?
4. Does recovery keep the server port? Are the message and temporary port the same as the first request?

Check: normal uses 59996 and 404 uses 59997. Packets 8 and 21 show their response bodies. 17 travels client→server; 21 travels server→client. 28 carries RST/ACK with no HTTP response. Recovery keeps server port 59995, uses client port 59999 and changes the message to `again`. Do not treat that message change as the same controlled run as your Linux E4 baseline `hello`.

## Keep the evidence distinct

Record filename, Windows loopback provenance, server port 59995, packets you inspected, both endpoint ports, HTTP status or its absence, and why your own capture was blocked. Keep your Linux values separately. This is evidence of packet reading, not proof of direct Linux capture or your own E1–E4 execution.
