#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Xray Helper - 简单的数据读取和保存工具
仅负责文件IO，不做任何分析决策
"""

import json
from pathlib import Path
from typing import List, Dict
from datetime import datetime


def load_prompts(pattern: str = "*_extracted.json",
                 base_dir: str = "extracted_results") -> List[Dict]:
    """
    读取已分析的提示词JSON文件

    Args:
        pattern: 文件名模式（如：moss_terrarium*）
        base_dir: JSON文件所在目录

    Returns:
        List of prompt data
    """
    base_path = Path(base_dir)
    prompts = []

    if not base_path.exists():
        print(f"❌ 目录不存在: {base_path}")
        return []

    for json_file in base_path.glob(pattern):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

                # 处理单个提示词或提示词数组
                if isinstance(data, list):
                    prompts.extend(data)
                else:
                    prompts.append(data)

                print(f"✅ 已加载: {json_file.name}")
        except Exception as e:
            print(f"❌ 加载失败 {json_file.name}: {e}")

    print(f"\n📊 总计加载: {len(prompts)} 个提示词")
    return prompts


def save_knowledge_card(dimension: str,
                       content: str,
                       metadata: Dict = None,
                       output_dir: str = "knowledge_base") -> str:
    """
    保存知识卡片到Markdown文件

    Args:
        dimension: 维度名称（color/layout/symbols等）
        content: Markdown内容
        metadata: 可选的元数据
        output_dir: 输出目录

    Returns:
        保存的文件路径
    """
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    # 生成文件名
    filename = f"how_to_control_{dimension}.md"
    filepath = output_path / filename

    # 保存文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"💾 已保存: {filepath}")

    # 如果有元数据，也保存JSON版本
    if metadata:
        json_filename = f"how_to_control_{dimension}.json"
        json_filepath = output_path / json_filename

        output_data = {
            'dimension': dimension,
            'creation_time': datetime.now().isoformat(),
            'metadata': metadata,
            'markdown_content': content
        }

        with open(json_filepath, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        print(f"💾 已保存元数据: {json_filepath}")

    return str(filepath)


def list_available_prompts(base_dir: str = "extracted_results") -> List[str]:
    """
    列出所有可用的提示词文件

    Args:
        base_dir: JSON文件所在目录

    Returns:
        文件名列表
    """
    base_path = Path(base_dir)

    if not base_path.exists():
        print(f"❌ 目录不存在: {base_path}")
        return []

    files = sorted([f.name for f in base_path.glob("*_extracted.json")])

    print(f"\n📁 可用的提示词文件 ({len(files)}个):")
    for f in files:
        print(f"  - {f}")

    return files


if __name__ == '__main__':
    """测试函数"""
    print("=" * 60)
    print("  🔬 Xray Helper - 工具测试")
    print("=" * 60)

    # 测试：列出可用文件
    list_available_prompts()

    # 测试：加载提示词
    print("\n" + "=" * 60)
    prompts = load_prompts()

    if prompts:
        print(f"\n📋 第一个提示词示例:")
        print(f"  ID: {prompts[0].get('prompt_id', 'unknown')}")
        print(f"  主题: {prompts[0].get('theme', 'unknown')}")

    # 测试：保存知识卡片
    print("\n" + "=" * 60)
    test_content = """# 测试知识卡片

这是一个测试。
"""

    save_knowledge_card(
        dimension="test",
        content=test_content,
        metadata={'test': True, 'samples': 2}
    )

    print("\n" + "=" * 60)
    print("✅ 测试完成！")
