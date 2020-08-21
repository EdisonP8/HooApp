from appium import webdriver
from HooApp.PO.OtcPage import OTCPage
from HooApp.PO.getconfig import setup_method
from HooApp.libs.ShareModules import Getdata
import pytest,time


Transaction_pwd = Getdata('Login_tc','Transaction_pwd') # 交易密码
code = Getdata('Login_tc','code')  # 验证码
@pytest.mark.skip
class TestOTC:
    """
    法币的测试用例
    """

    def setup_method(self):
        setup_method.android_driver_caps["noReset"] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', setup_method.android_driver_caps)  # 串联
        self.otc_page = OTCPage(self.driver)  # 初始化登录页元素以及方法
        time.sleep(5)  # 等待初始化完成

    def test_001_otc_buy(self):
        '''
        用例一: 出售流程
        '''
        try:
            self.otc_page.goto_otc_page()
            self.otc_page.buy_business("USDT",500, "000000")
        except (Exception, AssertionError):
            raise Exception

    def test_002_otc_sell(self):
        '''
        用例一: 出售流程
        '''
        try:
            self.otc_page.goto_otc_page()
            self.otc_page.sell_business("USDT",500, "000000")
        except (Exception, AssertionError):
            raise Exception


    def teardown_method(self):
        time.sleep(20)
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s','C:/Users/HP/Desktop/Auto/HooApp/Scripts/C_OTC_test.py'
                      '::TestOTC::test_001_otc_sell'])
