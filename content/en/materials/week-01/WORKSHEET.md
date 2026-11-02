# Week 1 shared question — response or connection failure?

Summary: Explain the difference between a normal response, HTTP 404 and connection failure. Find relevant evidence, change a path or server state, and compare your predictions with the lab results.

## The central question

**Why can requests to the same server address produce a normal response, a 404 response or a connection failure?**

State your current prediction. If you are unsure, look for the relevant section in the [concepts](CONCEPTS.md) and [reading guide](ARTICLE_LESSON.md). You do not need a long presentation.

## Explore, explain and test

| Step | Action | Evidence |
| --- | --- | --- |
| Choose | Identify where the request runs and which results you will compare | Central question and supporting questions below |
| Explore | Find the explanation of HTTP status versus connection failure | [Concepts](CONCEPTS.md), [sources](SOURCES.md) |
| Explain | Point to the relevant section and output; use your own words | Execution-host diagram, response, logs |
| Change | Ask what happens if only the URL path changes, or if the server stops | [Linux lab](LINUX.md) |
| Test | Each learner runs normal → 404 → stop → restart | curl output, server logs and one normal request's packets |

In a group, rotate the explainer as questions change. Others should also interpret output or answer a changed-condition question. Agreement without evidence leaves an open question. Treat AI explanations as hypotheses to compare with official sources and actual output.

## Read the relevant official sections

- [RFC 9110 §15.3.1](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.3.1) and [§15.5.5](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.5.5): meanings of 200 and 404.
- [curl exit codes](https://curl.se/docs/manpage.html#EXITCODES): compare HTTP status with the tool's exit code under the lab's options.

If an external source is unavailable or difficult to read, use the corresponding [concepts](CONCEPTS.md) and [reading guide](ARTICLE_LESSON.md). Do not claim to have read an original source you did not read.

## Optional supporting questions

### How do we distinguish programs at the same IP address?

Identify what an IP address and a port describe. How do the server's listening port and the client's temporary port differ? Explain using the listening socket, URL, logs and both endpoints in the capture. Two terminal windows do not imply two hosts.

### Does 127.0.0.1 mean the same place on my PC and VM?

Draw the execution host and destination first. Where do the shells opened through SSH run? Which interface observes HTTP inside the VM? Compare your command locations with the `lo` capture or supplied example. Do not combine addresses, ports or packet numbers from separate runs.

Use the [developer scenarios](ESSENTIALS.md) as additional prompts where relevant; you do not need to finish every optional question in the same session.

## Explain after the lab

Compare all four states and read one normal request's packet flow. Change one condition, rerun independently and restore the baseline. Answer the [review](REVIEW.md) before opening the [answers](ANSWERS.md).

Keep detailed evidence once in personal files or notes. If capture is blocked, use the [supplied example](SAMPLE_CAPTURE.md) and identify what you analyzed, ran directly or did not perform. Record the blocked step and next action alongside your lab evidence. Never record passwords or tokens.
