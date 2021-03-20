
"""执行用例&测试报告"""

import unittest
from BeautifulReport import BeautifulReport
# 解决cmd运行脚本找不到api模块，将脚本路径添加到环境变量
import sys
sys.path.append('/Pycharm/django_restful/')

from api.test_project.mysql_action import DB
import time
import yaml
# 导入日志模块
import logging.config


# 导入日志配置文件
CON_LOG = 'log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


# 数据初始化操作
db = DB()
f = open('datas.yaml', 'r', encoding="utf-8")
datas = yaml.load(f, Loader=yaml.FullLoader)   # 禁用警告 yaml.load(input, Loader=yaml.FullLoader)
db.init_data(datas)


# 指定测试用例为当前文件夹下的文件
test_dir = '.'

# 加载目录下 test.py结尾的py文件
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

# 加载测试用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_django_restful.py')

# 方式二.BeautifulReport
if __name__ == "__main__":
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = './reports/' + now + '_result.html'
	fp = open(filename, 'wb')
	BeautifulReport(discover).report(description='接口测试', filename=filename, report_dir='')
	logging.info("=============== Start API Test ===============")
