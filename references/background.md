# b2b-leads-miner Background

## Why this skill exists

This skill is designed for B2B sales users who still collect leads manually from Google and public web pages.

A real example behind this skill:

- a salesperson sells pool-related products
- she searches terms like `pool salt chlorinator`, `pool heat pump`, `pool lights`, `swimming pool distributor`, and `pool builder`
- she opens many search results manually, often reviewing the first 5 pages
- she filters out junk pages one by one
- she copies useful supplier details into Excel

The work is repetitive and tiring, even though the final data needed is simple.

## User pain points

### 1. Too much manual clicking

The user spends too much time opening result pages, checking whether the company is relevant, and copying details by hand.

### 2. Too much junk information

Search results often include:

- ads
- consumer-facing pages
- irrelevant pages
- low-quality directories

This wastes time and attention.

### 3. Low AI adoption tolerance

Many cross-border sales users are curious about AI, but they do not want a complex setup flow. They need something that feels practical and easy, not a tool that makes them feel they need to study a new system before getting value.

## Product direction

This skill should feel like a guided sales assistant, not like a developer tool.

The ideal experience:

1. Ask the user a few simple setup questions.
2. Confirm the search scope and output schema.
3. Run one live search task.
4. Export the result as a file to the exact path and filename the user asked for.

## Quality bar

A good result should:

- save the user real research time
- contain mostly relevant B2B companies
- avoid obvious junk pages
- leave missing information blank instead of making up data

## Non-goals

This skill should not try to:

- scrape private or login-protected data
- send outreach automatically
- promise perfect coverage of all search results
- force the user into automation if they only want a one-time run
