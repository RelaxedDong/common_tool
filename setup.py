# coding: utf-8

from setuptools import setup
from setuptools import find_packages


VERSION = "0.0.7"
AUTHOR = "donghao"
AUTHOR_EMAIL = "is_simple@163.com"

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='common_tool',
    version=VERSION,
    author='donghao',
    author_email=AUTHOR_EMAIL,
    url="https://github.com/RelaxedDong/dh_common",
    description='Basic toolkit packaging',
    packages=find_packages(),
    install_requires=['six>=1.15.0'],
    long_description=long_description,  # 项目的描述 读取README.md文件的信息
    long_description_content_type="text/markdown",  # 描述文档README的格式 一般md
    license="MIT",
)
