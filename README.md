# b2b-leads-miner

A Codex skill for finding B2B suppliers from public web sources and exporting the results as structured files.

It is designed for workflows like:

- finding suppliers, distributors, wholesalers, manufacturers, or dealers
- searching Google with product or market keywords
- reviewing company websites or directory pages
- extracting evidence-backed company information
- exporting results to formats like Excel, CSV, Markdown, JSON, or TXT

## What This Skill Does

`b2b-leads-miner` helps an agent run a guided supplier-search workflow:

1. confirm the search setup with the user step by step
2. search public web results
3. review relevant company pages
4. extract structured company information such as:
   - company name
   - website
   - phone
   - email
   - address
   - business role in the channel
5. export the final results as a reusable file

This skill is especially useful when the user wants a practical lead list for follow-up rather than a long prose summary.

## Best For

- supplier discovery
- distributor scouting
- importer / wholesaler lead mining
- market-entry research
- channel mapping for B2B sales

## Not For

- scraping private or login-only data
- guessing emails or hidden contact information
- mass outreach
- fake enrichment

## How The Interaction Works

This skill has 2 strict stages:

### 1. Recommendation

If the user is only asking which skill can help, the agent should:

- recommend `b2b-leads-miner`
- briefly explain what it does
- stop

At this stage, the agent should **not** ask setup questions.

### 2. Intake

If the user explicitly chooses this skill, or directly asks the agent to help find suppliers, the agent starts the intake workflow.

The intake flow is intentionally guided and beginner-friendly:

1. opening message only
2. language question only
3. one question at a time after that

This prevents the user from being overloaded by a long checklist too early.

## Installation

### Option 1: Local manual install

Place the folder into your local Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R b2b-leads-miner ~/.codex/skills/
```

### Option 2: Install from a Git repository

If this skill is published in a GitHub repository and your environment supports the Skills CLI:

```bash
npx skills add <owner>/<repo>@b2b-leads-miner
```

Replace `<owner>/<repo>` with the actual GitHub repository path.

## Repository Structure

```text
b2b-leads-miner/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── background.md
│   ├── browse-rules.md
│   ├── export-rules.md
│   ├── intake-workflow.md
│   └── lead-spec.md
└── scripts/
    └── resolve_output_config.py
```

## How To Use

### Example 1: Ask which skill can help

User:

```text
请帮我找下供应商信息，你有什么 skills 可以帮我
```

Expected behavior:

- the agent recommends `b2b-leads-miner`
- the agent does not begin intake yet

### Example 2: Start the workflow directly

User:

```text
我想找供应商信息
```

Expected behavior:

- the agent starts the intake workflow
- the first reply is the opening message only
- the next reply asks the language question only

### Example 3: Explicitly choose the skill

User:

```text
用 b2b-leads-miner 帮我找澳洲市场泳池设备供应商，并整理成 Excel
```

Expected behavior:

- the agent enters intake
- the agent follows the question order in `references/intake-workflow.md`
- the agent collects only one setup item at a time

## Output Formats

This skill can support outputs such as:

- `Excel (.xlsx)` for filtering and follow-up work
- `CSV` for importing into other systems
- `Markdown` for readable text output
- `JSON` for programmatic use
- `TXT` for simple plain-text storage

If the user is unsure, `Excel (.xlsx)` is usually the best default recommendation.

## Data Quality Rules

This skill is designed to keep output practical and trustworthy.

It should:

- keep only evidence-backed values
- leave fields blank when the source is unclear
- preserve source-language content by default
- avoid fabricating phone numbers, emails, company size, or revenue

## Included References

- `references/intake-workflow.md`
  Controls stage gating, the opening message, and question order.
- `references/lead-spec.md`
  Defines the structured execution spec collected from the user.
- `references/export-rules.md`
  Defines export structure and row behavior.
- `references/browse-rules.md`
  Helps decide whether deeper browsing is worth it.
- `references/background.md`
  Provides business context for the workflow.

## Publishing Tips

If you want to publish this skill publicly, these are good next steps:

1. keep `SKILL.md` concise and agent-facing
2. keep `README.md` human-facing and onboarding-focused
3. include 2-3 realistic usage examples
4. explain the stage behavior clearly
5. document supported output formats
6. state the safety boundaries explicitly
7. remove unnecessary local files like `.DS_Store` before publishing

## Recommended Release Checklist

- `SKILL.md` is accurate and concise
- `README.md` explains install and usage clearly
- `agents/openai.yaml` matches the skill behavior
- example prompts reflect the current stage-control rules
- no private files or machine-specific junk files are included

## License

Add your preferred license before publishing publicly.
