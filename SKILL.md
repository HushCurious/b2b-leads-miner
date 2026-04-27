---
name: b2b-leads-miner
description: Use this skill when the user wants a B2B lead mining workflow by searching Google and reviewing company websites or directory pages, then exporting the results as a file. Trigger it for tasks such as searching product keywords in Google, filtering out irrelevant pages, extracting supplier or company information, structuring fields like website, phone, email, and address, and saving the output to a user-specified path and filename.
---

# b2b-leads-miner

## Overview

Use this skill when a user wants to search Google and public company pages for B2B supplier information, reduce manual page review, and export the result as a structured file for follow-up.

By default, this skill uses:

- [file_columns.md](assets/output-config/file_columns.md) for the default output fields
- [file_format.md](assets/output-config/file_format.md) for the default export format

If the user wants a different field set, format, or save path, use the corresponding `*_userDefine.md` files as overrides.

Use these files as the main references:

- [references/background.md](references/background.md): business context and target user
- [references/intake-workflow.md](references/intake-workflow.md): intake questions and confirmation flow
- [references/lead-spec.md](references/lead-spec.md): the structured spec to build before search
- [references/export-rules.md](references/export-rules.md): export structure, row rules, and output behavior
- [references/browse-rules.md](references/browse-rules.md): when to stop at the homepage and when to keep clicking deeper

Use the files in [assets/output-config](assets/output-config) as the output-configuration layer:

- [file_columns.md](assets/output-config/file_columns.md): default field schema and field dictionary
- [file_columns_userDefine.md](assets/output-config/file_columns_userDefine.md): user override for field schema
- [file_format.md](assets/output-config/file_format.md): default format rule
- [file_format_userDefine.md](assets/output-config/file_format_userDefine.md): user override for format
- [filepath_userDefine.md](assets/output-config/filepath_userDefine.md): user-specified save path

Use [scripts/resolve_output_config.py](scripts/resolve_output_config.py) when you need a deterministic way to resolve default files vs user override files.

## When To Use

Use this skill when the user asks to:

- search public web results for suppliers, distributors, builders, manufacturers, or B2B buyers
- mine leads from keyword-based search terms such as product names or market categories
- extract company data into a reusable file
- export the result in Excel or another user-requested format

## Stage Control

Treat the interaction as having exactly 2 stages:

- `recommendation`
- `intake`

### `recommendation`

Use `recommendation` only when the user is asking which skill can help, what skills are available, or whether there is a skill for supplier search.

Required behavior in `recommendation`:

- Recommend `b2b-leads-miner`.
- Briefly state what it helps with.
- Stop.

Forbidden behavior in `recommendation`:

- Do not ask any question.
- Do not ask for product, market, country, quantity, format, path, filename, or any other setup detail.
- Do not include intake, execution guidance, examples, defaults, or next-step prompts.
- Do not say or imply "reply with these details" or "just answer these few questions".

### `intake`

Enter `intake` when either of these is true:

- the user explicitly chooses `b2b-leads-miner`
- the user directly asks the assistant to help find suppliers or do the supplier-search task

Required behavior in `intake`:

- Always follow [references/intake-workflow.md](references/intake-workflow.md) in order.
- Do not skip the opening message.
- Do not jump directly to later questions.

Do not use this skill for:

- private-data scraping, login-only pages, or restricted data extraction
- mass email sending
- fake contact enrichment or guessed emails

## Execution Workflow

Start this workflow only after the interaction has entered `intake` as defined above.

1. Follow [references/intake-workflow.md](references/intake-workflow.md) to collect the user's search goal, keywords, market, limits, output fields, format, save path, and filename.
2. Use [references/lead-spec.md](references/lead-spec.md) to turn the request into a clean execution spec.
3. Resolve default vs user override files in `assets/output-config/`.
4. Search public sources first, then use [references/browse-rules.md](references/browse-rules.md) to decide whether deeper browsing is worth it.
5. Extract only evidence-backed values and follow [references/export-rules.md](references/export-rules.md) for row rules and export behavior.
6. Export the result to the confirmed path and filename.

## Output Rules

The final exported file should be practical for sales follow-up. Unless the user specifies otherwise, structure rows around companies rather than people.

The file language should follow the source webpage language by default, not the conversation language.

Never fabricate:

- direct email addresses
- phone numbers
- company size
- product category fit

## Response Style

Keep the interaction simple and guided. The target user may be new to AI tools, short on time, and easily overloaded by too many choices.

- In `recommendation`, stay at recommendation level only.
- In `intake`, follow the question order from `references/intake-workflow.md` and ask only the current step.
- ask short concrete questions
- avoid jargon
- suggest defaults when the user is unsure
- confirm critical settings before running
- be explicit about missing information

## Safety And Quality

- Respect public-web and site-access boundaries.
- Do not claim to access hidden or private data.
- Do not browse logged-in content unless the user explicitly provides access and the environment supports it.
- Do not pretend a search was executed if it was not.
- If web access or model access is unavailable, say so clearly and stop at the setup stage.
