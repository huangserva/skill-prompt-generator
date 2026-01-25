# Tagger - 标签生成器模块

**功能**: 为提取的元素自动生成高质量标签

---

## 🎯 标签类型

### 1. 领域标签 (Domain Tags)
每个元素至少有一个领域标签

| 领域 | 标签 |
|------|------|
| portrait | `portrait` |
| product | `product` |
| design | `design` |
| art | `art` |
| video | `video` |
| interior | `interior` |
| common | `photography` |

### 2. 类别标签 (Category Tags)
基于元素所属类别

- `facial-features`, `makeup-styles`, `hair-styles`
- `product-types`, `material-textures`
- `layout-systems`, `visual-effects`
- `furniture-layouts`, `design-elements`
- etc.

### 3. 特征标签 (Feature Tags)
基于元素的关键特征

- 材质：`glass`, `wood`, `metal`, `fabric`
- 风格：`modern`, `vintage`, `luxury`, `minimal`
- 颜色：`red`, `gold`, `neutral`, `vibrant`
- 效果：`glossy`, `matte`, `reflective`, `translucent`

### 4. 跨领域标签 (Cross-Domain Tags)
可用于多个领域的通用标签

| 标签 | 适用领域 | 含义 |
|------|----------|------|
| `luxury` | product, interior, portrait | 高端奢华 |
| `glass` | design, art, product | 玻璃/透明效果 |
| `geometric` | design, interior, art | 几何图案 |
| `dynamic` | art, video, design | 动态/运动感 |
| `soft` | lighting, texture, makeup | 柔和效果 |
| `bold` | typography, color, makeup | 大胆/强烈 |

---

## 📋 标签生成流程

### Step 1: 从关键词提取

```python
def extract_tags_from_keywords(keywords: List[str]) -> List[str]:
    tags = []

    for kw in keywords:
        # 转换为标签格式
        tag = kw.lower()
        tag = tag.replace(' ', '-')
        tag = tag.replace('_', '-')

        # 过滤
        if is_valid_tag(tag):
            tags.append(tag)

    return tags

def is_valid_tag(tag: str) -> bool:
    # 长度检查
    if len(tag) < 2 or len(tag) > 30:
        return False

    # 避免无意义标签
    stopwords = ['the', 'a', 'an', 'with', 'and', 'or', 'of']
    if tag in stopwords:
        return False

    return True
```

### Step 2: 添加领域和类别标签

```python
def add_domain_category_tags(
    element: Dict,
    domain_id: str,
    category_id: str
) -> List[str]:
    tags = []

    # 领域标签
    domain_tag_map = {
        'portrait': 'portrait',
        'product': 'product',
        'design': 'design',
        'art': 'art',
        'video': 'video',
        'interior': 'interior',
        'common': 'photography'
    }
    tags.append(domain_tag_map[domain_id])

    # 类别标签
    category_tag = category_id.replace('_', '-')
    tags.append(category_tag)

    return tags
```

### Step 3: 智能特征标签识别

```python
def identify_feature_tags(element: Dict) -> List[str]:
    tags = []
    template = element['ai_prompt_template'].lower()

    # 材质特征
    material_patterns = {
        'wood': ['wood', 'wooden', 'walnut', 'oak', 'teak'],
        'metal': ['metal', 'brass', 'gold', 'copper', 'steel'],
        'glass': ['glass', 'translucent', 'transparent'],
        'fabric': ['fabric', 'linen', 'cotton', 'silk'],
        'leather': ['leather', 'calfskin', 'suede']
    }

    for tag, patterns in material_patterns.items():
        if any(p in template for p in patterns):
            tags.append(tag)

    # 风格特征
    style_patterns = {
        'modern': ['modern', 'contemporary', 'minimalist'],
        'vintage': ['vintage', 'retro', 'mid-century', 'classic'],
        'luxury': ['luxury', 'premium', 'high-end', 'upscale'],
        'geometric': ['geometric', 'angular', 'linear', 'grid']
    }

    for tag, patterns in style_patterns.items():
        if any(p in template for p in patterns):
            tags.append(tag)

    # 效果特征
    effect_patterns = {
        'glossy': ['glossy', 'shiny', 'reflective', 'polished'],
        'matte': ['matte', 'flat', 'non-reflective'],
        'soft': ['soft', 'gentle', 'subtle', 'diffused'],
        'bold': ['bold', 'strong', 'vibrant', 'dramatic']
    }

    for tag, patterns in effect_patterns.items():
        if any(p in template for p in patterns):
            tags.append(tag)

    return tags
```

### Step 4: 跨领域标签映射

```python
def identify_cross_domain_tags(element: Dict, domain_id: str) -> List[str]:
    tags = []
    template = element['ai_prompt_template'].lower()
    keywords = element.get('keywords', [])

    cross_domain_keywords = {
        'luxury': [
            'luxury', 'premium', 'high-end', 'upscale',
            'exclusive', 'collector', 'elite'
        ],
        'minimalist': [
            'minimal', 'clean', 'simple', 'streamlined'
        ],
        'dynamic': [
            'dynamic', 'motion', 'movement', 'flowing', 'energy'
        ],
        'organic': [
            'organic', 'natural', 'curved', 'flowing'
        ]
    }

    for tag, patterns in cross_domain_keywords.items():
        if any(p in template or p in ' '.join(keywords).lower()
               for p in patterns):
            tags.append(tag)

    return tags
```

---

## 📊 标签生成示例

### 示例1: Product Element

**输入元素**:
```json
{
  "category": "product_types",
  "name": "collector_edition_book",
  "ai_prompt_template": "premium collector's edition book, luxury binding, Italian calfskin cover",
  "keywords": ["collector's edition", "premium book", "luxury binding"]
}
```

**标签生成过程**:
1. 从keywords: `["collectors-edition", "premium-book", "luxury-binding"]`
2. 领域+类别: `["product", "product-types"]`
3. 智能特征: `["luxury", "leather"]` (从"calfskin"识别)
4. 跨领域: `["collectible", "book"]`

**最终标签**:
```json
[
  "product",
  "product-types",
  "collectors-edition",
  "premium-book",
  "luxury-binding",
  "luxury",
  "leather",
  "collectible",
  "book"
]
```

---

### 示例2: Design Element

**输入元素**:
```json
{
  "category": "visual_effects",
  "name": "glassmorphism",
  "ai_prompt_template": "frosted glass effect, 80% translucent, backdrop-filter blur",
  "keywords": ["glassmorphism", "frosted glass", "translucent"]
}
```

**标签生成过程**:
1. 从keywords: `["glassmorphism", "frosted-glass", "translucent"]`
2. 领域+类别: `["design", "visual-effects"]`
3. 智能特征: `["glass", "modern"]` (玻璃态是现代设计)
4. 跨领域: `["ui", "effect"]`

**最终标签**:
```json
[
  "design",
  "visual-effects",
  "glassmorphism",
  "frosted-glass",
  "translucent",
  "glass",
  "modern",
  "ui",
  "effect"
]
```

---

### 示例3: Interior Element

**输入元素**:
```json
{
  "category": "design_elements",
  "name": "sputnik_chandelier",
  "ai_prompt_template": "brass sputnik chandelier, mid-century iconic lighting",
  "keywords": ["sputnik", "chandelier", "brass", "mid-century"]
}
```

**标签生成过程**:
1. 从keywords: `["sputnik", "chandelier", "brass", "mid-century"]`
2. 领域+类别: `["interior", "design-elements"]`
3. 智能特征: `["metal", "vintage", "lighting"]`
4. 跨领域: `["statement-piece", "iconic"]`

**最终标签**:
```json
[
  "interior",
  "design-elements",
  "sputnik",
  "chandelier",
  "brass",
  "mid-century",
  "metal",
  "vintage",
  "lighting",
  "statement-piece",
  "iconic"
]
```

---

## 🎯 标签质量标准

### 优秀标签
- ✅ 描述性强：`geometric-pattern`, `soft-lighting`
- ✅ 适度具体：`mid-century`, `luxury`
- ✅ 可搜索：`glass`, `wood`, `modern`
- ✅ 跨领域复用：`luxury` (product/interior/portrait)

### 避免的标签
- ❌ 太泛泛：`good`, `nice`, `thing`
- ❌ 太具体：`my-grandmothers-rug`
- ❌ 无意义：`the`, `a`, `and`
- ❌ 过长：`mid-century-modern-walnut-tapered-leg-furniture`

---

## 🔍 标签去重和优化

```python
def optimize_tags(tags: List[str]) -> List[str]:
    # 1. 去重
    tags = list(set(tags))

    # 2. 移除冗余
    # 如果有"mid-century-modern"，移除"mid-century"
    if 'mid-century-modern' in tags and 'mid-century' in tags:
        tags.remove('mid-century')

    # 3. 长度限制（最多15个标签）
    if len(tags) > 15:
        # 优先保留：领域标签、类别标签、高频标签
        tags = prioritize_tags(tags)[:15]

    # 4. 排序（领域 > 类别 > 特征 > 其他）
    tags = sort_tags(tags)

    return tags
```

---

## ✅ 输出格式

```json
{
  "tags": [
    "product",
    "product-types",
    "collectors-edition",
    "premium-book",
    "luxury-binding",
    "luxury",
    "leather",
    "collectible",
    "book"
  ],
  "tag_count": 9,
  "cross_domain_tags": ["luxury", "collectible"],
  "primary_tags": ["product", "product-types"]
}
```

---

**状态**: ✅ 已实现
**目标**: 每个元素 5-15 个高质量标签
