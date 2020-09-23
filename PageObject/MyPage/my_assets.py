# @Author   : xiaoxie

from HooApp.Common.base_page import BasePage
from HooApp.PageLoact.MyassetsPage import Myassets

class my_assets(BasePage):

    def ck_my_page(self):
        name = "进入我的页面"
        self.wait_ele_visible(Myassets.ck_my_btn, doc=name)
        self.click_element(Myassets.ck_my_btn, doc=name)  # 点击 我

    def Myassets_scan(self):
        name = "扫码"
        self.wait_ele_visible(Myassets.ck_scan, doc=name)
        self.click_element(Myassets.ck_scan, doc=name)

    def Myassets_setting(self):
        name = "设置"
        self.wait_ele_visible(Myassets.ck_setting, doc=name)
        self.click_element(Myassets.ck_setting, doc=name)

    def Myassets_records(self):
        name = "资产记录"
        self.wait_ele_visible(Myassets.ck_assets_records, doc=name)
        self.click_element(Myassets.ck_assets_records, doc=name)

    def small_amount_and_explain(self):
        name = "小额币种、说明"
        self.wait_ele_visible(Myassets.ck_small_amount, doc=name)
        self.click_element(Myassets.ck_small_amount, doc=name)
        self.wait_ele_visible(Myassets.ck_small_amount_explain, doc=name)
        self.click_element(Myassets.ck_small_amount_explain, doc=name)
        msg = self.find_element("小额币种")
        self.wait_ele_visible(Myassets.ck_right, doc=name)
        self.click_element(Myassets.ck_right, doc=name)
        return msg

    def switch_to_spot(self):
        name = "切换到币币账户"
        self.wait_ele_visible(Myassets.ck_spot_account, doc=name)
        self.click_element(Myassets.ck_spot_account, doc=name)
        self.wait_ele_visible(Myassets.ck_symbol, doc=name)
        self.click_element(Myassets.ck_symbol, doc=name)

    def switch_to_otc(self):
        name = "切换到法币账户"
        self.wait_ele_visible(Myassets.ck_otc_account, doc=name)
        self.click_element(Myassets.ck_otc_account, doc=name)
        self.wait_ele_visible(Myassets.ck_symbol, doc=name)
        self.click_element(Myassets.ck_symbol, doc=name)

    def switch_to_futures(self):
        name = "切换到合约账户"
        self.wait_ele_visible(Myassets.ck_futures_account, doc=name)
        self.click_element(Myassets.ck_futures_account, doc=name)

    def switch_to_balance(self):
        name = "切换到钱包账户"
        self.wait_ele_visible(Myassets.ck_balance_account, doc=name)
        self.click_element(Myassets.ck_balance_account, doc=name)
        self.wait_ele_visible(Myassets.ck_symbol, doc=name)
        self.click_element(Myassets.ck_symbol, doc=name)

    def switch_user_info(self):
        name = "切换到个人信息界面"
        self.wait_ele_visible(Myassets.ck_user_info, doc=name)
        self.click_element(Myassets.ck_user_info, doc=name)

    def upload_head_img(self):
        name = "上传头像"
        self.click_element(Myassets.ck_user_icon, doc=name)
        self.wait_ele_visible(Myassets.add_img, doc=name)
        self.click_element(Myassets.add_img, doc=name)
        self.click_element(Myassets.add_img_ok, doc=name)
        self.wait_ele_visible(Myassets.add_img_crop, doc=name)
        self.click_element(Myassets.add_img_crop, doc=name)

    def update_user_name(self, user_name):
        name = "修改昵称"
        self.wait_ele_visible(Myassets.ck_user_name, doc=name)
        self.click_element(Myassets.ck_user_name, doc=name)
        self.wait_ele_visible(Myassets.clean_user_name, doc=name)
        self.click_element(Myassets.clean_user_name, doc=name)
        self.input_text(Myassets.ipt_user_name, user_name, doc=name)
        self.click_element(Myassets.ck_save, doc=name)

    def copy_user_id(self):
        name = "复制用户id"
        self.wait_ele_visible(Myassets.ck_user_id, doc=name)
        self.click_element(Myassets.ck_user_id, doc=name)

    def Kyc_verify(self):
        name = "实名认证"
        self.wait_ele_visible(Myassets.ck_shimin_name, doc=name)
        self.click_element(Myassets.ck_shimin_name, doc=name)