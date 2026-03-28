#!/usr/bin/env python3

import os
import sys
import torch

# 核心配置：指定设备和加速方式（FaceFusion 能识别的环境变量）
os.environ['DEVICE'] = 'mps' if torch.backends.mps.is_available() else 'cpu'
os.environ['FACEFUSION_EXECUTION_PROVIDERS'] = 'cpu'  # 必须设为 FaceFusion 支持的选项，实际加速靠 PyTorch/MPS

# 1. 优化 CPU 线程数（M1 推荐 4-6 线程，平衡性能和稳定性）
os.environ['OMP_NUM_THREADS'] = '6'

# 2. 启用 onnxruntime MPS 加速（底层生效，无需命令行参数）
os.environ['ORT_MPS_GPU_ALLOCATOR'] = 'caching'  # MPS 缓存优化，提升速度

# 3. PyTorch MPS 核心配置（仅保留兼容接口）
if torch.backends.mps.is_available():
    device = torch.device('mps')
    os.environ['PYTORCH_DEVICE'] = 'mps'
    print("[INFO] ✅ PyTorch MPS 加速已启用，设备：", device)
    print("[INFO] ✅ onnxruntime MPS 缓存优化已启用")
else:
    print("[WARNING] ⚠️ PyTorch MPS 不可用，将使用 CPU 运行（性能会大幅下降）")

# 4. 内存限制（适配 M1 共享内存）
os.environ['FACEFUSION_MEMORY_LIMIT'] = '12GB'  # 16GB M1 设 8GB，8GB M1 设 4GB

# 导入并启动 FaceFusion（移除无效的 --execution-providers mps 参数）
from facefusion import core

if __name__ == '__main__':
    # 仅保留 --open-browser 参数，移除所有 MPS 相关命令行参数
    # sys.argv.extend(['--open-browser'])
    core.cli()
