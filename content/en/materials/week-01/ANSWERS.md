# Week 1 answers and checks

Summary: Compare your answers with explanations of the ten review questions and developer scenarios. Reading a solution does not establish direct lab execution or an independent explanation.

## Compare after attempting the questions

Write your answers to the [review](REVIEW.md) first, then allow about ten minutes to compare. Keep the original prediction and add why you changed it.

1. The HTTP exchange stays inside **one VM**, between the curl and Python server processes. The overall setup includes the PC and VM, but the PC supplies SSH input and display rather than carrying this HTTP loopback exchange. Why are terminal windows different from hosts?
2. The response travels `127.0.0.1:8080 → 127.0.0.1:53120`. Here 53120 is the client's temporary port and need not recur. Check the server's `client` log and capture. What distinguishes direction when the IP addresses match?
3. The PC request targets the PC's own loopback, so it does not establish a VM fault. Check curl's execution host and the SSH destination; compare the VM's listening socket with the same request inside the VM. Why can the same URL text identify a different place?
4. Method `GET`, path `/missing`, status `404`, body JSON error data. An HTTP response was delivered, so this is not a TCP connection failure for the exchange. Matching your own server log strengthens attribution to this server. In a general service, check whether an intermediary produced the response.
5. Without `--fail`, curl can return 0 when it completes transfer of an HTTP error response. After `pwd`, `$?` refers to pwd rather than curl. HTTP status and process exit code come from different sources. The optional Node client's 404→2 mapping is a kit policy.
6. 7 is curl's connection-failure exit code, not HTTP status. Check execution host, port and whether the server is running. Stop → failure of the same request → restart on the same port → recovery strengthens the stopped-server hypothesis. An error message alone does not establish every environment's cause.
7. Use an additional shell C on the same Linux host to capture `lo` with permission. Save the capture on Linux, transfer it through an approved method and analyze it on the PC. The PC's Wi-Fi may show SSH traffic without showing the VM's internal loopback HTTP.
8. Use `tcp.port == 59995` for this file. Record supplied Windows example analysis separately from your own Linux execution/capture. Packet numbers are meaningful within that file only.
9. Multiple changed variables obscure which caused the difference. Restore successful `/echo`, then change only message or only path. If choosing service port as the variable, update server, URL and filters consistently. Three settings for one variable differ from three independent variables.
10. TCP delivery can carry a 404 response: inspect the status line. An HTTP message can span segments and be reassembled: inspect Follow TCP Stream. Listening shows local socket state; external reachability needs a real external request plus checks of binding, route and policy. This week's internal lab does not prove external access.

## What a facilitator should check

Prioritize confusing PC and VM loopback, calling 404 “no response,” or recording another person's execution as your own. Check the diagram, each learner's output and explanation. Return to concepts 2, 4 and 7; rerun the relevant request when the environment allows it.

If someone only memorized an answer, ask what they would check after changing only the port rather than the path. Apply the same evidence standard to the facilitator.

## Developer scenarios

Try the [essentials scenarios](ESSENTIALS.md) before comparing.

1. **W01-D1:** The VM's 200 and 404 are HTTP responses. The PC's loopback refers to the PC, so its failure does not prove that the VM server stopped. Distinguish this direct-request setup from a general service with intermediaries.
2. **W01-D2:** Success is not guaranteed. Check server binding and listening socket, PC-to-VM route and policy, and the destination port. Changing one URL component does not establish reachability.
3. **W01-D3:** First align curl's execution host and exact URL, then compare server logs and listening address/port inside the VM. Internal and external requests are different experiments.

Common mistakes include “404 is TCP failure,” “localhost always means my PC,” and “the correct IP guarantees success.” A concept explanation should identify location, failure stage and evidence. Direct lab completion needs the learner's own evidence separately.
