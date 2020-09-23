# @Author   : xiaoxie
from appium.webdriver.common.mobileby import MobileBy

class Myassets:
    """资产界面的页面元素"""

    ck_my_btn =(MobileBy.XPATH,"//android.widget.LinearLayout[@resource-id='com.hufu.qianbao:id/tabbar']/android.widget.RelativeLayout[5]") # 点击我的
    # 扫码、设置、资产记录
    ck_scan = (MobileBy.ID, "iv_property_scan")  # 点击扫码
    ck_setting = (MobileBy.ID, "iv_property_setting")  # 点击设置
    ck_assets_records = (MobileBy.ID, "iv_property_hd")  # 点击资产记录

    ck_btc_assets = (MobileBy.ID, "tv_tip_all_property") # 点击加密眼睛
    ck_assets_dist = (MobileBy.XPATH, "//android.widget.ImageView[@resource-id='com.hufu.qianbao:id/iv_arrow_right2']")  # 点击资产
    ipt_currency_search = (MobileBy.ID, "et_search")  # 输入查询的币种名称
    get_search_list =(MobileBy.ID, "tv_coin_default") # 获取查询的币种名称
    ck_small_amount= (MobileBy.ID, "tv_hide")  # 点击隐藏小额币种
    ck_small_amount_explain= (MobileBy.ID, "iv_hide")  # 隐藏小额币种说明
    ck_right= (MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_right']")  # 我知道了
    ck_spot_account = (MobileBy.XPATH, "//android.widget.TextView[@text='币币账户']")  # 切换币币账户
    ck_futures_account = (MobileBy.XPATH, "//android.widget.TextView[@text='合约账户']")  # 切换合约账户
    ck_otc_account = (MobileBy.XPATH, "//android.widget.TextView[@text='法币账户']")  # 切换法币账户
    ck_balance_account = (MobileBy.XPATH, "//android.widget.TextView[@text='钱包账户']")  # 切换钱包账户
    ck_symbol = (MobileBy.XPATH, "//*[@resource-id='com.hufu.qianbao:id/myRecycler']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]")  #点击第一个币种

    # 个人信息
    ck_user_info = (MobileBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.hufu.qianbao:id/ll_user_info']")  # 点击个人信息
    ck_user_icon = (MobileBy.XPATH, "//android.widget.ImageView[@resource-id='com.hufu.qianbao:id/iv_user_icon']")  # 点击头像
    # 上传头像图片
    add_img = (MobileBy.XPATH,"//android.support.v7.widget.RecyclerView[@resource-id='com.hufu.qianbao:id/picture_recycler']/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]")
    add_img_ok = (MobileBy.XPATH, "//*[@resource-id='com.hufu.qianbao:id/picture_tv_ok']")
    add_img_crop = (MobileBy.XPATH, "//*[@resource-id='com.hufu.qianbao:id/menu_crop']")

    ck_user_name = (MobileBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.hufu.qianbao:id/ll_username']")  # 点击昵称
    clean_user_name = (MobileBy.XPATH,"//android.widget.ImageView[@resource-id='com.hufu.qianbao:id/iv_reset']") #清除用户昵称
    ipt_user_name = (MobileBy.XPATH,"//android.widget.EditText[@resource-id='com.hufu.qianbao:id/et_modify_nickname']") #输入用户昵称
    ck_save = (MobileBy.XPATH,"//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_save']") #保存
    ck_user_id = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_user_id']")  # 复制用户id
    ck_shimin_name = (MobileBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.hufu.qianbao:id/ll_name']")  # 点击实名认证


