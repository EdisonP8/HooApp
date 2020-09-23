import time
import pytest
from appium import webdriver
from HooApp.Common.device_config import *
from HooApp.PageObject.HomePage.home_page import HomePage
from HooApp.PageObject.LoginRegisterPage.login_page import LoginPage
import logging
from HooApp.Common.get_data import GetData


# 启动会话设置noReset=False,启动重置
@pytest.fixture(scope="class")
def base_driver():
    # 读取全局的一个caps选项
    setup_method.driver_caps["noReset"] = False
    # 启动浏览器会话,与appium server进行连接，并发送要操作的设备对象信息。
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", setup_method.driver_caps)
    LoginPage(driver).getinto_login_page()
    yield driver
    # 登录成功后进行退出账号
    if HomePage(driver).is_welcome_exist():
        HomePage(driver).click_welcome_btn()
        HomePage(driver).click_confirm_btn()
    else:
        pass

# 启动会话设置noReset=True,启动不重置
@pytest.fixture(scope="class")
def is_logined():
    # 读取全局的一个caps选项。
    setup_method.driver_caps["noReset"] = True
    # 启动浏览器会话,与appium server进行连接，并发送要操作的设备对象信息。
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", setup_method.driver_caps)
    if HomePage(driver).is_loginRegisterBtn_exist():
        logging.info("当前尚未登陆状态")
        HomePage(driver).click_LoginRegister_Btn()
        LoginPage(driver).input_tel_box(GetData().get_login_tel())
        LoginPage(driver).input_password_box(GetData().get_login_pwd())
        LoginPage(driver).click_login_btn()
        time.sleep(3)
        LoginPage(driver).input_code(GetData().get_vcode())
    else:
        logging.info("当前用户已登陆")
    yield driver

