# ⚠️ 旧架构 - Recommender Module - 推荐模块

> **注意**：这是旧架构模块，属于prompt-master系统


**功能**: 推荐相似或相关的提示词和模块
**调用方式**: 通过主Skill路由或直接CLI调用

---

## 📋 功能概述

Recommender模块基于相似度算法推荐：
- 相似的Prompts（基于流派、设备、主题）
- 相关的五官模块组合
- 适合的摄影流派和设备

---

## 🔧 CLI命令

### 1. 推荐相似Prompts

**命令**:
```bash
python3 prompt_tool.py recommend <id> [-n <数量>]
```

**示例**:
```bash
python3 prompt_tool.py recommend 5 -n 3
```

**输出**:
```
🔍 为 Prompt #5 (清纯少女古典美) 推荐相关提示词

[1] #18 Princess Peach真人化
    相似度: 75%
    理由: 同为清纯少女风格 + 同用East Asian人种

[2] #10 温柔少女人像
    相似度: 65%
    理由: 同为人像美容摄影 + 主题相关

[3] #17 性感朋克Jinx
    相似度: 45%
    理由: 同为年轻女性人像（风格差异大）
```

---

## 📊 推荐算法

### 相似度计算

基于以下维度计算相似度：

| 维度 | 权重 | 说明 |
|------|------|------|
| 摄影流派 | 50% | 流派相同得分最高 |
| 相机设备 | 30% | 设备相同说明技术相似 |
| 主题关键词 | 20% | 主题相关性 |

**计算逻辑**:
```python
score = 0.0
reasons = []

# 流派相同 +0.5
if current_genre == candidate_genre:
    score += 0.5
    reasons.append(f"同为{genre_name}")

# 设备相同 +0.3
if current_camera == candidate_camera:
    score += 0.3
    reasons.append(f"同用{camera_name}")

# 主题相关 +0.2
if theme_keywords_match:
    score += 0.2
    reasons.append("主题相关")

similarity = score * 100  # 转换为百分比
```

---

## 🎯 使用场景

### 场景1: 寻找相似风格

```
用户: "推荐与Prompt #5相似的提示词"
→ 调用: python3 prompt_tool.py recommend 5
→ 获取Top 3相似Prompts
```

### 场景2: 发现新风格

```
用户: "我喜欢Prompt #17，还有类似的吗？"
→ 调用: python3 prompt_tool.py recommend 17
→ 发现性感、叛逆风格的其他Prompts
```

### 场景3: 学习特定流派

```
用户: "哪些Prompts属于电影叙事摄影？"
→ 调用: python3 prompt_tool.py search --genre cinematic_narrative
→ 查看该流派的所有Prompts
```

---

## 💡 推荐策略

### 1. 基于流派推荐

**最准确**: 流派相同的Prompts技术风格最接近
```
电影叙事摄影 → Prompt #18, #11
胶片艺术摄影 → Prompt #17
人像美容摄影 → Prompt #5, #10
```

### 2. 基于设备推荐

**技术维度**: 设备相同说明技术参数接近
```
Canon EOS R5 → #5, #18, #11
Hasselblad + Kodak Portra 400 → #17
```

### 3. 基于主题推荐

**内容维度**: 主题关键词重叠
```
清纯少女 → #5, #18
性感挑逗 → #17
角色Cosplay → #18, #11
```

---

## 📁 数据依赖

```
extracted_modules.json
├── prompt_id
├── theme
├── modules.visual_style.photography_genre
└── modules.technical_parameters.camera

module_library.json
├── photography_genres.<genre>.prompts
└── camera_equipment_index.<equipment>.prompts
```

---

## ⚠️ 注意事项

1. **相似度阈值**
   - > 70%: 高度相似，强推荐
   - 50-70%: 中度相似，可参考
   - < 50%: 低相似度，仅作参考

2. **多维度平衡**
   - 流派相同但主题不同 → 可学习技术
   - 主题相似但流派不同 → 可尝试新风格

3. **推荐数量**
   - 默认推荐Top 3
   - 可通过 `-n` 参数调整（最多10个）

---

**模块状态**: ✅ 可用
**CLI命令**: `recommend`, `search`
**推荐维度**: 流派、设备、主题
**算法**: 多维度加权相似度
