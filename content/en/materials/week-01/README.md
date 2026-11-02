# Week 1 — follow one request from start to finish

Summary: Compare a normal response, HTTP 404 and a connection failure using concepts, Linux commands, logs and packets. Keep predictions separate from observations and explain what your evidence supports.

## Start with one question

**Why can requests to the same server address produce a normal response, a 404 response or a connection failure?** Start with the [shared question](WORKSHEET.md). Find the relevant explanation, explain it in your own words, and change a path or server state to test it. In a group, take turns explaining and questioning each other's assumptions.

If connecting to a VM is new, consult the [VM and SSH guide (Korean)](../../../materials/ssh-top-down/index.html). Before starting, identify whether the shell that will run curl is on your PC or inside the VM. The [concepts](CONCEPTS.md) explain hosts, processes and loopback.

## Reading and experiments

| Step | Material | What to check |
| --- | --- | --- |
| Choose a question | [Shared question](WORKSHEET.md) | Select the central question and only the supporting questions you need |
| Find the explanation | [Concepts](CONCEPTS.md), [reading guide](ARTICLE_LESSON.md), [sources](SOURCES.md) | Execution host, IP and port, HTTP; the required 10 minutes of external reading are part of the 30-minute concept session |
| Explain and vary a condition | [Essentials](ESSENTIALS.md) | Explain from evidence, then change the path, server state or execution host |
| Test directly | [Linux lab](LINUX.md), [code walkthrough](CODE_READING.md) | Run Python and curl on the same Linux host; compare normal, 404, stopped and restarted states |
| Review | [Questions](REVIEW.md), then [answers](ANSWERS.md) | Answer before reading the explanations; use output, logs and packets to revise your reasoning |

Allow another 20–40 minutes for environment preparation if needed. A suggested personal study budget is 2–3 hours for the week; no separate presentation is required. See the [facilitator guide](FACILITATOR.md) for preparation and alternatives.

## Find a specific topic

- Confused by localhost or where a command runs? Read [concepts](CONCEPTS.md).
- Need to distinguish programs at the same IP address? Read [essentials](ESSENTIALS.md) and the [reading guide](ARTICLE_LESSON.md).
- Need to interpret 200, 404 or connection failure? Compare the [lab](LINUX.md) with the [code walkthrough](CODE_READING.md).
- Unable to capture packets yourself? Use the [supplied capture](SAMPLE_CAPTURE.md), keeping example analysis separate from your own execution.

The [global concept index](../../../materials/week-01/concept-index.html), [developer references](../../../materials/week-01/interview-references.html), [optional explorations](../../../materials/week-01/explorations.html), and [CCNA practice](../../../materials/week-01/ccna-practice.html) are available in Korean. Optional practice follows the required lab; it does not replace it.

## Completion and evidence

Keep your own commands and both sides' output for HTTP 200, HTTP 404, server stop and restart. Match addresses and ports across output and packets. Change one condition chosen with another learner, rerun independently and restore the baseline. Explain IP versus port, loopback, and 404 versus connection failure in your own words.

Analyze one normal request's packet flow. State whether you captured it yourself or analyzed the supplied example. Additional packet comparisons for 404, stop and recovery are optional; leave unobserved results unobserved. If the environment blocks execution, continue the concept work and leave direct execution as a task to complete later.

Keep commands, logs, curl output and captures once in your own notes or files. Show relevant evidence when explaining; extra notes are optional. Download any browser answers before navigating away and open the saved file to check it.

## Files and the next question

Use the shared <a download href="../../../labs/week-01/server.py">Python server</a>. The <a download href="../../../labs/week-01/client.mts">Node client</a> is optional; the [kit instructions (Korean)](../../../labs/week-01/README.md) describe that path. Inline code comments in the shared files are Korean; the English walkthrough explains the processing steps.

[Week 2 (Korean)](../../../materials/week-02/index.html) asks whether two VMs with similar IP addresses can communicate directly on the same network. The distinction between address and port leads into address ranges and route selection.
