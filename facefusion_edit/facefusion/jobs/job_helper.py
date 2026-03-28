import os
from datetime import datetime
from typing import Optional

from facefusion.filesystem import get_file_extension, get_file_name


def get_step_output_path(job_id: str, step_index: int, output_path: str) -> str:
    # 配置默认输出目录（不存在则自动创建）
    default_output_dir = os.path.join(os.path.dirname(__file__), "../../outputs")
    os.makedirs(default_output_dir, exist_ok=True)
    
    # 处理输出路径：若未指定，使用默认路径+自动生成文件名
    if not output_path or output_path.strip() == "":
        output_directory_path = default_output_dir
        output_file_name = f"facefusion_output_{uuid.uuid4().hex[:8]}"  # 随机8位文件名
        output_file_extension = ".mp4"  # 默认格式 mp4
    else:
        # 若指定了输出路径，按原逻辑解析
        output_directory_path = os.path.dirname(output_path)
        output_file_name = os.path.splitext(os.path.basename(output_path))[0]
        output_file_extension = os.path.splitext(os.path.basename(output_path))[1]
        # 确保扩展名不为空，默认 mp4
        if not output_file_extension:
            output_file_extension = ".mp4"
    
    # 拼接最终输出路径
    return os.path.join(
        output_directory_path,
        f"{output_file_name}-{job_id}-{str(step_index)}{output_file_extension}"
    )


def suggest_job_id(job_prefix : str = 'job') -> str:
	return job_prefix + '-' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
