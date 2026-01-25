# Product Builder - 产品Prompt组装器

**功能**: 从Universal Elements Database查询元素并组装产品摄影Prompt

---

## 🎯 组装策略

### 基础结构

```
产品摄影Prompt =
  产品描述 (20%) +
  材质纹理 (15%) +
  摄影技术 (25%) +
  光照设置 (20%) +
  技术参数 (10%) +
  质量增强 (10%)
```

---

## 📋 组装流程

### Step 1: 查询产品元素

```python
from element_db import ElementDB

db = ElementDB('extracted_results/elements.db')

# 查询产品类型
product_elements = db.search_by_domain(
    'product',
    category_id='product_types',
    min_reusability=6.0
)

# 如果用户指定了标签（如"luxury"）
if user_tags:
    product_elements = db.search_by_tags(
        user_tags + ['product'],
        require_all=False
    )
```

### Step 2: 查询材质纹理

```python
# 查询材质
materials = db.search_by_domain(
    'product',
    category_id='material_textures',
    min_reusability=7.0,
    limit=2
)

# 或按标签查询
materials = db.search_by_tags(['glossy', 'leather', 'metal'])
```

### Step 3: 查询摄影技术

```python
# 查询专业摄影技术
photo_tech = db.search_by_domain(
    'common',
    category_id='photography_techniques',
    min_reusability=8.0
)

# 产品摄影常用：macro, Phase One, editorial
macro_tech = [e for e in photo_tech if 'macro' in e['name'].lower()]
```

### Step 4: 查询光照技术

```python
# 查询光照
lighting = db.search_by_domain(
    'common',
    category_id='lighting_techniques',
    min_reusability=8.0
)

# 产品摄影常用：softbox, rim lighting, studio lighting
product_lighting = [e for e in lighting if any(kw in e['ai_prompt_template'].lower()
                    for kw in ['softbox', 'rim', 'studio'])]
```

### Step 5: 查询技术效果

```python
# 查询分辨率等技术参数
tech_effects = db.search_by_domain(
    'common',
    category_id='technical_effects',
    min_reusability=9.0
)

# 4K/8K resolution
resolution = [e for e in tech_effects if '4k' in e['name'].lower() or '8k' in e['name'].lower()]
```

---

## 🔧 组装算法

```python
def build_product_prompt(
    product_type: str = "premium product",
    style: str = "luxury",
    user_tags: list = None
) -> str:
    """
    组装产品摄影Prompt

    Args:
        product_type: 产品类型（如"book", "watch", "electronics"）
        style: 风格（如"luxury", "minimalist", "tech"）
        user_tags: 用户指定的标签

    Returns:
        完整的产品摄影Prompt
    """

    db = ElementDB('extracted_results/elements.db')
    prompt_parts = []

    # 1. 产品主体
    if product_type != "premium product":
        # 搜索特定产品
        products = db.search_by_tags([product_type, 'product'])
    else:
        # 使用通用产品描述
        products = db.search_by_domain('product', limit=1)

    if products:
        prompt_parts.append(products[0]['ai_prompt_template'])
    else:
        prompt_parts.append(f"premium {product_type}")

    # 2. 摄影技术（核心）
    photo_tech = db.search_by_domain('common', category_id='photography_techniques', limit=1)
    if photo_tech:
        prompt_parts.append(photo_tech[0]['ai_prompt_template'])

    # 3. 光照设置
    lighting = db.search_by_domain('product', category_id='lighting_techniques', limit=1)
    if lighting:
        prompt_parts.append(lighting[0]['ai_prompt_template'])

    # 4. 材质纹理（如果有style要求）
    if style and style.lower() in ['luxury', 'premium', 'high-end']:
        materials = db.search_by_tags(['luxury'], require_all=False)
        if materials:
            prompt_parts.append(materials[0]['ai_prompt_template'])

    # 5. 技术参数
    tech = db.search_by_tags(['4k', 'resolution'])
    if tech:
        prompt_parts.append(tech[0]['ai_prompt_template'])

    # 6. 质量增强词
    quality_enhancers = [
        "photorealistic",
        "ultra-detailed",
        "professional commercial photography",
        "editorial magazine quality",
        "pristine studio environment",
        "perfectly controlled lighting"
    ]

    prompt_parts.extend(quality_enhancers)

    # 组装
    prompt = ', '.join(prompt_parts)

    db.close()
    return prompt
```

---

## 📊 输出示例

### 示例1: 奢华书籍

**输入**:
```python
build_product_prompt(
    product_type="collector edition book",
    style="luxury"
)
```

**输出**:
```
Premium collector's edition book, luxury binding, Italian calfskin cover,
Phase One medium format camera with 100mm macro lens, sophisticated softbox
rim lighting, 4K resolution, photorealistic, ultra-detailed, professional
commercial photography, editorial magazine quality, pristine studio environment,
perfectly controlled lighting
```

---

### 示例2: 科技产品

**输入**:
```python
build_product_prompt(
    product_type="smartphone",
    style="tech",
    user_tags=["glass", "modern"]
)
```

**输出**:
```
Premium smartphone with glossy glass surface, modern sleek design, Phase One
camera with macro lens capturing screen details, soft studio lighting creating
elegant reflections, 4K ultra high resolution, photorealistic render,
professional tech product photography, minimal background, clean aesthetic
```

---

## ✅ 质量保证

### 必备元素检查

每个产品Prompt应包含：
- ✅ 产品描述
- ✅ 摄影技术（相机/镜头）
- ✅ 光照设置
- ✅ 分辨率/质量参数

### 长度控制

- 目标: 150-250词
- 最小: 100词
- 最大: 300词

---

**模块状态**: ✅ 已实现
**查询效率**: O(log n) 索引查询
