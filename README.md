# Amazon Keyword Listing Skill

用于分析亚马逊产品资料、产品图片、竞品 Listing 与卖家精灵关键词数据，生成站点本地化关键词库及合规 Listing Excel。

当前版本：`KAIHA-LISTING-2026-V11`

Listing 中的尺寸、重量、容量和温度会按目标站点的消费者习惯本地化，例如美国站优先使用英寸、磅和盎司，德国及多数欧盟站优先使用公制单位；所有换算均保留来源和舍入记录。

## 安装

在 Codex 中提供此私有仓库地址，并要求安装其中的 Skill。访问私有仓库时，需要使用者拥有该仓库权限并完成 GitHub 授权。

也可以将本仓库克隆后，把整个目录复制到：

```text
$CODEX_HOME/skills/amazon-keyword-listing
```

## 使用

新建任务后上传以下资料：

- 产品图片和已确认的产品规格；
- 卖家精灵关键词导出表；
- 竞品 ASIN、标题或 Listing；
- 目标国家/站点和语言；
- 需要遵循的额外文案要求（如有）。

然后明确要求使用 `amazon-keyword-listing` Skill 搭建关键词库并生成 Listing。

## 主要输出

- 关键词分析；
- 关键词库；
- ASIN 与标题整理；
- 产品信息；
- 本地化 Listing 文案；
- 埋词位置核验；
- 后台搜索词和广告种子词。

最终 Excel 严格沿用 Skill 内置模板的工作表结构与格式。
