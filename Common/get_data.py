
from HooApp.Common.read_config import ReadConfig,config_file_path

class GetData:

    # 获取log前的文字
    def get_info_for_log(self):
        return ReadConfig(config_file_path, 'basic_info', 'Info')

    # 获取URL
    def get_host_url(self):
        return ReadConfig(config_file_path, 'basic_info', 'HostURL')

    # 获取登录的手机号
    def get_login_tel(self):
        return ReadConfig(config_file_path, 'basic_info', 'LoginTel')

    # 获取登录邮箱
    def get_login_email(self):
        return ReadConfig(config_file_path, 'basic_info', 'LoginEmail')

    # 获取登录密码
    def get_login_pwd(self):
        return ReadConfig(config_file_path, 'basic_info', 'LoginPwd')

    # 获取交易密码
    def get_trade_pwd(self):
        return ReadConfig(config_file_path, 'basic_info', 'TradePwd')

    # 获取验证码
    def get_vcode(self):
        return ReadConfig(config_file_path, 'basic_info', 'vcode')

    # 获取证件号后四位
    def get_Id_number(self):
        return ReadConfig(config_file_path, 'basic_info', 'IdNumber')

    # 获取提现地址
    def get_withdraw_address(self):
        return ReadConfig(config_file_path, 'basic_info', 'withdraw_address')
