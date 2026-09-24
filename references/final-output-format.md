# Default final output format

Use this structure for the final `Listing文案` worksheet and for a chat-only Listing response. For workbook delivery, populate the bundled template defined in [excel-template-contract.md](excel-template-contract.md). The order, labels, ranges, and required details are fixed unless the user explicitly requests a change.

## 1. 基础产品信息合规校验

Include:

- brand;
- SKU/ASIN or `待创建`;
- confirmed product facts;
- excluded or unconfirmed facts;
- marketplace and language;
- a concise statement that raw keywords were filtered for truth, relevance, brand risk, and variant match.
- target-marketplace unit convention and a concise source-to-localized conversion record;
- `规则版本：KAIHA-LISTING-2026-V11`.

Any workbook missing this exact profile ID is not a valid final deliverable. The current exact profile ID is `KAIHA-LISTING-2026-V11`.

## 2. 主标题 Title

Show:

- localized title;
- Chinese reference translation;
- exact visible-character count and target range;
- keyword placement details with keyword type.
- title formula: brand + highest-traffic approved core category term + one natural secondary core term/long-tail when space permits;
- fixed target: 65-70 visible characters.

Specifications such as dimensions, quantity, load capacity, color, material, and compatibility belong in Item Highlights. The title must lead with recognizable product identity and read as natural customer-facing language, never as a keyword list.

Display `字符统计：XX / 70（严格控制 65-70）`. Treat this as a user production constraint, not a universal official Amazon rule.

## 3. 商品亮点 Item Highlights

Show:

- localized highlight text;
- Chinese translation;
- character count and target;
- short-sentence keyword mapping.
- fixed target: 120-125 visible characters;
- short clauses separated by ` | `.

Display `字符统计：XX / 125（严格控制 120-125）`.

## 4. 五点描述 Bullet Points

Provide exactly five bullets. For every bullet include:

- localized copy in `【概括短语】正文` format when compatible with the marketplace;
- Chinese translation;
- individual character count;
- exact embedded keywords and sentence positions.
- fixed target: 300-350 visible characters per bullet, including brackets, spaces, and punctuation.

Keep exactly five bullets, but derive and rank their topics for the current product. Do not use a fixed cross-category order. Display `本条字符统计：XX / 350（300-350 区间）` for each bullet.

Each bullet must be benefit-led and answer a different consumer purchase question. Present confirmed features and specifications as evidence for practical value, not as an isolated feature list.

In the internal compliance section, list the five selected bullet topics and why each matters for the current product. This planning note must not appear in localized buyer-facing copy.

## 5. 产品描述 Product Description

Show:

- localized HTML description using simple supported paragraph/bold tags;
- full Chinese translation;
- visible-text character count excluding HTML tags;
- paragraph-level keyword mapping.

Do not include speculative specifications or keyword-stuffed sentence fragments.

The description must follow a consumer journey: intended need/use, practical experience and benefits, realistic scenarios, then decision-relevant confirmed details. It must not simply repeat the bullets or list remaining keywords.

## 6. 后台搜索关键词 Search Term

Show:

- one space-separated backend search-term string;
- UTF-8 byte count with fixed target 240-249 bytes;
- supplemental terms with Chinese meanings;
- deliberately repeated core terms, if any, with rationale.

Exclude competitor brands, false attributes, wrong colors/variants, and prohibited words. Use spaces only, with no punctuation or vertical bars. Display `字节统计：XX / 249（严格控制 240-249）`.

## 7. 关键词位置核验表

Columns:

| 序号 | 已埋入关键词（本地语言 + 中文释义） | 标准化/语法变体 | 埋词位置 (Placement) | 覆盖确认 |
| --- | --- | --- | --- | --- |

List only approved keywords that are genuinely present in at least one Listing module. Every approved core keyword must show all five modules; every other listed keyword must show its actual placement. Do not add rows for excluded, risky, irrelevant, brand, wrong-variant, or unconfirmed terms. Their accounting belongs in `关键词分析` and `关键词库`.

Above or below the table, display `实际埋入关键词数：N / 25`. Count unique approved full phrases only. The final workbook must contain at least 25; repeated placements of one phrase count once.

## 8. 全链路合规与埋词自检

Check and report:

1. title length, structure, prohibited symbols, promotional/unsupported claims;
2. Item Highlights length and formatting;
3. each bullet's format and character count;
4. approved embedded-keyword coverage in the Listing table, with excluded-term accounting verified separately in `关键词分析` and `关键词库`;
5. minimum unique embedded-keyword count `N >= 25`;
6. product-fact consistency;
7. competitor-brand and infringement risk;
8. backend UTF-8 byte count, separators, duplicates, and prohibited terms;
9. localized copy and Chinese translation completeness.
10. marketplace-local units, conversion accuracy, rounding consistency, and agreement between localized copy and Chinese translation.

## Spreadsheet presentation

- Use `assets/amazon-keyword-listing-output-template.xlsx`; never redesign the workbook from scratch.
- Keep the template's six sheets and their order. Put these eight sections in its existing `Listing文案` worksheet.
- Preserve its dark-blue section bands, label columns, merged ranges, fills, fonts, borders, wrapping, widths, heights, filters, panes, charts, and visible character/byte-count positions.
- Write into existing merged ranges only through their top-left cells. Never flatten the A:J layout into ordinary A:E columns or display headings in narrow unmerged cells.
- Preserve the keyword library and raw data sheets in the same delivered workbook.
- Extend tables only when the current dataset exceeds the template capacity, copying the closest equivalent row's structure and formatting.
- Remove all old product/sample content before filling current data.
- Render every sheet and correct clipping, row height, wrapping, or broken merged-cell problems before export.
- In every `工作目标` cell, use only the fixed ranges from this profile. The strings `120-180`, `内部工作目标`, `建议范围`, and other substituted ranges are prohibited.
