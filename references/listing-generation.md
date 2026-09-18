# Listing generation

The default delivery layout is the eight-section structure in [final-output-format.md](final-output-format.md). Use another layout only when the user explicitly requests it.

## Marketplace adaptation

Write in the target marketplace's native language and natural syntax. The fixed house standard defines sections and target counts. Product-category examples must still pass the product-truth gate. Do not write installation tools, professional users, child use, or technical specifications unless the product data supports them.

Apply the fixed house targets unless the user explicitly changes them. Label them as user production constraints rather than official universal rules.

## Content hierarchy

Prioritize:

1. title: brand followed immediately by the strongest high-traffic exact core category terms, written for fast shopper recognition;
2. item highlights, when the marketplace/category exposes the field;
3. bullets: concrete benefits grounded in confirmed construction and use;
4. description: natural coverage of remaining approved long tails;
5. backend search terms: useful spelling/language variants and approved terms not efficiently covered on the front end.

Avoid keyword stuffing, repeated synonyms that reduce readability, and promises not supported by evidence.

## Keyword allocation logic

Allocate approved terms in this order:

### Title

1. Start with the brand.
2. Add the highest-priority exact category term.
3. Add one additional approved high-traffic core synonym or natural long-tail only when it adds distinct search intent and reads naturally.
4. Stop adding terms when the title begins to read like a keyword list.
5. Keep dimensions, quantity, load capacity, color, material, compatibility, functions, scenarios, and all specifications out of the title. Put them in Item Highlights or bullets.

The title must read naturally in the target language and reflect scan-first shopper behavior: product identity first, supporting core intent second. Record grammatical variants explicitly in the placement table. Search volume breaks ties only among truthful, highly relevant terms; it never justifies a broad or misleading term.

### Item Highlights

Use this field for confirmed specifications and compact differentiators that do not deserve scarce title characters, such as:

- color/variant;
- confirmed load capacity;
- confirmed material, dimensions, quantity, or compatibility;
- backrest, armrests, padding, folding, rotation, or use cases not already needed in the title.

Avoid unnecessary duplication with the title. Always produce this module as part of the fixed deliverable, even when the marketplace UI does not expose it.

### Bullet Points

- Build a fresh five-topic plan for the current product from confirmed facts, consumer decision factors, competitor pain points, and approved keyword intent. Do not reuse a topic sequence from a previous product.
- Write five decision-relevant consumer benefits from confirmed facts.
- Start with the shopper's outcome or problem, then connect the confirmed feature to its practical value and a realistic use situation.
- Use a concise benefit-led phrase plus customer-facing explanation. A material, mechanism, or number is evidence for a benefit, not the whole selling point.
- Distribute approved long tails naturally; do not pad character counts with disclaimers or internal reasoning.
- A missing material/specification does not justify a sentence telling the buyer it is missing. Choose another confirmed benefit instead.
- Each bullet's translation must describe the same consumer-facing content and must not contain internal notes absent from the localized copy.
- Each bullet must answer a different consumer question relevant to the actual category. Installation, accessories, included tools, setup, durability, professional users, and scenarios are optional topics, never mandatory slots.
- Reject low-value filler such as `no assembly required` for pillows, bedding, clothing, and other products where assembly is not a real purchase concern.

### Product Description

- Write from the shopper's journey: intended need and use first, experience/benefits second, realistic scenarios third, and decision-relevant confirmed details last.
- Explain how confirmed construction or functions affect actual use. Do not merely restate the five bullets or concatenate features.
- Use remaining approved long-tail phrases only when the sentence remains idiomatic; otherwise declare a grammatical variant in the placement map or place the exact phrase in backend terms.
- Do not mention keyword strategy, evidence status, future edits, missing fields, confirmation steps, or “refer to images/details” as a substitute for content.
- Keep HTML simple and count only visible text.

### Backend Search Terms

- Fill with approved exact phrases, spelling/language variants, and relevant terms not efficiently covered on the front end.
- Exclude competitor brands, wrong colors, false attributes, restricted terms, and unrelated products.
- Use UTF-8 byte counting and the applicable marketplace/template limit.
- Avoid punctuation when a space-separated format is required. Reduce redundant single-word repetition before deleting useful long tails.

## Customer-facing copy firewall

Before delivery, scan the localized title, Item Highlights, every bullet, product description, and all customer-facing translations for internal workflow language. Reject and rewrite any copy containing concepts such as:

- pending confirmation or missing information;
- “add/fill in later”;
- “according to the image” or “refer to the product page”;
- an explanation of why a term was or was not used;
- keyword/search-form/SEO commentary;
- claims that the wording was intentionally limited because evidence is absent.

These statements may appear only in the internal `基础产品信息合规校验` or `上线前待补充` section. They must never be used to reach a target character count.

## Final validation sequence

1. Check product truth against the product-information sheet and images.
2. Scan front-end copy and translations for internal-review wording.
3. Scan for competitor brands, prohibited words, wrong variants, and unsupported claims.
4. Recount title, highlights, every bullet, visible description text, and backend UTF-8 bytes.
5. Verify each keyword-placement claim by exact match or declared grammatical variant.
6. Confirm high-priority core terms occupy the title before specifications.
7. Confirm each bullet has one distinct product-specific consumer need, supported feature/evidence, and practical benefit; reject inherited topics from unrelated products.
8. Confirm the description has a coherent consumer journey and is not a specification list or keyword container.
9. Render the workbook and check wrapping, merged cells, clipping, and row heights.

## Character and byte counting

- Count visible Unicode characters for localized front-end text unless a template defines another method.
- Count backend terms as UTF-8 bytes. Non-ASCII characters may consume more than one byte.
- Count each section separately and store the result beside the copy.
- Enforce Title 65-70, Item Highlights 120-125, every bullet 300-350, and Search Term 240-249 UTF-8 bytes. Never use unsupported claims or internal notes to reach the range.

## Keyword coverage

Create a placement table with:

- approved embedded keyword and translation;
- normalized grammatical variant, if used;
- exact placement(s);
- coverage status.

The `Listing文案` placement table contains embedded keywords only. Keep non-approved terms and their exclusion reasons in `关键词分析` and `关键词库`; do not repeat them in the Listing worksheet.

`100% coverage` means every approved core keyword appears in all five modules, every other approved keyword appears at least once, and every rejected raw term is listed with its exclusion reason. It never means inserting rejected raw rows into the Listing.

The completed Listing must contain at least 25 unique approved full keyword phrases across the five modules. Normalize and de-duplicate before counting. A repeated phrase counts once; a root does not count as coverage of a longer phrase; Chinese translations and excluded phrases do not count. If the approved pool contains fewer than 25, stop final delivery and report the gap rather than weakening relevance or inventing terms.

## Pre-launch gaps

Keep missing facts visible, commonly:

- SKU/ASIN;
- dimensions and folded dimensions;
- net weight and packaging;
- confirmed material and filling;
- exact adjustment positions/angles;
- rotation range;
- assembly or folding instructions;
- package contents and warranty terms.

Do not block a first draft when these facts are unnecessary to truthful core copy.
