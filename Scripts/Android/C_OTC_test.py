from appium import webdriver
from HooApp.PO.Android.OtcPage import OTCPage
from HooApp.PO.getconfig import setup_method
from HooApp.libs.ShareModules import Getdata
import pytest,time

email = Getdata('Login_tc','email') # 登录邮箱
mobile = Getdata('Login_tc','mobile') # 登录手机号
loginpwd = Getdata('Login_tc','password') # 登陆密码
code = Getdata('Login_tc','code')  # 验证码

class TestOTC:
    """
    法币的测试用例
    """

    def setup_method(self):
        setup_method.android_driver_caps["noReset"] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', setup_method.android_driver_caps)  # 串联
        self.otc_page = OTCPage(self.driver)  # 初始化登录页元素以及方法
        time.sleep(5)  # 等待初始化完成

    def test_001_otc_sell(self):
        '''
        用例一: 出售流程
        '''
        try:
            # print(self.driver.page_source)
            self.otc_page.getinto_login_page()
            # time.sleep(5)
            # self.driver.tap([(106,984),(359,1114)],200)
            # time.sleep(2)
            self.otc_page.login_by_Email(500)
            self.otc_page.input_loginpwd_in("000000")
        except (Exception, AssertionError):
            raise Exception

    def teardown_method(self):
        time.sleep(20)
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s','C:/Users/HP/Desktop/Auto/HooApp/Scripts/Android/C_OTC_test.py'
                      '::TestOTC::test_001_login_by_email'])
