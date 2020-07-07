# coding:utf-8
# from PO.LoginRegisterPage.LoginPage import LoginPage
# from libs.ShareModules import Getdata
#
# #-------------------------------------------------------------------------------
# # 函数/过程名称：login_B
# # 函数/过程的目的：登录业务函数
# #-------------------------------------------------------------------------------
#
# email = Getdata('Login_tc', 'email')  # 邮箱地址
# pwd = Getdata('Login_tc', 'password')          # 密码
#
# def login_B(email='02575484@163.com',pwd='Abc123456'):
#     obj = LoginPage()
#     obj.open_url()
#     obj.login_operator(email, pwd)
#     obj.set_google_code()
#     return obj.driver  # 返回一个浏览器对象 create__browser_driver 模块下的driver
#
# if __name__ == "__main__":
#     login_B('02575484@163.com', 'Abc123456')
