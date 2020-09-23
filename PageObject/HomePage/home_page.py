
from HooApp.Common.base_page import BasePage
from HooApp.PageLoact.home_page import HomePageLocators as loc

class HomePage(BasePage):
    # 点击登陆注册按钮
    def click_LoginRegister_Btn(self):
        name = "点击登陆注册按钮"
        self.wait_ele_visible(locator=loc.login_register_btn, doc=name)
        self.click_element(locator=loc.login_register_btn, doc=name)

    def is_loginRegisterBtn_exist(self):
        name = "首页_登陆按钮是否存在"
        if self.is_ele_visible(locator=loc.login_register_btn, doc=name):
            return True  #代表尚未登陆状态
        else:
            return False

    def is_welcome_exist(self):
        name = "欢迎回来是否存在"
        if self.is_ele_visible(loc.welcome_btn, doc=name):
            return True
        else:
            return False

    def click_welcome_btn(self):
        name = "点击欢迎回来"
        self.click_element(loc.welcome_btn, doc=name)

    def click_confirm_btn(self):
        self.wait_ele_visible(loc.confirm_btn, doc="确认按钮是否可见")
        self.click_element(loc.confirm_btn, doc="点击确认按钮")

    # 点击法币
    def click_otc_btn(self):
        name = "点击法币小程序"
        self.wait_ele_visible(locator=loc.otc_btn, doc=name)
        self.click_element(locator=loc.otc_btn, doc=name)

    def click_comanagement_btn(self):
        name = "点击共管钱包小程序"
        self.wait_ele_exist(locator=loc.comanagement_btn, doc=name)
        self.click_element(locator=loc.comanagement_btn, doc=name)
