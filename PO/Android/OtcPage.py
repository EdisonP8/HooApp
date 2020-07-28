from HooApp.PO.Base import Base
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

class OTCPage(Base):
    """
    法币页面元素
    """
    ck_skip = (MobileBy.ID, "tv_skip") # 点击启动页跳过
    # ck_otc = (MobileBy.CSS_SELECTOR, ".textContains(\'我要买\')")  # 首页点击登录/注册按钮
    ck_otc = (MobileBy.XPATH, "//android.widget.ImageView[@resource-id='com.hufu.qianbao:id/iv_otc']")  # 首页点击登录/注册按钮
    ck_diefu = (MobileBy.ID,'tv_diefu')


    # 出售//android.widget.TextView[@text='币币']"
    ck_sell = (MobileBy.ID, "tv_sell")
    ipt_sell = (MobileBy.ID, "amount")
    ck_buy = (MobileBy.ID, "tv_buy")
    ck_shoukuan = (MobileBy.ID, "tv_name")
    ipt_verify_code = (MobileBy.ID, 'tv_0')  # 输入异常登录验证码
    #
    def getinto_login_page(self):
        """进入otc页面"""
        time.sleep(10)
        self.driver.find_element(*self.ck_otc).click()
        # self.driver.find_element(*self.ck_diefu).click()
        # self.driver.top_click_tap()
        time.sleep(2)

    def login_by_Email(self, amount):
        """出售流程"""
        self.driver.find_element(*self.ck_sell).click()
        self.driver.find_element(*self.ipt_sell).send_keys(amount)
        self.driver.find_element(*self.ck_buy).click()
        self.driver.find_element(*self.ck_shoukuan).click()
        self.driver.find_element(*self.ck_buy).click()

    def input_loginpwd_in(self,pwd):
        """输入密码流程"""
        action_a = ActionChains(self.driver)
        action_a.move_to_element(self.driver.find_element(*self.ipt_verify_code)).click().send_keys(pwd).perform() #输入异常验证码
