#coding:utf-8

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
      name='redis_netlock',
      version = '1.6',
      author="ruifengyun",
      author_email="rfyiamcool@163.com",
      url="http://xiaorui.cc/",
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      install_requires=['redis'],
      packages=['redis_netlock'],
      platforms=["Any"],
      license = "MIT",
      keywords=['redis lock distributed','fengyun'],
      description="一个用redis做的分布式锁，含有超时及重试机制.",
      long_description=open('README.md').read(),
)
