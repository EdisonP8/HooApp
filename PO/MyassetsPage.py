from HooApp.PO.Base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Myassets(Base):
    """
    资产界面的页面元素
    """
    ck_assets_icon = (By.XPATH, "//android.widget.FrameLayout/android.widget.RelativeLayout[5]") # 点击我的
    ck_btc_assets = (By.ID, "tv_tip_all_property") # 点击加密眼睛
    ck_assets_dist = (By.ID, "v_1")  # 点击进入资产分布
    ipt_currency_search = (By.ID, "et_search")  # 输入查询的币种名称
    get_search_list =(By.ID, "tv_coin_default") # 获取查询的币种名称
    ck_small_amount= (By.ID, "tv_hide")  # 点击隐藏小额币种
    ck_spot_account = (By.XPATH, "//android.widget.TextView[@text='币币']")  # 切换币币账户
    ck_futures_account = (By.XPATH, "//android.widget.TextView[@text='合约账户']")  # 切换合约账户
    ck_otc_account = (By.XPATH, "//android.widget.TextView[@text='法币账户']")  # 切换法币账户
    ck_balance_account = (By.XPATH, "//android.widget.TextView[@text='钱包账户']")  # 切换钱包账户
    ck_symbol = (By.ID, '')  #点击第一个币种
    get_account_txt = (By.ID, "tv_tip1")  # 切换不同账户后，获取对应的文本

    #扫码、设置
    ck_scan = (By.ID, "iv_property_scan")  # 点击扫码
    ck_setting = (By.ID, "iv_property_setting")  # 点击设置
    get_page_title = (By.ID, "tv_title")  # 获取界面的标题

    # 充值
    ck_receive = (By.ID, "tv_receive") # 点击充值
    get_currency_name = (By.ID, "tv_bit_name")  # 获取币种名称
    get_receive_txt = (By.XPATH, "//android.widget.TextView[@text='扫描二维码进行充值']")  # 扫描二维码进行充值

    # 提现
    ck_withdrawal = (By.ID, "tv_send")  # 点击提现
    ipt_address =(By.ID, "et_address") # 输入提现地址
    ck_address_list =(By.ID, "iv_address") # 点击地址簿
    ck_go_scan = (By.ID, "iv_scan")  # 点击扫码
    ipt_conut =(By.ID, "et_count") # 输入提现数量
    ck_all_conut =(By.ID, "tv_all") # 点击全部数量
    ipt_memo =(By.ID, "et_memo") # 输入memo
    ipt_msg =(By.ID, "et_msg") # 输入附言
    ck_next_step =(By.ID, "tv_next_step") # 下一步
    ck_send_code = (By.ID, 'tv_send_phone_code') #发送验证码
    ipt_veritfy_code = (By.ID, 'et_phone_code') # 输入验证码
    ipt_transaction_pwd = (By.ID, 'et_pwd') # 输入资金密码
    ck_confirm = (By.ID, 'tv_confirm') # 点击确认

    # 划转
    ck_transfer = (By.ID, "tv_transfer") # 点击划转
    switch_icon = (By.XPATH, "//android.widget.RelativeLayout[@index='1']") # 点击切换币种
    switch_account = (By.ID, "iv_switch") # 点击切换账户
    ipt_transfer_amount = (By.ID, "et_amount") # 点击输入金额
    ck_all_amount = (By.ID, "tv_send_all_2") # 点击全部金额
    ck_confirm_transfer = (By.ID, "tv_ok") # 点击划转

    # 资产记录
    ck_asset_records = (By.ID, "iv_property_hd")  # 点击进入资产记录
    switch_withdrawal_records = (By.XPATH, "//android.widget.TextView[@text='提现记录']")  # 切换到提现记录
    switch_asset_records = (By.XPATH, "//android.widget.TextView[@text='充值记录']")  # 切换到充值记录

    def getinto_Myassets_page(self):
        """进入我的资产"""

        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.ck_assets_icon, u"我"))
        self.driver.find_element(*self.ck_assets_icon).click()
        time.sleep(2)

    def Myassets_scan(self):
        """扫码"""

        self.driver.find_element(*self.ck_scan).click()
        time.sleep(2)
        return self.driver.find_element(*self.get_page_title).text()

    def Myassets_setting(self):
        """设置"""

        self.driver.find_element(*self.ck_setting).click()
        time.sleep(2)
        return self.driver.find_element(*self.get_page_title).text()

    def Myassets_records(self):
        """资产记录"""

        self.driver.find_element(*self.ck_asset_records).click()
        time.sleep(2)
        self.driver.find_element(*self.switch_withdrawal_records).click()
        return self.driver.find_element(*self.get_page_title).text()

    def input_currency_name(self,symbol):
        """选择需要的币种"""

        self.driver.find_element(*self.ipt_currency_search).send_keys(symbol)
        self.driver.find_element(*self.get_search_list).click()
        time.sleep(2)

    def Assets_receive(self, symbol):
        """充值"""

        self.driver.find_element(*self.ck_receive).click()
        time.sleep(2)
        self.input_currency_name(symbol)
        return self.driver.find_element(*self.get_receive_txt).text()

    def Assets_transfer(self,symbol,amount):
        """资产划转"""

        self.driver.find_element(*self.ck_transfer).click()
        time.sleep(1)
        self.driver.find_element(*self.switch_icon).click()
        time.sleep(1)
        self.input_currency_name(symbol)
        self.driver.find_element(*self.ipt_transfer_amount).send_keys(amount)
        self.driver.find_element(*self.ck_confirm_transfer).click()
        time.sleep(2)
        return self.driver.find_element(*self.get_page_title).text()

    def Assets_withdrawal(self,symbol,address,quantity,code,Transaction_pwd):
        """提现"""

        self.driver.find_element(*self.ck_withdrawal).click()
        time.sleep(1)
        self.input_currency_name(symbol)
        self.driver.find_element(*self.ipt_address).send_keys(address)
        self.driver.find_element(*self.ipt_conut).send_keys(quantity)
        time.sleep(2)
        self.driver.find_element(*self.ck_next_step).click()
        self.driver.find_element(*self.ipt_veritfy_code).send_keys(code)
        self.driver.find_element(*self.ipt_transaction_pwd).send_keys(Transaction_pwd)
        self.driver.find_element(*self.ck_confirm).click()

    def switch_to_spot(self):
        '''切换到币币账户'''
        self.driver.find_element(*self.ck_spot_account).click()
        time.sleep(1)
        self.driver.find_element(*self.ck_symbol).click()
        return self.driver.find_element(*self.get_page_title).text()

    def switch_to_otc(self):
        '''切换到法币账户'''
        self.driver.find_element(*self.ck_otc_account).click()
        time.sleep(1)
        self.driver.find_element(*self.ck_symbol).click()
        return self.driver.find_element(*self.get_page_title).text()

    def switch_to_futures(self):
        '''切换到合约账户'''
        self.driver.find_element(*self.ck_futures_account).click()
        time.sleep(1)
        return self.driver.find_element(*self.get_account_txt).text()

    def switch_to_balance(self):
        '''切换到钱包账户'''
        self.driver.find_element(*self.ck_balance_account).click()
        time.sleep(1)
        self.driver.find_element(*self.ck_symbol).click()
        return self.driver.find_element(*self.get_page_title).text()

