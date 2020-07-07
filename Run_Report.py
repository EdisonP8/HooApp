import os, time, pytest
import unittest
from dateutil.parser import parse
from BeautifulReport import BeautifulReport

# 获取测试用例文件夹路径
curpath = os.path.dirname(os.path.realpath(__file__))
reportpath = os.path.join(curpath, "Reports")  # 判断测试报告存放目录是否存在，不在则进行创建
if not os.path.exists(reportpath):
    os.mkdir(reportpath)

class BeautifulReport:
    """
    输出BeautifulReport报告
    """

    def __init__(self):
        # 测试用例位置
        self.case_path = os.path.join(curpath, "Scripts")
        print(f'执行的测试用例路径为：{self.case_path}')
        self.starttime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("开始测试时间:", self.starttime)

    def add_cases(self):
        """
        批量添加测试用例
        :return:
        """

        discover = unittest.defaultTestLoader.discover(self.case_path, pattern="*_test.py",
                                                       top_level_dir=None)
        return discover

    def run_cases_by_beautiful_report(self, cases):
        """
        借用BeautifulReport模版输出测试用例报告
        :param cases:测试用例集
        :return:
        """
        day = time.strftime('%Y-%m-%d')
        result = BeautifulReport(cases)
        result.report(filename='%s_report.html' % day,
                      description='自动化测试报告',
                      log_path='Reports')

    def __del__(self):
        self.endtime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("测试结束时间:", self.endtime)
        totaltime = (self.endtime - self.starttime).total_seconds()
        print("测试总时长:", totaltime, "秒")


class Allure_RunReport:
    """运行 & 产生Allure_RunReport报告"""

    def __init__(self, root='./Scripts'):
        self.root = root
        self.starttime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("开始测试时间:", self.starttime)

    def __del__(self):
        self.endtime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print("测试结束时间:", self.endtime)
        totaltime = (self.endtime - self.starttime).total_seconds()
        print("测试总时长:", totaltime, "秒")

    def terminal_report(self):
        """
        在pycharm终端跑测试用例,但不生成报告
        :root: 指定运行文件，默认testcase中所有含有test的py脚本
        """

        pytest.main(['-s', '-q', self.root])  # 在终端运行报告

    def generate_report(self):
        """
        生成allure报告
        """

        pytest.main(['-s', self.root, '--alluredir', './Reports/data/'])  # 在终端运行报告
        os.system(
            'allure generate ./Reports/data/ -o ./Reports/html/ --clean')  # --clean清除上一期数据

    def open_report(self):
        """
        生成报告，且用浏览器打开allure报告
        """

        self.generate_report()
        os.system('allure open -h 127.0.0.1 -p 8083 ./Reports/html/')

    def rerun(self):
        """
        失败重跑机制 & 生产报告
        --lf参数（last fail）：运行上次运行失败的测试用例，如果没有失败用例则运行全部测试用例。
        -–ff参数(fail first)：运行所有的测试用例，上次运行失败的用例优先执行。
        :return:
        """
        pytest.main(['-s', '--lf', self.root, '--alluredir', './Reports/data/'])  # 在终端运行报告
        os.system(
            'allure generate ./Reports/data/ -o ./Reports/html/ --clean')  # --clean清除上一期数据


if __name__ == '__main__':
    # beautiful报告
    # re = BeautifulReport()
    # cases = re.add_cases()
    # re.run_cases_by_beautiful_report(cases)

    # allure报告
    Allure_RunReport().rerun()