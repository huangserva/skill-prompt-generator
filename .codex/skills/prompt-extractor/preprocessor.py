#!/usr/bin/env python3
"""
提示词预处理和聚类脚本
支持 txt, csv, json 格式的自动解析和清洗
"""

import json
import csv
import re
from pathlib import Path
from typing import List, Dict, Any
from collections import Counter


class PromptPreprocessor:
    """提示词预处理器"""

    def __init__(self, min_length: int = 10):
        self.min_length = min_length
        self.prompts = []
        self.metadata = {}

    def load_file(self, file_path: str) -> List[str]:
        """自动识别格式并加载文件"""
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"文件不存在: {file_path}")

        suffix = path.suffix.lower()

        if suffix == '.txt':
            return self._load_txt(path)
        elif suffix == '.csv':
            return self._load_csv(path)
        elif suffix == '.json':
            return self._load_json(path)
        else:
            raise ValueError(f"不支持的文件格式: {suffix}. 支持 .txt, .csv, .json")

    def _load_txt(self, path: Path) -> List[str]:
        """加载txt文件（每行一个提示词）"""
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        prompts = [line.strip() for line in lines if line.strip()]
        self.metadata['format'] = 'txt'
        self.metadata['original_count'] = len(prompts)
        return prompts

    def _load_csv(self, path: Path) -> List[str]:
        """加载csv文件（自动识别提示词列）"""
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        if not rows:
            return []

        # 智能识别提示词列（包含 prompt, text, description 等关键词）
        headers = list(rows[0].keys())
        prompt_col = None

        for keyword in ['prompt', 'text', 'description', 'content']:
            for header in headers:
                if keyword in header.lower():
                    prompt_col = header
                    break
            if prompt_col:
                break

        # 如果没找到，使用第一列
        if not prompt_col:
            prompt_col = headers[0]

        prompts = [row[prompt_col].strip() for row in rows if row.get(prompt_col, '').strip()]

        self.metadata['format'] = 'csv'
        self.metadata['prompt_column'] = prompt_col
        self.metadata['original_count'] = len(prompts)

        return prompts

    def _load_json(self, path: Path) -> List[str]:
        """加载json文件（支持数组或对象数组）"""
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, list):
            # 如果是字符串数组
            if all(isinstance(item, str) for item in data):
                prompts = data
            # 如果是对象数组，尝试找到提示词字段
            else:
                prompt_key = None
                for key in ['prompt', 'text', 'description', 'content']:
                    if data and key in data[0]:
                        prompt_key = key
                        break

                if not prompt_key:
                    prompt_key = list(data[0].keys())[0] if data else None

                prompts = [item[prompt_key] for item in data if prompt_key in item]
                self.metadata['prompt_key'] = prompt_key
        else:
            raise ValueError("JSON格式错误：需要数组或对象数组")

        self.metadata['format'] = 'json'
        self.metadata['original_count'] = len(prompts)

        return prompts

    def clean_prompts(self, prompts: List[str]) -> List[str]:
        """清洗提示词"""
        cleaned = []

        for prompt in prompts:
            # 去除多余空格
            prompt = re.sub(r'\s+', ' ', prompt.strip())

            # 统一标点（全角转半角）
            prompt = prompt.replace('，', ', ').replace('。', '. ')

            # 过滤短提示
            if len(prompt) >= self.min_length:
                cleaned.append(prompt)

        # 去重（保持顺序）
        seen = set()
        unique = []
        for p in cleaned:
            if p not in seen:
                seen.add(p)
                unique.append(p)

        self.metadata['after_cleaning'] = len(unique)
        self.metadata['duplicates_removed'] = len(cleaned) - len(unique)

        return unique

    def extract_keywords(self, prompts: List[str], top_n: int = 50) -> List[tuple]:
        """提取高频关键词（用于聚类）"""
        # 简单的关键词提取（基于词频）
        all_words = []

        # 停用词（需要扩展）
        stopwords = {'a', 'an', 'the', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}

        for prompt in prompts:
            # 分词（简化版，按逗号和空格）
            words = re.split(r'[,\s]+', prompt.lower())
            words = [w.strip('.,!?;:()[]{}') for w in words]
            words = [w for w in words if w and w not in stopwords and len(w) > 2]
            all_words.extend(words)

        # 统计词频
        word_counts = Counter(all_words)

        return word_counts.most_common(top_n)

    def simple_cluster(self, prompts: List[str], n_clusters: int = 5) -> Dict[str, List[str]]:
        """简单聚类（基于关键词共现）"""
        # 提取关键词
        keywords = self.extract_keywords(prompts, top_n=30)
        top_keywords = [kw[0] for kw in keywords[:n_clusters * 2]]

        # 为每个关键词创建簇
        clusters = {f"cluster_{i}": [] for i in range(n_clusters)}
        cluster_keywords = {}

        # 选择最具代表性的关键词
        for i in range(min(n_clusters, len(top_keywords))):
            cluster_keywords[f"cluster_{i}"] = top_keywords[i]

        # 分配提示词到簇
        unassigned = []

        for prompt in prompts:
            assigned = False
            prompt_lower = prompt.lower()

            # 检查是否包含簇关键词
            for cluster_id, keyword in cluster_keywords.items():
                if keyword in prompt_lower:
                    clusters[cluster_id].append(prompt)
                    assigned = True
                    break

            if not assigned:
                unassigned.append(prompt)

        # 未分配的放入最后一个簇或新簇
        if unassigned:
            clusters["cluster_other"] = unassigned

        # 移除空簇
        clusters = {k: v for k, v in clusters.items() if v}

        return clusters

    def generate_stats(self, prompts: List[str]) -> Dict[str, Any]:
        """生成统计信息"""
        lengths = [len(p) for p in prompts]

        return {
            "total_prompts": len(prompts),
            "avg_length": sum(lengths) / len(lengths) if lengths else 0,
            "min_length": min(lengths) if lengths else 0,
            "max_length": max(lengths) if lengths else 0,
            "top_keywords": self.extract_keywords(prompts, top_n=20)
        }


def main():
    """命令行接口"""
    import sys

    if len(sys.argv) < 2:
        print("用法: python preprocessor.py <文件路径> [输出文件]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "preprocessed_prompts.json"

    preprocessor = PromptPreprocessor()

    # 加载和清洗
    print(f"正在加载: {input_file}")
    prompts = preprocessor.load_file(input_file)
    print(f"原始数量: {len(prompts)}")

    prompts = preprocessor.clean_prompts(prompts)
    print(f"清洗后: {len(prompts)}")

    # 聚类
    clusters = preprocessor.simple_cluster(prompts, n_clusters=5)
    print(f"\n聚类结果:")
    for cluster_id, cluster_prompts in clusters.items():
        print(f"  {cluster_id}: {len(cluster_prompts)} 条")

    # 生成统计
    stats = preprocessor.generate_stats(prompts)

    # 保存结果
    result = {
        "metadata": preprocessor.metadata,
        "statistics": stats,
        "clusters": {k: v[:10] for k, v in clusters.items()},  # 每簇只保存前10个示例
        "all_prompts": prompts
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"\n结果已保存到: {output_file}")


if __name__ == "__main__":
    main()
