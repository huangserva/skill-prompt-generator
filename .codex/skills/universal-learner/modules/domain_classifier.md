# Domain Classifier - 领域分类器模块

**功能**: 识别Prompt属于哪个领域（或多个领域）

---

## 🎯 7大领域定义

| 领域ID | 中文名 | 关键词 | 示例Prompts |
|--------|--------|--------|-------------|
| **portrait** | 人像摄影 | person, face, woman, man, beauty, makeup, facial | #5, #10, #11, #17, #18 |
| **product** | 产品摄影 | product, object, item, book, watch, bottle, package | #1, #6, #14, #16 |
| **design** | 平面设计 | poster, layout, UI, graphic, typography, bento grid | #2, #3, #7, #9, #13 |
| **art** | 艺术风格 | art, painting, surreal, artistic, illustration, effect | #8, #12, #15 |
| **video** | 视频生成 | video, scene, motion, cinematic, camera movement | #4 |
| **interior** | 室内设计 | interior, room, furniture, living room, bedroom | (v4.0新建) |
| **common** | 通用摄影 | photography, camera, lighting, lens, technical | (跨领域) |

---

## 📋 分类流程

### Step 1: 扫描关键词

```python
def classify_domain(prompt_text: str) -> Dict:
    # 1. 转为小写
    text_lower = prompt_text.lower()

    # 2. 关键词匹配
    domain_scores = {
        'portrait': 0,
        'product': 0,
        'design': 0,
        'art': 0,
        'video': 0,
        'interior': 0,
        'common': 0
    }

    # 3. 领域关键词权重表
    keywords = {
        'portrait': {
            'face': 3, 'woman': 3, 'man': 3, 'person': 3,
            'eyes': 2, 'skin': 2, 'makeup': 2, 'hair': 2,
            'beauty': 2, 'facial': 2, 'portrait': 3
        },
        'product': {
            'product': 3, 'book': 2, 'bottle': 2, 'watch': 2,
            'packaging': 2, 'item': 2, 'object': 1,
            'collector': 2, 'premium': 1
        },
        'design': {
            'poster': 3, 'layout': 3, 'bento': 3, 'ui': 3,
            'typography': 2, 'graphic': 2, 'card': 1,
            'grid': 2, 'design': 1
        },
        'art': {
            'painting': 3, 'artistic': 2, 'surreal': 3,
            'illustration': 2, 'art': 1, 'canvas': 2,
            'brushstroke': 2, 'effect': 1
        },
        'video': {
            'video': 3, 'scene': 2, 'cinematic': 3,
            'motion': 2, 'camera movement': 3, 'sequence': 2
        },
        'interior': {
            'interior': 3, 'room': 2, 'living room': 3,
            'bedroom': 3, 'furniture': 2, 'space': 1,
            'kitchen': 3, 'home': 1
        },
        'common': {
            'photography': 2, 'camera': 2, 'lens': 2,
            'lighting': 2, 'iso': 1, 'aperture': 1
        }
    }

    # 4. 计算各领域得分
    for domain, kw_dict in keywords.items():
        for keyword, weight in kw_dict.items():
            if keyword in text_lower:
                domain_scores[domain] += weight

    # 5. 排序
    sorted_domains = sorted(
        domain_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_domains
```

### Step 2: 确定主次领域

```python
def determine_primary_secondary(sorted_domains):
    primary = None
    secondary = []

    # 主领域：得分最高且 > 5
    if sorted_domains[0][1] > 5:
        primary = sorted_domains[0][0]

    # 次领域：得分 > 3 但不是主领域
    for domain, score in sorted_domains[1:]:
        if score > 3:
            secondary.append(domain)

    # common通常作为次领域
    if 'common' in [d[0] for d in sorted_domains if d[1] > 2]:
        if primary != 'common':
            secondary.append('common')

    return {
        'primary': primary,
        'secondary': secondary,
        'confidence': sorted_domains[0][1] / 20  # 归一化为0-1
    }
```

---

## 📊 分类示例

### 示例1: Prompt #1 (产品摄影)

**输入**:
```
A premium collector's edition book photographed with Phase One medium format camera,
featuring Italian calfskin leather binding with gold-embossed title...
```

**分析**:
- `book` +2
- `collector` +2
- `premium` +1
- `product` context implied +3
- `camera` +2 (common)
- `photography` +2 (common)

**输出**:
```json
{
  "primary": "product",
  "secondary": ["common"],
  "confidence": 0.4,
  "scores": {
    "product": 8,
    "common": 4,
    "design": 1
  }
}
```

---

### 示例2: Prompt #5 (人像摄影)

**输入**:
```
A young Asian woman with large expressive almond eyes, porcelain fair skin tone,
wearing elegant red silk qipao dress...
```

**分析**:
- `woman` +3
- `eyes` +2
- `skin` +2
- `facial features` context +3
- `beauty` implied +2

**输出**:
```json
{
  "primary": "portrait",
  "secondary": [],
  "confidence": 0.6,
  "scores": {
    "portrait": 12,
    "product": 0
  }
}
```

---

### 示例3: Prompt #2 (设计)

**输入**:
```
A modern Bento grid layout poster design with glassmorphism effects,
asymmetric card arrangement...
```

**分析**:
- `bento` +3
- `layout` +3
- `poster` +3
- `design` +1
- `grid` +2
- `card` +1

**输出**:
```json
{
  "primary": "design",
  "secondary": [],
  "confidence": 0.65,
  "scores": {
    "design": 13,
    "art": 1
  }
}
```

---

## 🚨 边界情况处理

### 1. 多领域Prompt

```
A woman holding a premium product in modern interior
```

**处理**:
- primary: "portrait" (woman +3, face implied)
- secondary: ["product", "interior"]
- 策略：提取多个领域的元素

### 2. 无法明确分类

```
High-resolution 8K photography
```

**处理**:
- primary: "common"
- secondary: []
- 策略：只提取通用摄影技术元素

### 3. 含糊描述

```
Beautiful scene with great composition
```

**处理**:
- 得分都很低 (<5)
- primary: None
- 策略：跳过，提示用户提供更具体的Prompt

---

## ✅ 输出格式

```json
{
  "primary_domain": "product",
  "secondary_domains": ["common"],
  "confidence": 0.75,
  "all_scores": {
    "product": 8,
    "common": 4,
    "portrait": 0,
    "design": 1
  },
  "recommendation": "Extract product_types, materials, and photography_techniques"
}
```

---

**状态**: ✅ 已实现
**准确率目标**: >90%
