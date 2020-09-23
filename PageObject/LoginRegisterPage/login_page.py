
from HooApp.Common.base_page import BasePage
from HooApp.PageLoact.login_register_page import LoginRegisterLocators as loc
from selenium.webdriver.common.action_chains import ActionChains

class LoginPage(BasePage):

    def getinto_login_page(self):
        name = "引导页点击跳过"
        self.wait_ele_visible(loc.ck_skip, doc=name)
        self.click_element(loc.ck_skip, doc=name)

    def input_tel_box(self, tel):
        name = "输入手机号码"
        self.wait_ele_visible(locator=loc.input_phone, doc=name)
        self.clear_loc_text(locator=loc.input_phone, doc=name)
        self.input_text(locator=loc.input_phone, text=tel, doc=name)

    def input_email_box(self, email):
        name = "输入邮箱"
        self.wait_ele_visible(locator=loc.switch_mode_email, doc=name)
        self.click_element(locator=loc.switch_mode_email, doc=name)
        self.wait_ele_visible(locator=loc.ipt_eamil, doc=name)
        self.clear_loc_text(locator=loc.ipt_eamil, doc=name)
        self.input_text(locator=loc.ipt_eamil, text=email, doc=name)

    def input_password_box(self, pwd):
        name = "输入密码"
        self.wait_ele_visible(locator=loc.input_pwd, doc=name)
        self.input_text(locator=loc.input_pwd, text=pwd, doc=name)

    def click_login_btn(self):
        name = "点击登录按钮"
        self.wait_ele_visible(locator=loc.bt_login, doc=name)
        self.click_element(locator=loc.bt_login, doc=name)

    def input_code(self,code):
        '''输入验证码'''
        BasePage.input_code(self,code)

    # def click_agree_box(self):
    #     name = "勾选同意复选框"
    #     self.wait_ele_visible(locator=loc.iv_select, doc=name)
    #     self.click_element(locator=loc.iv_select, doc=name)

    def login_by_Mobile_verify(self, code):
        name = "手机+验证码登录"
        self.wait_ele_visible(loc.switch_verify_login, doc=name)
        self.click_element(loc.switch_verify_login, doc=name)
        self.wait_ele_visible(loc.ck_verify_code, doc=name)
        self.click_element(loc.ck_verify_code, doc=name)
        self.input_text(loc.ipt_code, code, doc=name)

    def input_verify_code(self, code):
        action_a = ActionChains(self.driver)
        action_a.move_to_element(self.driver.find_element(*loc.ipt_verify_code)).click().send_keys(
            code).perform()  # 输入异常验证码

    def business_forgot_password(self, code, pwd):
        name = "忘记密码流程"
        self.wait_ele_visible(loc.ck_verify_code, doc=name)
        self.click_element(loc.ck_verify_code, doc=name)
        self.input_text(loc.ipt_code, code, doc=name)
        self.wait_ele_visible(loc.bt_login, doc=name)
        self.click_element(loc.bt_login, doc=name)  # 点击下一步
        self.wait_ele_visible(loc.input_pwd, doc=name)
        self.input_text(loc.input_pwd, pwd, doc=name)
        self.input_text(loc.ipt_login_comfirm_pwd, pwd, doc=name)
        self.wait_ele_visible(loc.bt_login, doc=name)
        self.click_element(loc.bt_login, doc=name)  # 点击完成

    def Email_Forgot_password(self, email):
        name = "邮箱忘记密码"
        self.wait_ele_visible(loc.ck_Forgot_password, doc=name)
        self.click_element(loc.ck_Forgot_password, doc=name)
        self.wait_ele_visible(loc.switch_mode_email, doc=name)
        self.click_element(loc.switch_mode_email, doc=name)
        self.wait_ele_visible(loc.ipt_eamil, doc=name)
        self.input_text(loc.ipt_eamil, email, doc=name)

    def Mobile_Forgot_password(self, mobile):
        name = "手机忘记密码,默认方式"
        self.wait_ele_visible(loc.ck_Forgot_password, doc=name)
        self.click_element(loc.ck_Forgot_password, doc=name)
        self.wait_ele_visible(loc.ipt_mobile, doc=name)
        self.input_text(loc.ipt_mobile, mobile, doc=name)