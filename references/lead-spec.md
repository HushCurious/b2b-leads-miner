# Lead Spec Reference

Use this reference when the user's request is broad, messy, or underspecified.

## Intake Checklist

Capture these fields before running the search:

| field | what it means | example |
| --- | --- | --- |
| language | conversation language | Chinese |
| product_or_offer | what the user sells | pool heat pump |
| target_keywords | search terms to use | pool heat pump distributor |
| keyword_strategy | keep user terms, suggested terms, or both | both |
| target_market | geography or region | Australia |
| target_company_type | who to find | distributors |
| search_depth | how many search-result pages per keyword | first 5 pages |
| desired_count | number of leads | top 50 |
| output_fields | columns to export | Website, Tel, Mail |
| output_format | file format | excel |
| file_content_language | keep source language or translate | keep source language |
| output_directory | save path | `/Users/name/Desktop/leads` |
| filename | output filename | `australia_pool_distributors.csv` |

## Field Source Of Truth

Do not define field meanings in this file.

Use these files instead:

- `assets/output-config/file_columns.md`: canonical default field dictionary
- `assets/output-config/file_columns_userDefine.md`: user override field dictionary
- `references/export-rules.md`: row model, fill policy, normalization, and export quality rules

## User-Controlled Limits

The user should decide these limits, not the agent:

- how many search-result pages to review per keyword
- how many records to return

The agent may suggest practical defaults, but must let the user confirm.

## Language Rule

- Conversation language is chosen by the user for the interaction.
- Exported file content should keep the source webpage language by default.
- Translate exported content only when the user explicitly requests it.

## Common Filtering Logic

Keep pages that are likely to represent:

- suppliers
- manufacturers
- distributors
- builders
- B2B service providers

Filter out when possible:

- ads
- consumer-only shops
- marketplaces with no company details
- duplicate domains
- irrelevant content pages
