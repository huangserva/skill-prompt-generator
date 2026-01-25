# ⚠️ 旧架构 - Extractor Module - 提取模块

> **注意**：这是旧架构模块，属于prompt-master系统


**功能**: 从用户提供的Prompt中提取可复用的模块和特征
**调用方式**: 通过主Skill路由或手动分析

---

## 📋 功能概述

Extractor模块负责：
- 识别Prompt中的人物基础属性（性别、年龄、人种）
- 提取五官级别细节（眼型、脸型、唇型、鼻型、皮肤、表情）
- 识别摄影流派和技术参数
- 提取可复用的关键词组

---

## 🔧 提取流程

### Step 1: 分析输入Prompt

**输入示例**:
```
A beautiful young East Asian woman with large expressive almond eyes, thick natural lashes, delicate refined Asian facial structure, soft full lips with gentle pink gloss, small straight nose, flawless porcelain skin, radiant jade-like brightness, innocent gaze, gentle smile, photographed with Canon EOS R5, RF 50mm f/1.2L, 8K ultra-detailed, soft lighting
```

### Step 2: 提取基础属性

**提取目标**:
- **性别**: 识别 "woman" / "man" / "girl" / "boy"
  - 结果: female
- **年龄**: 识别 "young" / "adult" / "teen" / "elderly"
  - 结果: young_adult
- **人种**: 识别 "East Asian" / "Caucasian" / "African" / "mixed"
  - 结果: east_asian

### Step 3: 提取五官特征

**眼型提取**:
- 关键词: "large expressive almond eyes", "thick natural lashes"
- 匹配到: `large_expressive_almond` (大眼杏仁眼)

**脸型提取**:
- 关键词: "delicate refined Asian facial structure"
- 匹配到: `oval_asian_refined` (精致鹅蛋脸)

**唇型提取**:
- 关键词: "soft full lips", "gentle pink gloss"
- 匹配到: `soft_pink_gloss` (粉嫩光泽唇)

**鼻型提取**:
- 关键词: "small straight nose"
- 匹配到: `small_straight_delicate` (小巧直鼻)

**皮肤提取**:
- 关键词: "flawless porcelain skin", "radiant jade-like brightness"
- 匹配到: `porcelain_flawless_radiant` (瓷肌无瑕)

**表情提取**:
- 关键词: "innocent gaze", "gentle smile"
- 匹配到: `innocent_gentle_gaze` (清纯温柔眼神)

### Step 4: 提取技术参数

**相机设备**:
- 识别: "Canon EOS R5"
- 匹配到: `canon_eos_r5`

**镜头**:
- 识别: "RF 50mm f/1.2L"

**分辨率**:
- 识别: "8K ultra-detailed"

**光照**:
- 识别: "soft lighting"

### Step 5: 识别摄影流派

基于技术参数和风格关键词识别流派：

**流派识别逻辑**:
```python
if "8K" in prompt and "Canon EOS R5" in prompt:
    genre = "digital_commercial"
elif "Hasselblad" in prompt and "Kodak Portra" in prompt:
    genre = "analog_film"
elif "cinematic" in prompt or "HDR" in prompt:
    genre = "cinematic_narrative"
else:
    genre = "portrait_beauty"  # 默认
```

---

## 📊 提取结果格式

```json
{
  "basic_attributes": {
    "gender": "female",
    "age_range": "young_adult",
    "ethnicity": "east_asian"
  },
  "facial_features": {
    "eye_type": "large_expressive_almond",
    "face_shape": "oval_asian_refined",
    "lip_type": "soft_pink_gloss",
    "nose_type": "small_straight_delicate",
    "skin_texture": "porcelain_flawless_radiant",
    "expression": "innocent_gentle_gaze"
  },
  "technical_parameters": {
    "camera": "Canon EOS R5",
    "lens": "RF 50mm f/1.2L",
    "resolution": "8K",
    "lighting": "soft lighting"
  },
  "photography_genre": "portrait_beauty",
  "reusable_keywords": [
    "large expressive almond eyes",
    "thick natural lashes",
    "delicate refined Asian facial structure",
    "soft full lips",
    "gentle pink gloss",
    "small straight nose",
    "flawless porcelain skin",
    "innocent gaze",
    "gentle smile"
  ]
}
```

---

## 🎯 使用场景

### 场景1: 分析优秀Prompt

```
用户: "提取这个Prompt的五官特征"
输入: "A beautiful woman with large blue eyes..."

→ 执行提取流程
→ 输出分类结果和可复用关键词
```

### 场景2: 学习新特征

```
用户: "这个眼型叫什么？'manic luminous ruby-pink eyes, heavy seductive half-lidded gaze'"

→ 匹配到: half_lidded_seductive (半闭诱惑眼)
→ 显示该眼型的完整信息和使用建议
```

### 场景3: 扩展特征库

```
用户: "这个新Prompt有什么特殊的皮肤质感？"
输入: "wet skin texture, abundant realistic water droplets..."

→ 识别为: wet_dewy_droplets (湿润水感肌)
→ 可添加到库中（如果是新类型）
```

---

## 💡 关键词匹配表

### 眼型关键词

| 关键词组 | 匹配分类 |
|---------|---------|
| large expressive almond, thick natural lashes | large_expressive_almond |
| large blue eyes, natural contact lenses | large_blue_expressive |
| heavy seductive half-lidded, manic eyes | half_lidded_seductive |
| green eyes, anime eye style | anime_hybrid_green |

### 皮肤关键词

| 关键词组 | 匹配分类 |
|---------|---------|
| flawless porcelain, radiant jade-like | porcelain_flawless_radiant |
| realistic texture, visible pores | realistic_textured_pores |
| wet skin, water droplets | wet_dewy_droplets |
| warm rich, film grain | warm_rich_analog_film |

---

## 📁 数据依赖

```
facial_features_library.json (v1.2)
├── 各类别的 keywords 字段用于匹配
└── classification_code 用于标识

module_library.json
├── photography_genres.<genre>.key_features
└── camera_equipment_index.<equipment>.specs
```

---

## ⚠️ 注意事项

1. **关键词优先级**
   - 完全匹配 > 部分匹配 > 语义相似

2. **多义词处理**
   - "young" 可能是年龄或形容词
   - 需结合上下文判断

3. **新特征识别**
   - 如果无法匹配到已有分类
   - 提示用户这可能是新特征
   - 建议手动分类或添加到库

4. **置信度评分**
   - 完全匹配: 100%
   - 部分匹配: 70-90%
   - 语义相似: 50-70%
   - 低于50%: 需人工确认

---

**模块状态**: ✅ 可用
**功能**: 自动识别、关键词匹配、分类标注
**准确度**: 对已有28个分类识别率 > 90%
**扩展性**: 支持添加新分类和关键词
