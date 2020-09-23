import pytest
from HooApp.PageObject.MyPage.my_assets import my_assets as My

@pytest.mark.usefixtures('is_logined')
class TestMyassets:
    """我的页面、修个个人信息"""

    # 余额切换到币币
    def test_Balance_Switch_Spot(self,is_logined):
        My(is_logined).ck_my_page()
        My(is_logined).switch_to_spot()
        assert My(is_logined).find_element("币币账户")
        My(is_logined).sys_back()

    # 币币切换到合约
    def test_Spot_Switch_Futures(self, is_logined):
        My(is_logined).ck_my_page()
        My(is_logined).switch_to_futures()
        assert My(is_logined).find_element("合约账户资产(BTC)" or "账户权益")

    # 合约切换到法币
    def test_Futures_Switch_OTC(self, is_logined):
        My(is_logined).ck_my_page()
        My(is_logined).switch_to_otc()
        assert My(is_logined).find_element("法币账户")
        My(is_logined).sys_back()

    # 法币切换到余额
    def test_OTC_Switch_Balance(self, is_logined):
        My(is_logined).ck_my_page()
        My(is_logined).switch_to_spot()
        assert My(is_logined).find_element("钱包账户")
        My(is_logined).sys_back()

    # 扫码界面
    def test_Click_Myassets_Scan(self, is_logined):
        My(is_logined).ck_my_page()
        My(is_logined).Myassets_setting()
        assert My(is_logined).find_element("手电" or "相册")
        My(is_logined).sys_back()

    # 资产记录
    def test_Click_Myassets_Records(self, is_logined):
        My(is_logined).ck_my_page()
        My(is_logined).Myassets_records()
        assert My(is_logined).find_element("充值记录" or "提现记录")
        My(is_logined).sys_back()

    # 隐藏小额币种功能
    def test_Click_Small_Amount(self, is_logined):
        My(is_logined).ck_my_page()
        assert My(is_logined).small_amount_and_explain()

    # 个人信息--更新头像
    def test_User_Update_head(self, is_logined):
        My(is_logined).ck_my_page()
        My(is_logined).switch_user_info()
        My(is_logined).upload_head_img()
        assert My(is_logined).find_element("修改成功")
        My(is_logined).sys_back()

    # 个人信息--修改昵称、复制用户id
    def test_User_Update_name(self, is_logined):
        My(is_logined).ck_my_page()
        My(is_logined).switch_user_info()
        My(is_logined).update_user_name("币圈小喽啰")
        assert My(is_logined).find_element("修改成功")
        My(is_logined).copy_user_id()
        assert My(is_logined).find_element("复制ID成功")
        My(is_logined).sys_back()

    # 个人信息--实名认证
    def test_User_Kyc_verify(self, is_logined):
        My(is_logined).ck_my_page()
        My(is_logined).switch_user_info()
        My(is_logined).Kyc_verify()
        assert My(is_logined).find_element("您已完成实名认证" or "实名认证已通过")
        My(is_logined).sys_back()
        My(is_logined).sys_back()