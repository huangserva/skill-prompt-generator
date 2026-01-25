# Prompt Extractor - AI绘画提示词模块化提取工具

## 快速开始

### 1. 激活Skill

在Claude Code中调用：
```
/skill prompt-extractor
```

或者直接说：
```
使用 prompt-extractor 分析我的提示词
```

### 2. 输入方式（二选一）

**方式A：文件路径**（适合大批量）

支持三种格式：

**TXT格式** (每行一个提示词)
```
a portrait of a woman, cinematic lighting, 85mm lens, ultra detailed
cyberpunk city at night, neon lights, rain, photorealistic
```

**CSV格式**
```csv
id,prompt,score
1,"a portrait of a woman, cinematic lighting",8.5
2,"cyberpunk city at night, neon lights",9.2
```

**JSON格式**
```json
[
  {"prompt": "a portrait of a woman, cinematic lighting, 85mm lens"},
  {"prompt": "cyberpunk city at night, neon lights, rain"}
]
```

**方式B：直接粘贴**（适合快速分析，推荐！✨）

```
我：帮我分析这些提示词：

a portrait of a woman, cinematic lighting, 85mm lens, ultra detailed
cyberpunk city at night, neon lights, rain, photorealistic
beautiful landscape, golden hour, dramatic clouds, HDR
```

**无需创建文件，直接粘贴即可！**

详见：[粘贴模式完整指南](PASTE_MODE_GUIDE.md)

### 3. 自动处理

Skill会自动：
1. 识别文件格式
2. 清洗和去重
3. 聚类分析（如果>100条）
4. 逐条提取模块
5. 生成模块库和分析报告

## 输出文件说明

### extracted_modules.json
完整的提取结果，每条提示词对应一个JSON对象：

```json
{
  "original_prompt": "a portrait of a young woman, cinematic lighting, 85mm lens f/1.4, ultra detailed, photorealistic",
  "theme": "人像摄影",
  "modules": {
    "subject_variables": {
      "main": "young woman",
      "modifiers": ["portrait"],
      "is_replaceable": true
    },
    "visual_style": {
      "art_style": "photorealistic",
      "reference_artists": [],
      "color_palette": "natural tones"
    },
    "technical_parameters": {
      "camera": "85mm lens f/1.4",
      "lighting": "cinematic lighting",
      "render_engine": null,
      "resolution": "ultra detailed"
    },
    "detail_enhancers": ["ultra detailed", "photorealistic"],
    "mood_atmosphere": "professional, elegant",
    "constraints": {
      "negative_prompt": "",
      "exclusions": []
    }
  },
  "quality_score": {
    "clarity": 9,
    "detail_richness": 8,
    "reusability": 9,
    "comments": "结构清晰，技术参数具体，高度可复用"
  },
  "extracted_patterns": {
    "structure_type": "分层描述：主体 + 技术 + 质量",
    "advantages": ["参数明确", "易于替换主体", "专业摄影标准"],
    "reusable_templates": "{主体}, {光线}, {镜头参数}, {质量增强}"
  }
}
```

### module_library.json
去重后的通用模块库：

```json
{
  "visual_styles": {
    "art_styles": ["photorealistic", "cinematic", "cyberpunk", "anime", "oil painting"],
    "frequency": {"photorealistic": 45, "cinematic": 38}
  },
  "technical_params": {
    "camera_angles": ["85mm lens", "wide angle", "macro", "aerial view"],
    "lighting": ["cinematic lighting", "soft light", "backlight", "golden hour"],
    "render_engines": ["Unreal Engine", "Octane Render", "V-Ray"]
  },
  "detail_enhancers": [
    "ultra detailed", "8k", "hyperrealistic", "intricate details",
    "sharp focus", "professional photography"
  ],
  "templates": [
    {
      "name": "人像摄影模板",
      "structure": "{主体}, {光线}, {镜头}, {质量增强}",
      "example": "a portrait of {subject}, cinematic lighting, 85mm lens, ultra detailed",
      "usage_count": 23,
      "avg_quality_score": 8.7
    },
    {
      "name": "场景构图模板",
      "structure": "{场景}, {氛围}, {视角}, {风格}, {质量}",
      "example": "{location} at {time}, {mood}, {camera_angle}, {art_style}, {detail_enhancers}",
      "usage_count": 18,
      "avg_quality_score": 8.2
    }
  ],
  "high_value_modules": [
    {
      "module": "cinematic lighting, 85mm lens f/1.4",
      "reusability_score": 9.5,
      "category": "technical_parameters",
      "usage_scenarios": ["人像", "产品", "静物"]
    }
  ]
}
```

### analysis_report.md
可读的分析报告：

```markdown
# 提示词分析报告

## 数据概览
- 总数：500条
- 清洗后：487条
- 去重：13条
- 主题分布：
  - 人像摄影：145条 (29.8%)
  - 风景场景：132条 (27.1%)
  - 概念艺术：98条 (20.1%)
  - 其他：112条 (23.0%)

## 高频模块

### 视觉风格 Top 5
1. photorealistic (92次)
2. cinematic (76次)
3. cyberpunk (54次)
4. anime style (43次)
5. oil painting (38次)

### 技术参数 Top 5
1. cinematic lighting (88次)
2. 85mm lens (67次)
3. ultra detailed (156次)
4. 8k (89次)
5. Unreal Engine (45次)

## 推荐组合

### 组合1：专业人像
**模板：** {人物}, cinematic lighting, 85mm lens f/1.4, ultra detailed, photorealistic
**优势：** 技术参数明确，成片率高
**适用场景：** 人像、半身像、特写

### 组合2：赛博朋克城市
**模板：** cyberpunk {场景}, neon lights, rain, night, cinematic, 8k
**优势：** 氛围强烈，视觉冲击力强
**适用场景：** 科幻、城市、未来主义

## 改进建议

1. **增加负面提示**：只有23%的提示词包含负面提示，建议补充
2. **细化技术参数**：67%的提示缺乏具体镜头参数
3. **明确艺术风格**：建议每个提示都指定清晰的风格标签
```

## 使用场景示例

### 场景1：新手学习优秀提示词结构

```
用户：我有一个收藏的500条AI绘画提示词，想学习它们的结构
操作：使用 prompt-extractor 分析 favorites.txt
输出：
  - 发现85%使用"主体+技术+质量"结构
  - 提取10个高复用模板
  - 生成学习手册
```

### 场景2：构建自己的模块库

```
用户：我想从1万条提示词中提炼出我的专属模块库
操作：分批处理，每次2000条
输出：
  - 去重后的5000+独特模块
  - 按主题分类的模板库
  - 可直接复用的JSON文件
```

### 场景3：提升提示词质量

```
用户：我的提示词效果不好，想找到高质量模式
操作：上传失败案例和成功案例两个文件对比
输出：
  - 识别成功案例的共同模式
  - 指出失败案例的缺陷（如缺乏技术参数）
  - 提供改进建议
```

## 高级功能

### 1. 增量更新模块库

```python
# 合并新提示词到现有库
python preprocessor.py new_prompts.txt updated_library.json
```

### 2. 主题过滤

在skill中指定：
```
只提取"人像摄影"主题的模块
```

### 3. 自定义评分标准

修改 skill.md 中的评分权重：
```json
"quality_score": {
  "clarity": {"weight": 0.3, "score": 8},
  "detail_richness": {"weight": 0.3, "score": 9},
  "reusability": {"weight": 0.4, "score": 7}
}
```

## 最佳实践

### 数据准备
1. 先清理明显无效的提示（如乱码、测试文本）
2. 如果有评分，保留高分提示优先处理
3. 按主题分文件更易管理

### 批次处理策略
- **<100条**：一次性处理，精细提取
- **100-500条**：推荐规模，单次skill调用
- **>500条**：分批处理，每批300-500条

### 质量保障
1. 首次处理前，手动标注20-50条作为基准
2. 对比AI提取结果，调整meta-prompt
3. 迭代3-5次达到满意精度

## 故障排除

### 问题1：文件格式识别失败
**原因**：编码问题或格式不标准
**解决**：
```bash
# 转换编码为UTF-8
iconv -f GBK -t UTF-8 input.txt > output.txt
```

### 问题2：提取质量差
**原因**：提示词本身质量低或结构混乱
**解决**：
- 先聚类，只处理主题清晰的簇
- 提高 min_length 阈值过滤短提示
- 人工review前100条，调整提取规则

### 问题3：处理速度慢
**原因**：单次处理量过大
**解决**：
- 减少批次大小（推荐50-100条/批）
- 先聚类后并行处理各簇
- 使用预处理脚本先过滤

## 技术支持

如需帮助，在Claude Code中问：
```
prompt-extractor 如何处理CSV中的多列数据？
prompt-extractor 如何自定义模块分类？
```

## 更新日志

**v1.0** (当前版本)
- 支持 txt/csv/json 三种格式
- 自动聚类和主题识别
- 模块化提取和质量评分
- 生成可复用模板库

**路线图**
- [ ] 支持多语言提示词（中文、日文）
- [ ] 可视化分析dashboard
- [ ] 与Midjourney/SD参数库对接
- [ ] 在线模块搜索引擎
