import zmail,time
from HooApp.Common.Run_Report import Allure_RunReport
from HooApp.Common.read_config import *

dd = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

# 获取报告文件绝对地址
def get_file():
    filepath = os.path.join(test_report_path, r'Allre\html')  # 获取报告文件夹路径
    print(f'输出的测试报告路径为：{filepath}')
    f = os.listdir(filepath)
    print(f)
    file = filepath + "\html\index.html"
    if file in f:
        file = filepath + "\html\index.html"
    else:
        print('开始产生测试报告...')
        file = Allure_RunReport()
    return file

# 读取邮箱数据
email = ReadConfig(config_file_path, 'EmailSetting', 'email')   # 邮箱地址
password = ReadConfig(config_file_path, 'EmailSetting', 'password')    # 客户端授权密码
receivers = ReadConfig(config_file_path, 'EmailSetting', 'receivers')  # 获取接收邮件人
try:
    # 获取邮件内容 --> 使用账号和密码登陆邮箱 --> 发送邮件
    mail_content = {'subject': '%s 自动化测试报告' % dd, 'attachments': get_file()}   # 邮件内容
    sendmail = zmail.server(email, password).send_mail(receivers.split(','), mail_content)
    print('结果反馈: 邮件发送成功 %s ' % dd)
except Exception:
    print('结果反馈: 无法发送邮件 %s' % dd)