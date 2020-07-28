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
    ck_otc = (MobileBy.XPATH, "//android.widget.ImageView[@resource-id='com.hufu.qianbao:id/iv_otc']")  #点击进入法币
    ck_colse = (MobileBy.ID,'iv_close')


    # 出售
    switch_to_buy = (MobileBy.ID, "tv_buy")  # 切换到购买界面
    switch_to_sell = (MobileBy.ID, "tv_sell")  #切换到出售界面
    ipt_amount = (MobileBy.ID, "et_amount")  # 请输入出售/购买金额
    ck_buy = (MobileBy.XPATH, "//android.widget.RelativeLayout/android.support.v4.view.ViewPager[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]")  # 点击出售/购买
    ck_sell = (MobileBy.XPATH, "//*[@resource-id='com.hufu.qianbao:id/tv_buy' and @text='出售']")  # 点击出售/购买
    sell_payment_method = (MobileBy.ID, "tv_name")  # 出售收款方式
    buy_payment_method = (MobileBy.XPATH, "//*[@resource-id='com.hufu.qianbao:id/tv_name' and @text='支付宝']") #购买的支付方式
    # st_payment_method = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_name' and @index='1']")
    ck_confirm_sell = (MobileBy.ID, 'tv_buy')  # 确认出售/购买
    ipt_verify_code = (MobileBy.ID, 'tv_0')  # 输入交易密码


    def goto_otc_page(self):
        """进入otc页面"""
        time.sleep(10)
        self.driver.find_element(*self.ck_otc).click()
        time.sleep(2)

    def buy_business(self, coin,amount,pwd):
        """购买流程"""
        switch_to_coin = (MobileBy.XPATH, f"//android.widget.TextView[@text='{coin}']")
        self.driver.find_element(*switch_to_coin).click()
        self.driver.find_element(*self.ipt_amount).send_keys(amount)
        self.driver.find_element(*self.ck_buy).click()
        time.sleep(2)
        self.driver.find_element(*self.buy_payment_method).click()
        time.sleep(1)
        self.driver.find_element(*self.ck_confirm_sell).click()
        self.input_payment_pwd(pwd)
        self.driver.find_element(*self.ck_colse).click()

    def sell_business(self, coin,amount,pwd):
        """出售流程"""
        self.driver.find_element(*self.switch_to_sell).click()
        switch_to_coin = (MobileBy.XPATH, f"//android.widget.TextView[@text='{coin}']")
        self.driver.find_element(*switch_to_coin).click()
        self.driver.find_element(*self.ipt_amount).send_keys(amount)
        self.driver.find_element(*self.ck_sell).click()
        time.sleep(2)
        self.driver.find_element(*self.sell_payment_method).click()
        time.sleep(1)
        self.driver.find_element(*self.ck_confirm_sell).click()
        self.input_payment_pwd(pwd)

    def input_payment_pwd(self,pwd):
        """输入密码流程"""
        time.sleep(2)
        action_a = ActionChains(self.driver)
        action_a.move_to_element(self.driver.find_element(*self.ipt_verify_code)).click().send_keys(pwd).perform() #输入交易密码
