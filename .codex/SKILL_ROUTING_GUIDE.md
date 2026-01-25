# 提示词生成 Skill 路由使用指南

本指南详细说明如何根据用户请求自动路由到正确的 Skill，包含每个步骤的详细解释和实际示例。

---

## 📚 目录

1. [架构概览](#架构概览)
2. [路由流程 4 步骤](#路由流程-4-步骤)
3. [每个 Skill 的详细示例](#每个-skill-的详细示例)
4. [常见问题处理](#常见问题处理)

---

## 架构概览

### 数据存储结构

```
elements.db (统一数据库)
    ├─ portrait domain (491 元素) → intelligent-prompt-generator
    ├─ art domain (51 元素) → art-master
    ├─ design domain (59 元素) → design-master
    ├─ product domain (77 元素) → product-master
    ├─ video domain (49 元素) → video-master
    └─ 其他 7 个 domain (common, interior, creative 等)
```

### 为什么需要不同的 Skill？

虽然所有数据在同一个数据库，但访问方式不同：

- **intelligent-prompt-generator**: 使用 `prompt_framework.yaml`（人像专用框架），包含 eyes, nose, lips, makeup, hairstyle, pose 等人像专用字段
- **domain expert skills**: 直接查询对应领域，无需人像框架

**关键**：风景画、产品、海报不需要 "眼睛"、"妆容"、"姿势" 这些字段 → 必须用专门的 domain expert skills

---

## 路由流程 4 步骤

### STEP 1: 判断主体（最重要）

**问题**：请求中是否包含人物？

#### 判断方法

**有人物** 的关键词：
- 明确的人物：女性、男性、女孩、男孩、人物、角色、肖像
- 职业/身份：模特、女演员、武侠人物、商务人士
- 人体部位：面部、五官、表情、姿势、妆容

**无人物** 的关键词：
- 风景：山水、风景、自然、树林、海洋
- 静物：花卉、静物、桌面
- 抽象：抽象艺术、几何图形
- 产品：手表、香水、书籍、商品
- 界面：海报、UI、布局、网页

#### 示例

| 用户请求 | 有人物？ | 下一步 |
|---------|---------|--------|
| "生成电影级亚洲女性" | ✅ YES | 默认 → intelligent-prompt-generator |
| "生成中国水墨画山水" | ❌ NO | 继续 STEP 2 |
| "生成武侠人物飞身跃起" | ✅ YES | 默认 → intelligent-prompt-generator |
| "生成奢华手表产品摄影" | ❌ NO | 继续 STEP 2 |

---

### STEP 2: 根据主体类型选择专家

**前提**：STEP 1 判断为 "无人物"

#### 分类规则

**🎨 艺术作品** → `art-master`
- 关键词：水墨画、油画、水彩画、抽象艺术、插画、绘画
- 特征：艺术风格、绘画技法、艺术流派
- Domain: art (51 元素)
- 专长：笔触、留白、泼墨、厚涂、肌理

**🎯 平面设计** → `design-master`
- 关键词：海报、UI、布局、Bento Grid、玻璃态、排版
- 特征：设计布局、视觉效果、现代设计系统
- Domain: design (59 元素)
- 专长：Bento Grid、Glassmorphism、网格系统

**📦 产品摄影** → `product-master`
- 关键词：产品、商品、商业摄影、包装、展示
- 特征：产品、商品、静物拍摄
- Domain: product (77 元素)
- 专长：Phase One 相机、商业布光、产品构图

**🎬 视频场景** → `video-master`
- 关键词：视频、镜头运动、运镜、转场、动态场景、延时摄影
- 特征：动态、镜头语言、视频效果
- Domain: video (49 元素)
- 专长：推拉摇移、转场、特效、镜头运动

**👤 人像摄影** → `intelligent-prompt-generator`
- 关键词：人物、肖像、面部、五官、表情、姿势、妆容
- 特征：人物属性、面部特征
- Domain: portrait (491 元素)
- 专长：五官、妆容、表情、人种推理、一致性检查

#### 示例

| 用户请求 | 主体类型 | 路由选择 |
|---------|---------|---------|
| "生成中国水墨画山水，飞白技法" | 艺术作品 | art-master |
| "生成 Bento Grid 布局海报" | 平面设计 | design-master |
| "生成奢华手表产品摄影，柔光箱布光" | 产品摄影 | product-master |
| "生成武侠场景推镜头运动" | 视频场景 | video-master |

---

### STEP 3: 冲突场景处理

**场景**：请求同时涉及 **人物 + 特殊风格**

#### 默认策略（80% 情况）

**规则**：有人物 → 优先 `intelligent-prompt-generator`

**原因**：
- 人像框架能处理人物属性（五官、表情、妆容）
- 风格通过 `art_style` 参数实现（如 art_style='watercolor'）

#### 例外情况（20% 情况）

**规则**：用户明确强调艺术技法专业术语 → 使用 `art-master`

**艺术技法关键词**：
- 笔触、留白、泼墨（水墨画）
- 厚涂、肌理、笔触（油画）
- 干湿浓淡、飞白（国画）
- 晕染、渐变（水彩）

#### 询问用户场景

**规则**：同时强调人物细节和艺术技法 → 询问用户偏好

#### 示例

| 用户请求 | 分析 | 路由选择 | 理由 |
|---------|------|---------|------|
| "生成水墨画风格的女性" | 人物 + 风格 | intelligent-prompt-generator | 默认策略，水墨画作为 art_style |
| "生成梵高风格的女性肖像" | 人物 + 风格 | intelligent-prompt-generator | 默认策略，梵高风格作为 art_style |
| "生成女性肖像，要求水墨画的笔触和留白技法" | 人物 + 艺术技法术语 | 询问用户 | 同时强调人物和技法 |
| "生成油画效果，要求厚涂和肌理" | 无人物 + 艺术技法 | art-master | 强调艺术技法 |

---

### STEP 4: 调用对应的 Skill

根据 STEP 1-3 的判断结果，调用相应的 Skill：

```python
# 调用示例
Skill(command="intelligent-prompt-generator")  # 人像
Skill(command="art-master")                    # 艺术
Skill(command="design-master")                 # 设计
Skill(command="product-master")                # 产品
Skill(command="video-master")                  # 视频
```

---

## 每个 Skill 的详细示例

### 1. intelligent-prompt-generator（人像专家）

**适用场景**：所有包含人物的请求

#### 示例 1: 电影级亚洲女性

**用户请求**：
```
生成电影级的亚洲女性，张艺谋电影风格
```

**路由流程**：
1. **STEP 1**: 包含 "亚洲女性" → 有人物 ✅
2. **结论**: intelligent-prompt-generator
3. **调用**: `Skill(command="intelligent-prompt-generator")`

**Skill 工作**：
- 解析 intent:
  ```json
  {
    "subject": {"gender": "female", "ethnicity": "East_Asian"},
    "lighting": "zhang_yimou",
    "visual_style": {"art_style": "cinematic"}
  }
  ```
- 查询 portrait domain (491 元素)
- 应用人像框架（facial, styling, expression 等字段）
- 生成包含戏剧性光影的完整人像提示词

#### 示例 2: 水墨画风格的女性

**用户请求**：
```
生成水墨画风格的女性
```

**路由流程**：
1. **STEP 1**: 包含 "女性" → 有人物 ✅
2. **STEP 3**: 人物 + 风格，但未强调技法术语 → 默认策略
3. **结论**: intelligent-prompt-generator
4. **调用**: `Skill(command="intelligent-prompt-generator")`

**Skill 工作**：
- 解析 intent:
  ```json
  {
    "subject": {"gender": "female", "ethnicity": "East_Asian"},
    "visual_style": {"art_style": "watercolor"}
  }
  ```
- 通过 art_style 参数实现水墨画风格
- 人像框架处理五官、表情、妆容

#### 示例 3: 古装女子

**用户请求**：
```
生成仙剑奇侠传真人电影风格的年轻古装女子
```

**路由流程**：
1. **STEP 1**: 包含 "古装女子" → 有人物 ✅
2. **结论**: intelligent-prompt-generator
3. **调用**: `Skill(command="intelligent-prompt-generator")`

**Skill 工作**：
- 解析 intent:
  ```json
  {
    "subject": {"gender": "female", "age_range": "young_adult"},
    "styling": {
      "clothing": "traditional_chinese",
      "makeup": "traditional_chinese",
      "hairstyle": "ancient_chinese"
    },
    "lighting": {"lighting_type": "cinematic"},
    "scene": {"era": "ancient", "atmosphere": "fantasy"}
  }
  ```
- 框架自动推导：era=ancient → makeup/clothing/hairstyle 自动匹配

---

### 2. art-master（艺术专家）

**适用场景**：无人物的艺术作品，或强调艺术技法术语

#### 示例 1: 中国水墨画山水

**用户请求**：
```
生成中国水墨画山水
```

**路由流程**：
1. **STEP 1**: 山水 → 无人物 ❌
2. **STEP 2**: 主体是艺术作品（水墨画） → art-master
3. **调用**: `Skill(command="art-master")`

**Skill 工作**：
- 查询 art domain (51 元素)
- 选择中国水墨画相关元素：
  - 艺术风格：Traditional Chinese ink painting
  - 技法：flowing brush strokes, varying ink density
  - 构图：minimalist composition, negative space
  - 特征：monochromatic, grey washes, calligraphic elements
- 生成包含专业艺术术语的提示词

#### 示例 2: 油画技法的厚涂效果

**用户请求**：
```
生成油画效果，强调厚涂和笔触肌理
```

**路由流程**：
1. **STEP 1**: 无人物明确提及 → 无人物 ❌
2. **STEP 2**: 强调艺术技法（厚涂、肌理） → art-master
3. **调用**: `Skill(command="art-master")`

**Skill 工作**：
- 查询 art domain
- 选择油画技法元素：
  - 技法：impasto technique, thick paint application
  - 笔触：visible brush strokes, textured surface
  - 效果：palette knife marks, layered paint
- 生成强调技法的艺术提示词

#### 示例 3: 超现实主义风格

**用户请求**：
```
生成超现实主义艺术作品，梦境氛围
```

**路由流程**：
1. **STEP 1**: 无人物 ❌
2. **STEP 2**: 主体是艺术作品（超现实主义） → art-master
3. **调用**: `Skill(command="art-master")`

**Skill 工作**：
- 查询 art domain
- 选择超现实主义元素：
  - 艺术风格：surrealism, dreamlike atmosphere
  - 特征：impossible scenarios, symbolic imagery
  - 效果：ethereal, mysterious, subconscious themes
- 生成超现实主义风格提示词

---

### 3. design-master（设计专家）

**适用场景**：无人物的平面设计、UI、海报、布局

#### 示例 1: Bento Grid 海报

**用户请求**：
```
生成 Bento Grid 布局海报
```

**路由流程**：
1. **STEP 1**: 海报 → 无人物 ❌
2. **STEP 2**: 主体是平面设计（Bento Grid） → design-master
3. **调用**: `Skill(command="design-master")`

**Skill 工作**：
- 查询 design domain (59 元素)
- 选择 Bento Grid 相关元素：
  - 布局系统：Bento grid layout, 8 asymmetric modular cards
  - 视觉效果：modern minimalist aesthetics
  - 技术参数：4K resolution, clean typography
- 生成包含专业设计术语的提示词

#### 示例 2: 玻璃态 UI 设计

**用户请求**：
```
生成玻璃态 UI 设计，现代极简风格
```

**路由流程**：
1. **STEP 1**: UI → 无人物 ❌
2. **STEP 2**: 主体是平面设计（玻璃态） → design-master
3. **调用**: `Skill(command="design-master")`

**Skill 工作**：
- 查询 design domain
- 选择玻璃态元素：
  - 视觉效果：Glassmorphism, frosted glass effect
  - 技术：80% translucency, backdrop blur filter
  - 风格：minimalist, modern aesthetics
  - 色彩：90% neutral colors with 10% vibrant accents
- 生成现代设计系统提示词

#### 示例 3: 包含人物头像的海报

**用户请求**：
```
生成 Bento Grid 海报，包含人物头像
```

**路由流程**：
1. **STEP 1**: 虽然提到"人物头像"，但主体是"海报" → 无人物 ❌
2. **STEP 2**: 主体是平面设计 → design-master
3. **调用**: `Skill(command="design-master")`

**解释**：人物头像只是海报的一个元素，不是主体

---

### 4. product-master（产品专家）

**适用场景**：无人物的产品摄影、商品展示

#### 示例 1: 奢华手表产品摄影

**用户请求**：
```
生成奢华手表产品摄影
```

**路由流程**：
1. **STEP 1**: 手表 → 无人物 ❌
2. **STEP 2**: 主体是产品 → product-master
3. **调用**: `Skill(command="product-master")`

**Skill 工作**：
- 查询 product domain (77 元素)
- 选择奢华产品摄影元素：
  - 相机：Phase One camera, macro lens
  - 灯光：softbox lighting, rim light
  - 构图：luxury product composition
  - 背景：premium backdrop
- 生成商业摄影级提示词

#### 示例 2: 香水瓶柔光布光

**用户请求**：
```
生成香水瓶产品摄影，柔光箱布光
```

**路由流程**：
1. **STEP 1**: 香水瓶 → 无人物 ❌
2. **STEP 2**: 主体是产品 → product-master
3. **调用**: `Skill(command="product-master")`

**Skill 工作**：
- 查询 product domain
- 选择柔光布光元素：
  - 灯光：softbox lighting, diffused light
  - 相机：DSLR, shallow depth of field
  - 效果：elegant, premium, glass reflections
- 生成包含专业摄影术语的提示词

#### 示例 3: 女模特展示香水（边界案例）

**用户请求**：
```
女模特展示香水瓶
```

**路由流程**：
1. **STEP 1**: 有 "女模特" → 有人物 ✅
2. **STEP 3**: 焦点不明确（人物 vs 产品）
3. **询问用户**:
   ```
   我注意到你的请求涉及：
   - 女模特（intelligent-prompt-generator）
   - 香水瓶产品（product-master）

   你的焦点是：
   A. 女模特（人物为主，香水为道具）
   B. 香水瓶（产品为主，模特为陪衬）

   请选择？
   ```

#### 示例 4: 9宫格产品摄影（Grid Collage 模式）

**用户请求**：
```
生成9宫格奢华手表产品摄影，中间3D突出
```

**路由流程**：
1. **STEP 1**: 手表 → 无人物 ❌
2. **STEP 2**: 主体是产品 → product-master
3. **调用**: `Skill(command="product-master")`

**Skill 工作**：
- 识别关键词："9宫格" → 自动切换到 **Grid Collage 模式**
- 加载专业模板：`modules/layouts/grid_collage.md`
- 查询 product domain (77 元素)
- 生成包含以下特性的专业提示词：
  - **3×3严格等分网格** + THICK WHITE LINES 分隔
  - **8个不同角度产品摄影**（背景层，全部清晰）
    - [1,1] 表盘俯视
    - [1,2] 表冠侧面
    - [1,3] 表扣细节
    - [2,1] 经典45度角
    - [2,3] 底盖机芯
    - [3,1] 上手效果
    - [3,2] 表带链节
    - [3,3] 包装盒
  - **1个超大3D渲染手表**（前景层）
    - 表冠触顶边，表带触底边
    - 占据最大垂直空间
    - 完全遮挡中间格子[2,2]
    - 部分遮挡周围4格（10-20%）
  - **深景深f/16** - 所有格子都清晰
  - **专业深度效果**：
    - Drop shadow (12px blur)
    - Contact shadow (8px blur)
    - 前景+10%亮度，+20%饱和度
  - **完整质量检查清单**
  - **一致性规则**（9个位置同一产品）

**输出效果**：
- 超现实拼贴艺术风格
- 适合电商详情页、社交媒体、产品宣传海报
- 同时展示多个角度 + 3D立体突出

**触发关键词**：
- "9宫格"、"3×3布局"、"grid"
- "多角度展示"、"多视角"
- "中间3D突出"、"3D pop-out"

---

### 5. video-master（视频专家）

**适用场景**：无人物的视频场景、镜头运动、动态效果

#### 示例 1: 武侠场景运镜

**用户请求**：
```
生成武侠场景推镜头运动
```

**路由流程**：
1. **STEP 1**: 场景 + 推镜头 → 无人物 ❌
2. **STEP 2**: 主体是视频（镜头运动） → video-master
3. **调用**: `Skill(command="video-master")`

**Skill 工作**：
- 查询 video domain (49 元素)
- 选择镜头运动元素：
  - 运镜：dolly in (推镜头), slow camera movement
  - 场景：wuxia atmosphere, ancient Chinese architecture
  - 效果：cinematic movement, dramatic reveal
- 生成包含镜头语言的提示词

#### 示例 2: 风景延时摄影

**用户请求**：
```
生成风景延时摄影，云雾流动效果
```

**路由流程**：
1. **STEP 1**: 风景 → 无人物 ❌
2. **STEP 2**: 主体是视频（延时摄影） → video-master
3. **调用**: `Skill(command="video-master")`

**Skill 工作**：
- 查询 video domain
- 选择延时摄影元素：
  - 技术：time-lapse photography
  - 效果：flowing clouds, dynamic motion
  - 运镜：static camera, long exposure effect
- 生成延时摄影提示词

#### 示例 3: 武侠人物飞身跃起（边界案例）

**用户请求**：
```
武侠人物飞身跃起的动态镜头
```

**路由流程**：
1. **STEP 1**: 包含 "武侠人物" → 有人物 ✅
2. **分析**: 主体是人物动作 vs 镜头运动？
3. **默认策略**: 主体是人物 → intelligent-prompt-generator
4. **调用**: `Skill(command="intelligent-prompt-generator")`

**解释**：
- 人物动作通过 `expression.pose` 字段处理（人像框架支持）
- 如果用户明确强调镜头运动（"跟随镜头"、"运镜"），则询问用户

---

## 常见问题处理

### Q1: 如何判断是 "人物肖像" 还是 "人物在场景中"？

**答案**：看主体是什么

| 描述 | 主体 | 路由 |
|------|------|------|
| "女性肖像" | 人物 | intelligent-prompt-generator |
| "女性在花园里" | 人物 | intelligent-prompt-generator |
| "花园场景，远处有人" | 场景 | 根据场景类型路由 |
| "Bento Grid 海报，包含人物头像" | 海报 | design-master |

### Q2: 用户说 "水墨画风格的人物"，为什么不用 art-master？

**答案**：默认策略

- 主体是 "人物" → 需要人像框架（facial, styling, expression）
- "水墨画风格" 作为 `art_style` 参数实现
- art-master 专注于艺术技法术语（笔触、留白、泼墨）
- 除非用户明确说 "水墨画的笔触和留白技法"

### Q3: 什么时候需要询问用户？

**答案**：两种情况

1. **焦点不明确**：
   - "女模特展示香水瓶" → 人物 vs 产品？
   - "产品海报设计" → 产品 vs 设计？

2. **同时强调人物和技法**：
   - "女性肖像，要求水墨画的笔触留白技法" → 人物细节 vs 艺术技法？

### Q4: 如果用户请求不属于任何 domain 怎么办？

**答案**：询问用户或直接处理

示例：
```
用户："帮我优化这段代码"
→ 不涉及提示词生成
→ 直接在 conversation 处理，不调用 skill
```

### Q5: 多个 domain 的组合请求怎么处理？

**答案**：确定主 domain

| 请求 | 主 domain | 路由 |
|------|----------|------|
| "产品海报设计" | 设计（海报） | design-master |
| "产品摄影布光" | 产品（摄影） | product-master |
| "人物产品广告" | 询问焦点 | 询问用户 |

---

## 总结

### 路由决策树（完整版）

```
用户请求
    ↓
【STEP 1: 有人物吗？】
    ↓
  YES ─────────┐
    │         ↓
    │    【STEP 3: 有艺术技法术语吗？】
    │         ↓
    │       NO ──→ intelligent-prompt-generator (默认)
    │         ↓
    │      YES ──→ 询问用户偏好
    │
  NO
    ↓
【STEP 2: 主体是什么？】
    ↓
    ├─ 艺术作品 → art-master
    ├─ 平面设计 → design-master
    ├─ 产品 → product-master
    ├─ 视频 → video-master
    └─ 人物 → intelligent-prompt-generator
```

### 核心原则

1. **人物优先**：有人物 → 优先 intelligent-prompt-generator
2. **技法例外**：明确艺术技法术语 → art-master
3. **主体判断**：无人物 → 根据主体类型路由
4. **焦点询问**：焦点不明确 → 询问用户

---

**最后更新**: 2026-01-04
**版本**: 1.0
