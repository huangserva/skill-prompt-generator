# Learner Skill - 自学习技能

**功能**: 自动学习新Prompt中的未定义特征，扩展特征库
**类型**: 独立Skill
**实现**: 混合学习系统（规则+AI+人工审核）

---

## 🎯 核心功能

本Skill提供以下能力：

1. **扫描单个Prompt** - 分析新Prompt，识别未定义的特征
2. **批量扫描** - 扫描所有18个Prompts，发现缺失维度
3. **生成审核报告** - 自动生成待审核的新特征列表
4. **自动更新库** - 审核通过后自动更新 facial_features_library.json

---

## 📋 使用方式

### 方式1: 自然语言调用（推荐）

直接描述你的需求，系统会自动理解：

```
示例1: "学习这个Prompt的新特征: A woman with long flowing red hair, fair skin..."
示例2: "扫描所有Prompts，发现缺失的特征维度"
示例3: "分析这个Prompt有什么新的发型或肤色"
```

### 方式2: 直接调用CLI

如果需要精确控制，可直接使用命令行：

```bash
# 扫描单个Prompt
python3 learner.py scan "A woman with long red hair, fair skin, wearing qipao"

# 批量扫描所有Prompts
python3 learner.py batch
```

---

## 🔧 工作原理

### 混合学习流程

```
新Prompt输入
    ↓
规则提取（Rule-Based）
  - 使用正则表达式匹配常见模式
  - 快速识别：发型、发色、肤色、服装、配饰等
    ↓
AI增强（AI-Assisted）
  - 调用LLM验证规则提取的准确性
  - 发现规则未覆盖的新维度
    ↓
特征合并与去重
  - 合并两种方法的结果
  - 计算置信度
    ↓
匹配现有库
  - 检查是否已在 facial_features_library.json 中
  - 计算关键词重叠度（>70%视为已存在）
    ↓
生成审核报告
  - 列出所有新发现的特征
  - 提供建议分类码
  - 评估复用性
    ↓
人工审核
  - 用户决定：批准/修改/拒绝
    ↓
自动更新库
  - 批准后自动添加到 facial_features_library.json
  - 更新版本号
  - 生成changelog
```

---

## 🎯 使用场景

### 场景1: 发现新Prompt的特殊特征

**用户请求**:
```
"这个Prompt有什么新特征？
'A woman with long flowing red hair, fair porcelain skin, wearing elegant red silk qipao dress, delicate silver earrings'"
```

**系统执行**:
1. 调用 `python3 learner.py scan "<prompt>"`
2. 规则提取识别到：
   - hair_style: "long flowing" (长发飘逸)
   - hair_color: "red" (红色)
   - skin_tone: "fair porcelain" (白皙瓷肌)
   - clothing: "elegant red silk qipao dress" (优雅红色丝绸旗袍)
   - accessories: "delicate silver earrings" (精致银色耳环)
3. 匹配现有库：发现 hair_style, hair_color, clothing, accessories 都是新类别
4. 生成审核报告

**输出**:
```
🔍 扫描Prompt中...
   文本长度: 150 字符

✅ 扫描完成！
   发现特征: 5 个
   新特征: 5 个
   已存在: 0 个

📋 新发现的特征类别:
   - hair_style: 1 个
   - hair_color: 1 个
   - skin_tone: 1 个
   - clothing: 1 个
   - accessories: 1 个

📄 审核报告已生成: extracted_results/new_features_review_20260101_120000.md
```

---

### 场景2: 批量扫描所有Prompts

**用户请求**:
```
"扫描所有18个Prompts，发现缺失的特征维度"
```

**系统执行**:
1. 调用 `python3 learner.py batch`
2. 逐个扫描 extracted_modules.json 中的所有Prompts
3. 统计所有新特征
4. 生成汇总报告

**输出**:
```
📚 批量扫描模式
   读取文件: extracted_results/extracted_modules.json
   共 18 个Prompts

[1/18] 扫描 Prompt #1...
[2/18] 扫描 Prompt #2...
...
[18/18] 扫描 Prompt #18...

============================================================
📊 批量扫描完成！
============================================================

发现新类别:

hair_style: 8 个新分类
   - long straight black (Prompt #5)
   - twin tails blue (Prompt #18)
   - short spiky (Prompt #17)
   ... 还有 5 个

hair_color: 6 个新分类
   - natural black (Prompt #5, #18)
   - vibrant blue (Prompt #18)
   - purple pink gradient (Prompt #17)
   ... 还有 3 个

skin_tone: 3 个新分类
   - fair pale (Prompt #5, #18)
   - porcelain (Prompt #10)
   - medium tan (Prompt #8)

clothing: 5 个新分类
   - traditional chinese qipao (Prompt #18)
   - punk street style (Prompt #17)
   ... 还有 3 个

📄 汇总报告: extracted_results/batch_scan_summary_20260101_120000.md
```

---

### 场景3: 审核新特征

生成的审核报告示例：

```markdown
# 新特征发现报告

**扫描时间**: 2026-01-01 12:00:00
**扫描来源**: 用户输入

## 源Prompt
A woman with long flowing red hair, fair porcelain skin, wearing elegant red silk qipao dress

## 新发现的特征 (4个)

### 1. hair_style - NEW_CATEGORY
**关键词**: "long flowing red hair"
**置信度**: 80%
**提取方法**: rule-based
**建议分类码**: `long_flowing_red_hair`
**复用性评估**: 高（这是人像的重要基础元素）

**审核选项**:
- [ ] 批准添加
- [ ] 需要修改（请说明）
- [ ] 拒绝（说明原因）

### 2. hair_color - NEW_CATEGORY
**关键词**: "red hair"
**置信度**: 80%
**提取方法**: rule-based
**建议分类码**: `red_hair`
**复用性评估**: 高（这是人像的重要基础元素）

**审核选项**:
- [ ] 批准添加
- [ ] 需要修改（请说明）
- [ ] 拒绝（说明原因）

...
```

---

## 📊 可检测的特征维度

### 高优先级（已实现）

| 维度 | 示例 | 正则表达式 |
|------|------|-----------|
| **hair_style** | long flowing, short curly, twin tails | `(long\|short)?\s*(straight\|curly)?\s*hair` |
| **hair_color** | black, blonde, red, blue | `(black\|blonde\|red)?\s+hair` |
| **skin_tone** | fair, tan, olive, dark | `(fair\|tan\|olive)\s+skin` |
| **body_type** | slim, athletic, curvy | `(slim\|athletic)\s+body` |
| **clothing** | qipao dress, punk outfit | `wearing\s+(elegant)?\s*(qipao\|dress)` |
| **accessories** | silver earrings, necklace | `(silver\|gold)\s+(earrings\|necklace)` |
| **pose** | confident pose, standing | `(confident)?\s+pose` |

### 中优先级（待扩展）

- **makeup**: 妆容风格（自然、浓妆、哥特）
- **facial_hair**: 胡须（对男性人像）
- **tattoos**: 纹身
- **background**: 背景环境

### 低优先级（未来考虑）

- **lighting_mood**: 光照情绪
- **color_palette**: 色彩基调
- **artistic_style**: 艺术风格

---

## 🔍 意图识别

本Skill会自动识别以下意图关键词：

| 关键词 | 意图 | 执行操作 |
|--------|------|---------|
| 学习、提取、分析、识别 | 扫描单个Prompt | `learner.py scan` |
| 批量、所有、全部、扫描 | 批量扫描 | `learner.py batch` |
| 发现、缺失、新的 | 发现新特征 | 自动判断单个/批量 |

**示例**:

```
用户: "学习这个Prompt的特征"
→ 识别为：扫描单个
→ 执行：learner.py scan "<prompt>"

用户: "扫描所有Prompts发现新维度"
→ 识别为：批量扫描
→ 执行：learner.py batch
```

---

## ⚙️ 配置和参数

### 置信度阈值

```python
# learner.py 中的配置
CONFIDENCE_THRESHOLD = 0.7  # 70%以上才建议添加
OVERLAP_THRESHOLD = 0.7     # 关键词重叠度>70%视为已存在
```

### 文件路径

```python
# 特征库路径
LIBRARY_PATH = "extracted_results/facial_features_library.json"

# Prompts数据路径
PROMPTS_PATH = "extracted_results/extracted_modules.json"

# 审核报告输出路径
REPORT_OUTPUT_DIR = "extracted_results/"
```

---

## 📁 输出文件

### 1. 单次扫描审核报告

**文件名**: `new_features_review_YYYYMMDD_HHMMSS.md`

**位置**: `extracted_results/`

**内容**:
- 源Prompt
- 新发现的特征列表
- 每个特征的详细信息
- 审核选项（批准/修改/拒绝）

### 2. 批量扫描汇总报告

**文件名**: `batch_scan_summary_YYYYMMDD_HHMMSS.md`

**位置**: `extracted_results/`

**内容**:
- 扫描统计信息
- 按类别分组的新特征
- 每个特征关联的Prompt ID
- 置信度评分

---

## 🎓 技术实现细节

### 规则提取示例

```python
# hair_style 提取
regex = r"(long|short|medium)?\s*(straight|curly|wavy)?\s*(black|blonde|red)?\s*(hair|ponytail)"

# 匹配示例
"long flowing black hair" → ("long", "flowing", "black", "hair")
"short curly blonde hair" → ("short", "curly", "blonde", "hair")
"twin tails" → ("", "", "", "twin tails")
```

### 关键词重叠度计算

```python
def calculate_overlap(keywords1, keywords2):
    set1 = set([k.lower() for k in keywords1])
    set2 = set([k.lower() for k in keywords2])

    intersection = len(set1 & set2)
    union = len(set1 | set2)

    return intersection / union  # Jaccard相似度
```

**示例**:
```
keywords1 = ["long flowing hair", "black hair"]
keywords2 = ["long straight hair", "black locks"]

重叠词: "long", "black", "hair" (3个)
总词汇: 6个
重叠度: 3/6 = 50%
```

---

## ⚠️ 注意事项

### 1. AI辅助功能需要LLM API

当前实现中，AI辅助提取功能返回空列表，需要集成真实的LLM API（Claude、GPT-4等）。

**集成方法**:
```python
# learner.py 中的 AIAssistedLearner.extract_features()
# 需要调用实际的LLM API
response = anthropic_client.messages.create(
    model="claude-sonnet-4-5-20250929",
    system=self.system_prompt,
    messages=[{"role": "user", "content": prompt_text}]
)
```

### 2. 人工审核是必须的

自动检测可能存在：
- ❌ 误识别（false positive）
- ❌ 遗漏（false negative）
- ❌ 分类码不够准确

**解决方案**:
- ✅ 始终需要人工审核
- ✅ 只有置信度>70%的才建议
- ✅ 多次出现的特征优先级更高

### 3. 避免过度细分

不要为每个细微差别创建分类：

```
✅ 好: long_straight (通用)
❌ 差: long_straight_waist_length_black_shiny (过细)

建议:
- 发型: long_straight
- 发色: black (单独分类)
- 长度: 用描述词表达，不单独分类
```

---

## 🚀 未来扩展

### 短期（1周内）

1. **集成真实LLM API**
   - 使用Claude API进行智能提取
   - 提高识别准确度

2. **优化正则表达式**
   - 添加更多匹配模式
   - 支持中文关键词

### 中期（1个月）

3. **Web审核界面**
   - 可视化审核流程
   - 一键批准/拒绝
   - 批量操作

4. **自动库更新**
   - 审核通过后自动更新JSON
   - 生成changelog
   - 版本控制

### 长期（3个月）

5. **智能推荐**
   - 基于使用频率推荐
   - 自动组合建议
   - 风格一致性检查

6. **多语言支持**
   - 中英文混合Prompt
   - 自动翻译分类名

---

## 📖 使用示例

### 完整工作流程

```
1. 用户发现新Prompt
   "我有一个新Prompt: A woman with long red hair, fair skin..."

2. 调用Learner Skill
   "学习这个Prompt的新特征"

3. 系统自动执行
   → 规则提取
   → 匹配现有库
   → 生成审核报告

4. 用户查看报告
   → 打开 new_features_review_*.md
   → 查看新发现的特征

5. 人工审核
   → 批准: hair_style (long_flowing_red)
   → 批准: hair_color (red)
   → 批准: skin_tone (fair_pale)

6. 手动更新库
   → 将批准的特征添加到 facial_features_library.json
   → 更新版本号至 v1.3

7. 验证
   → 重新运行生成工具
   → 检查新特征是否可用
```

---

**Skill状态**: ✅ 可用
**实现方式**: 混合学习（规则+AI+人工审核）
**CLI工具**: `learner.py`
**输出**: Markdown审核报告
**下一步**: 集成LLM API，创建Web审核界面
