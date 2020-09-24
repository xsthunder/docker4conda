FROM jupyter-base
WORKDIR /app

####################################
# 安装所需环境，放在这里方便复用   #
####################################
RUN conda install pytorch torchvision cpuonly -c pytorch # see https://pytorch.org/get-started/locally/


CMD ["jupyter", "notebook", "--notebook-dir=/opt/notebooks", "--ip='*'",  "--port=8888", "--no-browser", "--allow-root"]

# passwd ecustlab301
# docker build -t jupyter-torch-cpu .
# docker rm -f jt-cpu
# docker run --name jt-cpu -p 7777:8888 jupyter-torch-cpu
# docker run -it --rm jupyter-torch-cpu /bin/bash