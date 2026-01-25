# 粘贴式交互模式使用指南

## 什么是粘贴式交互？

**传统方式**：需要先创建文件 → 保存 → 提供路径
**粘贴模式**：直接复制提示词 → 粘贴给Claude → 立即分析 ✨

**适用场景**：
- 快速分析1-50条提示词
- 临时测试新prompt结构
- 从网页/社交媒体收集的片段
- 不想创建临时文件

## 使用方法

### 方式1：完整对话式

**步骤1：激活Skill**
```
用户：使用 prompt-extractor
```

**步骤2：选择粘贴模式**
```
Claude：请选择输入方式：
       1. 提供文件路径
       2. 直接粘贴提示词

用户：2
```

**步骤3：粘贴内容**
```
用户：
a portrait of a young woman, cinematic lighting, 85mm lens, ultra detailed
cyberpunk city at night, neon lights, rain, photorealistic, 8k
beautiful landscape, golden hour, dramatic clouds, HDR
```

**步骤4：自动处理**
```
Claude：
✓ 已接收3条提示词
✓ 开始提取模块...
[提取结果展示]
```

---

### 方式2：一句话启动（推荐）

直接说：
```
帮我分析这些AI绘画提示词：

a portrait of a young woman, cinematic lighting, 85mm lens, ultra detailed
cyberpunk city at night, neon lights, rain, photorealistic, 8k
```

Claude会自动：
- 识别你在粘贴提示词
- 激活 prompt-extractor skill
- 立即开始提取分析

---

### 方式3：混合模式

```
用户：用 prompt-extractor 分析下面这些：

1. "stunning portrait, soft lighting, dreamy atmosphere"
2. "futuristic cityscape, neon colors, cyberpunk style, 4k"
3. "landscape photography, misty mountains, sunrise, HDR"
```

支持：
- 带编号的列表
- 带引号的文本
- 用逗号/换行分隔

---

## 支持的格式

### ✅ 推荐格式

**换行分隔**（最清晰）
```
提示词1
提示词2
提示词3
```

**逗号+换行**
```
提示词1,
提示词2,
提示词3
```

**带编号**
```
1. 提示词1
2. 提示词2
3. 提示词3
```

**JSON数组**（适合从代码复制）
```json
[
  "提示词1",
  "提示词2",
  "提示词3"
]
```

### ⚠️ 需要注意的格式

**逗号分隔**（可能混淆提示词内部的逗号）
```
提示词1, 提示词2, 提示词3
# 如果提示词本身含逗号，会分割错误
```

建议改为：
```
提示词1
---
提示词2
---
提示词3
```

---

## 实战示例

### 示例1：分析收藏的优秀prompt

**场景**：从ArtStation看到5个优秀作品的提示词

```
我：帮我分析这些优秀提示词：

portrait of a woman, cinematic studio lighting, 85mm f/1.4, shallow depth of field, soft bokeh, professional photography, ultra detailed, photorealistic

cyberpunk samurai, neon-lit tokyo street, rain reflections, dramatic pose, blade runner aesthetic, purple and cyan color scheme, cinematic composition, 8k, trending on artstation

mystical forest, god rays through mist, ancient trees, magical atmosphere, fantasy art, greg rutkowski style, ethereal lighting, vibrant colors, highly detailed

macro photography of dewdrops on flower petals, golden hour lighting, shallow DOF, natural colors, bokeh background, canon 100mm macro, crystal clear details

futuristic architecture, zaha hadid style, flowing curves, white marble and glass, blue hour photography, symmetrical composition, architectural visualization, unreal engine 5
```

**Claude输出**：
```json
{
  "总览": {
    "数量": 5,
    "主题分布": {
      "人像摄影": 1,
      "场景概念": 2,
      "微距摄影": 1,
      "建筑设计": 1
    }
  },
  "提取的核心模块": {
    "高频技术参数": [
      "cinematic lighting (2次)",
      "8k/ultra detailed (5次)",
      "shallow depth of field (2次)"
    ],
    "高频视觉风格": [
      "photorealistic (1次)",
      "fantasy art (1次)",
      "cyberpunk (1次)"
    ],
    "高频构图": [
      "symmetrical composition (1次)",
      "dramatic pose (1次)"
    ],
    "色彩方案": [
      "purple and cyan (1次)",
      "natural colors (1次)"
    ],
    "参考艺术家": [
      "Greg Rutkowski",
      "Zaha Hadid"
    ]
  },
  "发现的模式": [
    "所有提示都包含质量增强词（ultra detailed/8k等）",
    "80%指定了具体光线类型",
    "60%引用了专业标准（摄影器材、艺术家）",
    "结构类型：主体 + 技术/风格 + 质量增强"
  ],
  "可复用模板": {
    "人像摄影": "{人物}, cinematic lighting, 85mm f/1.4, shallow DOF, ultra detailed, photorealistic",
    "场景概念": "{场景}, {氛围}, {色彩方案}, cinematic composition, 8k, trending on artstation",
    "建筑可视化": "{建筑风格}, {材质}, {时间}, symmetrical composition, unreal engine 5"
  }
}
```

---

### 示例2：快速测试单个prompt的结构

```
我：分析这个prompt的模块结构：

a mystical elven warrior princess, flowing silver hair, emerald eyes, ornate armor with Celtic patterns, standing in enchanted forest, magical blue fireflies, ethereal mist, dramatic rim lighting, fantasy art, artstation trending, highly detailed, 8k, unreal engine
```

**Claude输出**：
```json
{
  "original_prompt": "a mystical elven warrior princess...",
  "modules": {
    "subject_variables": {
      "main": "elven warrior princess",
      "modifiers": ["mystical"],
      "attributes": ["flowing silver hair", "emerald eyes"],
      "is_replaceable": true
    },
    "visual_style": {
      "art_style": "fantasy art",
      "era": "mythological"
    },
    "technical_parameters": {
      "lighting": "dramatic rim lighting",
      "render_engine": "unreal engine",
      "resolution": "8k"
    },
    "detail_enhancers": ["highly detailed", "8k"],
    "mood_atmosphere": "mystical, ethereal",
    "composition": {
      "perspective": "standing pose (full body implied)",
      "depth_of_field": "implied foreground subject focus"
    },
    "color_scheme": {
      "palette": ["silver", "emerald", "blue"],
      "tone": "cool tones",
      "specific_colors": "silver hair, emerald eyes, blue fireflies"
    },
    "time_season": {
      "weather": "misty"
    },
    "references": {
      "platforms": ["artstation trending"]
    }
  },
  "quality_score": {
    "clarity": 9,
    "detail_richness": 10,
    "reusability": 8,
    "comments": "结构完整，细节丰富，主体描述具体，易于替换核心元素"
  },
  "提取的模板": "{角色描述}, {外观细节}, {服饰/道具}, {场景环境}, {氛围元素}, {光线}, {风格}, {质量增强}"
}
```

**关键发现**：
- ✓ 10大模块中使用了8个
- ✓ 主体描述非常详细（发色、眼睛、服饰）
- ✓ 环境和氛围词丰富（森林、萤火虫、雾气）
- ⚠️ 缺少构图参数（可补充视角）
- ⚠️ 缺少约束条件（可添加负面提示）

**改进建议**：
```
原始：a mystical elven warrior princess, flowing silver hair...
改进：a mystical elven warrior princess, flowing silver hair..., **front view, rule of thirds composition, --no blurry, distorted**
```

---

### 示例3：对比两个prompt找差异

```
我：对比这两个提示词，哪个更好？

A: portrait of a woman, beautiful, detailed
B: portrait of a young woman, cinematic studio lighting, 85mm lens f/1.4, soft bokeh background, natural skin texture, professional photography, ultra high resolution, photorealistic
```

**Claude分析**：
```markdown
## 对比分析

### Prompt A
- 模块数量：2个（主体 + 细节增强）
- 质量评分：4/10
- 问题：
  - 缺乏技术参数（光线、镜头）
  - "beautiful"过于主观
  - "detailed"泛泛而谈
  - 无具体风格指引

### Prompt B
- 模块数量：7个（主体、技术、细节、构图、视觉风格等）
- 质量评分：9/10
- 优势：
  - 技术参数明确（85mm f/1.4）
  - 光线指定（cinematic studio lighting）
  - 细节具体（natural skin texture）
  - 质量标准清晰（photorealistic, ultra high resolution）
  - 构图暗示（soft bokeh background → 浅景深）

### 结论
**B 明显优于 A**

差距原因：
1. 技术参数的缺失vs完整
2. 主观形容词vs客观描述
3. 模糊指引vs精确指令

### 学习要点
从B中提取的可复用模式：
- ✓ 永远指定光线类型
- ✓ 镜头参数提升专业度
- ✓ 用技术词替代主观词（"photorealistic" > "beautiful"）
- ✓ 细节具体化（"natural skin texture" > "detailed"）
```

---

## 高级技巧

### 技巧1：批量粘贴变体测试

```
我：分析这3个渐进版本的差异：

v1: girl, pink hair, cute
v2: anime girl, pink hair, cute expression, colorful
v3: anime girl, vibrant pink hair, cute expression with sparkles in eyes, colorful outfit, studio ghibli style, soft lighting, pastel colors, highly detailed, 4k
```

Claude会自动：
- 对比3个版本的模块覆盖度
- 展示渐进优化路径
- 给出继续改进建议

---

### 技巧2：从Midjourney/SD导出直接粘贴

**Midjourney导出格式**：
```
我：分析我的MJ历史记录：

/imagine prompt: cyberpunk city, neon lights --ar 16:9 --v 5
/imagine prompt: portrait, cinematic --ar 2:3 --stylize 750
/imagine prompt: landscape, epic --q 2
```

Claude会：
- 自动剔除MJ命令语法
- 只提取核心prompt部分
- 识别参数（--ar, --v等）并归类到"约束条件"

---

### 技巧3：混合文件+粘贴

```
我：先分析 my_library.json，然后对比这个新prompt：

stunning landscape, misty mountains at sunrise, golden light, dramatic clouds
```

Claude会：
- 加载现有库
- 分析新prompt
- 对比找出库中已有/缺失的模块
- 建议如何融合

---

## 限制与最佳实践

### 数量限制

| 模式 | 推荐数量 | 最大数量 | 处理时间 |
|------|---------|---------|---------|
| 单条分析 | 1 | 1 | <10秒 |
| 小批量 | 5-10 | 50 | 1-3分钟 |
| 中批量 | - | 100 | 5-10分钟 |
| 大批量 | 用文件 | - | - |

**建议**：
- 1-10条 → 粘贴模式
- 10-50条 → 粘贴模式（分批）
- >50条 → 文件模式

---

### 格式建议

**✅ 推荐**：
```
# 每行一个，清晰明确
提示词1
提示词2
提示词3
```

**⚠️ 小心**：
```
# 逗号分隔（提示词内部也有逗号时易混淆）
girl, pink hair, cute, boy, blue shirt, cool
# ↑ 会被错误分为6条而非2条
```

**解决方案**：
```
# 用换行或明确分隔符
girl, pink hair, cute
---
boy, blue shirt, cool
```

---

## 常见问题

### Q1: 粘贴长文本后没反应？
**A**: 可能超过了上下文限制。建议：
- 分批粘贴（每批20-30条）
- 或保存为文件使用文件模式

### Q2: 提示词被错误分割怎么办？
**A**: 使用更明确的分隔符：
```
===提示词1===
a portrait of woman, detailed

===提示词2===
landscape, mountains
```

### Q3: 能粘贴中文提示词吗？
**A**: 完全支持！
```
我：分析这些中文提示词：

一位年轻女性的肖像，电影级光线，85mm镜头，超高清细节
赛博朋克城市夜景，霓虹灯，雨水反射，8k超高清
```

### Q4: 能从Excel复制粘贴吗？
**A**: 可以！复制Excel的一列：
```
[从Excel复制]
portrait, lighting, 8k
landscape, sunset, HDR
cityscape, neon, 4k

[粘贴到Claude]
我：分析这些从表格复制的提示词：
portrait, lighting, 8k
landscape, sunset, HDR
cityscape, neon, 4k
```

---

## 实用工作流

### 工作流1：日常收集与分析

```mermaid
浏览网页/社交媒体
  ↓
看到好提示词 → 复制
  ↓
粘贴给Claude Code
  ↓
立即获得结构分析
  ↓
积累到个人模块库
```

### 工作流2：提示词优化迭代

```
1. 粘贴初稿提示词
2. 获得结构分析 + 缺失模块提示
3. 根据建议补充模块
4. 再次粘贴新版本
5. 对比改进效果
6. 重复直到满意
```

### 工作流3：学习大师作品

```
1. 从顶级作品提取提示词
2. 批量粘贴给Claude
3. 分析共同模式
4. 提取复用模板
5. 应用到自己创作
```

---

**开始尝试粘贴模式吧！** 🚀

随时在Claude Code中粘贴你的提示词，无需创建文件，立即开始分析！
