# Fixed Listing writing standard

This is the user's mandatory house standard. Do not change its order, modules, ranges, or coverage definition when the product changes unless the user explicitly requests a new profile.

Build buyer-facing copy only from approved keywords and `已确认` product facts. Do not begin drafting until the keyword library, product truth table, and module allocation plan are complete. Missing facts remain only in the internal pre-launch section.

## Priority and counting

- Weight order: `Title = Item Highlights > Bullet Points > Product Description > Search Term`.
- Count visible localized text characters: letters, digits, spaces, punctuation, hyphens, brackets, and vertical bars each count as one character. Exclude HTML tags from description counts.
- Count Search Term in UTF-8 bytes.
- Fixed targets: Title 65-70 characters; Item Highlights 120-125; every bullet 300-350; Search Term 240-249 bytes.
- These are user-defined production constraints. Do not call them universal official Amazon limits.

## Marketplace measurement units

Localize every buyer-facing dimension, weight, volume, capacity, and temperature to the units normally used by shoppers on the target marketplace. Determine the marketplace before conversion and keep a traceable conversion table in the internal product/compliance area.

- United States: lead with inches (`in`), feet only when natural, pounds (`lb`), and ounces (`oz`). Use Fahrenheit only when temperature is relevant.
- Germany and most continental EU marketplaces: lead with millimetres/centimetres/metres (`mm`, `cm`, `m`), grams/kilograms (`g`, `kg`), litres/millilitres (`l`, `ml`), and Celsius (`°C`). Use German decimal commas in German prose when appropriate.
- United Kingdom: normally use centimetres/metres and grams/kilograms for product specifications; use inches or pounds only when the category and current UK customer convention clearly favor them.
- Canada: normally lead with metric units; add an imperial equivalent only when category convention materially helps shoppers.
- Japan: normally use millimetres/centimetres and grams/kilograms.
- Australia: normally use centimetres/metres and grams/kilograms.
- For any other marketplace, use the local convention demonstrated by the supplied marketplace data or authoritative site/category fields; if unclear, use that country's official measurement system and flag the decision internally.

Conversions must be mathematical and reproducible: `1 in = 2.54 cm`, `1 lb = 0.45359237 kg`, `1 oz = 28.349523125 g`. Never convert an estimated or missing value. Round only to useful product precision, do not imply greater accuracy than the source, and use the same localized value consistently across product information, Item Highlights, bullets, description, and translations. If both systems are shown, put the local unit first and the confirmed source-unit equivalent in parentheses. Specifications remain out of the title unless the user explicitly overrides the fixed title rule.

## Prohibited language

Exclude from all localized front-end copy and Search Term, including plurals and disguised variants:

- kid, kids, child, children, toy, toys;
- set, sets, kit, kits, pack, packs, bundle, bundles, suite, suites, combination, combinations;
- Best, Bestseller, Premium, promotional claims, competitor brands, patent-sensitive wording, and unsupported superlatives.

If a source keyword contains prohibited wording, list it in the risk table with a replacement recommendation. Never force it into the Listing.

## Fixed module allocation

### Title

- Formula: `Brand + highest-traffic approved core category term + one natural secondary core term/long-tail when space permits`.
- Put the clearest exact product identity immediately after the brand so shoppers can recognize the product in the first scan.
- Select title terms only after the truth and relevance gates. Among equally exact terms, rank by search volume, genuinely comparable competitor coverage, purchase/conversion evidence, and buyer intent.
- Add a secondary core term only when it contributes a distinct natural search expression and the title remains idiomatic. Do not concatenate synonyms, repeat a root merely for SEO, or write a comma-separated keyword list.
- Use Title Case where appropriate to the target language; keep prepositions naturally cased.
- Keep dimensions, quantity, load capacity, color, material, compatibility, functions, scenarios, and other specifications in Item Highlights or bullets.
- No keyword repetition, promotional wording, competitor brands, or symbols such as `! * # ? _`.
- Output localized title, Chinese translation, `XX / 70（65-70）`, and keyword type plus exact position.

### Item Highlights

- Use 120-125 characters.
- Put confirmed dimensions, quantity, load capacity, color, material, compatibility, function, adult-relevant scenario, and high-value long tails here without copying the title.
- Present dimensions, weight, load capacity, volume, and temperature in the target marketplace's localized units; use the same rounded values everywhere.
- Use short clauses separated by ` | `; separators count toward length.
- Output localized text, clause-by-clause Chinese translation, `XX / 125（120-125）`, and clause-level keyword placement.

### Bullet Points

Before drafting, create a `bullet topic plan` containing five distinct topics chosen for the current product. Rank candidate topics by consumer decision importance, confirmed differentiation, keyword intent, and evidence strength. Keep exactly five bullets, but do not impose a universal topic order across product categories.

Potential topic families include primary outcome, usage experience, design/shape, material/construction, fit/compatibility, dimensions/capacity, care/maintenance, storage/portability, included components/setup, and realistic scenarios. Select only the five that matter for this product.

Every bullet must:

- start with `【English Title Case Noun Phrase】 `, normally 2-4 content words, followed by localized buyer-facing copy;
- contain 300-350 visible characters including the bracketed phrase, spaces, and punctuation;
- include natural approved long tails without copying competitor sentences;
- show the full Chinese translation, individual count, and every embedded keyword with sentence position.
- open with the consumer outcome, problem solved, or decision-relevant benefit—not the technical feature name alone;
- connect `consumer need/use situation -> confirmed feature/evidence -> practical benefit`, in the most natural order for the target language;
- answer one clear shopping question per bullet and avoid repeating the same benefit in different wording;
- use second-person or direct buyer-facing language only when natural for the marketplace; do not overuse rhetorical questions or commands.

Use consumer questions appropriate to the category. For a pillow or other soft sleep product, relevant confirmed topics may include shape/profile, height/firmness options, filling/cover, sleep-position fit, breathability, dimensions, or care; `no assembly` is normally filler and must not be used. For furniture, tools, storage, electronics, apparel, and other categories, derive different concerns from their product facts and keyword intent.

Do not mention assembly, setup, installation, mounting hardware, accessories, or included tools merely because a template once contained that topic. Use such content only when the buyer genuinely needs it to evaluate or use the current product. Likewise, do not force durability, professional-user, adult-user, or scenario language when it is not a meaningful differentiator.

For variants, distinguish parent-common content from child-specific content. When requested, create an independent Title, Item Highlights, differentiated bullets, counts, and keyword placement for each child.

### Product Description

- Use simple HTML paragraphs and bold headings.
- Write a consumer journey rather than a catalogue entry: begin with the intended use/problem, show how confirmed features improve the experience, help the shopper picture realistic use, and close with decision-relevant confirmed specifications or care information.
- Each paragraph must have a buyer-facing purpose. Cover remaining approved long tails only when they fit that purpose naturally.
- Translate technical attributes into concrete consumer meaning without inventing performance: explain what the confirmed feature changes in setup, use, comfort, storage, compatibility, or maintenance.
- Use specific, credible language. Avoid generic claims such as `ideal choice`, `perfect for everyone`, `excellent experience`, or empty lifestyle wording.
- Output localized HTML, complete Chinese translation, visible-text character count excluding tags, and paragraph-level keyword placement.
- Never include drafting rationale, missing-data wording, keyword explanations, or phrases equivalent to `待确认`, `确认后补充`, `资料未提供`, or `以图片为准`.

### Search Term

- Use 240-249 UTF-8 bytes.
- Use approved residual terms and language/spelling variants. Separate words with spaces only; no punctuation or vertical bars.
- Ordinary words should appear once where possible. Approved core terms may be deliberately repeated because the house standard requires cross-module coverage.
- Output the localized term string, byte count, supplemental new long tails with Chinese meanings, and deliberately repeated core terms with Chinese meanings.

## Fixed keyword coverage

- Embed at least 25 unique approved target keywords across the five modules. De-duplicate by normalized full phrase; repeating the same keyword in multiple modules still counts as one.
- Every approved core keyword must appear in all five modules: Title, Item Highlights, Bullet Points, Product Description, and Search Term.
- Every other approved keyword must appear at least once across those modules.
- Preserve complete long-tail phrases; a root alone does not count as phrase coverage.
- Only localized copy counts for SEO coverage; Chinese translations do not.
- Every raw keyword must be accounted for. Rejected brand, prohibited, false-attribute, wrong-variant, and irrelevant terms are listed with an exclusion reason and never marked embedded.

This complete accounting belongs in `关键词分析` and `关键词库`. The `Listing文案` placement table must contain only the approved keywords that were actually embedded.

Thus `100% coverage` means all approved terms are actually embedded according to these rules and all rejected terms are explicitly accounted for. It never means inserting unsafe or irrelevant raw terms.

The minimum of 25 never overrides truth, relevance, readability, or compliance. If fewer than 25 eligible phrases remain after filtering, do not deliver a final Listing; report the eligible count and request more relevant keyword data or product facts.

## Delivery validation

Before delivery, verify:

1. exact character/byte targets for every module;
2. exact or declared grammatical-variant placement for each approved keyword;
3. all approved core terms appear in all five modules;
4. complete long tails are not falsely credited from roots;
5. no prohibited words, competitor brands, wrong variants, unsupported facts, internal notes, or copied competitor sentences;
6. localized copy and Chinese translations match semantically;
7. title formula is followed and the five bullet topics are distinct, product-specific, and decision-relevant;
8. the keyword placement table reconciles with actual copy.
9. every bullet states a distinct consumer benefit supported by a confirmed feature or fact;
10. the description reads as a coherent purchase/use narrative rather than a feature list or keyword container.
11. at least 25 unique approved full phrases are genuinely present and mapped; duplicates, roots, translations, and excluded phrases are not counted.
12. no category-inappropriate filler appears, including assembly/setup claims for products that do not require meaningful setup.
13. every buyer-facing measurement follows the target marketplace convention, matches the conversion table, and uses consistent rounding across all modules and Chinese translations.

If any check fails, revise and re-run validation. Do not deliver a workbook labeled final with known failures.
