# Hands-on Computer Networks

Summary: Learn computer networking through explanations, Linux experiments, packets and logs. The English path covers the home, study guidance and Week 1 core materials; the full course is in Korean.

**[English learning site](https://ostenhun.github.io/hands-on-computer-networks/en/)** · [한국어](README.md) · [English lesson sources](content/en/materials/week-01/)

Follow one request from curl to a Python server. Compare HTTP 200, HTTP 404, connection refusal and recovery; explain where the command runs and which addresses and ports identify the endpoints.

The materials are for students learning networking fundamentals, developers investigating communication problems, and study groups comparing evidence. They began in the fourth network study group of [Aolda](https://aoldacloud.com/), the cloud operations club at Ajou University, and are open to learners outside the group.

## Start with Week 1

1. Choose the [central question](https://ostenhun.github.io/hands-on-computer-networks/en/materials/week-01/worksheet.html).
2. Read the [concepts](https://ostenhun.github.io/hands-on-computer-networks/en/materials/week-01/concepts.html) and selected [original sources](https://ostenhun.github.io/hands-on-computer-networks/en/materials/week-01/sources.html).
3. Run the [Linux experiment](https://ostenhun.github.io/hands-on-computer-networks/en/materials/week-01/linux.html), predicting first and changing one condition at a time.
4. Read your own packets, or identify the [supplied capture](https://ostenhun.github.io/hands-on-computer-networks/en/materials/week-01/sample-capture.html) as example analysis.
5. Attempt the [review](https://ostenhun.github.io/hands-on-computer-networks/en/materials/week-01/review.html) before opening its separate explanations.

Use **한국어 / English** at the top of a translated page to read its counterpart. Search follows the current language. On Korean-only pages, **English home** links to the English starting point rather than pretending that the current page is translated. Optional links labeled “Korean” retain their original language. Weeks 2–16 are available through the Korean home.

The required lab uses Python 3.10+, curl and an authorized Linux environment; Node is optional. Capture requires appropriate permissions. Use your own connection details, keep predictions separate from observations, and never put passwords or tokens into your notes. Browser answer fields do not autosave or submit work: download and check the file before leaving.

## Reuse and contribute

Lesson Markdown, practice files and official-source links live in this repository. Follow the [authoring guide (Korean)](docs/AUTHORING.md) for content changes and the [operations guide (Korean)](docs/OPERATIONS.md) for the publication boundary. External reading remains subject to its original attribution and reuse terms. Do not include participant details, credentials, private environment values or raw operational evidence in contributions.

The site is built from public sources with Astro and published on GitHub Pages. To validate a checkout, run `npm ci --ignore-scripts`, `npm test` and `npm run build` using the Node version declared in `package.json`. Building locally does not publish the site or establish that a learner completed the experiments.
