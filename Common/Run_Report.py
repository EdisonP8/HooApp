import pytest
import unittest
from HooApp.Common.read_config import *
from datetime import datetime
from BeautifulReport import BeautifulReport

class Beautiful_RunReport:
    """使用BeautifulReport模块产生报告"""

    # 添加测试用例-->产生测试报告
    def run_make_report(self):
        self.case_path = os.path.join(TestCases_file_path)
        print(f'执行的测试用例路径为：{self.case_path}')
        start_time = datetime.now()
        print("开始测试时间:", start_time)
        cases = unittest.defaultTestLoader.discover(self.case_path, pattern="*Swap_api.py")
        # print(cases)
        BeautifulReport(cases).report(description='测试报告',log_path=test_report_path)
        ends_time = datetime.now()
        print("测试结束时间:", ends_time)
        total_time = (ends_time - start_time).seconds
        print("测试总时长:", total_time, "秒")

class Allure_RunReport:
    """使用Allure模块产生报告"""

    #  生成allure报告
    def run_make_report(self):
        # 产生数据源 pytest.main(['--alluredir', './Outputs/data']) ['操作命令'，'保存地址']
        # 生成报告 allure generate ./<测试生成的数据>/ -o ./<测试报告存放的路径>/ --clean
        # 这样在report目录下就生成了Allure的测试报告了，–clean目的是先清空测试报告目录，再生成新的测试报告。
        self.case_path = os.path.join(TestCases_file_path)
        pytest.main(['-s', self.case_path, '--alluredir', '../Test_Result/Allure/data'])  # 在终端运行报告
        os.system('allure generate ../Test_Result/Allure/data -o ../Test_Result/Allure/html/ --clean')

    # 生成报告，且用浏览器打开allure报告
    def open_report(self):
        self.run_make_report()
        os.system('allure serve ../Test_Result/Allure/data')


if __name__ == '__main__':
    # beautiful报告
    # Beautiful_RunReport().run_make_report()

    # allure报告
    Allure_RunReport().run_make_report()