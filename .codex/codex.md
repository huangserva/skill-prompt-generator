# Codex Code 项目规则

## ⚠️ SKILL调用规则（最高优先级）

### 当用户请求生成提示词时

---

### 📊 架构原理（重要！）

**统一数据源，分层访问**：

所有学习成果都存储在 `elements.db`（1103元素，12领域），但每个skill访问不同的领域：

| Skill | 访问Domain | 元素数 | 框架/方法 | 专长 |
|-------|-----------|--------|----------|------|
| intelligent-prompt-generator | portrait | 491 | 人像框架(7大类) | 五官、妆容、表情、人像光影 |
| art-master | art | 51 | 直接查询 | 艺术技法、笔触、留白 |
| design-master | design | 59 | 直接查询 | Bento Grid、玻璃态、布局 |
| product-master | product | 77 | 直接查询 | 商业摄影、产品布光 |
| video-master | video | 49 | 直接查询 | 镜头运动、转场、特效 |
| **prompt-crafter** ⭐ | design (变量库) | 20万+组合 | 专业设计系统 | 配色方案、装饰元素、风格推荐 |

**关键**：
- intelligent-prompt-generator 使用 `prompt_framework.yaml`（人像专用框架）
- 框架包含：subject（主体）、facial（面部）、styling（造型）、expression（表情）、lighting（光影）、scene（场景）、technical（技术）
- **所有字段都是人像专用**：eyes, nose, lips, makeup, hairstyle, pose 等
- 风景画、产品、海报不需要这些字段 → 必须用domain expert skills

---

### ⚡ 快速决策树

```
用户请求
    ↓
【有人物吗？】
    ↓
  YES ────────────→ intelligent-prompt-generator
    │               （portrait domain, 491元素）
    │               除非强调艺术技法术语
    │
  NO
    ↓
【主体是什么？】
    ↓
    ├─ 风景/静物/艺术绘画 → art-master (art domain, 51元素)
    ├─ 产品/商品 → product-master (product domain, 77元素)
    ├─ 海报/UI/布局（需要设计术语） → design-master (design domain, 59元素)
    ├─ 海报/卡片（需要配色+风格系统） → prompt-crafter ⭐ (20万+组合)
    └─ 视频/镜头运动 → video-master (video domain, 49元素)
```

---

**STEP 1: 判断主体（最重要）**

首先判断：**请求中是否包含人物？**

**YES - 有人物**：
- 默认倾向 → `intelligent-prompt-generator`（人像专家）
- 除非用户明确强调艺术技法/设计布局

**NO - 无人物**：
- 根据主体类型选择专家（见下方）

---

**STEP 2: 根据主体类型选择专家**

**🎨 艺术作品（无人物）** → `art-master`
- 关键词：水墨画山水、油画风景、抽象艺术、静物绘画
- 示例："生成中国水墨画山水" "油画风格的静物"

**🎯 平面设计（无人物）** → 两种选择：

**A. design-master** - 设计术语和布局描述
- 关键词：Bento Grid、玻璃态、UI、排版技术术语
- 示例："生成Bento Grid海报" "玻璃态UI设计"
- 输出：设计术语描述

**B. prompt-crafter** ⭐ - 专业设计规范和配色系统
- 关键词：温馨可爱、现代简约、配色方案、儿童教育、卡片设计
- 示例："生成温馨可爱的儿童海报" "现代简约科技宣传图"
- 输出：完整设计规范（配色+圆角+阴影+装饰+技术参数）

**如何选择**：
- 需要设计术语 → design-master
- 需要完整设计系统（配色+装饰+风格） → prompt-crafter

**📦 产品摄影（无人物）** → `product-master`
- 关键词：产品、商品、商业摄影、包装、静物
- 示例："生成奢华手表产品摄影" "书籍产品展示"

**🎬 视频场景（无人物）** → `video-master`
- 关键词：视频、镜头运动、运镜、转场、动态场景
- 示例："生成武侠场景运镜" "风景延时摄影"

**👤 人像摄影（有人物）** → `intelligent-prompt-generator`
- 关键词：人物、肖像、面部、五官、表情、姿势、妆容
- 示例："生成电影级亚洲女性" "美少女肖像"

---

**STEP 3: 冲突场景处理**

**当请求同时涉及人物 + 特殊风格时**（如："水墨画风格的人物"）

**默认策略**（80%的情况适用）：
- 有人物 → 优先 `intelligent-prompt-generator`
- 原因：人像框架能处理人物属性（五官、表情、妆容），风格通过 art_style 参数实现

**何时使用 art-master**（20%的情况）：
用户明确强调艺术技法专业术语时：
- "水墨画的**笔触和留白技法**"
- "油画的**厚涂和笔触肌理**"
- "超现实主义的**艺术手法**"
- 关键词：笔触、留白、泼墨、厚涂、肌理、技法

**何时询问用户**：
当同时强调人物细节和艺术技法时：
```
我注意到你的请求涉及：
- 人物肖像（intelligent-prompt-generator 专长：深度五官理解）
- 水墨画技法（art-master 专长：笔触、留白、泼墨）

你更关注：
A. 人物细节（五官、表情、妆容）
B. 艺术技法（笔触、留白、泼墨）

请选择？
```

---

### 📝 示例对比表

**典型场景路由示例**：

| 用户请求 | 有人物？ | 路由选择 | 理由 |
|---------|---------|---------|------|
| "生成电影级亚洲女性" | ✅ | intelligent-prompt-generator | 人物肖像，需要五官妆容 |
| "生成水墨画风格的女性" | ✅ | intelligent-prompt-generator | 主体是人物，水墨画作为art_style |
| "生成中国水墨画山水" | ❌ | art-master | 无人物，纯艺术风格 |
| "生成Bento Grid海报" | ❌ | design-master | 无人物，设计布局术语 |
| "生成温馨可爱的儿童海报" | ❌ | **prompt-crafter** ⭐ | 需要配色+装饰+风格系统 |
| "生成现代简约科技宣传图" | ❌ | **prompt-crafter** ⭐ | 需要专业设计规范 |
| "生成奢华手表产品摄影" | ❌ | product-master | 产品摄影 |
| "生成武侠场景运镜" | ❌ | video-master | 镜头运动 |
| "生成女性肖像，要求水墨画的笔触留白" | ✅ | 询问用户 | 同时强调人物和艺术技法 |
| "生成Bento Grid海报，包含人物头像" | ❌ | design-master | 主体是海报，人物只是元素 |

**边界案例示例**：

| 用户请求 | 分析 | 路由选择 |
|---------|------|---------|
| "梵高风格的女性肖像" | 主体：女性肖像 / 风格：梵高 | intelligent-prompt-generator (art_style='van_gogh') |
| "油画技法的厚涂肌理效果" | 无人物，强调技法 | art-master |
| "女模特展示香水瓶" | 焦点不明确（人物 vs 产品） | 询问用户焦点 |
| "武侠人物飞身跃起" | 人物动作 vs 镜头运动 | intelligent-prompt-generator (pose字段) |

---

**STEP 4: 调用对应的专家 Skill**

使用 `Skill` tool 调用选定的专家：
- `Skill(command="art-master")`
- `Skill(command="design-master")`
- `Skill(command="product-master")`
- `Skill(command="video-master")`
- `Skill(command="intelligent-prompt-generator")`
- `Skill(command="prompt-crafter")` ⭐ **新增**

**你绝对不能**：
- ❌ 在conversation里直接用Bash调用Python
- ❌ 在conversation里直接生成提示词
- ❌ 绕过skill自己做所有事情
- ❌ 所有请求都默认调用 intelligent-prompt-generator（要先识别领域）

### 为什么要智能路由？

**我们的目标**：让每个领域专家发挥专长，不是把所有任务都扔给一个skill

**每个专家的独特价值**：
- art-master: 艺术流派专业术语（笔触、留白、泼墨）
- design-master: 现代设计系统（Bento Grid、Glassmorphism）
- product-master: 商业摄影器材（Phase One相机、softbox）
- video-master: 镜头语言（运镜、转场、特效）
- intelligent-prompt-generator: 深度人像理解（五官、人种推理）
- **prompt-crafter** ⭐: 专业设计规范（配色方案、装饰元素、风格系统、20万+组合）

---

## 🎯 其他Skill调用规则

### 当用户请求专业设计提示词时 ⭐ **新增**

**用户说**：
- "生成温馨可爱/现代简约的海报"
- "我要做儿童教育/科技宣传的设计"
- "需要配色方案"
- "帮我设计XX风格的卡片"

**你必须**：
✅ 调用 `prompt-crafter` skill

**prompt-crafter 的特点**：
- 从20万+变量组合中采样
- 输出完整设计规范（配色+圆角+阴影+装饰+技术参数）
- 支持风格：温馨可爱、现代简约
- 适用场景：儿童教育、科技商务、海报卡片设计

### 当用户请求NotebookLM相关功能时

**用户说**：
- "查询NotebookLM"
- "生成播客/视频/思维导图"
- NotebookLM相关任务

**你必须**：
✅ 调用 `notebooklm` skill

### 当用户请求推特写作时

**用户说**：
- "生成推特内容"
- "基于知识库写推文"

**你必须**：
✅ 调用 `twitter-writer` skill

### 当用户请求健身计划时

**用户说**：
- "制定健身计划"
- "规划运动安排"

**你必须**：
✅ 调用 `workout-planner` skill

### 当用户请求写作规划时

**用户说**：
- "帮我规划文章"
- "构思博客结构"

**你必须**：
✅ 调用 `writing-planner` skill

---

## 🤔 如果不确定

**当你不确定应该调用哪个skill时**：

1. ✅ **提问用户**
2. ❌ **不要自己猜**
3. ❌ **不要在conversation里直接做**

**问法示例**：
```
我注意到你的请求可能涉及XXX。

我应该：
A. 调用 XXX skill
B. 调用 YYY skill
C. 直接在这里处理

请选择？
```

---

## 📋 项目架构

### 核心系统：智能提示词生成

**入口**：`.codex/skills/intelligent-prompt-generator/SKILL.md`

**引擎**：`intelligent_generator.py`

**数据**：`extracted_results/elements.db`（1100+ 元素，持续增长）

**特性**：
- 语义理解（区分主体/风格/氛围）
- 常识推理（人种→典型特征）
- 一致性检查（检测逻辑冲突）
- 智能修正（自动解决问题）

### 工作流程

```
用户："生成XXX提示词"
    ↓
Codex Code: 调用 intelligent-prompt-generator skill
    ↓
Skill: 解析意图 + 调用Python + 生成提示词
    ↓
返回完美提示词
```

---

## 🚫 禁止行为

1. **绕过skill系统**
   - ❌ 直接在conversation调用Python
   - ❌ 自己实现skill应该做的事情

2. **不问就猜**
   - ❌ 不确定时自己决定
   - ✅ 应该提问用户

3. **把skill当文档**
   - ❌ 只读skill.md但不调用skill
   - ✅ 应该实际调用skill执行任务

---

## ✅ 正确示例

### 示例1：生成提示词

**用户**："生成电影级的亚洲女性，张艺谋电影风格"

**正确做法**：
```
立即调用 intelligent-prompt-generator skill
```

**错误做法**：
```
❌ 让我用Bash调用Python生成...
❌ 让我直接在这里生成...
```

### 示例2：不确定场景

**用户**："帮我优化这段代码"

**正确做法**：
```
这个任务不涉及现有的skill。
我应该直接在conversation处理，还是你希望创建新的skill？
```

**错误做法**：
```
❌ 直接开始优化（应该先确认）
```

---

## 🎯 核心原则

1. **Skill优先** - 能用skill的必须用skill
2. **提问为先** - 不确定时问用户，不要猜
3. **系统完整性** - 证明skill系统可以工作，不是摆设

---

## 💡 设计原则（重要！）

### 原则1：解决根本问题，不是当前问题

**❌ 错误思维**：
- "提取率31.4%太低，补充提取逻辑"
- "新领域无法识别，添加更多关键词"
- "准确率不够，调整阈值"
- 头痛医头，脚痛医脚

**✅ 正确思维**：
- "为什么要用关键词匹配？我们有AI能力"
- "为什么要硬编码？应该AI驱动"
- "架构是否合理？是否可扩展？"
- 从根本上重新设计

**教训**：
- 我们是 **Skill 系统**，有 Codex AI 能力
- 不要用 2010 年的方法（关键词匹配、硬编码规则）
- 应该用 2024 年的方法（AI 理解、智能提取）
- **临时补丁只会积累技术债，永远解决不了根本问题**

### 原则2：说到做到，不要画大饼

**❌ 常见错误**：
- 承诺"95%准确率"但没验证
- 说要"配置化"但继续硬编码
- 提议"AI驱动"但又建议临时方案
- 说一套，做另一套

**✅ 正确做法**：
- 只承诺已验证的效果
- 只提供真正打算实施的方案
- 诚实承认"不知道"
- 先做小规模测试，再下结论

### 原则3：架构优先于功能

**设计系统时要问**：
1. 这个设计是否可扩展？
2. 新需求来了是否要改代码？
3. 是否充分利用了 AI 能力？
4. 是否方便维护和测试？

**不要问**：
1. 能不能快速修复当前问题？
2. 能不能少改点代码？
3. 能不能不重构？

---

**记住**：
- 我们在建立 skill 系统，不是展示 Codex Code 有多强！
- **解决根本问题，不是当前问题**
- **说到做到，不要画大饼**
