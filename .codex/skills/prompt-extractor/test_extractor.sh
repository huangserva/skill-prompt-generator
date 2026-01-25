#!/bin/bash
# 快速测试脚本

echo "===== Prompt Extractor 测试 ====="
echo ""

# 检查Python
if ! command -v python3 &> /dev/null; then
    echo "错误: 需要安装 Python 3"
    exit 1
fi

# 测试预处理器
echo "1. 测试预处理器..."
python3 preprocessor.py example_prompts.txt test_output.json

if [ -f test_output.json ]; then
    echo "✓ 预处理成功"
    echo ""
    echo "2. 查看统计信息..."
    python3 -c "
import json
with open('test_output.json', 'r') as f:
    data = json.load(f)
    print(f\"  原始数量: {data['metadata']['original_count']}\")
    print(f\"  清洗后: {data['metadata']['after_cleaning']}\")
    print(f\"  平均长度: {data['statistics']['avg_length']:.1f} 字符\")
    print(f\"  聚类数量: {len(data['clusters'])}\")
    print(f\"\\n  Top 10 关键词:\")
    for kw, count in data['statistics']['top_keywords'][:10]:
        print(f\"    - {kw}: {count}次\")
"
else
    echo "✗ 预处理失败"
    exit 1
fi

echo ""
echo "===== 测试完成 ====="
echo "下一步: 在 Claude Code 中运行 'prompt-extractor' skill"
