# ⚠️ 旧架构 - Analyzer Module - 分析查询模块

> **注意**：这是旧架构模块，属于prompt-master系统


**功能**: 分析、查询、对比提示词和模块信息
**调用方式**: 通过主Skill路由或直接CLI调用

---

## 📋 功能概述

Analyzer模块提供以下分析功能：
- 查看Prompt详细信息
- 对比两个Prompts的差异
- 查询五官模块信息
- 查询流派和设备信息

---

## 🔧 CLI命令

### 1. 查看Prompt详细信息

**命令**:
```bash
python3 prompt_tool.py show <id>
```

**示例**:
```bash
python3 prompt_tool.py show 5
```

**输出**:
```
📸 Prompt #5: 清纯少女古典美

基本信息:
  主题: 清纯少女 / 古典优雅 / 自然光人像
  长度: 892 字符
  评分: 10.0/10

摄影流派:
  人像美容摄影 (置信度: 95%)

技术参数:
  相机: Canon EOS R5
  镜头: RF 50mm f/1.2L
  分辨率: 8K

对立标准:
  aesthetic:
    ✓ 必须: flawless porcelain skin, soft classical contour
    ✗ 禁止: modern edgy makeup, harsh contours
```

### 2. 对比两个Prompts

**命令**:
```bash
python3 prompt_tool.py compare <id1> <id2>
```

**示例**:
```bash
python3 prompt_tool.py compare 5 17
```

**输出**:
```
⚖️  对比: #5 vs #17

属性         Prompt #5                  Prompt #17
=======================================================
标题         清纯少女古典美             性感朋克Jinx
评分         10.0/10                    9.8/10
流派         人像美容摄影               胶片艺术摄影
相机         Canon EOS R5               Hasselblad 503CX
分辨率       8K                         medium format
```

### 3. 查询五官类型列表

**命令**:
```bash
python3 prompt_tool.py facial --list-types
```

**输出**:
```
📊 五官特征分类库

眼型 (4种):
  large_expressive_almond    大眼杏仁眼      (9.8/10) Prompts: [5]
  large_blue_expressive      大蓝眼（真人化）(8.5/10) Prompts: [18]
  half_lidded_seductive      半闭诱惑眼      (8.0/10) Prompts: [17]
  anime_hybrid_green         动漫混合绿眼    (8.5/10) Prompts: [11]

脸型 (2种):
  oval_asian_refined         精致鹅蛋脸（亚洲）(10.0/10) Prompts: [17, 18]
  classical_soft_contour     柔和古典脸型      (9.5/10)  Prompts: [5]

... (其他类别)
```

### 4. 查询特定五官类型

**命令**:
```bash
python3 prompt_tool.py facial --eye-type <类型>
python3 prompt_tool.py facial --skin-texture <类型>
python3 prompt_tool.py facial --expression <类型>
```

**示例**:
```bash
python3 prompt_tool.py facial --eye-type almond
```

**输出**:
```
🔍 五官特征: 大眼杏仁眼

视觉特征:
  • size: 大而富有表现力 (large and expressive)
  • shape: 杏仁形 (almond-shaped)
  • eyelashes: 浓密修长的自然睫毛 (thick long natural lashes)

提示词关键词:
  • large expressive eyes
  • almond eyes
  • thick natural lashes
  • deep clear iris
  • dewy sparkle

适合风格:
  • 清纯少女
  • 邻家小妹
  • 古典温柔
  • 现代商业人像

使用该特征的Prompts (1个):
  #5   清纯少女古典美                      10.0/10

使用建议:
  • best_for: 万能眼型，适合清纯、优雅、古典风格
  • pair_with: 搭配 'innocent', 'gentle', 'youthful' 强化纯净感
  • lighting: 黄金时刻柔和光 (golden hour soft light) 最佳
```

### 5. 按风格推荐五官组合

**命令**:
```bash
python3 prompt_tool.py facial --style <风格>
```

**示例**:
```bash
python3 prompt_tool.py facial --style "清纯少女"
```

**输出**:
```
🎨 风格: 清纯少女

推荐五官组合:

性别: 女性 (female)
年龄: 青年（18-25岁） (young_adult) [10.0/10]
人种: 东亚人 (east_asian) [10.0/10]
  关键词: East Asian, Asian features

眼型: 大眼杏仁眼 (large_expressive_almond) [9.8/10]
  关键词: large expressive eyes, almond eyes, thick natural lashes

唇型: 粉嫩光泽唇 (soft_pink_gloss) [9.0/10]
  关键词: soft full lips, gentle pink gloss, natural lip color

鼻型: 小巧直鼻 (small_straight_delicate) [9.0/10]
  关键词: small straight nose, delicate nose

皮肤: 瓷肌无瑕（发光质感） (porcelain_flawless_radiant) [9.5/10]
  关键词: flawless porcelain skin, radiant jade-like brightness

表情: 清纯温柔眼神 (innocent_gentle_gaze) [9.5/10]
  关键词: innocent gaze, gentle smile, soft introspective
```

### 6. 按流派搜索

**命令**:
```bash
python3 prompt_tool.py search --genre <流派>
```

**示例**:
```bash
python3 prompt_tool.py search --genre cinematic_narrative
```

**输出**:
```
🔍 流派: 电影叙事摄影

流派特征:
  • 8K HDR超高清数码摄影
  • 电影级实景拍摄
  • 自然叙事性光照
  • 真人化角色演绎

典型设备:
  • Canon EOS R5
  • RF 35mm f/2.8 macro IS STM

应用场景:
  • 真人化角色摄影
  • 电影级概念艺术
  • 游戏IP真人化

相关提示词 (2个):
  #18  Princess Peach真人化                    9.8/10
  #11  Saber真人化                             9.5/10
```

### 7. 按设备搜索

**命令**:
```bash
python3 prompt_tool.py search --equipment <设备>
```

**示例**:
```bash
python3 prompt_tool.py search --equipment R5
```

---

## 🎯 使用场景

### 场景1: 学习优秀Prompt

```
用户: "我想学习Prompt #5的细节"
→ 调用: python3 prompt_tool.py show 5
→ 查看完整技术参数、对立标准、独特特征
```

### 场景2: 对比两种风格

```
用户: "清纯和性感风格有什么区别？"
→ 调用: python3 prompt_tool.py compare 5 17
→ 对比表格一目了然
```

### 场景3: 查询五官库

```
用户: "有哪些眼型可选？"
→ 调用: python3 prompt_tool.py facial --list-types
→ 查看所有6大类五官分类
```

### 场景4: 学习风格搭配

```
用户: "古典优雅风格应该用什么五官？"
→ 调用: python3 prompt_tool.py facial --style "古典优雅"
→ 获取完整五官组合推荐
```

---

## 📁 数据依赖

```
facial_features_library.json (v1.2)
├── 9大类别、28个分类
└── usage_index.by_style_mood (4种风格)

module_library.json
├── photography_genres (10流派)
└── camera_equipment_index (设备库)

extracted_modules.json
└── 18个源Prompts的完整数据
```

---

**模块状态**: ✅ 可用
**CLI命令**: `show`, `compare`, `search`, `facial`
**支持查询**: Prompt、流派、设备、五官、风格
