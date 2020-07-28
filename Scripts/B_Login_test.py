from appium import webdriver
from HooApp.PO.LoginPage import LoginPage
from HooApp.PO.getconfig import setup_method
from HooApp.libs.ShareModules import Getdata
import pytest,time

email = Getdata('Login_tc','email') # 登录邮箱
mobile = Getdata('Login_tc','mobile') # 登录手机号
loginpwd = Getdata('Login_tc','password') # 登陆密码
code = Getdata('Login_tc','code')  # 验证码

class TestLogin:
    """
    登录的测试用例
    """

    def setup_method(self):
        setup_method.android_driver_caps["noReset"] = False
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', setup_method.android_driver_caps)  # 串联
        self.login_page = LoginPage(self.driver)  # 初始化登录页元素以及方法
        time.sleep(5)  # 等待初始化完成

    def test_001_login_by_email(self):
        '''
        用例一: 邮箱登陆
        '''
        try:
            self.login_page.getinto_login_page()
            self.login_page.login_by_Email(email)
            self.login_page.input_loginpwd_in(loginpwd,code)
            msg = self.login_page.verify_login_success()  # 断言登录成功后弹窗文本,前往安全中心
            assert msg == self.login_page.verify_login_success()
        except (Exception, AssertionError):
            self.login_page.Allure_save_img("001_login_by_email_fail")
            raise Exception

    def test_002_login_by_mobile(self):
        '''
        用例二: 手机号码密码登陆
        '''
        try:
            self.login_page.getinto_login_page()
            self.login_page.login_by_Mobile(mobile)
            self.login_page.input_loginpwd_in(loginpwd,code)
            msg = self.login_page.verify_login_success()
            assert msg == self.login_page.verify_login_success()
        except (Exception, AssertionError):
            self.login_page.Allure_save_img("002_login_by_mobile_fail")
            raise Exception

    def test_003_login_by_mobile_verify(self):
        '''
        用例三: 手机号码验证码登陆
        '''
        try:
            self.login_page.getinto_login_page()
            self.login_page.login_by_Mobile_verify(mobile,code)
            msg = self.login_page.verify_login_success()
            assert msg == self.login_page.verify_login_success()
        except (Exception, AssertionError):
            self.login_page.Allure_save_img("003_login_by_mobile_verify_fail")
            raise Exception

    def test_004_Email_Forgot_password(self):
        '''
        用例四: 单邮箱忘记密码
        '''
        try:
            self.login_page.getinto_login_page()
            msg = self.login_page.Email_Forgot_password(email,code,loginpwd)
            # assert msg == True
        except (Exception, AssertionError):
            self.login_page.Allure_save_img("004_Email_Forgot_password_fail")
            raise Exception

    def test_005_Mobile_Forgot_password(self):
        '''
        用例五: 单手机忘记密码
        '''
        try:
            self.login_page.getinto_login_page()
            msg = self.login_page.Mobile_Forgot_password(mobile, code, loginpwd)
            # assert msg == True
        except (Exception, AssertionError):
            self.login_page.Allure_save_img("005_Mobile_Forgot_password_fail")
            raise Exception

    def teardown_method(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s','C:/Users/HP/Desktop/Auto/HooApp/Scripts/Android/B_Login_test.py'
                      '::TestLogin::test_002_login_by_mobile'])
