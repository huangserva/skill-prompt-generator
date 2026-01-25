---
name: product-master
description: 产品摄影主控 - 自动生成产品摄影提示词，支持商业拍摄、电商图片等场景
---

# Product Master - 产品摄影主控 Skill

**版本**: 1.0
**领域**: 产品摄影
**架构**: Master-Subordinate
**数据源**: Universal Elements Database

## 🎯 核心功能

自动生成高质量的产品摄影提示词，支持：
- 📦 多种产品类型（书籍、电子产品、食品、时尚等）
- 📸 专业摄影技术（Phase One相机、微距、光照设置）
- 🎨 材质纹理（皮革、金属、玻璃、木材等）
- 💡 光照布局（柔光箱、环形光、自然光等）
- 🏆 高端质感（奢华、简约、科技、复古等）

---

## 📋 使用方式

### 方式1：快速生成

```
生成一个高端书籍产品摄影
```

或

```
产品摄影：收藏版游戏周边
```

### 方式2：详细定制

```
生成一个产品摄影：
- 产品：奢华手表
- 风格：极简高端
- 材质：金属+皮革
- 光照：柔和反光
```

### 方式3：参考风格

```
生成类似Prompt #1的产品摄影（收藏版书籍风格）
```

### 方式4：网格拼贴布局（Grid Collage）

**适用场景**：
- 多角度产品展示
- 电商详情页
- 社交媒体内容
- 产品对比展示

**触发关键词**：
- "9宫格"、"3×3布局"、"grid"
- "多角度展示"、"多视角"
- "中间3D突出"、"3D pop-out"
- "4宫格"、"2×2布局"

**示例**：
```
生成9宫格手表产品摄影，中间3D突出
```

**Skill会自动：**
1. 识别这是Grid Collage模式
2. 加载专业框架模板（参考 `modules/layouts/grid_collage.md`）
3. 生成包含以下特性的完整提示词：
   - 严格的网格等分布局（3×3、2×2等）
   - THICK WHITE LINES 清晰分隔
   - 中间格子被3D产品完全遮挡
   - 深景深（f/16）确保所有格子清晰
   - 专业深度效果（投影、层次、饱和度提升）
   - 完整的一致性检查清单

**输出特点**：
- 8个不同角度的产品摄影（背景层）
- 1个超大3D渲染产品（前景层，从顶到底占满画布）
- 遮挡机制：中间格子100%遮挡，周围4格部分遮挡
- 超现实拼贴艺术效果

---

## 🔄 工作流程

```
用户输入
  ↓
【识别需求】
  - 产品类型
  - 风格偏好
  - 材质要求
  ↓
【查询数据库】builder.md
  - 从elements.db搜索product领域元素
  - 按标签筛选（luxury, premium, glass...）
  - 按复用性排序
  ↓
【组装Prompt】
  1. 产品主体描述 (product_types)
  2. 材质纹理 (material_textures)
  3. 摄影技术 (photography_techniques)
  4. 光照设置 (lighting_techniques)
  5. 技术参数 (technical_effects)
  6. 质量增强词
  ↓
【输出完整Prompt】
```

---

## 📊 数据源

**主要库**:
- `product` domain (4 elements)
- `common` domain (31 elements)

**元素类别**:
- `product_types` - 产品类型
- `material_textures` - 材质纹理
- `photography_techniques` - 摄影技术
- `lighting_techniques` - 光照技术
- `technical_effects` - 技术效果

**可用标签**:
- `luxury`, `premium`, `high-end`
- `glossy`, `matte`, `reflective`
- `leather`, `metal`, `glass`, `wood`
- `macro`, `editorial`, `commercial`

---

## 🎨 支持的风格

- **Luxury Editorial** - 奢华编辑风格（杂志级）
- **Minimalist Modern** - 极简现代风格
- **Tech Premium** - 科技高端风格
- **Vintage Classic** - 复古经典风格
- **Artisanal Craft** - 手工艺品风格

---

## ✅ 输出示例

**输入**:
```
生成一个奢华书籍产品摄影
```

**输出**:
```
Premium collector's edition book photographed with Phase One medium format
camera with 100mm macro lens, sophisticated softbox rim lighting creating
elegant highlights on Italian calfskin leather binding, glossy reflective
surface with high-end finish, metallic gold-embossed details, 4K ultra high
resolution, shallow depth of field isolating the subject, editorial magazine
quality photography, razor-sharp macro focus capturing every texture detail,
photorealistic render, professional commercial product shot, luxury brand
aesthetic, pristine studio environment with controlled lighting
```

---

## 🔧 模块说明

| 模块 | 文件 | 功能 |
|------|------|------|
| 主控 | `skill.md` | 意图识别和路由 |
| 组装器 | `modules/core/builder.md` | 查询数据库并组装Prompt |

---

**Skill状态**: ✅ 已实现
**最后更新**: 2026-01-01
**维护者**: Universal Library System
