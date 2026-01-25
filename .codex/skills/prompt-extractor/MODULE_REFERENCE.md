# 10大模块分类完整参考手册

## 模块体系概览

```
AI绘画提示词 = 10大模块的组合
├── 1. 主体变量 (Subject Variables)
├── 2. 视觉风格 (Visual Style)
├── 3. 技术参数 (Technical Parameters)
├── 4. 细节增强 (Detail Enhancers)
├── 5. 情绪氛围 (Mood & Atmosphere)
├── 6. 约束条件 (Constraints)
├── 7. 构图参数 (Composition) ← 新增
├── 8. 色彩方案 (Color Scheme) ← 新增
├── 9. 时间/季节 (Time & Season) ← 新增
└── 10. 参考艺术家/作品 (References) ← 新增
```

---

## 1. 主体变量 (Subject Variables)

**定义**：提示词的核心对象，可替换性最强的部分。

### 子模块
- **main**: 主对象（人物、物体、场景）
- **modifiers**: 修饰词
- **attributes**: 具体属性
- **is_replaceable**: 是否可替换（布尔值）

### 示例

| 提示词 | 主对象 | 修饰词 | 属性 |
|--------|--------|--------|------|
| "a young woman" | woman | young | - |
| "cyberpunk city" | city | cyberpunk | - |
| "red sports car" | sports car | - | red |
| "elven warrior, silver hair" | elven warrior | - | silver hair |

### 提取技巧
- 通常在提示词开头
- 名词或名词短语
- 去掉后提示词失去主题的部分

### 复用价值
⭐⭐⭐⭐⭐ (最高)
- 替换主体可生成同风格不同主题的作品
- 模板复用的核心

---

## 2. 视觉风格 (Visual Style)

**定义**：整体艺术风格、画风、年代感。

### 子模块
- **art_style**: 艺术风格
- **era**: 年代感/时代

### 常见风格分类

**写实类**：
- photorealistic, hyperrealistic, photo-real
- cinematic, filmic
- documentary style

**艺术类**：
- oil painting, watercolor, ink drawing
- digital art, concept art
- pixel art, low poly

**风格流派**：
- impressionism, surrealism, abstract
- anime style, manga style
- art deco, art nouveau

**特定世界观**：
- cyberpunk, steampunk, dieselpunk
- fantasy, sci-fi, post-apocalyptic
- retro, vintage, futuristic

### 示例

```
photorealistic → 照片级真实
anime style → 动漫风格
oil painting, renaissance style → 文艺复兴油画
cyberpunk aesthetic → 赛博朋克美学
minimalist design → 极简主义设计
```

### 复用价值
⭐⭐⭐⭐⭐
- 定义整体视觉基调
- 风格一致性的关键

---

## 3. 技术参数 (Technical Parameters)

**定义**：摄影/渲染的技术规格。

### 子模块
- **camera**: 镜头参数
- **lighting**: 光线描述
- **render_engine**: 渲染引擎
- **resolution**: 分辨率/质量

### 镜头参数详解

**焦距**：
- 14mm, 24mm → 超广角
- 35mm, 50mm → 标准镜头
- 85mm, 105mm → 人像镜头
- 200mm+ → 长焦/野生动物

**光圈**：
- f/1.4, f/1.8 → 大光圈，浅景深
- f/8, f/11 → 小光圈，大景深

### 光线类型

**自然光**：
- natural lighting, sunlight
- window light, diffused light
- golden hour, blue hour

**人工光**：
- studio lighting, softbox
- ring light, key light
- neon lights, LED

**特殊光效**：
- rim lighting (轮廓光)
- backlighting (逆光)
- volumetric lighting (体积光)
- god rays (丁达尔效应)

### 渲染引擎

```
Unreal Engine 5 → 游戏级实时渲染
Octane Render → 高质量离线渲染
V-Ray → 建筑可视化
Blender Cycles → 开源渲染器
```

### 示例

```
85mm lens f/1.4 → 人像标准配置
wide angle 24mm → 风光/建筑
macro 100mm lens → 微距摄影
cinematic lighting, rim light → 电影级光效
rendered in Unreal Engine 5 → UE5渲染
```

### 复用价值
⭐⭐⭐⭐
- 直接影响成片质量
- 专业感的体现

---

## 4. 细节增强 (Detail Enhancers)

**定义**：提升质量、细节的修饰词。

### 分类

**分辨率/清晰度**：
- 8k, 4k, ultra high resolution
- sharp focus, crystal clear
- highly detailed, intricate details

**质量标准**：
- professional photography
- award-winning
- masterpiece, best quality

**平台/竞赛**：
- trending on artstation
- featured on behance
- contest winner

### 常见组合

```
ultra detailed, 8k, sharp focus
highly detailed, intricate, professional
hyperrealistic, photorealistic, 8k uhd
masterpiece, best quality, award-winning
```

### 示例

| 提示词 | 效果 |
|--------|------|
| 8k | 暗示极高分辨率 |
| sharp focus | 强调清晰度 |
| intricate details | 复杂细节 |
| professional photography | 专业摄影水准 |

### 复用价值
⭐⭐⭐⭐
- 几乎所有提示词都需要
- 显著提升生成质量

---

## 5. 情绪氛围 (Mood & Atmosphere)

**定义**：情感基调、氛围感受。

### 情绪类型

**正面情绪**：
- joyful, cheerful, uplifting
- peaceful, serene, calm
- epic, majestic, grand

**负面情绪**：
- melancholic, sad, somber
- tense, anxious, ominous
- dark, gloomy, moody

**中性/复杂**：
- mysterious, enigmatic
- nostalgic, wistful
- ethereal, dreamlike

### 氛围描述

**空间氛围**：
- cozy, intimate
- vast, expansive
- claustrophobic, confined

**时间氛围**：
- timeless, eternal
- fleeting, transient
- suspended in time

### 示例

```
peaceful morning atmosphere
dark and mysterious mood
epic and dramatic feeling
nostalgic 80s vibe
ethereal dreamlike quality
```

### 复用价值
⭐⭐⭐
- 传递情感信息
- 提升艺术表现力

---

## 6. 约束条件 (Constraints)

**定义**：负面提示、排除元素、技术约束。

### 子模块
- **negative_prompt**: 负面提示
- **exclusions**: 排除元素

### 常见负面提示

**质量相关**：
- no blur, not blurry
- no distortion, no artifacts
- no noise, no grain (除非刻意要胶片感)

**内容相关**：
- no text, no watermark
- no extra limbs, no deformed
- no low quality, no bad anatomy

**Stable Diffusion专用**：
```
Negative: ugly, tiling, poorly drawn hands, poorly drawn feet,
poorly drawn face, out of frame, extra limbs, disfigured,
deformed, body out of frame, blurry, bad anatomy, blurred,
watermark, grainy, signature, cut off, draft
```

**Midjourney专用**：
```
--no text, watermark, signature
--no blur, distortion
```

### 示例

```
portrait of a woman, beautiful, detailed
Negative: ugly, deformed, blurry, low quality

landscape, mountains, epic
--no people, buildings, text
```

### 复用价值
⭐⭐⭐⭐
- 避免常见问题
- 提高成片率

---

## 7. 构图参数 (Composition) ✨ 新增

**定义**：画面构图、视角、景深等视觉组织方式。

### 子模块
- **perspective**: 视角
- **depth_of_field**: 景深
- **aspect_ratio**: 画幅比例
- **symmetry**: 对称性
- **rule**: 构图法则

### 视角类型

**高度视角**：
- bird's eye view (鸟瞰)
- high angle (俯视)
- eye level (平视)
- low angle (仰视)
- worm's eye view (虫视)

**距离视角**：
- extreme close-up (大特写)
- close-up (特写)
- medium shot (中景)
- full body (全身)
- wide shot (远景)

**特殊视角**：
- first person POV (第一人称)
- over the shoulder (过肩)
- dutch angle (荷兰角/倾斜)

### 景深描述

```
shallow depth of field (浅景深) → 背景虚化
deep depth of field (大景深) → 全景清晰
bokeh background (焦外散景)
f/1.4, soft bokeh → 柔美散景
```

### 画幅比例

| 比例 | 用途 | 示例 |
|------|------|------|
| 1:1 | 社交媒体 | Instagram |
| 16:9 | 电影/横屏 | YouTube |
| 9:16 | 竖屏视频 | TikTok |
| 4:3 | 传统摄影 | 经典照片 |
| 21:9 | 超宽电影 | 影院 |

### 构图法则

**经典法则**：
- rule of thirds (三分法)
- golden ratio (黄金分割)
- leading lines (引导线)
- frame within frame (框中框)

**对称构图**：
- symmetrical composition
- centered composition
- radial symmetry

### 示例

```
portrait, close-up, shallow DOF, f/1.4
landscape, wide shot, deep focus, rule of thirds
architectural photo, symmetrical composition, centered
bird's eye view, urban cityscape, dramatic perspective
```

### 复用价值
⭐⭐⭐⭐⭐
- 专业摄影必备
- 显著提升构图质量

---

## 8. 色彩方案 (Color Scheme) ✨ 新增

**定义**：色调、配色、饱和度等色彩相关描述。

### 子模块
- **tone**: 色调（暖/冷）
- **palette**: 调色板/主要颜色
- **saturation**: 饱和度
- **contrast**: 对比度
- **temperature**: 色温

### 色调分类

**温度色调**：
- warm tones (暖色调) → 红橙黄
- cool tones (冷色调) → 蓝绿紫
- neutral tones (中性色调) → 灰白黑

**明度色调**：
- bright colors (明亮色)
- pastel colors (粉彩色)
- dark colors (深色)
- muted colors (柔和色)

### 配色方案

**单色系**：
- monochromatic (单色)
- black and white (黑白)
- sepia tones (棕褐色)

**互补色**：
- blue and orange
- purple and yellow
- red and cyan

**类似色**：
- analogous colors (邻近色)
- earth tones (大地色)
- jewel tones (宝石色)

**特定配色**：
- cyberpunk colors (赛博朋克) → 紫、青、粉
- vaporwave aesthetic → 粉、青、紫渐变
- autumn colors → 橙、黄、棕
- nordic palette → 灰、白、蓝

### 饱和度描述

```
highly saturated, vibrant colors → 高饱和鲜艳
desaturated, washed out → 低饱和褪色
oversaturated, neon colors → 过饱和霓虹
natural colors, true to life → 自然真实色彩
```

### 对比度

```
high contrast → 强对比
low contrast, soft → 低对比柔和
dramatic contrast → 戏剧性对比
subtle contrast → 微妙对比
```

### 示例

```
warm color palette, golden tones → 暖色系金色调
cool blue and purple tones, high contrast
cyberpunk colors, neon pink and cyan, vibrant
pastel colors, soft and dreamy, low saturation
monochromatic blue, various shades of blue
```

### 复用价值
⭐⭐⭐⭐⭐
- 定义视觉情绪
- 风格一致性关键

---

## 9. 时间/季节 (Time & Season) ✨ 新增

**定义**：时间段、季节、天气状态。

### 子模块
- **time_of_day**: 时间段
- **season**: 季节
- **weather**: 天气状态

### 时间段

**黄金时刻**：
- golden hour (日出日落前后1小时)
- blue hour (民用曙暮光时段)
- magic hour (魔法时刻)

**一天时段**：
- dawn, sunrise (黎明、日出)
- morning, noon (早晨、正午)
- afternoon (下午)
- dusk, sunset (黄昏、日落)
- twilight (暮光)
- night, midnight (夜晚、午夜)

### 季节特征

| 季节 | 视觉特征 | 关键词 |
|------|---------|--------|
| 春 Spring | 新绿、花朵 | cherry blossoms, fresh green |
| 夏 Summer | 明亮、阳光 | bright sunlight, lush |
| 秋 Autumn | 金黄、落叶 | golden leaves, harvest |
| 冬 Winter | 雪、冷色 | snow, frost, cold |

### 天气状态

**晴朗**：
- clear sky, sunny
- cloudless, bright

**云雾**：
- cloudy, overcast
- misty, foggy
- hazy

**降水**：
- rainy, rain drops
- snowy, snowfall
- stormy

**特殊天气**：
- dramatic clouds
- storm clouds, lightning
- rainbow after rain

### 光线与时间的关系

```
golden hour → 温暖金色光线，长阴影
blue hour → 冷蓝色调，柔和光线
noon → 强烈顶光，短阴影
overcast → 柔和漫射光，无明显阴影
```

### 示例

```
golden hour lighting, warm sunset glow
misty morning, soft diffused light
winter scene, snow falling, cold blue tones
stormy sky, dramatic clouds, moody atmosphere
cherry blossom season, spring, soft pink petals
```

### 复用价值
⭐⭐⭐⭐
- 自然光效的关键
- 氛围营造重要元素

---

## 10. 参考艺术家/作品 (References) ✨ 新增

**定义**：引用特定艺术家、作品风格、平台风格。

### 子模块
- **artists**: 艺术家名称列表
- **styles**: 特定风格引用
- **platforms**: 平台风格

### 热门艺术家

**数字艺术**：
- Greg Rutkowski (奇幻、史诗)
- Artgerm (人物、插画)
- Sakimichan (动漫风)
- Loish (色彩、角色)

**传统大师**：
- Rembrandt (光影大师)
- Monet (印象派)
- Van Gogh (后印象派)
- Caravaggio (巴洛克)

**概念艺术**：
- Syd Mead (未来主义)
- H.R. Giger (生物机械)
- Moebius (科幻漫画)

**摄影师**：
- Annie Leibovitz (人像)
- Ansel Adams (风光)
- Steve McCurry (纪实)

### 工作室/品牌风格

```
Studio Ghibli style → 吉卜力动画风格
Pixar style → 皮克斯3D动画
Disney animation → 迪士尼风格
Wes Anderson aesthetic → 韦斯·安德森电影美学
```

### 平台引用

**艺术社区**：
- trending on ArtStation
- featured on Behance
- DeviantArt popular

**摄影平台**：
- 500px, Flickr
- National Geographic style
- Vogue magazine style

### 使用技巧

**单一引用**：
```
portrait by Annie Leibovitz → 清晰风格指向
```

**混合引用**：
```
Greg Rutkowski and Alphonse Mucha style → 融合两种风格
in the style of Studio Ghibli meets Moebius → 风格碰撞
```

**时代引用**：
```
renaissance painting style → 文艺复兴风格
80s retro aesthetic → 80年代复古
```

### 示例

```
fantasy landscape, Greg Rutkowski style, dramatic lighting
portrait, Annie Leibovitz style, fashion photography
cyberpunk city, Syd Mead inspired, futuristic
anime character, Studio Ghibli style, watercolor
trending on ArtStation, award-winning digital art
```

### 复用价值
⭐⭐⭐⭐⭐
- 快速传达风格期望
- 专业圈层认可度高

---

## 模块使用策略

### 必备模块（每个提示词都应包含）

1. ✅ **主体变量** - 核心对象
2. ✅ **细节增强** - 质量保障
3. ✅ **视觉风格** 或 **参考艺术家** - 风格定义

### 高价值模块（显著提升质量）

4. ⭐ **技术参数** - 专业感
5. ⭐ **构图参数** - 专业摄影感
6. ⭐ **色彩方案** - 视觉一致性

### 氛围模块（增强表现力）

7. **情绪氛围** - 情感传递
8. **时间/季节** - 自然光效

### 辅助模块（按需使用）

9. **约束条件** - 避免常见问题
10. 其他专项模块

---

## 模块组合模板

### 人像摄影模板

```
{主体} + {技术参数} + {光线} + {构图} + {细节增强}

示例：
portrait of a young woman, 85mm lens f/1.4, soft studio lighting,
shallow depth of field, rule of thirds composition,
ultra detailed, photorealistic, 8k
```

使用模块：1, 3, 4, 7, 5

---

### 风景摄影模板

```
{场景} + {时间/季节} + {色彩} + {构图} + {氛围} + {细节}

示例：
mountain landscape, golden hour sunset, warm orange and purple tones,
wide angle shot, dramatic atmosphere, highly detailed, 8k, HDR
```

使用模块：1, 9, 8, 7, 5, 4

---

### 概念艺术模板

```
{主体} + {风格} + {参考} + {色彩} + {氛围} + {细节}

示例：
futuristic city, cyberpunk aesthetic, Syd Mead inspired,
neon purple and cyan colors, moody atmosphere,
highly detailed, trending on ArtStation, 8k
```

使用模块：1, 2, 10, 8, 5, 4

---

### 角色设计模板

```
{角色} + {外观} + {风格} + {参考} + {细节}

示例：
elven warrior princess, silver armor with celtic patterns,
fantasy art, Greg Rutkowski style, intricate details,
highly detailed, 8k, masterpiece
```

使用模块：1, 2, 10, 4

---

## 模块权重建议

不同AI工具对模块的敏感度不同：

| 模块 | Midjourney | Stable Diffusion | DALL-E 3 |
|------|------------|------------------|----------|
| 主体变量 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 视觉风格 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 技术参数 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| 细节增强 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| 参考艺术家 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| 构图参数 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 色彩方案 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 时间/季节 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 约束条件 | ⭐⭐⭐ (--no) | ⭐⭐⭐⭐⭐ | ⭐⭐ |

---

## 快速参考卡片

**最小可用提示词**（3模块）：
```
{主体} + {风格} + {质量}
girl + anime style + detailed
```

**标准提示词**（5-6模块）：
```
{主体} + {风格} + {技术} + {构图} + {色彩} + {质量}
portrait + cinematic + 85mm f/1.4 + close-up + warm tones + 8k
```

**专业提示词**（8-10模块全覆盖）：
```
所有模块精细配置，300+ tokens
```

---

**使用这个参考手册**可以：
- 快速查找模块定义
- 理解每个模块的作用
- 学习专业术语
- 构建自己的提示词模板