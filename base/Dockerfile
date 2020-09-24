FROM continuumio/miniconda3
WORKDIR /app

# 换源

##################
#  换源&安装依赖 #
##################

RUN conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
RUN conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/

RUN conda install pandas xlrd tqdm numpy ipykernel jupyter -y

##################
#  激活和准备插件#
##################
# 参考 https://github.com/xsthunder/linux-setting/blob/master/bash-script/conda/setup-jupyter-plugin.sh

# 插件管理器

## 用pip
# RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple;
# RUN pip install pip;

# RUN pip install jupyter_contrib_nbextensions;
# RUN jupyter contrib nbextension install --user;
# RUN pip install jupyter_nbextensions_configurator;
# RUN jupyter nbextensions_configurator enable --user

## 用conda
RUN conda install -y -c conda-forge jupyter_contrib_nbextensions
RUN jupyter contrib nbextension install --user
RUN conda install -y -c conda-forge jupyter_nbextensions_configurator
RUN jupyter nbextensions_configurator enable --user



# 下载vim插件
RUN git clone --depth=1 https://github.com/lambdalisue/jupyter-vim-binding /root/.local/share/jupyter/nbextensions/vim_binding
RUN chmod -R go-w /root/.local/share/jupyter/nbextensions/vim_binding

#  激活vim
RUN jupyter nbextension enable vim_binding/vim_binding
## snippets
RUN jupyter nbextension enable snippets/main
## freeze
RUN jupyter nbextension enable freeze/main
## ExecuteTime
RUN jupyter nbextension enable execute_time/ExecuteTime
## Toggle all line numbers
RUN jupyter nbextension enable toggle_all_line_numbers/main
## 代码折叠
RUN jupyter nbextension enable collapsible_headings/main

##################
#  准备配置      #
##################
RUN mkdir /opt/notebooks
RUN jupyter notebook --generate-config
COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py

####################################
# 安装所需环境，放在这里方便复用   #
####################################

CMD ["jupyter", "notebook", "--notebook-dir=/opt/notebooks", "--ip='*'",  "--port=8888", "--no-browser", "--allow-root"]


# docker build -t jupyter-base .
# docker rm -f jt-cpu
# docker run --name jbase -p 7777:8888 jupyter-base
# docker run -it --rm jupyter-torch-cpu /bin/bash