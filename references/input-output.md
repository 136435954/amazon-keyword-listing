# Input and output contract

## Execution modes

A complete production run requires all four input groups:

- target marketplace/country;
- product images plus confirmed product facts/specifications;
- a keyword export;
- competitor ASIN/title data or competitor Listing copy.

If any group is absent or unreadable, use `输入审计` mode: inventory received files, list missing items and confirmable visible facts, then stop. Do not generate a final keyword library or Listing.

Advertising search-term reports and Search Query Performance are not required for a pre-launch product. SellerSprite metrics and competitor overlap are planning evidence, not proof of actual conversion for the new product.

## Required product fact record

Before keyword decisions, record each claim with `字段`, `值`, `状态`, `证据来源`, and `可用于文案`. Allowed states are `已确认`, `待确认`, and `不具备/不匹配`. Only `已确认` facts may enter buyer-facing copy.

For every confirmed measurement, also retain `原始数值`, `原始单位`, `目标站点单位`, `换算数值`, `换算系数`, and `舍入规则`. Unit conversion changes presentation only; it never upgrades an unconfirmed value into a confirmed fact.

## Preferred workbook inputs

Recognize equivalent headers instead of requiring fixed names:

- keyword/search term;
- translation;
- monthly search volume;
- purchase volume or conversion/purchase rate;
- related product count/product count;
- title density;
- PPC bid/range;
- related ASINs or competitor rank/coverage;
- traffic type.

Preserve identifiers such as ASIN and SKU as text.

## Default workbook outputs

Use the simplest structure that preserves traceability. A complete workflow commonly contains:

1. `Listing文案` or localized equivalent: final copy, translations, counts, placement map, and pre-launch gaps.
2. `关键词分析`: summary, methodology, approved attributes, brands, colors, and risk explanations.
3. `关键词库`: derived row-level decisions with original metrics.
4. `ASIN与标题`: competitor inputs and title-root coverage.
5. `卖家精灵原始数据`: untouched export.
6. `产品信息`: confirmed facts and unresolved fields.

Do not add empty tabs. Preserve an existing workbook's intentional structure.

## Evidence labels

Use concise evidence labels such as:

- `用户确认`
- `产品图片可见`
- `产品资料字段`
- `竞品标题交叉覆盖`
- `关键词导出指标`
- `待确认`

Image-visible evidence may support basic form, color, presence of armrests/backrest, or obvious components. Do not infer hidden mechanisms, exact dimensions, materials, safety performance, ergonomic benefits, or continuous 360-degree rotation from appearance alone.
