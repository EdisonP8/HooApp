from appium import webdriver
from PO.Android.RegisterPage import registerPage
from PO.getconfig import setup_method
from PO.Base import Base
from libs.ShareModules import Getdata
import pytest,time

loginpwd = Getdata('Login_tc','password') # 登陆密码
code = Getdata('Login_tc','code')  # 验证码

class TestRigister:
    """
    注册的测试用例
    """
    def setup_method(self):
        # setup_method.android_driver_caps["noReset"] = False
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', setup_method.android_driver_caps)  # 串联
        self.register_page = registerPage(self.driver)  # 初始化登录页元素以及方法
        time.sleep(5)  # 等待初始化完成

    def test_001_mobile_register(self):
        """
        用例一： 手机注册
        :param create_mobile: 随机生成手机号码
        :param loginpwd: 登陆密码
        :param code:  验证码
        """
        try:
            mobile =Base.create_CH_mobile()  # 随机生成手机号码
            print(mobile)
            self.register_page.getinto_register_page()
            self.register_page.register_by_mobile(mobile)
            self.register_page.send_loginpwd_paypwd_code(loginpwd,code)
            # assert msg
        except (Exception, AssertionError):
            self.register_page.Allure_save_img("001_mobile_register_fail")
            raise Exception

    def test_002_email_register(self):
        """
        用例二： 邮箱注册
        :param create_email: 随机生成邮箱地址
        :param loginpwd: 登陆密码
        :param code:  验证码
        """
        try:
            email = Base.create_email()  # 随机生成邮箱地址
            self.register_page.getinto_register_page()
            self.register_page.register_by_eamil(email)
            self.register_page.send_loginpwd_paypwd_code(loginpwd, code)
            # assert msg
        except (Exception, AssertionError):
            self.register_page.Allure_save_img("002_email_register_fail")
            raise Exception

    def test_003_switch_nation_register(self, nation='委内瑞拉'):
        """
        用例三: 切换国家注册,委内瑞拉
        :param create_VE_mobile: 随机生成委内瑞拉手机号码
        :param nation: 国家名称
        :param loginpwd: 登陆密码
        :param code:  验证码
        """
        try:
            mobile= Base.create_VE_mobile()  # 随机生成邮箱地址
            self.register_page.getinto_register_page()
            self.register_page.select_nation_list()
            self.register_page.input_nanme_select_nation(nation)
            self.register_page.register_by_mobile(mobile)
            self.register_page.send_loginpwd_paypwd_code(loginpwd, code)
            # assert msg
        except (Exception, AssertionError):
            self.register_page.Allure_save_img("003_switch_nation_register_fail")
            raise Exception

    def teardown_method(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s', 'C:/Users/HP/Desktop/HooApp/Scripts/Android/A_Register_test.py::TestRigister::test_003_switch_nation_register'])
    # pytest.main()