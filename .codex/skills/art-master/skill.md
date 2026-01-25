---
name: art-master
description: 艺术风格主控 - 自动生成艺术风格提示词，支持水墨画、油画、超现实、插画等多种艺术风格
---

# Art Master - 艺术风格主控 Skill

**版本**: 1.0
**领域**: 艺术风格
**架构**: Master-Subordinate
**数据源**: Universal Elements Database

## 🎯 核心功能

自动生成高质量的艺术风格提示词，支持：
- 🎨 艺术风格（水墨画、油画、超现实、插画等）
- ✨ 特殊效果（玻璃碎片、光影、粒子效果等）
- 🖌️ 绘画技法（笔触、质感、构图等）
- 🌈 色彩运用（冷暖色调、对比、和谐）
- 📜 文化风格（中式、日式、西方古典等）

---

## 📋 使用方式

### 快速生成

```
生成一个中国水墨画风格
```

或

```
艺术风格：超现实主义，梦境氛围
```

---

## 🔄 工作流程

```
用户输入
  ↓
查询art领域元素 (1 element)
  - art_styles: 中国水墨画等
  - special_effects: 玻璃碎片等（需补充）
  ↓
组装Prompt
  1. 艺术风格描述
  2. 特殊效果
  3. 绘画技法
  4. 色彩运用
  ↓
输出完整艺术Prompt
```

---

## 📊 数据源

**主要库**: `art` domain (1 element)

**元素类别**:
- `art_styles` - 艺术风格
- `special_effects` - 特殊效果（待补充）

**可用标签**:
- `chinese-ink`, `painting`, `traditional`
- `surreal`, `dreamlike`, `artistic`

---

## ✅ 输出示例

**输入**: `生成中国水墨画`

**输出**:
```
Traditional Chinese ink painting style, flowing brush strokes with varying
ink density, minimalist composition emphasizing negative space, monochromatic
black ink with subtle grey washes, artistic interpretation of natural subjects,
poetic atmosphere with calligraphic elements, traditional Eastern aesthetics,
masterful brushwork technique, contemplative mood
```

---

**Skill状态**: ✅ 已实现
**Note**: 艺术领域元素较少（1个），建议后续补充更多art_styles和special_effects
