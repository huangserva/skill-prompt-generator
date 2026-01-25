---
name: prompt-analyzer
description: 提示词分析与洞察 - 查看Prompt详情、对比差异、推荐相似提示词、元素库统计
---

# Prompt Analyzer - 提示词分析器

## 🎯 核心职责

**专注于已生成Prompt的分析和洞察**，不负责生成新Prompt。

提供以下5大功能：
1. **查看详情** - 分析Prompt使用了哪些元素
2. **对比分析** - 对比两个Prompt的差异
3. **相似推荐** - 推荐相似的Prompt
4. **元素统计** - 查询元素库统计信息
5. **风格推荐** - 按风格推荐最佳元素组合

---

## 📋 功能1：查看Prompt详情

### 触发场景

用户说：
- "查看Prompt #5的详情"
- "分析一下Prompt #5用了哪些元素"
- "显示Prompt #5的完整信息"
- "Prompt #5包含什么？"

### SKILL处理流程

#### 步骤1：识别意图

从用户输入中提取Prompt ID：

```python
# 示例：用户说 "查看Prompt #5的详情"
prompt_id = 5
```

#### 步骤2：调用执行层

```python
from prompt_analyzer import analyze_prompt_detail

result = analyze_prompt_detail(prompt_id=5)
```

#### 步骤3：检查结果

如果Prompt不存在：
```python
if 'error' in result:
    print(f"❌ {result['error']}")
    # 提示用户：该Prompt不存在，可能还没生成过任何Prompt
```

#### 步骤4：格式化展示

```markdown
📸 Prompt #5 详情

**用户需求**: {result['user_intent']}
**生成时间**: {result['generation_date']}
**质量评分**: {result['quality_score']}/10
**风格标签**: {result['style_tag']}

**使用的元素** ({len(result['elements'])}个):

1. [{field_name}] {chinese_name} (复用度: {reusability})
   - 类别: {category}
   - 模板: {template}

2. ...

**完整Prompt**:
────────────────────────────────────────────────────────
{result['prompt_text']}
────────────────────────────────────────────────────────
```

---

## 📋 功能2：对比两个Prompts

### 触发场景

用户说：
- "对比Prompt #5和#17"
- "#5和#17有什么区别？"
- "比较一下Prompt #5和#17"

### SKILL处理流程

#### 步骤1：识别意图

从用户输入中提取两个Prompt ID：

```python
# 示例：用户说 "对比Prompt #5和#17"
prompt_id1 = 5
prompt_id2 = 17
```

#### 步骤2：调用执行层

```python
from prompt_analyzer import compare_prompts

result = compare_prompts(prompt_id1=5, prompt_id2=17)
```

#### 步骤3：分析差异维度

SKILL分析返回的数据，生成对比表格：

```markdown
⚖️ Prompt对比：#5 vs #17

### 基本信息对比

| 维度 | Prompt #5 | Prompt #17 |
|------|-----------|-----------|
| 用户需求 | {p1['user_intent']} | {p2['user_intent']} |
| 风格标签 | {p1['style_tag']} | {p2['style_tag']} |
| 质量评分 | {p1['quality_score']}/10 | {p2['quality_score']}/10 |
| 元素总数 | {len(p1['elements'])}个 | {len(p2['elements'])}个 |
| 生成时间 | {p1['generation_date']} | {p2['generation_date']} |

### 元素差异分析

**相似度**: {result['similarity_score']*100:.1f}%

**共同元素** ({len(result['common_elements'])}个):
- {common_element['chinese_name']} ({common_element['category']})
- ...

**Prompt #5 独有** ({len(result['unique_to_p1'])}个):
- {element['chinese_name']} ({element['category']})
  关键词: {element['template'][:50]}...
- ...

**Prompt #17 独有** ({len(result['unique_to_p2'])}个):
- {element['chinese_name']} ({element['category']})
  关键词: {element['template'][:50]}...
- ...
```

#### 步骤4：分析结论

SKILL根据相似度给出结论：

```python
if result['similarity_score'] > 0.7:
    print("💡 这两个Prompt非常相似，风格接近")
elif result['similarity_score'] > 0.4:
    print("💡 这两个Prompt有一定相似性，但风格有明显差异")
else:
    print("💡 这两个Prompt完全不同，属于不同风格")
```

---

## 📋 功能3：推荐相似Prompts

### 触发场景

用户说：
- "推荐与#5相似的Prompt"
- "有没有类似#5的？"
- "找一些相似的提示词"
- "基于Prompt #5推荐相似的"

### SKILL处理流程

#### 步骤1：识别意图

```python
# 示例：用户说 "推荐与#5相似的Prompt"
prompt_id = 5
top_n = 3  # 默认推荐3个
```

#### 步骤2：调用执行层

```python
from prompt_analyzer import recommend_similar_prompts

result = recommend_similar_prompts(prompt_id=5, top_n=3)
```

#### 步骤3：分析推荐理由

SKILL解读相似度原因，为每个推荐Prompt生成理由：

```python
# 分析共同元素，找出相似的原因
def analyze_similarity_reason(common_element_ids, target_prompt, candidate_prompt):
    """
    分析两个Prompt为什么相似

    返回：
    - 共同的风格标签
    - 共同的元素类别
    - 推荐理由列表
    """
    reasons = []

    # 检查风格标签
    if target_prompt['style_tag'] == candidate_prompt['style_tag']:
        reasons.append(f"✓ 同为{candidate_prompt['style_tag']}风格")

    # 按类别统计共同元素
    category_count = {}
    for elem_id in common_element_ids:
        # 查询元素详情获取category
        # ... (执行层已返回)
        category = ...
        category_count[category] = category_count.get(category, 0) + 1

    # 列出重要的共同类别
    for category, count in category_count.items():
        if count >= 2:
            reasons.append(f"✓ {count}个共同的{category}元素")

    return reasons
```

#### 步骤4：格式化展示

```markdown
🔍 为Prompt #5推荐相似提示词

[1] Prompt #{recommendation['prompt_id']} - {recommendation['user_intent']}
    相似度: {recommendation['similarity']*100:.1f}%
    共同元素: {recommendation['common_count']}个
    质量评分: {recommendation['quality_score']}/10

    理由:
    - ✓ 同为{style_tag}风格
    - ✓ 共用3个makeup元素
    - ✓ 共用2个lighting元素

[2] ...

[3] ...
```

---

## 📋 功能4：元素库统计

### 触发场景

用户说：
- "元素库有哪些类别？"
- "makeup类别有多少个元素？"
- "哪些元素用得最多？"
- "查看元素库统计"
- "makeup_styles的详细信息"

### SKILL处理流程

#### 步骤1：识别意图

```python
# 场景A：用户说 "元素库有哪些类别？"
category = None  # 查询整体统计

# 场景B：用户说 "makeup类别有多少个元素？"
category = 'makeup_styles'  # 查询特定类别
```

#### 步骤2：调用执行层

```python
from prompt_analyzer import get_library_statistics

# 整体统计
result = get_library_statistics()

# 或者特定类别
result = get_library_statistics(category='makeup_styles')
```

#### 步骤3：格式化展示

**场景A：整体统计**

```markdown
📊 元素库统计

**总计**: {result['total_elements']} 个元素

**按类别分布**:
- makeup_styles: {count}个
- clothing_styles: {count}个
- hair_styles: {count}个
- lighting_techniques: {count}个
- facial_features: {count}个
- ...

💡 使用 "查看makeup_styles详情" 查看具体元素列表
```

**场景B：类别详情**

```markdown
📊 元素库统计 - {category}

**类别**: {result['category_details']['category']}
**总数**: {result['category_details']['total_count']} 个元素

**最常用元素** (Top 10):

| 排名 | 元素名称 | 复用度 | 使用次数 | 平均质量 |
|------|---------|--------|---------|---------|
| 1 | {chinese_name} | {reusability} | {usage_count}次 | {avg_quality}/10 |
| 2 | ... | ... | ... | ... |
| ... |

**最高质量元素** (Top 5):
[按avg_quality排序]

**从未使用的元素** ({count}个):
[usage_count = 0的元素]
```

---

## 📋 功能5：按风格推荐元素组合

### 触发场景

用户说：
- "古装风格应该用什么元素？"
- "科幻风格的最佳元素组合是什么？"
- "推荐西部世界风格的元素"
- "ancient_chinese风格用哪些元素好？"

### SKILL处理流程

#### 步骤1：识别意图

```python
# 示例：用户说 "古装风格应该用什么元素？"

# 映射用户描述到style_tag
style_mapping = {
    '古装': 'ancient_chinese',
    '古装中式': 'ancient_chinese',
    '仙剑奇侠传': 'ancient_chinese',
    '科幻': 'modern_sci_fi',
    '西部世界': 'westworld_android',
    '赛博朋克': 'cyberpunk',
    '奇幻': 'fantasy'
}

style = style_mapping.get('古装', 'ancient_chinese')
```

#### 步骤2：调用执行层

```python
from prompt_analyzer import recommend_elements_by_style

result = recommend_elements_by_style(style='ancient_chinese')
```

#### 步骤3：按类别组织推荐

SKILL将返回的元素按类别分组，便于展示：

```python
# 按category分组
elements_by_category = {}
for element in result['recommended_elements']:
    category = element['category']
    if category not in elements_by_category:
        elements_by_category[category] = []
    elements_by_category[category].append(element)

# 按类别的最高使用频率排序
sorted_categories = sorted(
    elements_by_category.items(),
    key=lambda x: max(e['usage_frequency'] for e in x[1]),
    reverse=True
)
```

#### 步骤4：格式化展示

```markdown
🎨 风格推荐：{result['style']}

**数据来源**: 基于{result['total_prompts']}个历史Prompt分析

**推荐元素组合** (按类别):

### 1. {category_name}

[{field_name}] {chinese_name}
- 使用频率: {usage_frequency*100:.0f}% ({usage_count}/{total_prompts}个Prompt使用)
- 复用度: {reusability}/10
- 平均质量: {avg_quality}/10
- 关键词: {template[:80]}...

### 2. {category_name}

...

**使用建议**:
- ✓ 这个组合在{style}风格中最常用，质量稳定
- ✓ 推荐搭配：{推荐的基础属性，如"东亚女性"}
- ⚠️ 避免搭配：{冲突的元素}
```

---

## 🔧 执行层函数列表

SKILL调用以下执行函数（代码层只执行，不决策）：

```python
# 所有函数在 prompt_analyzer.py 中

def analyze_prompt_detail(prompt_id: int) -> dict:
    """查询Prompt完整信息"""

def compare_prompts(prompt_id1: int, prompt_id2: int) -> dict:
    """对比两个Prompt差异"""

def recommend_similar_prompts(prompt_id: int, top_n: int = 3) -> list:
    """推荐相似Prompts"""

def get_library_statistics(category: str = None) -> dict:
    """查询元素库统计"""

def recommend_elements_by_style(style: str) -> dict:
    """按风格推荐元素组合"""
```

---

## 📁 数据依赖

```
elements.db
├── elements                 # 元素库（由universal-learner维护）
├── generated_prompts        # 生成历史（由intelligent-prompt-generator写入）
├── prompt_elements          # Prompt-元素关联
└── element_usage_stats      # 元素使用统计
```

**重要**：prompt-analyzer依赖intelligent-prompt-generator生成的历史数据。如果数据库中没有generated_prompts记录，分析功能无法工作。

---

## ⚙️ 架构原则

✅ **SKILL = 大脑（决策层）**
- 识别用户意图
- 分析返回数据
- 格式化展示结果
- 生成推荐理由

✅ **代码 = 手脚（执行层）**
- 查询数据库
- 计算相似度
- 返回原始数据

❌ **代码不做决策**
- 不判断"哪个更好"
- 不决定"展示什么"
- 只负责"取数据"

---

## 使用示例

### 示例1：查看详情

**用户**: "查看Prompt #1的详情"

**SKILL处理**:
```python
from prompt_analyzer import analyze_prompt_detail

result = analyze_prompt_detail(prompt_id=1)

# 展示格式化结果
print(f"📸 Prompt #{result['prompt_id']} 详情\n")
print(f"**用户需求**: {result['user_intent']}")
print(f"**生成时间**: {result['generation_date']}")
# ...
```

### 示例2：对比Prompts

**用户**: "对比Prompt #1和#2"

**SKILL处理**:
```python
from prompt_analyzer import compare_prompts

result = compare_prompts(prompt_id1=1, prompt_id2=2)

# 分析相似度
similarity = result['similarity_score']
if similarity > 0.7:
    conclusion = "非常相似"
elif similarity > 0.4:
    conclusion = "有一定相似性"
else:
    conclusion = "完全不同"

# 展示对比表格和结论
# ...
```

### 示例3：推荐相似Prompt

**用户**: "推荐与#1相似的Prompt"

**SKILL处理**:
```python
from prompt_analyzer import recommend_similar_prompts

recommendations = recommend_similar_prompts(prompt_id=1, top_n=3)

# 为每个推荐分析理由
for rec in recommendations:
    reasons = analyze_similarity_reason(
        rec['common_element_ids'],
        target_prompt_id=1,
        candidate_prompt_id=rec['prompt_id']
    )

    # 展示推荐和理由
    # ...
```

### 示例4：元素库统计

**用户**: "查看makeup_styles类别详情"

**SKILL处理**:
```python
from prompt_analyzer import get_library_statistics

result = get_library_statistics(category='makeup_styles')

# 展示统计表格
details = result['category_details']
print(f"📊 {details['category']} - {details['total_count']}个元素\n")

# 按使用次数排序展示
# ...
```

### 示例5：风格推荐

**用户**: "古装风格应该用什么元素？"

**SKILL处理**:
```python
from prompt_analyzer import recommend_elements_by_style

result = recommend_elements_by_style(style='ancient_chinese')

# 按类别组织展示
elements_by_category = group_by_category(result['recommended_elements'])

# 展示每个类别的推荐
for category, elements in elements_by_category.items():
    print(f"### {category}")
    for elem in elements:
        print(f"  - {elem['chinese_name']} (使用频率: {elem['usage_frequency']*100:.0f}%)")
# ...
```

---

## ⚠️ 重要提醒

1. **数据前提**：必须先有生成历史才能分析
   - 如果用户说"查看Prompt #5"，但数据库中没有任何Prompt，应提示：
     ```
     ❌ 数据库中还没有生成历史。
     💡 请先使用 intelligent-prompt-generator 生成一些Prompt。
     ```

2. **Prompt ID范围**：只能查询已存在的Prompt ID
   - 用户输入的ID可能不存在，需要检查error字段

3. **风格标签一致性**：风格推荐依赖style_tag
   - style_tag由intelligent-prompt-generator在保存时设置
   - 常见标签：ancient_chinese, modern_sci_fi, cyberpunk, fantasy, westworld_android

4. **元素类别名称**：查询统计时使用正确的category名称
   - makeup_styles (不是makeup)
   - lighting_techniques (不是lighting)
   - clothing_styles, hair_styles, facial_features 等

---

准备好分析提示词！等待用户的分析请求。
