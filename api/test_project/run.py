
"""执行用例&测试报告"""

import unittest
from BSTestRunner import BSTestRunner
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

# 指定测试用例和测试报告的路径、
test_dir = '.'
report_dir = './reports'

# 加载测试用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_django_restful.py')

# 定义报告的文件格式
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir + '/' + now + 'test_report.html'

if __name__ == '__main__':
	# 运行用例并生成测试报告
	with open(report_name, 'wb') as f:
		runner = BSTestRunner(stream=f, title='API Test Report', description='Django Restful API Test Report')
		logging.info("=============== Start API Test ===============")
		runner.run(discover)