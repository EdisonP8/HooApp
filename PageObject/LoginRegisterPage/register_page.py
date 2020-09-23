import time
from HooApp.Common.base_page import BasePage
from HooApp.PageLoact.login_register_page import LoginRegisterLocators as loc
from appium.webdriver.common.mobileby import MobileBy

class RegisterPage(BasePage):

    def getinto_register_page(self):
        name = "注册页面"
        self.wait_ele_visible(loc.ck_register_btn, doc=name)
        self.click_element(loc.ck_register_btn, doc=name)

    def register_by_mobile(self, mobile):
        name = "手机号码注册"
        self.wait_ele_visible(loc.input_phone, doc=name)
        self.input_text(loc.input_phone, mobile, doc=name)  # 输入手机号码

    def register_by_eamil(self, email):
        name = "邮箱注册"
        self.wait_ele_visible(loc.ipt_eamil, doc=name)
        self.input_text(loc.ipt_eamil, email, doc=name)  # 输入邮箱

    def send_loginpwd_paypwd_code(self, code, loginpwd):
        name = "输入登陆密码、验证码"
        self.wait_ele_visible(loc.ck_verify_code, doc=name)
        self.click_element(loc.ck_verify_code, doc=name)
        self.input_text(loc.ipt_code, code, doc=name)
        self.wait_ele_visible(loc.bt_login, doc=name)
        self.click_element(loc.bt_login, doc=name)  # 点击下一步
        self.wait_ele_visible(loc.input_pwd, doc=name)
        self.input_text(loc.input_pwd, loginpwd, doc=name)
        self.input_text(loc.ipt_login_comfirm_pwd, loginpwd, doc=name)
        self.wait_ele_visible(loc.bt_login, doc=name)
        self.click_element(loc.bt_login, doc=name)  # 点击完成

    def verify_login_success(self):
        name = "注册成功后弹窗文本，前往安全中心"
        self.wait_ele_visible(loc.get_register_success_txt, doc=name)
        self.click_element(loc.get_register_success_txt, doc=name)

    def tap_select_nation(self, nation):
        name = "切换注册国家，直接滑动选择 "
        nation_XPATH = (MobileBy.XPATH, f'//android.widget.TextView[contains(@text, "{nation}")]')  # 定位国家
        self.wait_ele_visible(loc.select_nation_list, doc=name)
        self.click_element(loc.select_nation_list, doc=name)
        time.sleep(2)
        while not self.find_element(nation):
            self.swipeUP(loc.swipe_loc)
            self.swipeUP(loc.swipe_loc)
        else:
            self.find_element(*nation_XPATH).click()

    def input_nanme_select_nation(self, nation):
        name = "切换注册国家，输入国家名称选择国家 "
        self.wait_ele_visible(loc.select_nation_list, doc=name)
        self.click_element(loc.select_nation_list, doc=name)
        self.wait_ele_visible(loc.ipt_nation_name, doc=name)
        self.input_text(loc.ipt_nation_name, nation, doc=name)
        self.wait_ele_visible(loc.ck_nation_name, doc=name)
        self.click_element(loc.ck_nation_name, doc=name)