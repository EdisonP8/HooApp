
import pytest
from HooApp.PageObject.HomePage.home_page import HomePage
from HooApp.PageObject.LoginRegisterPage.login_page import LoginPage  as LR
from HooApp.Common.get_data import GetData
import time

@pytest.mark.usefixtures("base_driver")
class TestLogin:

    # 手机号码 + 密码登录
    def test_login_password_success(self, base_driver):
        # 点击登录注册按钮
        HomePage(base_driver).click_LoginRegister_Btn()
        # 输入用户名，输入密码，点击登录
        LR(base_driver).input_tel_box(GetData().get_login_tel())
        LR(base_driver).input_password_box(GetData().get_login_pwd())
        LR(base_driver).click_login_btn()
        time.sleep(5)
        LR.input_code(base_driver, GetData().get_vcode())
        # 断言:判断首页-->登录/注册按钮 ,返回False代表已登录,Ture代表未登录
        # assert HomePage(base_driver).is_loginRegisterBtn_exist() == False
        assert LR(base_driver).find_element("欢迎回来")

    # 手机号码 + 验证码登录
    def test_login_verify_code_success(self, base_driver):
        # 点击登录注册按钮
        HomePage(base_driver).click_LoginRegister_Btn()
        # 输入手机号，发送验证码、输入验证码，点击登录
        LR(base_driver).input_tel_box(GetData().get_login_tel())
        LR(base_driver).login_by_Mobile_verify(GetData().get_vcode())
        LR(base_driver).click_login_btn()
        time.sleep(5)
        LR(base_driver).input_verify_code(GetData().get_Id_number())
        # 断言:判断首页-->登录/注册按钮 ,返回False代表已登录,Ture代表未登录
        assert LR(base_driver).find_element("欢迎回来")

    # 邮箱 + 密码登录
    def test_email_password_success(self, base_driver):
        # 点击登录注册按钮
        HomePage(base_driver).click_LoginRegister_Btn()
        # 输入邮箱，输入密码，点击登录
        LR(base_driver).input_email_box(GetData().get_login_email())
        LR(base_driver).input_password_box(GetData().get_login_pwd())
        LR(base_driver).click_login_btn()
        time.sleep(5)
        input_code(base_driver, GetData().get_vcode())
        # 断言:判断首页-->登录/注册按钮 ,返回False代表已登录,Ture代表未登录
        assert HomePage(base_driver).is_loginRegisterBtn_exist() == False

    # 手机忘记密码
    def test_Mobile_Forgot_password(self, base_driver):
        HomePage(base_driver).click_LoginRegister_Btn()
        LR(base_driver).Mobile_Forgot_password(GetData().get_login_tel())
        LR(base_driver).business_forgot_password(GetData().get_vcode(), GetData().get_login_pwd())
        assert LR(base_driver).find_element("设置密码成功")

    # 邮箱忘记密码
    def test_Email_Forgot_password(self, base_driver):
        HomePage(base_driver).click_LoginRegister_Btn()
        LR(base_driver).Email_Forgot_password(GetData().get_login_email())
        LR(base_driver).business_forgot_password(GetData().get_vcode(), GetData().get_login_pwd())
        assert LR(base_driver).find_element("设置密码成功")
