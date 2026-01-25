# ⚠️ 旧架构 - Optimizer Module - 优化模块

> **注意**：这是旧架构模块，属于prompt-master系统


**功能**: 优化和增强用户提供的提示词
**调用方式**: 通过主Skill路由或手动优化

---

## 📋 功能概述

Optimizer模块负责：
- 检测提示词缺失的关键信息
- 优化词汇顺序（人种前置）
- 增强细节描述
- 修正常见错误
- 提供改进建议

---

## 🔧 优化流程

### Step 1: 诊断问题

**检查清单**:

| 检查项 | 问题示例 | 严重性 |
|--------|---------|--------|
| 人种缺失 | "A beautiful woman, large eyes..." | ⚠️ 高 |
| 人种位置错误 | "A woman, East Asian features..." | ⚠️ 中 |
| 年龄缺失 | "A woman with..." | ⚠️ 中 |
| 五官描述过于简单 | "large eyes" (缺少细节) | ⚠️ 低 |
| 关键词重复 | "young woman, youthful..." | ⚠️ 低 |
| 技术参数缺失 | 无相机、分辨率 | ℹ️ 信息 |

### Step 2: 应用优化规则

#### 规则1: 补充缺失的基础属性

**优化前**:
```
A beautiful woman, large eyes, soft lips
```

**问题诊断**:
- ❌ 缺少人种
- ❌ 缺少年龄
- ⚠️ 眼型描述过于简单

**优化后**:
```
A beautiful East Asian young woman, large expressive almond eyes, thick natural lashes, deep clear iris, soft full lips with gentle pink gloss
```

**改进说明**:
- ✅ 添加人种 "East Asian"
- ✅ 添加年龄 "young"
- ✅ 增强眼型细节 "expressive almond", "thick natural lashes", "deep clear iris"
- ✅ 增强唇型细节 "soft full", "gentle pink gloss"

#### 规则2: 修正顺序错误

**优化前**:
```
A woman with expressive eyes, East Asian features, young and beautiful
```

**问题诊断**:
- ❌ 人种位置错误（应在最前面）
- ❌ 年龄位置错误
- ❌ "beautiful" 应在主体描述最前面

**优化后**:
```
A beautiful young East Asian woman, large expressive eyes
```

**修正逻辑**:
```
正确顺序: [形容词] [人种] [性别+年龄], [五官细节]
          ↓        ↓      ↓
      A beautiful  East Asian  young woman
```

#### 规则3: 去除重复词汇

**优化前**:
```
A beautiful young East Asian young woman, youthful appearance
```

**问题诊断**:
- ❌ "young" 重复出现

**优化后**:
```
A beautiful East Asian young woman, youthful appearance
```

#### 规则4: 增强细节描述

**优化前**:
```
A woman with blue eyes
```

**优化后**:
```
A beautiful young East Asian woman, large expressive blue eyes (natural contact lenses), photorealistic eye texture, bright blue iris
```

**增强策略**:
- 从特征库中提取完整关键词组
- 添加技术细节（如 "natural contact lenses" 使蓝眼更真实）
- 增加质感描述（如 "photorealistic eye texture"）

#### 规则5: 添加技术参数

**优化前**:
```
A beautiful East Asian young woman, large eyes, soft skin
```

**优化后**:
```
A beautiful East Asian young woman, large expressive almond eyes, thick natural lashes, flawless porcelain skin, radiant glow, photographed with Canon EOS R5, RF 50mm f/1.2L, 8K ultra-detailed, soft lighting, professional portrait photography
```

**添加内容**:
- ✅ 相机设备（基于风格推荐）
- ✅ 分辨率
- ✅ 光照描述
- ✅ 流派关键词

---

## 📊 优化级别

### 级别1: 基础修正 (必须)

**修正内容**:
- 补充人种（如果缺失）
- 修正人种位置（移到最前面）
- 补充年龄（如果缺失）
- 补充性别（如果缺失）

**适用场景**: 所有不完整的提示词

### 级别2: 细节增强 (推荐)

**增强内容**:
- 从简单描述扩展到完整关键词组
  - "large eyes" → "large expressive almond eyes, thick natural lashes, deep clear iris"
- 添加质感描述
  - "soft skin" → "flawless porcelain skin, radiant jade-like brightness, natural subtle blush"

**适用场景**: 描述过于简单的提示词

### 级别3: 技术优化 (可选)

**添加内容**:
- 相机设备
- 分辨率
- 光照描述
- 流派关键词

**适用场景**: 需要专业摄影效果的提示词

---

## 🎯 使用场景

### 场景1: 快速修正错误

```
用户: "优化这个提示词: A woman with eyes"

诊断:
- ❌ 缺少人种、年龄
- ❌ 眼型描述过于简单

优化结果:
A beautiful East Asian young woman, large expressive almond eyes, thick natural lashes, deep clear iris, dewy sparkle
```

### 场景2: 增强细节

```
用户: "增强这个提示词的细节: A beautiful young woman, blue eyes, pink lips"

增强结果:
A beautiful East Asian young woman, large expressive blue eyes (natural contact lenses), photorealistic eye texture, bright blue iris, soft full lips with gentle pink gloss, natural lip color, fresh look, flawless porcelain skin, radiant glow
```

### 场景3: 添加技术参数

```
用户: "为这个提示词添加专业摄影参数"

添加结果:
... photographed with Canon EOS R5, RF 50mm f/1.2L, 8K ultra-detailed, soft lighting, golden hour, professional portrait photography, high-end retouching
```

---

## 💡 优化策略

### 策略1: 保守优化

**原则**: 只修正明显错误，不改变原意
- 仅补充缺失的基础属性
- 修正顺序错误
- 去除重复

**适用**: 用户已有明确意图，只需小幅调整

### 策略2: 激进增强

**原则**: 大幅扩展细节，追求专业效果
- 补充所有模块
- 扩展所有描述到完整关键词组
- 添加所有技术参数

**适用**: 用户提供的描述过于简单，需要专业提示词

### 策略3: 风格定向优化

**原则**: 基于目标风格优化
- 识别目标风格（清纯/性感/古典/真人化）
- 使用该风格的预设五官组合
- 添加该风格的特定关键词

**适用**: 用户明确表示想要某种风格

---

## 📁 优化模板

### 模板1: 清纯少女风格

**基础结构**:
```
A beautiful East Asian young woman, [眼型:大眼杏仁眼], [唇型:粉嫩光泽唇], [鼻型:小巧直鼻], [皮肤:瓷肌无瑕], [表情:清纯温柔], photographed with Canon EOS R5, soft lighting, 8K ultra-detailed
```

### 模板2: 性感挑逗风格

**基础结构**:
```
A beautiful East Asian young woman, [眼型:半闭诱惑眼], [皮肤:温润胶片肌], [表情:挑逗顽皮], photographed with Hasselblad 503CX, Kodak Portra 400, warm tones, fine grain
```

### 模板3: 电影叙事风格

**基础结构**:
```
A beautiful East Asian young woman, [眼型:大蓝眼真人化], [脸型:精致鹅蛋脸], [皮肤:真实质感肌], [表情:宁静冒险], photographed with Canon EOS R5, 35mm f/2.8, 8K HDR, cinematic lighting, photorealistic
```

---

## ⚠️ 优化注意事项

1. **尊重原意**
   - 不要改变用户明确指定的特征
   - 优化应该是"增强"而非"替换"

2. **避免过度优化**
   - 提示词过长可能影响AI理解
   - 建议控制在200-300词以内

3. **保持一致性**
   - 风格统一（不要混合清纯和性感）
   - 技术参数匹配流派

4. **提供解释**
   - 告知用户做了哪些优化
   - 解释为什么这样优化

---

**模块状态**: ✅ 可用
**功能**: 诊断、修正、增强、建议
**优化级别**: 基础修正、细节增强、技术优化
**支持风格**: 4种预设模板 + 自定义
