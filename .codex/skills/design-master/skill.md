---
name: design-master
description: 平面设计主控 - 自动生成平面设计提示词，支持海报、logo、插画等多种设计类型
---

# Design Master - 平面设计主控 Skill

**版本**: 1.0
**领域**: 平面设计
**架构**: Master-Subordinate
**数据源**: Universal Elements Database

## 🎯 核心功能

自动生成高质量的平面设计提示词，支持：
- 🎨 布局系统（Bento Grid、对分屏、网格拼贴等）
- ✨ 视觉效果（Glassmorphism、渐变、3D等）
- 🎭 设计风格（现代极简、复古、科技等）
- 🌈 色彩方案（配色规则、色调控制）
- 📐 构图技巧（对称、黄金比例、视觉层次）

---

## 📋 使用方式

### 方式1：元素级生成（灵活组合）

```
生成一个Bento Grid布局海报
```

或

```
平面设计：现代极简风格，玻璃态效果
```

**原理**：从80个design元素中智能选择并组合

---

### 方式2：模板级生成（完整系统）⭐ 新增

```
生成Apple风格PPT模板
```

或

```
使用现代商务科技典雅风格PPT模板
```

**关键词**：包含"模板"一词触发模板查询

**原理**：从design_templates表查询完整设计系统

**返回内容**：
- 设计理念说明
- 完整元素列表（12个元素，按结构组织）
- 使用场景和指南
- 组装好的完整提示词

---

## 🔄 工作流程

### 元素级流程（默认）

```
用户输入（不含"模板"关键词）
  ↓
查询design领域元素 (80 elements)
  - layout_systems: Bento网格、对分屏等
  - visual_effects: 玻璃态、渐变等
  - color_schemes: 配色方案
  - typography: 字体系统
  - backgrounds: 背景系统
  ↓
智能选择元素
  - 根据用户需求匹配
  - 语义相关性排序
  ↓
组装Prompt
  1. 布局系统
  2. 视觉效果
  3. 色彩方案
  4. 技术参数（4K、DPI）
  ↓
输出完整设计Prompt
```

### 模板级流程（包含"模板"关键词）⭐ 新增

```
用户输入（包含"模板"）
  ↓
检测关键词："模板" | "template"
  ↓
查询design_templates表
  - 匹配name、chinese_name、style_tags
  - 示例：Apple → "Apple淡蓝商务PPT"
  ↓
返回完整模板
  - 设计理念
  - 12个元素（按结构组织）
  - 使用场景
  - 完整提示词
  ↓
输出模板详情 + 提示词
```

---

## 📊 数据源

### 元素库（elements表）

**领域**: `design` domain (80 elements)

**元素类别**:
- `layout_systems` - 布局系统
- `visual_effects` - 视觉效果
- `color_schemes` - 配色方案
- `typography` - 字体系统
- `backgrounds` - 背景系统

**可用标签**:
- `bento-grid`, `glassmorphism`, `modern`
- `minimalist`, `grid`, `layout`, `apple`

### 模板库（design_templates表）⭐ 新增

**当前模板数**: 1个

**已有模板**:
1. **Apple淡蓝商务PPT** (template_apple_soft_blue_ppt_v1)
   - 类别: ppt_design
   - 包含: 12个元素
   - 标签: apple, business, soft_blue, minimal, professional
   - 适用: 商务汇报、产品发布会、数据分析

**模板分类**:
- `ppt_design` - PPT演示设计
- `ui_system` - UI设计系统
- `brand_vi` - 品牌视觉识别
- `web_design` - 网页设计系统
- `dashboard` - 仪表板设计

---

## ✅ 输出示例

### 示例1：元素级生成

**输入**: `生成Bento Grid玻璃态海报`

**输出**:
```
Modern Bento grid layout with 8 asymmetric modular cards, frosted glass effect
with 80% translucency and backdrop blur filter, minimalist modern aesthetics,
90% neutral colors with 10% vibrant accent colors, clean typography, 4K
resolution, professional graphic design, UI/UX design system, contemporary
digital poster design
```

### 示例2：模板级生成 ⭐ 新增

**输入**: `生成Apple风格PPT模板`

**输出**:
```
📋 找到匹配模板：现代商务科技典雅风格PPT - 淡蓝装饰版

🎯 设计理念：
极简主义美学融合温和的科技感。在Apple设计语言基础上，
加入淡雅的蓝色调和细腻的装饰纹理，营造既专业又不失温度
的商务氛围。

📦 完整模板包含（12个元素）：

【背景系统】
• Apple风格淡蓝渐变背景
• 四层装饰背景系统

【布局系统】
• Apple风格玻璃卡片系统
• 12列8点网格系统

【配色系统】
• Apple商务蓝配色系统

【字体系统】
• Apple字体层级系统

【视觉效果】
• macOS窗口三色圆点
• SF Symbols超细线性图标
• Apple风格柔和蓝数据图表
• 淡蓝标签组件
• Apple圆角层级系统
• 蓝色调投影系统

🎨 使用场景：
高端商务汇报、产品发布会、数据分析报告

✨ 完整模板提示词：
────────────────────────────────────────
[包含全部12个元素的完整提示词]
────────────────────────────────────────
```

---

**Skill状态**: ✅ 已实现（v1.1 - 支持模板系统）
