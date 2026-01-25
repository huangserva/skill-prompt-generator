# ⚠️ 旧架构 - Learner Module - 自学习模块

> **注意**：这是旧架构模块，属于prompt-master系统


**功能**: 从新Prompt中自动学习和提取未定义的特征模块
**调用方式**: 通过主Skill路由或独立运行

---

## 📋 功能概述

Learner模块负责：
1. **自动识别**新的特征维度（发型、发色、肤色等）
2. **智能提取**特征关键词和描述
3. **自动分类**新特征到合适的类别
4. **生成建议**供人工审核和添加
5. **增量学习**持续扩展分类库

---

## 🎯 解决的问题

### 当前缺失的模块

| 类别 | 当前状态 | 缺失的维度 | 重要性 |
|------|---------|-----------|--------|
| **人物基础** | ✅ 性别、年龄、人种 | ❌ 肤色、身材、身高 | 高 |
| **头发** | ❌ 无 | ❌ 发型、发色、发质 | 高 |
| **五官** | ✅ 眼/脸/唇/鼻/肤/情 | ❌ 眉毛、耳朵 | 中 |
| **妆容** | ❌ 无 | ❌ 妆容风格、口红色号 | 中 |
| **服装** | ❌ 无 | ❌ 服装风格、颜色、材质 | 高 |
| **配饰** | ❌ 无 | ❌ 耳环、项链、眼镜 | 低 |
| **姿势** | ❌ 无 | ❌ 站姿、坐姿、动作 | 中 |
| **视角** | ❌ 无 | ❌ 特写、全身、侧面 | 中 |

---

## 🤖 自学习流程

### Step 1: 扫描新Prompt

**输入**: 用户提供的新Prompt文本

**示例**:
```
A beautiful young Asian woman with long flowing black hair, fair skin tone, wearing elegant traditional Chinese qipao dress in red silk, delicate silver earrings, confident pose, full body shot, photographed with Canon EOS R5
```

### Step 2: 分词和特征提取

**使用NLP技术**:
1. 分词（tokenization）
2. 词性标注（POS tagging）
3. 命名实体识别（NER）
4. 依存关系分析

**提取结果**:
```json
{
  "detected_features": [
    {
      "category": "hair",
      "keywords": ["long flowing black hair"],
      "attributes": {
        "length": "long",
        "style": "flowing",
        "color": "black"
      }
    },
    {
      "category": "skin",
      "keywords": ["fair skin tone"],
      "attributes": {
        "tone": "fair"
      }
    },
    {
      "category": "clothing",
      "keywords": ["traditional Chinese qipao dress", "red silk"],
      "attributes": {
        "style": "traditional Chinese",
        "type": "qipao dress",
        "color": "red",
        "material": "silk"
      }
    },
    {
      "category": "accessories",
      "keywords": ["delicate silver earrings"],
      "attributes": {
        "type": "earrings",
        "material": "silver",
        "style": "delicate"
      }
    },
    {
      "category": "pose",
      "keywords": ["confident pose", "full body shot"],
      "attributes": {
        "posture": "confident",
        "view": "full body"
      }
    }
  ]
}
```

### Step 3: 匹配现有分类

**检查每个特征是否已存在**:
```python
def check_existing_category(feature):
    """检查特征是否已在库中"""

    # 读取现有库
    facial_lib = load_json("facial_features_library.json")

    category = feature["category"]
    keywords = feature["keywords"]

    # 检查类别是否存在
    if category not in facial_lib:
        return "NEW_CATEGORY"

    # 检查关键词是否已存在
    existing_items = facial_lib[category]
    for item_code, item_data in existing_items.items():
        item_keywords = item_data.get("keywords", [])
        # 关键词重叠度检查
        overlap = calculate_keyword_overlap(keywords, item_keywords)
        if overlap > 0.7:  # 70%以上重叠
            return "EXISTS", item_code

    return "NEW_ITEM"
```

### Step 4: 生成新分类建议

**对于新发现的特征**:

#### 4.1 新类别（如 hair）

**生成模板**:
```json
{
  "hair_styles": {
    "long_flowing_black": {
      "chinese_name": "长发飘逸（黑色）",
      "classification_code": "long_flowing_black",
      "visual_features": {
        "length": "long (shoulder length or longer)",
        "style": "flowing, natural movement",
        "color": "black (natural Asian hair color)",
        "texture": "straight, silky"
      },
      "keywords": [
        "long flowing black hair",
        "silky straight hair",
        "natural black hair"
      ],
      "suitable_styles": [
        "古典优雅",
        "现代时尚",
        "真人化Cosplay"
      ],
      "prompts_using_this": [],  // 将被自动填充
      "reusability_score": 0,     // 待评估
      "usage_recommendations": {
        "best_for": "需要展示头发细节的人像",
        "pair_with": "搭配柔和光照展现发质",
        "lighting": "backlight or soft window light"
      },
      "auto_detected": true,       // 标记为自动检测
      "needs_review": true,         // 需要人工审核
      "detection_confidence": 0.85  // 检测置信度
    }
  }
}
```

#### 4.2 新子分类（在现有类别下）

**示例**: 在 skin_textures 下添加 skin_tone

```json
{
  "skin_textures": {
    // ... 现有的4种皮肤质感

    "fair_skin_tone": {
      "chinese_name": "白皙肤色",
      "classification_code": "fair_skin_tone",
      "visual_features": {
        "tone": "fair, light",
        "undertone": "cool or neutral",
        "characteristics": "pale complexion, minimal melanin"
      },
      "keywords": [
        "fair skin",
        "pale skin",
        "light skin tone",
        "porcelain complexion"
      ],
      "suitable_styles": [
        "所有风格"
      ],
      "prompts_using_this": [],
      "reusability_score": 0,
      "auto_detected": true,
      "needs_review": true,
      "detection_confidence": 0.90
    }
  }
}
```

### Step 5: 人工审核流程

**生成审核报告**:
```markdown
# 新特征发现报告

## 扫描来源
- Prompt来源: 用户输入 / Prompt #XX
- 扫描时间: 2026-01-01 12:00:00

## 新发现的特征 (5个)

### 1. 发型 (hair_styles) - 新类别 ⭐
**关键词**: "long flowing black hair"
**建议分类码**: long_flowing_black
**置信度**: 85%
**复用性评估**: 高（发型是人像的重要元素）

**审核选项**:
- [ ] 批准添加
- [ ] 需要修改（请说明）
- [ ] 拒绝（说明原因）

### 2. 肤色 (skin_tone) - 新子类别
**关键词**: "fair skin tone"
**建议分类码**: fair_skin_tone
**置信度**: 90%
**建议**: 添加到 skin_textures 类别

**审核选项**:
- [ ] 批准添加
- [ ] 需要修改
- [ ] 拒绝

### 3. 服装 (clothing_style) - 新类别 ⭐
**关键词**: "traditional Chinese qipao dress", "red silk"
**建议分类码**: traditional_chinese_qipao
**置信度**: 92%
**复用性评估**: 中（特定于文化主题）

**审核选项**:
- [ ] 批准添加
- [ ] 需要修改
- [ ] 拒绝

... (其他特征)
```

### Step 6: 自动更新分类库

**审核通过后**:
1. 自动添加到 `facial_features_library.json`
2. 更新 `library_metadata`
3. 关联到源Prompt
4. 生成changelog

---

## 🔧 实现技术

### 方案1: 规则基础（初级版）

**优点**: 简单、可控、快速实现
**缺点**: 需要手动定义规则

**实现**:
```python
class RuleBasedLearner:
    """基于规则的特征学习器"""

    def __init__(self):
        self.patterns = {
            "hair": {
                "keywords": ["hair", "hairstyle", "hairdo"],
                "attributes": ["long", "short", "curly", "straight", "black", "blonde"],
                "regex": r"(long|short|curly|straight)\s+(flowing|silky)?\s*(black|blonde|brown|red)?\s+hair"
            },
            "skin_tone": {
                "keywords": ["skin tone", "complexion", "skin color"],
                "attributes": ["fair", "pale", "tan", "olive", "dark"],
                "regex": r"(fair|pale|tan|olive|dark)\s+skin(\s+tone)?"
            },
            "clothing": {
                "keywords": ["dress", "outfit", "wearing", "clothes"],
                "attributes": ["traditional", "modern", "casual", "formal"],
                "regex": r"wearing\s+(elegant|traditional|modern)?\s*(\w+)\s+(dress|outfit)"
            }
        }

    def extract_features(self, prompt_text):
        """提取特征"""
        detected = []

        for category, pattern_info in self.patterns.items():
            # 正则匹配
            matches = re.findall(pattern_info["regex"], prompt_text, re.IGNORECASE)

            if matches:
                detected.append({
                    "category": category,
                    "raw_text": matches[0],
                    "confidence": 0.8
                })

        return detected
```

### 方案2: AI辅助（高级版）

**优点**: 智能、灵活、可发现未知维度
**缺点**: 需要LLM API、成本较高

**实现**:
```python
class AIAssistedLearner:
    """AI辅助的特征学习器"""

    def extract_features(self, prompt_text):
        """使用LLM提取特征"""

        system_prompt = """
        你是一个提示词分析专家。请从以下Prompt中提取所有人物特征，
        并按类别组织。对于每个特征，提供：
        1. 类别（如 hair, skin_tone, clothing等）
        2. 关键词
        3. 属性（如长度、颜色、风格等）

        返回JSON格式。
        """

        user_prompt = f"Prompt: {prompt_text}"

        # 调用LLM（如Claude、GPT-4）
        response = call_llm_api(system_prompt, user_prompt)

        # 解析返回的JSON
        features = json.loads(response)

        return features
```

### 方案3: 混合模式（推荐）

**结合两者优势**:
1. **规则提取**: 快速识别常见特征
2. **AI验证**: 检查提取准确性
3. **AI发现**: 识别未定义的新维度
4. **人工审核**: 最终确认

**工作流程**:
```python
def hybrid_learning_pipeline(prompt_text):
    """混合学习流程"""

    # Step 1: 规则提取
    rule_learner = RuleBasedLearner()
    rule_features = rule_learner.extract_features(prompt_text)

    # Step 2: AI增强提取
    ai_learner = AIAssistedLearner()
    ai_features = ai_learner.extract_features(prompt_text)

    # Step 3: 合并和去重
    merged_features = merge_features(rule_features, ai_features)

    # Step 4: 匹配现有库
    new_features = []
    for feature in merged_features:
        status = check_existing_category(feature)
        if status in ["NEW_CATEGORY", "NEW_ITEM"]:
            new_features.append(feature)

    # Step 5: 生成审核报告
    if new_features:
        report = generate_review_report(new_features)
        save_report(report)

    return new_features
```

---

## 📊 优先级建议

### 高优先级（立即添加）

**1. 发型 (hair_styles)**
```json
{
  "hair_styles": {
    "long_straight_black": "长直黑发",
    "long_curly_brown": "长卷棕发",
    "short_bob_blonde": "短发波波头（金色）",
    "ponytail_high": "高马尾",
    "twin_tails": "双马尾"
  }
}
```

**2. 发色 (hair_colors)**
```json
{
  "hair_colors": {
    "natural_black": "自然黑色",
    "dark_brown": "深棕色",
    "blonde": "金色",
    "red_auburn": "红棕色",
    "silver_gray": "银灰色（染发）"
  }
}
```

**3. 肤色 (skin_tones)**
```json
{
  "skin_tones": {
    "fair_pale": "白皙",
    "medium_tan": "小麦色",
    "olive": "橄榄色",
    "dark_rich": "深色"
  }
}
```

### 中优先级（逐步添加）

**4. 身材 (body_types)**
```json
{
  "body_types": {
    "slim_petite": "纤细娇小",
    "athletic_fit": "运动健美",
    "curvy_voluptuous": "曲线丰满",
    "average_balanced": "匀称标准"
  }
}
```

**5. 服装风格 (clothing_styles)**
```json
{
  "clothing_styles": {
    "traditional_chinese": "中式传统",
    "modern_casual": "现代休闲",
    "formal_business": "正式商务",
    "cosplay_character": "角色扮演"
  }
}
```

### 低优先级（按需添加）

**6. 配饰 (accessories)**
**7. 妆容 (makeup_styles)**
**8. 姿势 (poses)**

---

## 🎯 使用场景

### 场景1: 扫描新Prompt发现特征

**用户操作**:
```
"学习这个Prompt的新特征: A woman with long flowing red hair..."
```

**执行流程**:
1. 调用 `learner.md`
2. 提取特征: 发型(long flowing), 发色(red)
3. 检查库: 未找到对应分类
4. 生成建议: 添加 hair_styles.long_flowing_red
5. 输出审核报告

**输出**:
```
发现新特征:
- 发型: long_flowing_red (长发飘逸-红色)
- 置信度: 88%
- 建议: 添加到hair_styles类别

是否批准添加？
```

### 场景2: 批量扫描提升覆盖率

**用户操作**:
```
"扫描所有18个Prompts，发现缺失的特征维度"
```

**执行**:
```python
# 扫描所有Prompts
all_prompts = load_json("extracted_modules.json")
missing_features = {}

for prompt in all_prompts:
    prompt_text = prompt["original_prompt"]
    features = hybrid_learning_pipeline(prompt_text)

    for feature in features:
        category = feature["category"]
        if category not in missing_features:
            missing_features[category] = []
        missing_features[category].append(feature)

# 生成报告
print(f"发现 {len(missing_features)} 个新类别")
for category, items in missing_features.items():
    print(f"  {category}: {len(items)} 个新子分类")
```

**输出示例**:
```
扫描完成！发现新类别:

1. hair_styles (发型): 8个新分类
   - long_straight_black (Prompt #5)
   - twin_tails_blue (Prompt #18)
   - short_spiky (Prompt #17)
   ...

2. skin_tones (肤色): 3个新分类
   - fair_pale (Prompt #5, #18)
   - tan_healthy (Prompt #10)
   ...

3. clothing_styles (服装): 5个新分类
   - traditional_chinese (Prompt #18)
   - punk_street (Prompt #17)
   ...

生成审核报告: new_features_review_2026-01-01.md
```

---

## 📁 自动生成的文件

### 1. 审核报告 (`new_features_review_YYYY-MM-DD.md`)

**内容**:
- 发现的新特征列表
- 每个特征的详细信息
- 审核选项（批准/修改/拒绝）
- 关联的Prompt ID

### 2. 待审核特征库 (`pending_features.json`)

**格式**:
```json
{
  "pending_items": [
    {
      "category": "hair_styles",
      "code": "long_flowing_red",
      "chinese_name": "长发飘逸（红色）",
      "keywords": ["long flowing red hair"],
      "source_prompts": [],
      "detection_date": "2026-01-01",
      "confidence": 0.88,
      "status": "pending_review"
    }
  ]
}
```

### 3. 更新日志 (`feature_library_changelog.md`)

**记录所有变更**:
```markdown
## 2026-01-01
- 新增类别: hair_styles (5个分类)
- 新增类别: hair_colors (4个分类)
- 新增子类别: skin_tones (在skin_textures下，3个分类)
- 来源: 自动学习 + 人工审核
```

---

## ⚠️ 注意事项

### 1. 质量控制

**自动检测的局限**:
- ❌ 可能误识别（false positive）
- ❌ 可能遗漏（false negative）
- ❌ 关键词可能不够准确

**解决方案**:
- ✅ 始终需要人工审核
- ✅ 设置置信度阈值（>80%才建议）
- ✅ 多次出现的特征优先级更高

### 2. 分类一致性

**确保新分类符合现有规范**:
- 命名规范（classification_code）
- 数据结构一致
- 复用性评分标准
- 关键词格式

### 3. 避免过度细分

**不要为每个细微差别创建分类**:
- ✅ 好: long_straight (通用)
- ❌ 差: long_straight_waist_length (过细)

**合并相似分类**:
- long_straight_black + long_straight_brown → long_straight (颜色单独分类)

---

## 🚀 实施建议

### 阶段1: 手动扩展（立即开始）

**不等自学习系统，先手动添加常见维度**:
1. 从18个现有Prompts中人工提取发型、发色、肤色
2. 创建3个新类别的基础分类（各3-5个）
3. 更新 facial_features_library.json 至 v1.3

**时间**: 1-2小时

### 阶段2: 规则学习（1周内）

**实现规则基础的learner**:
1. 编写正则表达式提取器
2. 实现特征匹配逻辑
3. 生成审核报告

**时间**: 1-2天

### 阶段3: AI增强（2周内）

**集成LLM API**:
1. 使用Claude/GPT-4分析Prompt
2. 自动提取和分类特征
3. 混合模式（规则+AI）

**时间**: 3-5天

---

**模块状态**: 🚧 设计完成，待实施
**优先级**: 高（发型、发色、肤色）
**推荐方案**: 混合模式（规则+AI+人工审核）
**下一步**: 先手动扩展，再实现自动学习
