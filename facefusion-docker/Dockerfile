# 基于原CPU镜像
FROM facefusion/facefusion:3.3.2-cpu

# 删除容器内默认的 facefusion 代码（如果存在）
RUN rm -rf /facefusion

# 将本地克隆的代码复制到容器内 /facefusion 目录
COPY ./facefusion /facefusion

# 进入代码目录
WORKDIR /facefusion

# 安装你的代码所需的依赖（包括修复 requests 缺失问题）
RUN pip install --no-cache-dir -r requirements.txt && \
pip install --no-cache-dir requests

# 启动命令（根据你的代码入口调整）
RUN python install.py --onnxruntime default --skip-conda