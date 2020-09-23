
from appium.webdriver.common.mobileby import MobileBy

class HomePageLocators:
    '''首页界面'''

    # 首页登录注册按钮
    login_register_btn = (MobileBy.XPATH, "//android.widget.TextView[@text='登录/注册']")
    # 欢迎回来按钮
    welcome_btn = (MobileBy.XPATH, "//android.widget.TextView[@text='欢迎回来']")
    # 确认退出
    confirm_btn = (MobileBy.ID, "tv_right")
    # 取消退出
    cancel_btn = (MobileBy.ID, 'tv_left')

    # 法币按钮
    otc_btn = (MobileBy.XPATH, "//android.widget.ImageView[@resource-id='com.hufu.qianbao:id/iv_otc']")
    # 关闭小程序
    iv_close = (MobileBy.XPATH, "//android.widget.ImageView[@resource-id='com.hufu.qianbao:id/iv_close']")
    # 共管钱包按钮
    comanagement_btn = (MobileBy.XPATH, "//android.widget.TextView[@text='共管钱包']/..")
