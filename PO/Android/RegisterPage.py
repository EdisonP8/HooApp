from PO.Base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class registerPage(Base):
    """
    启动页+注册界面的页面元素
    """

    # ck_login_register_button = (By.ID, "tv_login_register")  # 首页点击登录/注册按钮
    ck_login_register_button = (By.ID, "ll_5")  # 首页点击登录/注册按钮
    ck_register = (By.XPATH,"//android.widget.TextView[@text='立即注册']") # 点击立即注册

    # 手机注册 # 邮箱注册
    switch_mode_email = (By.ID, "tv_email") # 切换邮箱注册
    switch_mode_phone = (By.ID, "tv_phone") # 切换手机注册
    ipt_mobile = (By.ID, "et_input_phone")  # 输入手机号码
    ipt_eamil = (By.ID, "et_input_email")  # 输入邮箱
    ck_verify_code = (By.ID, "tv_phonecode")  # 点击发送验证码
    ipt_code = (By.ID, "et_input_code")  # 输入验证码
    ck_next_btn = (By.ID, "bt_login")  # 点击下一步
    ck_invite_code = (By.XPATH, "//android.widget.TextView[@text='立即填写']")  # 点击立即填写邀请码
    ipt_invite_code = (By.ID, "et_input_invite")  # 输入邀请码

    ipt_login_pwd = (By.ID, "et_input_pwd")  # 输入登录密码
    ck_pwd_display = (By.ID, "iv_pwd_on") # 点击密码加密显示
    ipt_login_comfirm_pwd = (By.ID, "et_input_pwd2")  # 再次输入登录密码
    ck_skip_setp = (By.XPATH, "//android.widget.TextView[@text='跳过此步骤']")  # 点击跳过此步骤

    # 切换国家
    select_nation_list = (By.ID, "com.hufu.qianbao:id/tv_area")  # 国家下拉框
    ipt_nation_name =(By.ID, "et_search") # 输入查询的国家名称
    ck_nation_name = (By.ID, "tv_name") #选择对应的国家，默认第一个

    def getinto_register_page(self):
        """进入注册页面"""
        # WebDriverWait(self.driver, 10, 0.5).until(
        #     # EC.text_to_be_present_in_element(self.ck_login_register_button, u"登录 / 注册"))
        #     EC.text_to_be_present_in_element(self.ck_login_register_button, u"我"))
        self.driver.find_element(*self.ck_login_register_button).click()
        time.sleep(2)
        self.driver.find_element(*self.ck_register).click()
        time.sleep(2)

    def register_by_mobile(self, mobile):
        """手机号码注册"""
        time.sleep(1)
        self.driver.find_element(*self.ipt_mobile).send_keys(mobile)  # 输入手机号码

    def register_by_eamil(self, email):
        """邮箱注册"""
        time.sleep(1)
        self.driver.find_element(*self.switch_mode_email).click() # 切换邮箱注册

        self.driver.find_element(*self.ipt_eamil).send_keys(email)  # 输入邮箱

    def send_loginpwd_paypwd_code(self,loginpwd,code):
        """输入登陆密码、验证码"""

        self.driver.find_element(*self.ck_verify_code).click()  # 点击发送验证码
        time.sleep(3)
        self.driver.find_element(*self.ipt_code).send_keys(code)  # 验证码默认456321
        self.driver.find_element(*self.ck_next_btn).click()  # 点击下一步
        time.sleep(2)
        self.driver.find_element(*self.ipt_login_pwd).send_keys(loginpwd)
        self.driver.find_element(*self.ipt_login_comfirm_pwd).send_keys(loginpwd)
        self.driver.find_element(*self.ck_pwd_display).click()
        self.driver.find_element(*self.ck_next_btn).click()  # 点击下一步
        time.sleep(5)

    def tap_select_nation(self, nation):
        """切换注册国家，直接滑动选择 """
        nation_XPATH = (By.XPATH, f'//android.widget.TextView[contains(@text, "{nation}")]')  # 定位国家
        self.driver.find_element(*self.select_nation_list).click()
        time.sleep(2)
        while not self.findElement(nation):
            self.swipeUP(duration=150)
            self.swipeUP(duration=150)
        else:
            self.driver.find_element(*nation_XPATH).click()

    def input_nanme_select_nation(self, nation):
        """切换注册国家，输入国家名称选择国家 """
        self.driver.find_element(*self.select_nation_list).click()
        time.sleep(2)
        self.driver.find_element(*self.ipt_nation_name).send_keys(nation)
        time.sleep(2)
        self.driver.find_element(*self.ck_nation_name).click()




