from PO.Base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage(Base):
    """
    启动页+登录界面的页面元素
    """
    # ck_skip = (By.XPATH, "//android.widget.TextView[@text='跳过' and @index='1']") # 点击启动页跳过
    ck_skip = (By.ID, "com.hufu.qianbao:id/tv_skip") # 点击启动页跳过
    # ck_login_register_button = (By.XPATH, "//android.widget.TextView[@text='登录/注册' and @index='1']")  # 首页点击登录/注册按钮
    ck_login_register_button = (By.ID, "tv_login_register")  # 首页点击登录/注册按钮

    def getinto_login_page(self,text='跳过'):
        """进入登录页面"""
        time.sleep(2)
        print(self.findElement(text))
        text_loc = ("xpath", ".//*[contains(.,'%s')]" % text)
        self.driver.find_element(*text_loc).click()
        self.driver.find_element(*text_loc).click()
        # self.driver.find_element(*self.ck_skip).click()
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.ck_login_register_button, u"登录/注册"))
        self.driver.find_element(*self.ck_login_register_button).click()
        time.sleep(2)


    # 手机登录 # 邮箱登录
    switch_mode_email = (By.ID, "tv_email")  # 切换邮箱注册
    switch_mode_phone = (By.ID, "tv_phone")  # 切换手机注册
    ipt_mobile = (By.ID, "et_input_phone")  # 输入手机号码
    ipt_eamil = (By.ID, "et_input_email")  # 输入邮箱

    # 密码登录
    ipt_login_pwd = (By.ID, "et_input_pwd")  # 输入登录密码
    ck_pwd_display = (By.ID, "iv_pwd_on")  # 点击密码加密显示
    # 验证码登录
    switch_verify_login = (By.ID, "tv_change_verify")  # 切换验证码登录
    ck_verify_code = (By.ID, "tv_phonecode")  # 点击发送验证码
    ipt_code = (By.ID, "et_input_code")  # 输入验证码

    ck_login_btn = (By.ID, "bt_login")  # 点击登录
    ck_send_verify_code = (By.ID, "tv_miss_google_validation")  # 点击异常登录验证码
    ipt_verify_code = (By.ID, "tv_0")  # 输入异常登录验证码
    get_login_success_txt = (By.ID, "tv_enter")  # 登录成功后弹窗文本，前往安全中心

    # 忘记密码流程
    ck_Forgot_password = (By.ID, "tv_forget_pwd")  # 点击忘记密码
    ipt_login_comfirm_pwd = (By.ID, "et_input_pwd2")  # 再次输入登录密码


    def login_by_Email(self, email):
        """使用邮箱登录"""
        self.driver.find_element(*self.switch_mode_email).click()
        self.driver.find_element(*self.ipt_eamil).send_keys(email)

    def login_by_Mobile(self, mobile):
        """使用手机登录"""
        self.driver.find_element(*self.ipt_mobile).send_keys(mobile)

    def login_by_Mobile_verify(self, mobile,code):
        """使用手机验证码登录"""
        self.driver.find_element(*self.ipt_mobile).send_keys(mobile)
        self.driver.find_element(*self.switch_verify_login).click()
        self.driver.find_element(*self.ipt_code).send_keys(code)
        self.driver.find_element(*self.ck_login_btn).click()  # 点击登陆

    def input_loginpwd_in(self,pwd,code):
        """输入密码、点击登录"""
        self.driver.find_element(*self.ipt_login_pwd).send_keys(pwd) # 输入登陆密码
        self.driver.find_element(*self.ck_login_btn).click() #点击登陆
        self.driver.find_element(*self.ipt_verify_code).send_keys(code) #输入异常验证码

    def verify_login_success(self):
        """登登录成功后弹窗文本，前往安全中心"""
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.get_login_success_txt, u"前往安全中心"))
        return self.driver.find_element(*self.get_login_success_txt).text

    def business_forgot_password(self,code,pwd):
        """忘记密码流程"""

        self.driver.find_element(*self.ck_verify_code).click()
        self.driver.find_element(*self.ipt_code).send_keys(code)
        self.driver.find_element(*self.ck_login_btn).click()  # 点击登陆
        time.sleep(2)
        self.driver.find_element(*self.ipt_login_pwd).send_keys(pwd)
        self.driver.find_element(*self.ipt_login_comfirm_pwd).send_keys(pwd)
        self.driver.find_element(*self.ck_login_btn).click()
        return self.is_toast_exist('设置密码成功')

    def Email_Forgot_password(self,email,code,pwd):
        '''单邮箱忘记密码'''

        self.driver.find_element(*self.ck_Forgot_password).click()
        time.sleep(2)
        self.driver.find_element(*self.switch_mode_email).click()
        self.driver.find_element(*self.ipt_eamil).send_keys(email)
        self.business_forgot_password(code, pwd)

    def Mobile_Forgot_password(self,mobile,code,pwd):
        '''单手机忘记密码,默认方式'''

        self.driver.find_element(*self.ck_Forgot_password).click()
        time.sleep(2)
        self.driver.find_element(*self.ipt_mobile).send_keys(mobile)
        self.business_forgot_password(code, pwd)

