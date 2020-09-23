
from appium.webdriver.common.mobileby import MobileBy

class LoginRegisterLocators:
    '''登录界面'''

    # 引导页
    ck_skip = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/tv_skip']")  # 点击启动页跳过
    # 手机号输入框
    input_phone = (MobileBy.XPATH, "//android.widget.EditText[@resource-id='com.hufu.qianbao:id/et_input_phone']")
    # 密码输入框
    input_pwd = (MobileBy.XPATH, "//android.widget.EditText[@resource-id='com.hufu.qianbao:id/et_input_pwd']")
    # “登录”按钮
    bt_login = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.hufu.qianbao:id/bt_login']")

    # 手机登录 # 邮箱登录
    switch_mode_email = (MobileBy.ID, "tv_email")  # 切换邮箱登录
    switch_mode_phone = (MobileBy.ID, "tv_phone")  # 切换手机登录
    ipt_mobile = (MobileBy.ID, "et_input_phone")  # 输入手机号码
    ipt_eamil = (MobileBy.ID, "et_input_email")  # 输入邮箱
    switch_area = (MobileBy.XPATH, "//*[@resource-id='com.hufu.qianbao:id/tv_area']")  # 登录页面切换国家
    ck_pwd_on = (MobileBy.XPATH, "//*[@resource-id='com.hufu.qianbao:id/iv_pwd_on']")  # 显示登录密码
    ck_pwd_off = (MobileBy.XPATH, "//*[@resource-id='com.hufu.qianbao:id/iv_pwd_off']") # 关闭密码显示

    # 验证码登录
    switch_verify_login = (MobileBy.ID, "tv_change_verify")  # 切换验证码登录
    ck_verify_code = (MobileBy.ID, "tv_phonecode")  # 点击发送验证码
    ipt_code = (MobileBy.ID, "et_input_code")  # 输入验证码

    ipt_verify_code = (MobileBy.ID, 'tv_0')  # 输入异常登录验证码
    get_login_success_txt = (MobileBy.ID, "tv_enter")  # 登录成功后弹窗文本，前往安全中心

    # 忘记密码流程
    ck_Forgot_password = (MobileBy.ID, "tv_forget_pwd")  # 点击忘记密码
    ipt_login_comfirm_pwd = (MobileBy.ID, "et_input_pwd2")  # 再次输入登录密码

    # 切换语言
    tv_language = (MobileBy.XPATH, "//*[@resource-id='com.hufu.qianbao:id/tv_language']")
    # 选择语言 //android.widget.TextView[@text='简体中文']
    def select_language(self, language):
        """ language: 简体中文,English,繁體中文,한국어  """
        return (MobileBy.XPATH, "//android.widget.TextView[@text='" + language + "']")

    # 立即注册
    ck_register_btn = (MobileBy.XPATH, "//android.widget.TextView[@text='立即注册']")
    ck_invite_code = (MobileBy.XPATH, "//android.widget.TextView[@text='立即填写']")  # 点击立即填写邀请码
    ipt_invite_code = (MobileBy.ID, "et_input_invite")  # 输入邀请码
    ck_skip_setp = (MobileBy.XPATH, "//android.widget.TextView[@text='跳过此步骤']")  # 点击跳过此步骤
    # 切换国家
    select_nation_list = (MobileBy.XPATH, "//*[@resource-id='com.hufu.qianbao:id/tv_area']")  # 国家下拉框
    ipt_nation_name = (MobileBy.ID, "et_search")  # 输入查询的国家名称
    ck_nation_name = (MobileBy.ID, "tv_name")  # 选择对应的国家，默认第一个
    get_register_success_txt = (MobileBy.ID, "tv_enter")  # 登录成功后弹窗文本，前往安全中心
    swipe_loc = (MobileBy.XPATH,"//android.view.ViewGroup[@resource-id='com.hufu.qianbao:id/refreshLayout']") #国家列表界面滑动区域