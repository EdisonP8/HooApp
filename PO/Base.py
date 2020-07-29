from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from HooApp.libs.ShareModules import Getdata
import os,time,allure
import random,string

class Base():
    """
    一些公共方法
    """

    def __init__(self, driver):
        self.driver = driver

    def findElement(self, el):
        """判断某元素是否存在"""

        source = self.driver.page_source  # 打印当前页面全部的元素
        if el in source:
            return True
        else:
            print('找不到该元素...')
            return False

    def Sys_back(self):
        """点击系统返回键"""

        self.driver.keyevent(4)

    def Sys_home(self):
        """点击系统home键"""

        self.driver.keyevent(3)

    def Sys_power(self):
        """点击power按键"""

        self.driver.keyevent(26)

    def get_size(self):
        """获取屏幕分辨率大小"""

        size = self.driver.get_window_size()
        print(size['width'], size['height'])
        return size['width'], size['height']

    def swipeUP(self, element):
        """滑动到顶部"""

        self.driver.find_element(*element).send_keys(Keys.UP)

    def swipeDown(self,element):
        """滑动到底部"""
        self.driver.find_element(*element).send_keys(Keys.DOWN)

    # 滚动到页面底部
    def move_to_baseOfWindow(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # 滚动到页面底部
    def move_to_topOfWindow(self):
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

    def touch_tap(self, x, y, duration=100):  # 点击坐标  ,x1,x2,y1,y2,duration
        '''点击坐标'''
        screen_width = self.driver.get_window_size()['width']  # 获取当前屏幕的宽
        screen_height = self.driver.get_window_size()['height']  # 获取当前屏幕的高
        a = (float(x) / screen_width) * screen_width
        x1 = int(a)
        b = (float(y) / screen_height) * screen_height
        y1 = int(b)
        self.driver.tap([(x1, y1), (x1, y1)], duration)

    def wait_element(self,element):
        """
        等待元素出现，默认等待10秒，0.5毫秒扫描一次
        :param element: 元素(部分或者全部元素内容)
        """

        get_error_msg = (MobileBy.CSS_SELECTOR, 'p.el-message__content')  # 提示语
        try:
            WebDriverWait(self.driver, 10, 0.5).until(
                EC.text_to_be_present_in_element(get_error_msg, element))
            return True
        except:
            return False

    def upload_img_path(picname):
        """上传文件的路径"""

        return os.path.abspath(os.path.dirname(os.getcwd())) + '/PO/AddCardPage/upload_img/' + '%s.png' % picname
    #
    def Beautiful_save_img(self, picname):
        """
        截图并保存
        :param picname:文件名
        :使用例子：self.obj.save_img('003_password_error')
        """
        # path = os.path.abspath(os.path.dirname(os.getcwd())) + '/Img/'
        path = Getdata('pictures', 'path')
        if not os.path.exists(path):
            os.mkdir(path)
        self.driver.get_screenshot_as_file(path + picname + '.png')

    def Allure_save_img(self, picname):
        """
        截图并保存
        :param filename:文件名
        :使用例子：self.usercenterPage.save_img('/hello')
        """

        path = Getdata('pictures', 'path')
        if not os.path.exists(path):
            os.mkdir(path)
        filename = path + picname + '.png'
        self.driver.get_screenshot_as_file(filename)
        file = open(filename, 'rb').read()
        allure.attach(file, picname, allure.attachment_type.PNG)

    def is_toast_exist(self, text):
        """
        定位toast提示语
        :param text: 提示语内容（全部）
        :param timeout: 多少秒后超时，不再监控
        :param poll_frequency: 监控间隔
        :return:
        """
        try:
            toast_loc = ("xpath", "//*[contains(@text,'%s')]" % text)

            WebDriverWait(self.driver, 10, 0.1).until(
                EC.presence_of_element_located(toast_loc))
            print(self.driver.find_element(MobileBy.XPATH,toast_loc).text)
            return True
        except:
            print('没有获取到toast信息')
            return False

    def click_text(self, text):
        """
        特殊点击法，点击一些只有text标识的元素
        :param text: 元素名称
        :return:
        """

        try:
            # text_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
            text_loc = ("xpath", f'//*[text()="{text}"]')
            self.driver.find_element(*text_loc).click()
        except:
            raise AttributeError('不存在该元素...')

    def send_keys_text(self,el,text):
        """
        特殊输入法，点击一些只有text标识的元素
        :param el: 元素名称
        :text: 输入内容
        :return:
        """

        try:
            text_loc = ("xpath", ".//*[contains(@text,'%s')]" % el)
            self.driver.find_element(*text_loc).send_keys(text)
        except:
            raise AttributeError('不存在该元素...')

    def clear_and_sendkeys(self, sendtexts, *loc):
        """
        先清除当前文本框内的文字再输入新的文字
        :param sendtexts:要输入的新的文字
        :return:None
        """
        webelement = self.driver.find_element(*loc)
        webelement.clear()
        webelement.send_keys(sendtexts)


    def action_chains_send_keys(self,element,text):
        """
        方法使用介绍：ActionChains创建鼠标事件,move_to_element鼠标移动到某个元素,click单击鼠标左键,
        send_keys发送某个键到当前焦点的元素,perform执行鼠标事件
        :param element: 查找的元素
        :param text: 需要输入的信息
        :return:
        """
        a = self.driver.find_element(element)
        action_a = ActionChains(self.driver)
        action_a.move_to_element(a).click().send_keys(text).perform()

    def switch_to_view(self, target='H5'):
        """
        切换app视窗 或 h5视窗
        :target:目标视窗（app/H5），默认切换到H5
        :return:
        """

        view_list = self.driver.contexts
        print('当前页面的webview元素有：', view_list)
        webview = [i for i in view_list if 'xwallet' in i]
        app = [a for a in view_list if 'APP' in a]

        if target == 'H5':
            self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": webview[0]})
        else:
            self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": app[0]})
        print(self.driver.current_context)
        time.sleep(2)

    def authority(self):
        """授予权限"""

        time.sleep(1)
        if self.findElement('Allow'):  # 权限询问弹窗
            self.driver.switch_to.alert.accept()  # 系统弹窗默认允许
        else:
            pass
        time.sleep(1)


    # -------------------------------随机生成数据部分,用于注册------------------------------- #

    def create_CH_mobile():
        """随机生成中国电话号码 """

        num = '0123456789'
        code = ['13', '15', '18', '19']  # 中国
        # code = ['4120', '4123', '4124']  # 委内瑞拉
        mobile = random.choice(code) + ''.join(random.choice(num) for i in range(9))  # 中国
        return mobile

    def create_VE_mobile():
        """随机生成委内瑞拉电话号码 """

        num = '0123456789'
        code = ['4120', '4123', '4124']  # 委内瑞拉
        mobile = random.choice(code) + ''.join(random.choice(num) for i in range(7))  # 委内瑞拉
        return mobile

    def create_email():
        """随机生成邮箱地址"""

        num = '0123456789'
        server = '@qq.com', '@163.com'  # 邮箱域名
        email = ''.join(random.choice(num) for i in range(8)) + random.choice(server)
        return email

    def create_address(size=8, chars=string.digits + string.ascii_letters + string.digits):
        """
        随机生成字符串（字母+数字）
        :param size: 随机生产字符串的长度
        :param chars: 字符串范围（字母+数字)
        :return:
        """

        return ''.join(random.choice(chars) for _ in range(size))

    def create_string(size=8, chars=string.ascii_letters):
        """ 随机字符串 """

        return ''.join(random.choice(chars) for _ in range(size))


if __name__ == '__main__':

    print(Base.create_email(),Base.create_VE_mobile())