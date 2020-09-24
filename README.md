# 个人用的简易jupyter docker

内含常用插件，有vim插件

## base 基础包

> 可用于基础数据清洗

1. `cd base`

1. 运行`generate-jupyter_notebook_config.py <password>`生成jupyter的密码文件`jupyter_notebook_config.py`

1. 运行`docker build -t jupyter-base .`


1. 运行`docker run --name jbase -p 7777:8888 jupyter-base`，浏览器打开`http://localhost:8888`

## torch cpu

> 在base的基础上加入cpu版的torch，可用于简易深度学习开发

1. `cd torch`

1. 运行`docker build -t jupyter-torch .`

1. 运行`docker run --name jtorch -p 7778:8888 jupyter-base`，浏览器打开`http://localhost:8888`

### TODO

加入目录映射
