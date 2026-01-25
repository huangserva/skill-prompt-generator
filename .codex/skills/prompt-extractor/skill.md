---
name: prompt-extractor
description: 自动化提取AI绘画提示词的模块化结构，从海量提示词中提炼可复用的模块组件
---

# Prompt Extractor Skill

自动化提取AI绘画提示词的模块化结构，从海量提示词中提炼可复用的模块组件。

## 核心功能

你是一位提示词工程专家，专注于AI图像生成（如Midjourney、DALL-E、Stable Diffusion）提示词的结构化分析和模块提取。

## 工作流程

当用户调用此skill时，按以下步骤执行：

### 1. 数据读取与预处理

支持两种输入方式：

**方式A：文件路径**
- 接收用户提供的提示词文件路径（支持 txt, csv, json 格式）
- 自动识别文件格式并解析

**方式B：直接粘贴**（推荐用于小批量）
- 用户可以直接粘贴提示词文本（每行一个或用分隔符）
- 无需创建文件，实时处理
- 支持单条或多条（最多100条/次）

**数据清洗：**
- 去重、去除无效短提示（<10字符）
- 统一标点符号
- 如果是CSV/JSON，自动识别包含提示词的列/字段

### 2. 智能聚类分析（仅处理>100条时）

对于大批量数据，先进行主题聚类：
- 基于关键词频率统计（如"微距"、"电影感"、"梦幻"）
- 分组相似提示（建议3-5个主题簇）
- 为每个簇生成主题标签

### 3. 模块化提取

针对每条提示词，提取以下模块：

**核心模块类型（10大类）：**
1. **主体变量** (Subject Variables)：可替换的核心对象（人物、物体、场景）
2. **视觉风格** (Visual Style)：艺术风格、画风、年代感
3. **技术参数** (Technical Parameters)：镜头、光线、分辨率、渲染引擎
4. **细节增强** (Detail Enhancers)：质量修饰词、强调词
5. **情绪氛围** (Mood & Atmosphere)：情感基调、氛围描述
6. **约束条件** (Constraints)：负面提示、排除元素
7. **构图参数** (Composition)：视角、景深、框架比例、对称性、构图法则
8. **色彩方案** (Color Scheme)：色调、配色、饱和度、对比度、色温
9. **时间/季节** (Time & Season)：时间段（黎明/黄昏）、季节、天气状态
10. **参考艺术家/作品** (References)：艺术家引用、特定作品风格、平台风格

### 3.5 特殊模式识别（针对复杂摄影提示词）

**摄影流派自动识别** (10大流派):
扫描关键词自动标记 `photography_genre` 字段，按优先级依次匹配：

**高优先级（直接设备/软件识别）**:
- `analog_film`: "Kodak Portra", "Hasselblad medium format", "film grain", "analog", "organic grain"
- `editorial_macro`: "Phase One", "100mm macro", "medium format", "editorial", "glossy", "collector's edition"
- `3d_render`: "C4D", "Blender", "Octane", "3D rendering", "Pixar", "Disney", "cartoon rendering"

**中优先级（组合关键词）**:
- `studio_product`: "studio lighting" + "seamless background" + "product photography" + "softbox/rim light"
- `cinematic_narrative`: "Canon R5" + "cinema" + "practical props/live-action" + "film set/movie"
- `conceptual_art`: "surrealism" + "conceptual/artistic" + "material sculpting/consciousness" + "award-winning"
- `collage_composite`: "grid layout" + "multi-panel/collage" + "composite" + "3x3/4-panel"
- `hybrid_illustration`: "Neo-Chinese/ink wash/shuimo" + "traditional" + "abstract illustration" + "watercolor"

**低优先级（默认分类）**:
- `portrait_beauty`: "beauty portrait" + "golden hour" + "shallow DOF" + "bokeh" + (非Cosplay + 非概念)
- `digital_commercial`: "8K digital" + "commercial photography" + (无其他明确特征时默认)

**对立标准结构化提取**:
在 `constraints` 模块中识别"必须 vs 禁止"对立结构，创建 `critical_oppositions` 字段：
```json
"constraints": {
  "critical_oppositions": {
    "production": {
      "required": "practical props, real sets",
      "forbidden": "CGI, greenscreen, digital effects"
    },
    "rendering": {
      "required": "realistic skin texture, photorealistic",
      "forbidden": "plastic skin, wax figure, 3D render"
    },
    "photography": {
      "required": "analog film, cinema camera",
      "forbidden": "digital photo, smartphone"
    }
  }
}
```

**设备规格索引化**:
自动提取相机型号、镜头、胶卷信息，记录到 `module_library.json` 的 `camera_equipment_index` 中：
- 识别设备名称（Canon EOS R5, Hasselblad, Phase One等）
- 记录技术规格（分辨率、镜头焦段、胶卷型号）
- 关联应用场景（产品摄影、人像、Cosplay等）
- 标注设备租赁成本参考

**提取输出格式（JSON）：**
```json
{
  "original_prompt": "原始提示词全文",
  "theme": "主题分类（如'人像摄影'、'自然风光'）",
  "modules": {
    "subject_variables": {
      "main": "主对象",
      "modifiers": ["修饰词1", "修饰词2"],
      "is_replaceable": true
    },
    "visual_style": {
      "art_style": "艺术风格（如'电影级'、'赛博朋克'）",
      "era": "年代感（如'80年代'、'未来主义'）",
      "photography_genre": "摄影流派（可选，digital_commercial/analog_film/cinematic_narrative）",
      "genre_confidence": 0.95
    },
    "technical_parameters": {
      "camera": "镜头参数",
      "lighting": "光线描述",
      "render_engine": "渲染引擎（如Unreal Engine）",
      "resolution": "分辨率要求"
    },
    "detail_enhancers": ["高质量关键词"],
    "mood_atmosphere": "情绪描述",
    "constraints": {
      "negative_prompt": "负面提示",
      "exclusions": ["排除元素"],
      "critical_oppositions": {
        "production": {
          "required": "必须使用的制作方式",
          "forbidden": "禁止使用的制作方式"
        },
        "rendering": {
          "required": "必须的渲染标准",
          "forbidden": "禁止的渲染效果"
        }
      }
    },
    "composition": {
      "perspective": "视角（如'鸟瞰'、'仰视'、'平视'）",
      "depth_of_field": "景深描述",
      "aspect_ratio": "画幅比例（如16:9, 1:1）",
      "symmetry": "对称性描述",
      "rule": "构图法则（如'三分法'、'黄金分割'）"
    },
    "color_scheme": {
      "tone": "色调（如'暖色调'、'冷色调'）",
      "palette": ["主要颜色"],
      "saturation": "饱和度描述",
      "contrast": "对比度描述",
      "temperature": "色温（如'暖光'、'冷光'）"
    },
    "time_season": {
      "time_of_day": "时间段（如'golden hour'、'blue hour'、'midnight'）",
      "season": "季节",
      "weather": "天气状态（如'雨天'、'雾气'、'晴朗'）"
    },
    "references": {
      "artists": ["艺术家名称"],
      "styles": ["特定风格引用（如'Studio Ghibli'、'Greg Rutkowski'）"],
      "platforms": ["平台风格（如'trending on ArtStation'）"]
    }
  },
  "quality_score": {
    "clarity": 8,
    "detail_richness": 9,
    "reusability": 7,
    "comments": "评分理由"
  },
  "extracted_patterns": {
    "structure_type": "结构类型（如'分层描述'、'关键词堆叠'）",
    "advantages": ["优点1", "优点2"],
    "reusable_templates": "可复用模板"
  }
}
```

### 3.6 人像面部细节自动提取（针对人像摄影提示词）

**适用流派**: `portrait_beauty`, `analog_film`（人像类）, `cinematic_narrative`（真人角色）

当识别到提示词属于人像摄影类型时，自动提取五官级别的细节并映射到 `facial_features_library.json` 分类库。

**五官分类器** (6大类):

#### 1. **眼型识别** (Eye Type Detection)

**匹配规则**（按优先级）:
```python
# 高优先级：直接关键词匹配
"large expressive eyes" + "almond" → large_expressive_almond
"half-lidded" + "seductive" → half_lidded_seductive
"large" + "blue eyes" + "contact lenses" → large_blue_expressive

# 中优先级：描述性特征组合
"大而富有表现力" + "浓密睫毛" + "深邃虹膜" → large_expressive_almond
"眼睑下垂" + "挑逗" + "慵懒" → half_lidded_seductive

# 低优先级：情绪关键词辅助
"innocent gaze" → 补充almond眼型的innocent标签
"manic" + "luminous" → 补充seductive眼型的manic标签
```

**输出字段**:
```json
"facial_features": {
  "eye_type": {
    "classification": "large_expressive_almond",
    "confidence": 0.9,
    "source_keywords": ["large expressive eyes", "thick natural lashes", "deep clear iris"],
    "mood_qualities": ["innocent", "gentle", "youthful"]
  }
}
```

#### 2. **脸型识别** (Face Shape Detection)

**匹配规则**:
```python
# 直接关键词
"delicate refined Asian facial structure" → oval_asian_refined
"oval face" → oval_asian_refined
"柔和经典的轮廓" + "瓜子脸" → classical_soft_contour

# 结构描述
"symmetrical" + "refined" + "East Asian" → oval_asian_refined
```

**输出字段**:
```json
"facial_features": {
  "face_shape": {
    "classification": "oval_asian_refined",
    "confidence": 0.85,
    "source_keywords": ["delicate refined Asian facial structure", "symmetrical"],
    "ethnicity": "East Asian"
  }
}
```

#### 3. **唇型识别** (Lip Type Detection)

**匹配规则**:
```python
# 关键词匹配
"cherry lips" + "cupid's bow" → cherry_lips_cupids_bow
"soft full" + "gentle pink gloss" → soft_pink_gloss

# 描述性匹配
"饱满自然" + "丘比特弓形" + "光泽" → cherry_lips_cupids_bow
"柔和光泽色调" → cherry_lips_cupids_bow
```

**输出字段**:
```json
"facial_features": {
  "lip_type": {
    "classification": "cherry_lips_cupids_bow",
    "confidence": 0.9,
    "source_keywords": ["full natural cherry lips", "cupid's bow", "soft glossy tone"]
  }
}
```

#### 4. **鼻型识别** (Nose Type Detection)

**匹配规则**:
```python
# 关键词匹配
"small straight nose" → small_straight_delicate
"straight refined nose bridge" + "classical proportions" → straight_classical_refined

# 描述性匹配
"笔直柔和鼻梁" + "古典比例" + "小巧鼻尖" → straight_classical_refined
```

**输出字段**:
```json
"facial_features": {
  "nose_type": {
    "classification": "straight_classical_refined",
    "confidence": 0.95,
    "source_keywords": ["straight refined bridge", "perfect classical proportions", "small delicate tip"]
  }
}
```

#### 5. **皮肤质感识别** (Skin Texture Detection)

**匹配规则**（按特征组合）:
```python
# 瓷肌无瑕型
"flawless" + "porcelain" + "radiant" + "dewy glow" → porcelain_flawless_radiant

# 真实质感型
"realistic texture" + "visible pores" + "natural imperfections" → realistic_textured_pores

# 湿润水感型
"wet skin" + "water droplets" + "dewy" → wet_dewy_droplets

# 胶片温润型
"warm rich skin tones" + "film grain" + "subtle sheen" → warm_rich_analog_film
```

**输出字段**:
```json
"facial_features": {
  "skin_texture": {
    "classification": "porcelain_flawless_radiant",
    "confidence": 0.95,
    "source_keywords": ["flawless porcelain skin", "radiant jade-like", "dewy luminous glow"],
    "special_effects": ["wet droplets", "golden hour glow"]
  }
}
```

#### 6. **表情/情绪识别** (Expression Detection)

**匹配规则**:
```python
# 清纯温柔型
"innocent gaze" + "gentle smile" + "soft introspective" → innocent_gentle_gaze

# 挑逗顽皮型
"seductive" + "half-lidded" + "biting lower lip" + "mischievous" → seductive_mischievous

# 宁静冒险型
"serene" + "adventurous" + "whimsical" + "dreamy" → serene_adventurous
```

**输出字段**:
```json
"facial_features": {
  "expression": {
    "classification": "innocent_gentle_gaze",
    "confidence": 0.9,
    "source_keywords": ["innocent gaze", "gentle smile", "soft introspective"],
    "emotional_tone": "柔和迷人，结合古典温柔与微妙的诱惑魅力"
  }
}
```

---

**完整人像提示词输出示例**（Prompt #5）:

```json
{
  "prompt_id": 5,
  "theme": "人物肖像摄影 / 参数化提示词系统",
  "modules": {
    "visual_style": {
      "photography_genre": "portrait_beauty",
      "genre_confidence": 0.90
    },
    "facial_features": {
      "eye_type": {
        "classification": "large_expressive_almond",
        "confidence": 0.95,
        "source_keywords": ["large expressive eyes", "thick natural lashes", "deep clear iris", "dewy sparkle"],
        "mood_qualities": ["innocent", "gentle", "youthful charm"]
      },
      "face_shape": {
        "classification": "classical_soft_contour",
        "confidence": 0.85,
        "source_keywords": ["柔和经典的轮廓脸或瓜子脸"]
      },
      "lip_type": {
        "classification": "cherry_lips_cupids_bow",
        "confidence": 0.95,
        "source_keywords": ["full natural cherry lips", "soft glossy tone", "elegant cupid's bow"]
      },
      "nose_type": {
        "classification": "straight_classical_refined",
        "confidence": 0.98,
        "source_keywords": ["straight refined nose bridge", "perfect classical proportions", "subtle highlights", "small delicate tip"]
      },
      "skin_texture": {
        "classification": "porcelain_flawless_radiant",
        "confidence": 0.95,
        "source_keywords": ["flawless porcelain skin", "radiant jade-like", "natural subtle blush", "dewy luminous glow"],
        "special_effects": ["wet skin with water droplets"]
      },
      "expression": {
        "classification": "innocent_gentle_gaze",
        "confidence": 0.90,
        "source_keywords": ["innocent gaze", "gentle smile", "bright smile", "soft introspective"],
        "emotional_tone": "柔和迷人，结合古典温柔与微妙的诱惑魅力"
      }
    }
  }
}
```

---

**五官库引用系统**:

提取后的五官分类会自动关联到 `facial_features_library.json`，支持：

1. **快速查询**: "哪些Prompt使用了杏仁眼？" → [#5]
2. **风格映射**: "清纯少女风格推荐什么五官组合？" → 大眼杏仁眼 + 粉嫩唇 + 小巧鼻 + 瓷肌
3. **模块复用**: 直接引用分类代码生成完整描述
   ```
   {{eye_type: large_expressive_almond}}
   → 展开为: "高度细节化，大而富有表现力，浓密修长的自然睫毛，深邃清晰的虹膜..."
   ```
4. **推荐系统集成**: 基于五官相似度推荐（"喜欢#5的眼型？推荐#10"）

---

**AI生成挑战标注**:

对于五官细节，自动识别并标注生成难点：
```json
"ai_generation_challenges": [
  "眼睛细节（睫毛、虹膜、高光）需高分辨率",
  "皮肤质感（毛孔vs光滑）的平衡控制",
  "水滴物理效果的真实性",
  "表情的自然度（避免僵硬或过度夸张）"
]
```

---

### 4. 批量处理策略

**小规模（<100条）：**
- 逐条精细提取，输出完整JSON数组

**中规模（100-500条）：**
- 每50条一批次处理
- 每批次后生成中间结果文件
- 汇总时合并并去重模块

**大规模（>500条）：**
- 先聚类分5-10组
- 每组并行提取（如果条件允许）
- 最终汇总生成模块库

### 5. 输出成果

生成以下文件：

#### 核心数据文件

1. **extracted_modules.json** - 完整提取结果（机器可读）
2. **module_library.json** - 去重后的通用模块库
   ```json
   {
     "visual_styles": ["电影级", "赛博朋克", ...],
     "technical_params": {
       "camera_angles": ["微距", "鸟瞰", ...],
       "lighting": ["柔光", "逆光", ...]
     },
     "detail_enhancers": ["超高清", "细节丰富", ...],
     "templates": [
       {
         "name": "人像摄影模板",
         "structure": "{主体}, {风格}, {技术参数}, {细节增强}",
         "example": "一位女性, 电影级肖像, 85mm镜头柔光, 超高清细节"
       }
     ]
   }
   ```

#### 学习增强文件（NEW! 🎓）

3. **analysis_report.md** - 完整分析报告，包含以下学习增强部分：

   **A. 学习卡片集** (Learning Cards)
   - 自动生成可打印/复习的技巧卡片
   - 每个高价值模板（reusability > 8）生成一张卡片
   - 卡片包含：技巧名称、复用性评分、结构模板、应用示例、练习题

   示例：
   ```markdown
   ## 🎴 学习卡片集

   ### 卡片 #1: Cold-Warm Color Opposition (冷暖色彩对立)

   **复用性**: 10/10 ⭐⭐⭐⭐⭐
   **难度**: 中级
   **应用场景**: 人像摄影、产品摄影、概念艺术

   **结构模板**:
   ```
   {subject}, Color Palette: {body zone} = {cool colors},
   {focal object} = {warm colors},
   Lighting from {focal object} illuminating {subject}
   ```

   **应用示例**:
   - 原提示词: "Entity, Body=cyan/teal, Cube=pink/amber"
   - 你的应用: "Crystal sorceress, Body=ice blue, Orb=ruby red"

   **💡 学习要点**:
   - 冷色环境 → 营造距离感、神秘感
   - 暖色焦点 → 吸引注意力、制造对比
   - 光源来自焦点 → 增强戏剧性

   **✏️ 练习题**:
   试着用这个技巧创作一个"冰雪女王"主题的提示词
   ```

   **B. 快速参考卡** (Quick Reference Cards)
   - 根据提示词类型生成速查表
   - 包含常用参数配置、技术设置

   示例：
   ```markdown
   ## 📋 快速参考卡

   ### 微距摄影参数速查表

   | 参数类型 | 推荐配置 | 效果说明 |
   |---------|---------|---------|
   | 镜头 | 105mm Macro | 标准微距，适合产品/花卉 |
   |      | 60mm Macro | 中距，适合昆虫/珠宝 |
   |      | 180mm Macro | 远距，适合野生动物 |
   | 光圈 | f/1.8 | 极浅景深，梦幻虚化 |
   |      | f/4-f/5.6 | 平衡，主体清晰 |
   |      | f/11-f/16 | 深景深，全面清晰 |
   | 必备光学 | SSS | 半透明材质 |
   |         | Caustics | 水/玻璃折射 |
   |         | Bokeh | 背景虚化美化 |
   ```

   **C. 注释式学习版本** (Annotated Learning Version)
   - 在原始提示词上添加学习注释
   - 解释每个关键词的作用和原理

   示例：
   ```markdown
   ## 📖 注释式学习版本

   ```
   An ethereal deity composed of intricate white translucent optical fibers
   │            │              │                   │
   │            │              │                   └─ 材质参考词 (增加真实感)
   │            │              └───────────────────── 材质核心描述 (触发SSS)
   │            └──────────────────────────────────── 复杂性强调 (增加细节密度)
   └───────────────────────────────────────────────── 主体定义

   💡 学习要点：
   - "intricate" 触发 AI 增加细节密度
   - "translucent" 触发次表面散射效果
   - 使用多个材质参考 → 创造混合质感
   ```
   ```

   **D. 技能树与进度追踪** (Skill Tree & Progress)
   - 自动识别提示词中使用的技巧
   - 生成技能树可视化
   - 追踪学习进度

   示例：
   ```markdown
   ## 🌳 提示词技能树

   ### 当前提示词使用的技能

   ```
                       提示词技能
                           │
           ┌───────────────┼───────────────┐
           │               │               │
       结构组织          技术参数          创意策略
           │               │               │
      ✅ 7层结构       ✅ 相机设置      ✅ 色彩对立
      ✅ 3层景深       ✅ 渲染引擎      ✅ 剧情光源
                      ⏸️ 后期处理       ⏸️ 材质混合
   ```

   **已识别技能**: 6/10
   **技能等级**: 中级提示词工程师
   **下一个学习目标**: 后期处理技巧
   ```

   **E. 对比学习表格** (仅当分析多个提示词时生成)
   - 横向对比多个提示词的参数差异
   - 帮助理解风格变化的关键因素

   示例：
   ```markdown
   ## 📊 风格对比分析表

   | 参数维度 | 提示词A (清纯风) | 提示词B (赛博朋克) | 提示词C (史诗风) |
   |---------|----------------|------------------|----------------|
   | 主色调 | 粉/白/桃 | 霓虹粉/蓝/紫 | 金/棕/深蓝 |
   | 饱和度 | 低 (30%) | 高 (90%) | 中 (60%) |
   | 光线类型 | 柔和漫射 | 硬边霓虹 | 戏剧侧光 |
   | 情绪词 | innocent | edgy | epic |
   | 光圈 | f/1.4 柔焦 | f/4 锐利 | f/2.8 平衡 |
   | 适用场景 | 日系人像 | 科幻角色 | 英雄肖像 |

   💡 关键发现：
   - 色彩饱和度直接影响风格基调
   - 光线硬度 = 情绪强度
   - 光圈选择要匹配风格需求
   ```

4. **learning_cards.json** - 学习卡片的结构化数据（可导入到Anki等记忆工具）

### 6. 质量保障

- 每个模块附带复用性评分（1-10）
- 标记高价值模块（评分>8）
- 提供改进建议

## 使用示例

**场景1：处理单个文件**
```
用户：使用 prompt-extractor 分析 my_prompts.txt
系统：自动执行完整流程，生成3个输出文件
```

**场景2：指定主题**
```
用户：从 image_prompts.csv 中只提取"人像摄影"相关的模块
系统：先聚类识别"人像"主题，针对性提取
```

**场景3：增量更新**
```
用户：将 new_prompts.json 合并到现有模块库
系统：读取现有库，去重后追加新模块
```

## 技术细节

**数据清洗规则：**
- 去除长度<10字符的提示
- 统一标点符号（英文逗号分隔）
- 移除重复连续空格

**聚类算法（简化版）：**
- 基于关键词TF-IDF向量化
- 使用余弦相似度分组
- 阈值：相似度>0.6归为同一簇

**评分标准：**
- **清晰度(Clarity)**：结构完整、无歧义
- **细节丰富度(Detail Richness)**：参数详细、描述具体
- **复用性(Reusability)**：模块独立性、通用性

## 交互引导

执行时向用户确认：
1. 文件路径是否正确？
2. 是否需要过滤特定主题？
3. 输出文件保存位置？（默认：./extracted_results/）

## 错误处理

- 文件格式无法识别 → 提示用户指定格式
- 提示词质量过低（平均<5分）→ 建议优化数据源
- 批次处理中断 → 保存中间结果，支持断点续传

---

## 🎓 学习增强模式执行指南

### 何时生成学习增强内容？

**默认行为**: 分析提示词时**自动生成**以下学习内容：
- ✅ 学习卡片集 (针对 reusability > 8 的模板)
- ✅ 快速参考卡 (根据提示词类型自动生成)
- ✅ 注释式学习版本 (原始提示词 + 注释)
- ✅ 技能树 (识别使用的技巧)

**可选**: 对比学习表格 (需要2个以上提示词)

### 执行步骤

当用户输入提示词后，按以下顺序生成：

1. **标准分析** (JSON + Markdown报告)
2. **学习卡片集** (在报告末尾添加)
   - 遍历 `high_value_modules`
   - 为每个 reusability ≥ 8 的模板生成卡片
   - 包含：模板、示例、学习要点、练习题

3. **快速参考卡** (根据流派生成)
   - 如果是 `3d_render` → 生成"渲染参数速查表"
   - 如果是 `editorial_macro` → 生成"微距摄影速查表"
   - 如果是 `portrait_beauty` → 生成"人像光线速查表"

4. **注释式学习版本**
   - 将原始提示词拆分成关键短语
   - 为每个短语添加学习注释
   - 解释其作用和原理

5. **技能树**
   - 识别使用的技巧类别
   - 生成可视化技能树
   - 显示掌握程度

6. **对比表格** (如果有多个提示词)
   - 横向对比关键参数
   - 标注差异和共同点

### 输出示例

执行后会在 `extracted_results/` 目录生成：

```
extracted_results/
├── ethereal_deity_extracted.json          (数据)
├── ethereal_deity_analysis_report.md      (完整报告，包含学习内容)
├── ethereal_deity_learning_cards.json     (卡片数据，可导入Anki)
└── module_library.json                    (模板库)
```

**analysis_report.md 的结构**:
```markdown
# 提示词结构分析报告
## [提示词主题]

[标准分析内容...]

---

## 🎓 学习增强部分

### 🎴 学习卡片集
[卡片1: 技巧A]
[卡片2: 技巧B]
...

### 📋 快速参考卡
[速查表]

### 📖 注释式学习版本
[带注释的原文]

### 🌳 提示词技能树
[技能树可视化]

### 📊 对比分析表 (如有)
[对比表格]
```

---

**开始执行时，首先询问用户：**
"请选择输入方式：
1. 提供文件路径（支持 .txt, .csv, .json）
2. 直接粘贴提示词（每行一个，或用换行分隔）

请回复数字或直接提供内容："

**然后**，在分析完成后，自动生成学习增强内容并添加到报告中。
