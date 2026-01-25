---
name: video-master
description: 视频生成主控 - 自动生成视频场景提示词，支持动态效果、转场、运镜等
---

# Video Master - 视频生成主控 Skill

**版本**: 1.0
**领域**: 视频生成
**架构**: Master-Subordinate
**数据源**: Universal Elements Database

## 🎯 核心功能

自动生成高质量的视频场景提示词，支持：
- 🎬 场景类型（武侠、科幻、动作、剧情等）
- 📹 相机运动（推进、拉远、跟踪、环绕等）
- ⚡ 动作效果（慢动作、快速剪辑、特效）
- 🎭 叙事元素（角色、环境、氛围）
- 🌅 光照场景（黄昏、黎明、夜晚、室内）

---

## 📋 使用方式

### 快速生成

```
生成一个武侠动作场景视频
```

或

```
视频场景：电影级质感，慢镜头，动态相机运动
```

---

## 🔄 工作流程

```
用户输入
  ↓
查询video领域元素 (1 element)
  - scene_types: 武侠等
  - camera_movements: 动态运镜（待补充）
  - motion_effects: 慢动作等（待补充）
  ↓
组装Prompt
  1. 场景描述
  2. 相机运动
  3. 动作效果
  4. 技术参数（8K HDR）
  ↓
输出完整视频Prompt
```

---

## 📊 数据源

**主要库**: `video` domain (1 element)

**元素类别**:
- `scene_types` - 场景类型
- `camera_movements` - 相机运动（待补充）
- `motion_effects` - 动态效果（待补充）
- `transitions` - 转场效果（待补充）

**可用标签**:
- `cinematic`, `action`, `dramatic`
- `slow-motion`, `tracking-shot`

---

## ✅ 输出示例

**输入**: `生成武侠动作场景`

**输出**:
```
Cinematic Chinese martial arts action scene, dynamic tracking shot following
warrior through bamboo forest, slow-motion combat sequences with sword fighting,
dramatic lighting with volumetric fog effects, 8K HDR quality, film-grade
cinematography, fluid camera movements, epic atmosphere with traditional
Chinese aesthetics, professional action choreography, movie-quality VFX
```

---

**Skill状态**: ✅ 已实现
**Note**: 视频领域元素较少（1个），建议后续补充更多camera_movements和motion_effects
