# Intake Workflow

Use this reference before any lead-mining run. The goal is to ask the user the right questions in a simple, friendly way, confirm the setup, and avoid starting a search with missing or ambiguous requirements.

Only use this intake workflow after the user has already decided to use `b2b-leads-miner`.

If the user is only asking what skills are available, or which skill can help with supplier search, do not start asking these intake questions yet.

## Tone

The target user may be busy, not technical, and not comfortable with AI tools yet.

So the intake should feel like:

- a helpful sales assistant
- short and clear
- practical, not academic
- guided, not overwhelming

Avoid:

- long multi-part questions
- technical jargon
- sounding like a form or survey
- asking everything in one big block unless necessary

## Interaction Pace

Collect the intake step by step.

- Ask one question at a time by default.
- Wait for the user's answer before moving to the next required question.
- Do not dump the whole intake checklist in one message.
- Do not make the user feel like they need to fill out a form.
- If the user is unsure, help them with examples or a suggested default before asking the next question.
- Only bundle multiple items together when the user explicitly asks to move faster.

## Opening Message

Start with a short, reassuring opening before asking questions.

Do not skip the opening message in a real user conversation.
Do not jump directly to the language question.
For beginner users, the opening message is required because it lowers anxiety and explains why the questions are being asked.

Suggested opening:

- `CN`: "我先问你几个很简单的小问题，帮你把这次搜索设置好。这样我后面搜出来的结果会更贴近你的习惯，也方便你下次继续复用。整个确认一般几分钟就可以。"
- `EN`: "I’ll ask a few quick questions first to set up this search properly. That will make the results more relevant and easier to reuse next time. The whole setup usually takes just a few minutes."

Alternative wording:

- `CN`: "开始前我先帮你做个小设置，我会问你几个跟搜索有关的问题，比如关键词、想看的市场、输出格式这些。确认好以后，后面跑起来会更快，也不用每次重复说。"
- `EN`: "Before we start, I’ll help you do a quick setup. I’ll ask a few search-related questions like keywords and output format. Once that’s confirmed, future runs will be faster and easier."

If the user seems impatient, use a shorter version:

- `CN`: "我先快速确认几个小问题，几分钟内搞定，后面结果会更准。"
- `EN`: "Let me quickly confirm a few things first. It only takes a couple of minutes, and the results will be more accurate."

## Opening Conversation Script

Use this when starting a real user conversation. The goal is to sound practical, friendly, and easy to follow.

In a real run, follow the sequence from `Opening` to `Language` to the remaining questions.
Do not start at `Language` unless the user has already seen and acknowledged the opening.

### Recommended Script

1. Opening

- `CN`: "我先问你几个很简单的小问题，帮你把这次搜索设置好。这样我后面搜出来的结果会更贴近你的习惯，也方便你下次继续复用。整个确认一般几分钟就可以。"
- `EN`: "I’ll ask a few quick questions first to set up this search properly. That will make the results more relevant and easier to reuse next time. The whole setup usually takes just a few minutes."

2. Language

- `CN`: "我们继续用中文聊?"
- `EN`: "Should we keep chatting in English?"

3. Search goal

- `CN`: "你想在 Google 搜什么关键词？"
- `EN`: "What search term would you like to use on Google?"

4. Keywords

- `CN`: "你要不要我顺手帮你补几个相关的搜索词，或者优化一下你现在这组关键词？"
- `EN`: "Would you like me to suggest a few related search terms, or optimize your current keywords?"

5. Search limit

- `CN`: "你这次想怎么限制搜索范围？要我按多少家公司来整理，还是按 Google 前几页来搜？"
- `EN`: "How would you like to limit this search? Should I work toward a target number of companies, or stop after a certain number of Google result pages?"

6. Output fields

- `CN`: "我默认会按这套字段帮你整理：`Region`、`Country`、`CompanyName`、`Channel`、`Specialty`、`Scale`、`CoreProductOrMainBusiness`、`EstablishedYear`、`EmployeeCount`、`AnnualRevenue`、`ContactPerson`、`Mail`、`Tel`、`Website`、`Address`、`Source`、`FollowUpStatus`。你先看看能不能接受？"
- `EN`: "By default, I’ll organize the results with these fields: `Region`, `Country`, `CompanyName`, `Channel`, `Specialty`, `Scale`, `CoreProductOrMainBusiness`, `EstablishedYear`, `EmployeeCount`, `AnnualRevenue`, `ContactPerson`, `Mail`, `Tel`, `Website`, `Address`, `Source`, and `FollowUpStatus`. Does this default field set work for you?"
- `CN`: "如果你觉得可以，我就按这套默认字段走。"
- `EN`: "If that looks good to you, I’ll go with this default field set."
- `CN`: "如果你不想用这套字段，也没关系，你可以告诉我想删掉哪些，或者有没有其他想加的字段。"
- `EN`: "If you don’t want to use this set, that’s totally fine. Just tell me which fields you want to remove, or if there are any other fields you’d like to add."

7. Export format

- `CN`: "结果你想要什么格式？"
- `EN`: "What format would you like for the final result?"

8. Save path and filename

- `CN`: "最后文件你想存到哪个路径？文件名你想叫什么？如果你还没想好，我也可以顺手帮你起一个。"
- `EN`: "Where would you like to save the file, and what should the filename be? If you haven’t decided yet, I can suggest one for you."

### Shorter Version

Use this when the user wants to move fast, but still keep the same confirmation structure.

- "我先快速确认几个关键点。"
- "你要在 Google 搜什么产品？pls provide the search term, 还是你想先听我的建议？"
- "你这次想怎么限制搜索范围？要我按多少家公司来整理，还是按 Google 前几页来搜？"
- "输出字段这边，我会先按默认字段给你看；如果你能接受，我就直接按那套走，不行再改。"
- "结果要什么格式？文件存哪里，文件名叫什么？"

### More Supportive Version

Use this when the user sounds unsure or unfamiliar with AI tools.

- "没关系，我们一步一步来，我会尽量问得简单一点。"
- "你先告诉我你这次最想找哪类客户，我再帮你一项项确认。"
- "如果你现在只有产品名也可以，你发给我，我帮你补成适合 Google 搜索的关键词。"
- "如果你没有固定字段，我就先按默认字段给你看，你接受的话我们就直接用。"

### Confirmation Script

Before starting the real run, summarize briefly:

- "我先帮你确认一下这次设置，没问题我就开始搜。"
- "这次我会按这些条件来跑："

Then list:

- language
- search goal
- keywords
- search limit
- output fields:
  `Region`, `Country`, `CompanyName`, `Website`, `Address`, `ContactPerson`, `Mail`, `Tel`, `Channel`, `Specialty`, `Scale`, `CoreProductOrMainBusiness`, `EstablishedYear`, `EmployeeCount`, `AnnualRevenue`, `Source`, `FollowUpStatus`
- export format
- save path
- filename

Close with:

- "如果这些都对，我就按这个版本开始跑。"

## Intake Principles

- Ask short, concrete questions.
- Ask one thing at a time.
- If the user already answered something, do not ask again.
- Suggest a default when the user is unsure.
- Confirm user-controlled limits instead of deciding for them.
- Treat output path and filename as mandatory before export.
- Separate conversation language from exported file language.
- Do not present the intake like a long form the user must complete in one go.

## Recommended Question Style

Good style:

- "我们先确认几个小问题，这样我搜出来的结果会更准。"
- "你想继续用中文还是英文？"
- "你这次主要想找哪类公司？比如英国的泳池设备供应商、欧洲的热泵经销商，或者美国的 pool builder。"
- "你已经有想搜的 Google 关键词了吗？比如 `pool heat pump distributor`、`pool salt chlorinator supplier` 这种，有的话直接发我就行。"
- "你想让我看每个关键词的前几页 Google 结果？比如前 3 页、前 5 页，还是前 10 页。"
- "你最后想让我整理多少条给你？比如先给你 20 家、50 家，还是 100 家。"
- "字段这边我会逐项帮你确认，你可以告诉我哪些要留，哪些不要。"

Avoid style like:

- "Please specify the target company type, geography, output schema, and crawl depth."
- "Select one of the following configuration options."

## Required Questions

Ask these questions before starting the crawl or search run unless the answer is already clearly available from the current conversation or a confirmed saved preference file.

### 1. Conversation language

Suggested wording:

- `CN`: "我们继续用中文聊?"
- `EN`: "Should we keep chatting in English?"

Note:

- This controls the conversation language only.
- It does not automatically control the language of exported file content.
- Ask this question in the same language the user is already using at the start of the conversation.
- The goal is to reduce friction for beginners and avoid an abrupt language switch in the very first intake step.

### 2. Search goal

Suggested wording:

- `CN`: "你想在 Google 搜什么关键词？"
- `EN`: "What search term would you like to use on Google?"
- `CN`: "比如你是想找英国的供应商、欧洲的经销商，还是美国做某类产品的公司？"
- `EN`: "For example, are you looking for suppliers in the UK, distributors in Europe, or companies in the US for a specific product?"
- `CN`: "你是卖什么产品，或者这次想重点找什么类型的公司？"
- `EN`: "What product are you selling, or what type of companies do you want to focus on this time?"

Helpful examples if the user is unsure:

- pool salt chlorinator suppliers
- pool heat pump distributors in Europe
- swimming pool builders in Australia

### 3. Search keywords

Suggested wording:

- `CN`: "你要不要我顺手帮你补几个相关的搜索词，或者优化一下你现在这组关键词？"
- `EN`: "Would you like me to suggest a few related search terms, or optimize your current keywords?"

Then follow up gently:

- `CN`: "我也可以顺手帮你优化一下关键词。你想直接用你的词，还是我给你补几个更容易搜到客户的版本？"
- `EN`: "I can also help optimize the keywords for you. Would you like to use your own terms directly, or should I suggest a few versions that may work better?"
- `CN`: "如果你现在只有产品名也没关系，你发产品名给我，我帮你补成更适合 Google 搜索的词。"
- `EN`: "If you only have the product name right now, that’s fine. Send it to me and I’ll turn it into better Google search terms."

Goal:

- let the user feel supported, not corrected

### 4. Optional geography filter

Ask this only if the user explicitly wants to limit the search by country or region.

Suggested wording:

- `CN`: "你想限定国家或地区吗？如果不想限定，我就直接按关键词去搜。"
- `EN`: "Do you want to limit the search by country or region? If not, I’ll search by keyword directly."
- `CN`: "如果你想加地理限制，可以直接告诉我国家名或地区名。"
- `EN`: "If you want a geographic filter, just tell me the country or region name."

Default rule:

- Do not ask for `Region` or `Country` unless the user wants a geographic filter.
- If the user gives only a keyword, treat the search as unrestricted by geography.

### 5. Search limit

Suggested wording:

- `CN`: "你这次想怎么限制搜索范围？要我按多少家公司来整理，还是按 Google 前几页来搜？"
- `EN`: "How would you like to limit this search? Should I work toward a target number of companies, or stop after a certain number of Google result pages?"
- `CN`: "如果你想按数量来做，可以直接告诉我要 20 家、50 家还是 100 家。"
- `EN`: "If you want to limit it by result count, you can just tell me whether you want 20, 50, or 100 companies."
- `CN`: "如果你想按页数来做，也可以直接告诉我要看 Google 前 3 页、前 5 页，还是前 10 页。"
- `EN`: "If you want to limit it by search depth, you can tell me whether to review the first 3, 5, or 10 Google result pages."

Important:

- The user decides the search limit style.
- Do not ask both page count and company count as two separate required questions.

### 6. Output fields

Suggested wording:

- `CN`: "我默认会按这套字段帮你整理：`Region`、`Country`、`CompanyName`、`Channel`、`Specialty`、`Scale`、`CoreProductOrMainBusiness`、`EstablishedYear`、`EmployeeCount`、`AnnualRevenue`、`ContactPerson`、`Mail`、`Tel`、`Website`、`Address`、`Source`、`FollowUpStatus`。你先看看能不能接受？"
- `EN`: "By default, I’ll organize the results with these fields: `Region`, `Country`, `CompanyName`, `Channel`, `Specialty`, `Scale`, `CoreProductOrMainBusiness`, `EstablishedYear`, `EmployeeCount`, `AnnualRevenue`, `ContactPerson`, `Mail`, `Tel`, `Website`, `Address`, `Source`, and `FollowUpStatus`. Does this default field set work for you?"
- `CN`: "如果你觉得可以，我就按这套默认字段走。"
- `EN`: "If that looks good to you, I’ll go with this default field set."
- `CN`: "如果你不想用这套字段，也没关系，你可以告诉我想删掉哪些，或者有没有其他想加的字段。"
- `EN`: "If you don’t want to use this set, that’s totally fine. Just tell me which fields you want to remove, or if there are any other fields you’d like to add."

Field explanation for user-facing conversation:

- `Region`: 市场区域，不是注册地
- `Country`: 公司所在国家，或网页/资料中显示的主要国家
- `Channel`: 公司在销售链路中的角色，例如 manufacturer、master distributor、distributor、dealer、online store
- `Specialty`: 这家公司和目标泳池分销客户画像的匹配等级
- `Scale`: 公司规模等级，优先按公开营业额判断，没有再参考 dealer 或 network 规模

Resolution logic:

1. Check `assets/output-config/file_columns_userDefine.md`
2. If it contains a real customized schema, use it as the starting point
3. If it is blank, fall back to `assets/output-config/file_columns.md`

Good follow-up wording:

- `CN`: "如果你有自己常用的表头，也可以直接告诉我，我按你的来。"
- `EN`: "If you already have a field layout you usually use, just send it to me and I’ll follow that."
- `CN`: "如果你现在手上有正在用的 Excel 表头，你直接发我，我照着你的表来。"
- `EN`: "If you already have an Excel header row you’re using, send it over and I’ll match your sheet."
- `CN`: "如果你先接受默认字段，我们就先按这个版本走；后面你想删减也可以再调。"
- `EN`: "If you accept the default field set for now, we can start with that version and adjust it later if needed."

### 8. Export format

Suggested wording:

- `CN`: "结果你想要什么格式？"
- `EN`: "What output format would you like?"
- `CN`: "也可以做成 CSV、Markdown、JSON。"
- `EN`: "It can also be exported as CSV, Markdown, or JSON."

Resolution logic:

1. Check `assets/output-config/file_format_userDefine.md`
2. If it contains a value, use it as the starting point
3. If it is blank, fall back to `assets/output-config/file_format.md`

If the user says Excel:

- `CN`: "可以，我按 Excel 方向给你准备。"
- `EN`: "Sure, I’ll prepare it in that format."

### 9. File content language

Ask only if needed.

Suggested wording:

- `CN`: "文件里的内容要保持网页原文，还是你想让我翻译一下？"
- `EN`: "Would you like the file content to stay in the original webpage language, or should I translate it?"

Default rule:

- Keep source webpage language unless the user explicitly asks for translation.

### 10. Output path

Suggested wording:

- `CN`: "最后这个文件你想存到哪个路径？"
- `EN`: "Where would you like to save the final file?"
- `CN`: "你给我一个文件夹路径就行。"
- `EN`: "You can just give me a folder path."
- `CN`: "比如桌面某个文件夹，或者你项目里的一个固定路径。"
- `EN`: "For example, a folder on your desktop or a fixed path inside your project."

Resolution logic:

1. Check `assets/output-config/filepath_userDefine.md`
2. If it contains a real path, use it as the starting point
3. If it is blank, ask the user to provide the save path before export

Important:

- do not invent the save path

### 11. Filename

Suggested wording:

- `CN`: "文件名你想叫什么？"
- `EN`: "What would you like the filename to be?"
- `CN`: "如果你还没想好，我也可以先给你几个命名建议。"
- `EN`: "If you haven’t decided yet, I can suggest a few filename options."
- `CN`: "比如 `uk_pool_suppliers.xlsx`、`europe_heat_pump_distributors.csv` 这种。"
- `EN`: "For example, `uk_pool_suppliers.xlsx` or `europe_heat_pump_distributors.csv`."

Important:

- Filename must be explicitly confirmed before export

### 12. Reuse saved preferences

Ask when prior configuration exists.

Suggested wording:

- "我这边有你之前用过的设置，要不要直接沿用？如果这次有变化，我也可以帮你改。"

## Confirmation Step

Before starting the real search, summarize the confirmed setup in a short checklist.

Suggested wording:

- "我先帮你确认一下这次设置，没问题我就开始搜。"

Checklist:

- conversation language
- search goal
- keywords strategy
- target market
- record count
- search depth
- output fields
- export format
- file content language policy
- save path
- filename

If there are major changes, ask for one final confirmation in a relaxed way:

- "如果这些都对，我就按这个版本开始跑。"

## After Confirmation

If the user wants these answers reusable in future runs, write the confirmed values back into the appropriate files under `assets/output-config/`.

Suggested wording:

- "如果你愿意，我也可以把这次设置记下来，下次你换关键词时就不用重新说一遍。"
