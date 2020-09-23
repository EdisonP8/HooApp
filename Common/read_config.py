import os
import pymysql
import configparser
import logging

# 框架项目顶层目录
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 配置文件的路径
config_file_path = os.path.join(project_path, "config", "config.ini")

# 存储日志的文件的路径
log_path = os.path.join(project_path, 'Test_Result','test_logs.txt')

# 测试报告的路径
test_report_path = os.path.join(project_path, 'Test_Result')

# 测试结果截图路径
screenshot_path = os.path.join(project_path, "Test_Result/screenshots")

# 测试用例文件路径
TestCases_file_path = os.path.join(project_path, "Test_Cases")


# -------------------------------------------------------------------------------
# 函数/类/过程名称：GetData
# 函数/类/过程目的：读取测试数据
# -------------------------------------------------------------------------------
def ReadConfig(config_file_path,title,subtitle):
    config = configparser.ConfigParser()  # 创建管理对象

    config.read(config_file_path,encoding='utf-8')
    return config.get(title, subtitle)

# -------------------------------------------------------------------------------
# 函数/类/过程名称：Connect_sql
# 函数/类/过程目的：从数据获取数据
# -------------------------------------------------------------------------------
host = ReadConfig(config_file_path,'Database_config','db_host')
port = ReadConfig(config_file_path,'Database_config','db_port')
user = ReadConfig(config_file_path,'Database_config','db_user')
password = ReadConfig(config_file_path,'Database_config','db_password')
db1 = ReadConfig(config_file_path,'Database_config','db_database')

def Connect_sql(sql):
    # 连接数据库
    conn = pymysql.connect(host=host, user=user,password=password,
                         db=str(db1), port=int(port),charset='utf8')
    curs = conn.cursor()  # 获取操作游标
    curs.execute(sql)  # 执行sql语句
    data = curs.fetchall()  # 获取返回所有的数据中的第一条
    # data = curs.fetchone() # 获取返回所有的数据中的第一条
    curs.close()
    conn.close()
    return data

# -------------------------------------------------------------------------------
# 函数/类/过程名称：MyLog
# 函数/类/过程目的：写日志
# -------------------------------------------------------------------------------
class MyLog:

    def my_log(self, msg, level):
        Info = 'HooAPITest'
        my_logger = logging.getLogger(Info)
        my_logger.setLevel('DEBUG')

        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(formatter)
        fh = logging.FileHandler(log_path, encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        # 收集日志
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)

        # 关闭渠道
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log(msg, 'DEBUG')

    def info(self, msg):
        self.my_log(msg, 'INFO')

    def error(self, msg):
        self.my_log(msg, 'ERROR')

    def critical(self, msg):
        self.my_log(msg, "CRITICAL")

    def warning(self, msg):
        self.my_log(msg, "WARNING")

if __name__ == '__main__':
    query_sql = "SELECT * from user_phonecode where phone='13632548888' ORDER BY id DESC LIMIT 3"
    res = Connect_sql(query_sql)
    print(res[0], res[0][3])
