# ⚠️ 旧架构 - Builder Module - 提示词组装模块

> **注意**：这是旧架构模块，属于prompt-master系统

**功能**: 根据用户描述智能组装完整提示词
**调用方式**: 通过主Skill路由或直接CLI调用

---

## 📋 功能概述

Builder模块负责根据用户的自然语言描述，智能选择合适的模块并组装成完整的提示词。

---

## 🔧 实现方式

### 方式1: 智能描述组装 (`build`命令)

**CLI命令**:
```bash
python3 prompt_tool.py build "用户描述"
```

**功能**:
- 自动识别关键词（流派、风格）
- 从风格库中提取五官组合
- 智能组装完整提示词

**示例**:
```bash
python3 prompt_tool.py build "电影级的清纯美少女"
```

**输出**:
```
✓ 识别成功:
  流派: 电影叙事摄影
  风格: 清纯少女

📦 五官模块组合:
  性别: 女性
  年龄: 青年（18-25岁）
  人种: 东亚人
  眼型: 大眼杏仁眼
  唇型: 粉嫩光泽唇
  鼻型: 小巧直鼻
  皮肤: 瓷肌无瑕
  表情: 清纯温柔眼神

✨ 组装后的提示词:
A beautiful East Asian young woman, large expressive almond eyes, ...
```

### 方式2: 交互式生成 (`generate`命令)

**CLI命令**:
```bash
python3 prompt_tool.py generate
```

**功能**:
- 10步交互式问答
- 用户自由选择每个模块
- 实时组装并显示结果

**交互流程**:
1. 选择性别 (2选项)
2. 选择年龄段 (3选项)
3. 选择人种 (3选项)
4. 选择摄影流派 (10选项)
5. 选择眼型 (4选项)
6. 选择脸型 (2选项)
7. 选择唇型 (2选项)
8. 选择鼻型 (2选项)
9. 选择皮肤质感 (4选项)
10. 选择表情 (3选项)

**优势**:
- 完全自由组合
- 可视化选项和评分
- 适合新手学习

---

## 📊 组装逻辑

### 提示词结构

```
[形容词] [人种] [性别+年龄], [眼型关键词], [脸型关键词], [唇型关键词], [鼻型关键词], [皮肤关键词], [表情关键词], [技术参数]
```

### 关键顺序

1. **主体描述** (必须在最前面):
   - 形容词: "A beautiful" / "A handsome"
   - 人种: "East Asian" / "Caucasian"
   - 性别+年龄: "young woman" / "adult man"

2. **五官细节**:
   - 眼型 → 脸型 → 唇型 → 鼻型 → 皮肤 → 表情

3. **技术参数** (最后):
   - 相机设备
   - 流派特定关键词
   - 分辨率、光照等

---

## 🎯 使用场景

### 场景1: 快速生成 (适合有经验用户)

```
用户: "生成一个性感挑逗风格的提示词"
→ 调用: python3 prompt_tool.py build "性感挑逗"
→ 自动匹配风格并组装
```

### 场景2: 自由组合 (适合新手或定制需求)

```
用户: "我想自己选择每个细节"
→ 调用: python3 prompt_tool.py generate
→ 交互式选择10个模块
```

### 场景3: 部分定制

```
用户: "电影级美少女，但用白种人"
→ 调用: python3 prompt_tool.py build "电影级美少女"
→ 然后手动修改人种为 Caucasian
```

---

## 💡 关键词映射表

### 流派关键词

| 用户输入 | 映射到 |
|---------|--------|
| 电影、电影级、cinematic | cinematic_narrative |
| 胶片 | analog_film |
| 人像 | portrait_beauty |
| 商业 | digital_commercial |
| 产品 | studio_product |

### 风格关键词

| 用户输入 | 映射到 |
|---------|--------|
| 美少女、少女、清纯 | 清纯少女 |
| 性感 | 性感挑逗 |
| 优雅、古典 | 古典优雅 |
| cosplay、真人化 | 真人化Cosplay |

---

## 📁 数据依赖

```
facial_features_library.json
├── gender (2分类)
├── age_range (3分类)
├── ethnicity (3分类)
├── eye_types (4分类)
├── face_shapes (2分类)
├── lip_types (2分类)
├── nose_types (2分类)
├── skin_textures (4分类)
├── expressions (3分类)
└── usage_index
    └── by_style_mood (4种风格预设)

module_library.json
├── photography_genres (10流派)
└── camera_equipment_index (设备库)
```

---

## ⚠️ 注意事项

1. **人种必须前置**
   - ❌ 错误: "A beautiful woman, East Asian features, ..."
   - ✅ 正确: "A beautiful East Asian woman, ..."

2. **避免关键词重复**
   - 使用 `age_based_terms` 避免 "young" 重复

3. **流派与设备匹配**
   - 电影叙事 → Canon EOS R5
   - 胶片艺术 → Hasselblad + Kodak Portra 400

---

**模块状态**: ✅ 可用
**CLI命令**: `build`, `generate`
**支持风格**: 4种预设 + 自由组合
