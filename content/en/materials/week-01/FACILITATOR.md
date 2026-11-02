# Week 1 facilitator guide

Summary: Connect execution location, IP and port, and HTTP responses with the Linux lab. Check preparation, compare evidence and use alternatives without treating demonstrations as each learner's execution.

## Connect concepts with questions

Use [essentials](ESSENTIALS.md) to answer an existing shared question, then ask how a changed condition would alter it and which evidence would narrow the cause. Open the [developer explanations](ANSWERS.md#developer-scenarios) after attempting them.

Review prompt: “How does localhost's target change if the previous request runs in the PC shell rather than the remote shell?”

## Check the environment

If VM access is new, use the [SSH preparation guide (Korean)](../../../materials/ssh-top-down/FACILITATOR.md). Split the HTTP lab according to actual preparation needs.

| Item | Evidence |
| --- | --- |
| Permitted Linux access | The learner opens a shell and checks the connection destination/account |
| Two shells on the same host | Compare connection destinations, hostname and working directory |
| Files and tools | server.py location, Python and curl versions |
| Start, stop and recovery | Listening log, first 200, Ctrl+C and restart |
| Packet observation | `lo` and capture privileges, or supplied capture ready |
| Record retention | Download answers and open the saved file |

Do not put passwords, keys or real connection details into shared records. Redact identifying addresses and hostnames before sharing output.

## Explore and explain together

Use the [central question](WORKSHEET.md): how do normal, 404 and connection failure differ at the same server address? Find the relevant [concepts](CONCEPTS.md), RFC 9110 sections for 200/404, and curl exit-code documentation. The [reading guide](ARTICLE_LESSON.md) provides a fallback when source access is blocked.

One possible 60-minute concept discussion is: ten minutes revisiting concepts/questions, twenty exploring, fifteen explaining, ten asking changed-condition questions, and five preparing the lab. This is a suggestion, not a fixed schedule or requirement to answer every optional question. Rotate explainers and involve everyone in output reading and changed-condition reasoning.

Do not add long presentations or fixed record forms. Keep raw output once in each learner's own files and show only relevant evidence during discussion.

## Compare four states on Linux

Each learner follows the [lab](LINUX.md): normal → 404 → stop → restart on the same port. Match output, server logs and packets by addresses and ports. Change one condition and rerun without help, then restore the baseline.

Use the [supplied capture](SAMPLE_CAPTURE.md) when capture is blocked. Distinguish supplied-file analysis from direct capture and leave unobserved results blank.

## Common problems

| Symptom | First check | Continue with |
| --- | --- | --- |
| Missing file | `pwd`, `ls`, transfer destination | Correct the location and retry |
| Connection failure | Execution host, listening socket and URL | Controlled stop/recovery at the same endpoint |
| Port conflict | Your process and occupied port | Stop only your server or change the service port consistently |
| Empty capture or no privileges | `lo`, timing, filter and permissions | Supplied capture; complete direct capture later |

Use the [lab's alternatives](LINUX.md#if-the-environment-blocks-you) for details. If setup takes too long, continue learning through a demonstration or example analysis while leaving direct execution incomplete.

## Finish with an explanation

Ask each learner to explain normal/404/failure/recovery, localhost's execution environment, and server versus temporary port in their own words. Attempt the [review](REVIEW.md), then compare with [answers](ANSWERS.md). Another person's execution or opening an example is not your own direct work.
