# Prompt Xray - 提示词X光透视系统

**状态**: 🚧 开发中
**版本**: 1.0
**灵感**: BerryXia Multi-Agent Architecture

## 快速开始

```bash
# 从项目根目录运行
python -m claude.skills.prompt_xray.xray_controller
```

## 目录结构

```
prompt-xray/
├── skill.md          # Skill说明文档
├── xray_controller.py  # 主控制器
├── agents/            # 8个分析Agent
│   ├── color_analyzer.py
│   ├── layout_architect.py
│   └── ...
└── utils/             # 工具函数
```

## 已实现功能

- [x] COLOR_ANALYZER - 配色知识提取
- [x] LAYOUT_ARCHITECT - 布局知识提取
- [ ] SYMBOL_EXTRACTOR - 符号添加方法
- [ ] TYPOGRAPHY_ANALYST - 排版知识
- [ ] MATERIAL_ENGINEER - 材质知识
- [ ] LIGHT_PHYSICIST - 光影知识
- [ ] KNOWLEDGE_SYNTHESIZER - 知识聚合
