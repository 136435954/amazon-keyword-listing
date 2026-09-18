# Keyword analysis method

## End-to-end decision logic

Process every raw keyword through the following gates in order. Do not reverse the order to favor high search volume.

### Gate 1: normalize without destroying the source

- Keep the raw export unchanged.
- In the derived layer, trim whitespace, decode HTML entities, normalize case for matching, standardize decimal separators, and create a normalized keyword key.
- De-duplicate by normalized keyword for the decision library. Preserve the strongest/most complete metric row and retain source-row references when duplicates differ.
- Extract reusable components: brand, color, category root, attribute, audience, scenario, size/material/specification, and suspicious claim.

### Gate 2: product-truth match

Assign one status:

- `confirmed`: explicitly supplied by the user or safely visible in the product image;
- `unconfirmed`: plausible but no evidence supports the exact claim;
- `contradicted`: the product information or image shows the claim is false;
- `not_applicable`: the term describes a different product type or intent.

Product truth is a hard gate. `unconfirmed`, `contradicted`, and `not_applicable` terms cannot enter the Listing or backend search terms. A high search volume never overrides this gate.

### Gate 3: search-intent relevance

Score relevance from 0 to 5:

- **5**: exact product/category or exact confirmed attribute phrase;
- **4**: close synonym or strong functional long tail with the same buying intent;
- **3**: valid use case or broad adjacent category that could describe the product;
- **2**: weak adjacency with substantial ambiguity;
- **1**: mostly unrelated intent with only a shared generic word;
- **0**: incompatible product, false claim, or clear negative term.

Judge the complete phrase, not isolated roots. A phrase with a valid root can still score 0–2 if another component is false, such as wheels, wrong color, unsupported angle, or sleeping function.

### Gate 4: brand, variant, and claim risk

Apply independent flags:

- third-party brand/trademark;
- wrong color or variant;
- unsupported material, size, load, safety, ergonomic, medical, environmental, angle, adjustment, or performance claim;
- prohibited/restricted word from the user's template or marketplace rule;
- misleading audience or product category.

Brand flags block Listing and backend use even when the branded search term is relevant. Store possible advertising use separately and never imply that brand bidding is automatically safe.

### Gate 5: market and competitor evidence

Use available fields without inventing missing data:

- search volume and purchase volume/rate;
- ABA/rank or traffic tier;
- related-product count, product count, title density, supply-demand ratio, and bid range;
- number of comparable competitor ASINs associated with the keyword;
- competitor coverage rate = matched comparable ASIN count / comparable ASIN count.

Competitor overlap is evidence only when the ASINs are genuinely comparable. One very broad high-volume term should not outrank a lower-volume exact category term solely because of traffic.

### Gate 6: class, priority, and activation

Classify the term using the classes below. Then assign:

- Listing eligibility: `title`, `highlights`, `bullets`, `description`, `backend`, or `exclude`;
- advertising use: `exact`, `phrase`, `broad test`, `negative`, `brand-isolated review`, or `do not advertise`;
- priority A/B/C/D;
- explicit evidence and exclusion reason.

Priority decision order:

1. truth and risk status;
2. relevance score and buyer intent;
3. comparable-ASIN overlap;
4. search and conversion evidence;
5. competition/bid considerations.

Use dataset-relative thresholds, such as quantiles or natural tiers, rather than universal search-volume cutoffs. Zero/missing search volume can still be useful for an exact product phrase, but it should not be described as proven high traffic.

## Required keyword-library fields

Keep source metrics and add at least:

- original keyword and normalized keyword;
- translation;
- root/components;
- class;
- product-truth status and evidence;
- relevance score;
- brand/color/risk flags;
- comparable competitor count and coverage rate;
- priority;
- Listing eligibility and recommended placement;
- advertising match/use;
- negative/exclusion reason;
- decision notes.

## Synchronization rule

When the user confirms a product fact, update every dependent view in the same run:

- remove the base attribute from `违规/待确认`;
- add it to confirmed attributes;
- re-evaluate all complete phrases containing it;
- update Listing eligibility, priority, and placement in the keyword library;
- keep mixed-risk phrases excluded when another component remains false or unconfirmed.

## Decision dimensions

Evaluate each term independently on:

1. **Product truth**: exact match, plausible but unconfirmed, or contradicted.
2. **Search intent**: same product, adjacent use case, broad category, or different product.
3. **Market evidence**: keyword volume, purchase/conversion data, rank, and title density when supplied.
4. **Competitor evidence**: number and share of genuinely comparable ASINs associated with the term.
5. **Listing safety**: brand/trademark, unsupported function, wrong color/material/size, regulated claim, or misleading wording.
6. **Activation use**: title, bullets, description, backend terms, exact/phrase/broad ads, negative keyword, or exclude.

Do not use search volume alone as relevance. Do not sum overlapping keyword volumes as unique market demand.

## Recommended classes

- `核心品类词`: directly names the product and matches intent.
- `核心属性词`: confirmed feature attached to a core category term.
- `功能长尾词`: confirmed function or construction detail.
- `场景拓展词`: valid use case but broader intent.
- `颜色词`: activate only for the actual variant.
- `宽泛测试词`: relevant enough for controlled ads but too broad for primary SEO.
- `竞品品牌词`: never place in Listing/backend terms; isolate for risk-reviewed ads if appropriate.
- `属性待确认词`: relevant wording whose claim lacks evidence.
- `不相关/否定词`: different product, false feature, wrong variant, or misleading intent.

## Priority guidance

Use A/B/C/D only when helpful:

- **A**: exact product intent plus strong evidence; primary Listing and exact ads.
- **B**: relevant long-tail or scene term; bullets/description and phrase/exact testing.
- **C**: broad, low-evidence, or variant-dependent term; backend or controlled test only after review.
- **D**: brand risk, false claim, wrong variant, or irrelevant intent; exclude/negative.

Thresholds must reflect the supplied dataset. Do not hard-code one search-volume cutoff across marketplaces or categories.

## Title-candidate selection

Create a title candidate pool only from keywords that are all of the following:

- product truth `confirmed`;
- relevance 4–5, or relevance 3 only when the user intentionally wants a broader scenario term;
- not a competitor brand, wrong variant, or unsupported claim;
- natural in the target language.

Rank title candidates by category exactness first, then dataset search demand and competitor overlap. Specifications such as color, load, dimensions, and material do not displace stronger core category terms unless they define the variant or the user asks for them in the title.

## Required risk sections

List every detected:

- third-party brand/trademark term with Listing and ad guidance;
- color term with current variant match status;
- prohibited, unsupported, or misleading claim with evidence gap and action;
- confirmed attribute previously misclassified as a violation, showing corrected status.

When a phrase contains both a valid attribute and an invalid component, judge the whole phrase. For example, a phrase containing `drehbar` may still be excluded if it also asserts an unconfirmed angle, wrong color, or wheels.
