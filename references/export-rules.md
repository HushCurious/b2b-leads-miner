# Export Rules

Use this reference when deciding what fields to export, how to normalize them, and how to handle blanks or uncertain values.

## Purpose

This skill is not only about finding company names. The exported file should be usable for real sales follow-up without forcing the user to clean the table again by hand.

That means the agent should:

- export one row per company unless the user explicitly wants person-level rows
- keep field meanings stable across runs
- leave unverifiable fields blank instead of guessing
- preserve the source-language value for company names, addresses, and product labels unless the user explicitly asks for translation

## Source Of Truth

This file is not the canonical field dictionary.

Field names, meanings, and suggested values should live in:

- `assets/output-config/file_columns.md`
- `assets/output-config/file_columns_userDefine.md`

This file only defines:

- row model
- field selection order
- fill policy
- missing-data policy
- normalization policy
- output quality checks
- supplementary export rules

## Row Model

Default row model:

- one row = one company

Do not create multiple rows for the same company just because:

- the company has several products
- the company has several emails
- the company has multiple branch addresses on one page

If multiple values exist, use the best public primary value.

## Field Selection Rule

Choose fields in this order:

1. user-requested fields from the conversation
2. `assets/output-config/file_columns_userDefine.md` if it contains a real customized schema
3. otherwise `assets/output-config/file_columns.md`

If a user asks for extra fields not listed in the default dictionary, add them when they can be grounded in public evidence.


## Supplementary Rules

### Code-only export fields

For `Channel`, `Specialty`, and `Scale`:

- when talking with the user, you can explain the meaning in plain language
- when exporting the file, write only the code or level value
- do not write the explanation text inside the table cell

Example:

- `Channel`: write `A`, `B1`, `B2`, `B3`, `C1`, `C2`, or `C3`
- `Specialty`: write `1`, `2`, `3`, `4`, or `5`
- `Scale`: write `1`, `2`, `3`, `4`, or `5`

If the user wants to see what the codes mean, put the explanation at the end of the file, not in each row.

### User-specific customization

Other users or other industries may need a different coding system, especially for `Channel`.

If the current coding system does not fit the user's business, confirm a new one before export.

### Maintenance rule

`Channel`, `Specialty`, and `Scale` use business scoring logic defined by sales and should stay consistent across runs.

## Fill Rules

### CompanyName

- Prefer the official company name shown on the site header, footer, contact page, or about page.
- If a directory listing and the official site disagree slightly, prefer the official site version.

### Mail / Tel / Address

- Only use public values visible on the page or directly linked subpages.
- Do not infer missing contact info from domain patterns.
- If several values are shown, prefer the main headquarters or main sales contact unless the user asked for branch-level detail.

### Website

- Prefer the official domain for `Website`.

## Missing Data Rule

When a field is missing:

- leave it blank
- do not fabricate

Good example:

- `Mail`: blank when no public email is shown

Bad example:

- guessing `sales@domain.com`
- converting a contact form into a fake email value

## Normalization Rule

Normalize only when safe and low-risk:

- trim obvious whitespace noise
- keep full URLs
- standardize phone spacing lightly if the country code is already visible
- preserve original company names and addresses

Do not over-normalize when it may destroy useful source detail.

## Final Check Before Export

Before exporting, quickly check:

1. The same company is not listed more than once.
2. Each row represents one real company.
3. No values are guessed or fabricated.
4. Basic fields like `CompanyName`, `Website`, and `Source` are filled when the information is publicly available.
