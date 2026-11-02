# Week 1 review

Summary: Answer ten questions using diagrams, output and hypotheses before reading the separate explanations. Keep example analysis, your own execution and independent explanation distinct.

## Before you begin

Try these without help for about 20 minutes. All data below are question examples, not your measurements. Give an answer and one sentence of evidence for each question. Open the [answers](ANSWERS.md) afterward.

## Q1. How many hosts carry this HTTP exchange?

SSH terminal A runs Python and terminal B runs curl on the same VM. How many hosts carry this HTTP request/response, and which two application processes exchange it? What role does the personal PC play?

## Q2. Which way does the response travel?

Draw the response direction for `127.0.0.1:53120 → 127.0.0.1:8080`. Which is the temporary port? Must 53120 be reused next time?

## Q3. What does the local URL test?

You request `http://127.0.0.1:8080/echo` on the PC and find no VM server log. Can you conclude the VM server is broken? Name two next checks.

## Q4. What does 404 show?

In `> GET /missing HTTP/1.1`, `< HTTP/1.1 404 Not Found`, `{"error":"not found"}`, identify method, path, status and body. Is this evidence of a TCP connection failure?

## Q5. Can curl exit with 0 after 404?

The preceding request returns curl exit code 0. Does that contradict HTTP 404? What goes wrong if you run `pwd` before `echo $?`?

## Q6. Is 7 an HTTP status?

After stopping the server, curl prints `curl: (7) Failed to connect`. Is this HTTP status 7? Does the absence of a new server log establish the cause by itself?

## Q7. Where should you capture?

You capture on your PC's Wi-Fi and find no HTTP for the VM-internal request. Where should you capture instead? Draw the capture shell, saved file and Wireshark location.

## Q8. Which port belongs to the supplied file?

The supplied capture uses server port 59995. What should you change first if `tcp.port == 8080` finds nothing? Does analyzing the supplied file complete your own Linux capture?

## Q9. Why change one condition?

You change the message, path and port together, and a 404 becomes a connection error. Why is the result difficult to interpret? Describe a controlled rerun.

## Q10. Correct three claims

Correct each claim and identify the evidence needed: “Successful TCP always means HTTP 200”; “one packet is one HTTP message”; “listening means an external PC can connect.”

## After answering

Choose one prediction you got wrong and explain in three sentences which actual output or supplied-example evidence changed it. If Q1–Q8 are difficult, reconnect the concept with the lab. A score alone does not establish completion; also consider direct evidence, explanation and changed-condition reasoning.

[CCNA-linked practice (Korean)](../../../materials/week-01/ccna-practice.html) is optional: three externally linked questions and two authored supplements take about 15–20 minutes. Optional C6 adds about five minutes and is not a verified past exam question. Open its [explanations (Korean)](../../../materials/week-01/ccna-answers.html) only after attempting it.

To revisit key ideas, cover the memory sentences in [essentials](ESSENTIALS.md) and explain the same phenomenon. Developer scenarios may replace a related review question without increasing the required question count. Separate your answer, its conditions and the next evidence to check.
