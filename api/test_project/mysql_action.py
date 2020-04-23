
from pymysql import connect
import yaml
import logging.config


class DB():
	def __init__(self):
		"""连接数据库"""
		logging.info('===================== init data =====================')
		logging.info("connect db")
		self.conn = connect(host='127.0.0.1', user='root', password='Zx123456', db='django_restful')

	def clear(self, table_name):
		"""清除表中数据"""
		logging.info("clear db...")
		clear_sql = 'truncate ' + table_name + ';'   # 注意在truncate后面加上空格
		with self.conn.cursor() as cursor:
			# 清除外键约束
			cursor.execute("set foreign_key_checks=0;")
			cursor.execute(clear_sql)
		self.conn.commit()

	def insert(self, table_name, table_data):
		"""插入数据"""
		logging.info("insert data...")

		# 遍历数据
		for key in table_data:
			table_data[key] = "'" + str(table_data[key]) + "'"

		key = ','.join(table_data.keys())
		value = ','.join(table_data.values())
		logging.info(key, value)

		insert_sql = 'insert into ' + table_name + '('+key+')'+'values'+'('+value+')'
		logging.info(insert_sql)

		with self.conn.cursor() as cursor:
			cursor.execute(insert_sql)
		self.conn.commit()

	def close(self):
		"""关闭数据库连接"""
		logging.info("close db")
		self.conn.close()
		logging.info("===========init finisher!===========")

	def init_data(self, datas):
		"""初始化数据"""
		logging.info("init ab...")
		for table, data in datas.items():
			self.clear(table)
			for d in data:
				self.insert(table, d)
		self.close()


if __name__ == '__main__':
	db = DB()
	# 调试各个方法
	# db.clear("api_user")
	# db.clear("api_group")
	# user_data = {'id': 1, 'username': '51zxw', 'email': '51zxw@163.com', 'groups': 'http://127.0.0.1:8000/groups/1'}
	# db.insert("api_user", user_data)
	# group_data = {'id': 1, 'name': 'Developer'}
	# db.insert('api_group', group_data)
	# db.close()

	# 初始化数据
	f = open('datas.yaml', 'r', encoding="utf-8")
	datas = yaml.load(f, Loader=yaml.FullLoader)   # 禁用警告 yaml.load(input, Loader=yaml.FullLoader)
	db.init_data(datas)
