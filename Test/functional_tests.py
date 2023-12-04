#!/user/bin/env python
# -*-coding:utf-8 -*-
"""

@File   : functional_tests.py 
@Desc   :
@Author : WANGCHANGGUAN
@Version: 0.0.1
@Time : 2023/12/4 15:25 
"""

from selenium import webdriver

Broser = webdriver.Chrome()
Broser.get('http://localhost:8000')

assert 'install' in Broser.title

