
import pytest
from HooApp.PageObject.HomePage.home_page import HomePage
from HooApp.PageObject.LoginRegisterPage.register_page import RegisterPage
from HooApp.Common.get_data import GetData

@pytest.mark.usefixtures("base_driver")
class TestRegister:

    # 手机注册
    def test_mobile_register(self,base_driver):
        # 点击登录注册按钮
        HomePage(base_driver).click_LoginRegister_Btn()
        # 输入用户名，输入密码，点击登录
        RegisterPage(base_driver).getinto_register_page()
        RegisterPage(base_driver).register_by_mobile(RegisterPage.create_CH_mobile(9))  # 随机生成手机号码
        RegisterPage(base_driver).send_loginpwd_paypwd_code(GetData().get_vcode(),GetData().get_login_pwd())
        assert RegisterPage(base_driver).find_element("注册成功")

    # 邮箱注册
    def test_email_register(self,base_driver):
        # 点击登录注册按钮
        HomePage(base_driver).click_LoginRegister_Btn()
        # 输入用户名，输入密码，点击登录
        RegisterPage(base_driver).getinto_register_page()
        RegisterPage(base_driver).register_by_eamil(RegisterPage.create_email(4))  # 随机生成邮箱地址
        RegisterPage(base_driver).send_loginpwd_paypwd_code(GetData().get_vcode(), GetData().get_login_pwd())
        assert RegisterPage(base_driver).find_element("注册成功")

    # 国外手机注册
    def test_switch_nation_register(self, base_driver):
        # 点击登录注册按钮
        HomePage(base_driver).click_LoginRegister_Btn()
        # 输入用户名，输入密码，点击登录
        RegisterPage(base_driver).getinto_register_page()
        RegisterPage(base_driver).input_nanme_select_nation("委内瑞拉")
        RegisterPage(base_driver).register_by_mobile(RegisterPage.create_VE_mobile(7))  # 委内瑞拉国家手机号码
        RegisterPage(base_driver).send_loginpwd_paypwd_code(GetData().get_vcode(), GetData().get_login_pwd())
        assert RegisterPage(base_driver).find_element("注册成功")
