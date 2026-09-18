# Keyword library construction logic

Follow this decision sequence. Do not rank keywords before the product-truth and risk gates are complete.

## 1. Establish the product truth table

Create one authoritative product-fact table from user-provided data and clearly visible image evidence:

- product type and intended marketplace;
- brand and variant;
- confirmed functions and structural features;
- confirmed colors, dimensions, materials, weight/load claims, package contents, and scenarios;
- unresolved or contradicted attributes;
- evidence source for every material claim.

Use three states: `已确认`, `待确认`, `不具备/不匹配`. User confirmation overrides an earlier tentative image judgment. A keyword metric never confirms a product feature.

## 2. Preserve and normalize source data

- Keep the raw export unchanged.
- Normalize a derived copy: trim whitespace, decode HTML entities, normalize case for matching, preserve original spelling for reporting, and deduplicate by normalized full phrase.
- Preserve ASIN/SKU as text.
- Map equivalent export headers rather than assuming one fixed SellerSprite schema.
- Parse numeric fields as numbers and keep source units/periods visible.

## 3. Apply hard gates in order

For every full keyword phrase, evaluate:

1. **Third-party brand gate**: if it contains a competitor brand/trademark, classify as `竞品品牌词`; exclude from Listing/backend terms.
2. **Product-truth gate**: if the phrase asserts a wrong product type, color, material, size, function, audience, accessory, or variant, classify as `不相关/否定词`.
3. **Unsupported-claim gate**: if the phrase is relevant but relies on an unconfirmed feature, classify as `属性待确认词`; do not use until evidence is supplied.
4. **Intent gate**: classify remaining phrases as exact product intent, adjacent scenario, or broad discovery intent.

Judge the complete phrase, not an isolated valid word inside it. A phrase containing a valid term such as `drehbar` still fails when it also includes an unconfirmed angle, wheels, a wrong color, or another product type.

## 4. Classify approved terms

- `核心品类词`: exact product identity; primary SEO and exact advertising seed.
- `核心属性词`: core category plus a confirmed differentiator.
- `功能长尾词`: confirmed function expressed as a useful long-tail phrase.
- `场景拓展词`: plausible use case with broader intent.
- `颜色词`: only active for the matching variant.
- `宽泛测试词`: high-volume adjacent term that is not precise enough to lead the Listing.

Keep rejected classes separate: `竞品品牌词`, `属性待确认词`, `不相关/否定词`.

## 5. Evaluate evidence and demand

Use available signals without pretending they are independent:

- relevance to the exact product;
- number/share of genuinely comparable competitor ASINs associated with the term;
- monthly search volume or rank;
- purchase volume/rate or conversion signal;
- title density/competition;
- PPC bid and advertising competitor count;
- phrase specificity and buyer intent.

Do not use search volume alone. A very large generic term can remain a broad advertising test rather than a title keyword. Do not add overlapping phrase volumes together as unique market demand.

## 6. Assign priority

Use this decision ladder:

- **A**: exact product intent, confirmed truth, no risk, and strong market or competitor evidence. Use in title/primary bullets and exact ads.
- **B**: relevant confirmed function or scenario with useful demand. Use in bullets/description and exact/phrase ads.
- **C**: broad, low-evidence, language variant, or variant-dependent term. Use in backend terms or controlled ad testing only when appropriate.
- **D**: brand risk, false claim, wrong variant, misleading intent, or different product. Exclude and add to negative/risk lists.

Dataset-relative thresholds are allowed for sorting within A/B/C. Never use a universal volume cutoff across countries or categories.

For repeatable scoring within one uploaded dataset, calculate a `排序分` only after all hard gates:

- relevance: 0-40;
- exact buyer intent: 0-20;
- normalized dataset-relative demand: 0-15;
- genuinely comparable competitor coverage: 0-15;
- purchase/conversion evidence: 0-10;

Use `A = 75-100`, `B = 55-74`, `C = 0-54`. Any hard-gate failure is `D` regardless of score. Missing metrics contribute zero; do not invent them. The score sorts approved phrases but never overrides product truth, brand risk, or variant match.

## 7. Required keyword-library columns

Include, when source data permits:

- keyword and translation;
- normalized phrase/root;
- classification and relevance;
- product-fact status and evidence;
- priority;
- Listing eligibility and exact placement;
- advertising action and match type;
- negative/exclusion action;
- competitor coverage count/rate and related ASINs;
- search/purchase/conversion metrics;
- competition/title-density/bid metrics;
- risk explanation.

## 8. Required review sections

The analysis must explicitly list:

- every detected third-party brand and restriction explanation;
- every color and whether it matches the current variant;
- every unsupported/prohibited/misleading phrase with reason and required evidence/action;
- confirmed attributes that were previously tentative, shown as corrected and synchronized into the keyword library.

## 9. Synchronization checks

Before delivery:

- confirm that approved attributes are not still labeled violations;
- confirm that every A/B keyword has an intended Listing/ad use;
- confirm that every D keyword has an exclusion reason;
- confirm that brand/color/risk summary sections reconcile to row-level classifications;
- confirm that whole phrases containing mixed valid/invalid components remain correctly excluded.
- confirm that counts by classification in the summary equal row-level counts in `关键词库`;
- confirm that the same normalized phrase has one authoritative final classification;
- confirm that every source row remains traceable to a normalized-library row.
