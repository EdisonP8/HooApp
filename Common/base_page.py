from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.mobileby import MobileBy
import random, string,time,allure
from datetime import datetime
from HooApp.Common.read_config import *

class BasePage():
    '''页面操作基础方法类'''

    def __init__(self, driver):
        self.driver = driver

    # 手机键盘缩回
    def sys_hide_keyboard(self):
        self.driver.hide_keyboard()

    # 手机键盘返回
    def sys_back(self):
        self.driver.back()

    # 判断元素是否存在当前页面
    def find_element(self, el):
        time.sleep(2)
        source = self.driver.page_source  # 打印当前页面全部的元素
        if el in source:
            return True
        else:
            print('页面不存在此元素.....')
            return False

    # 截屏
    def save_screenshot(self, doc):
        MyLog().info("截取屏幕")
        # 图片名称:模块名_页面名_操作名_时间.png
        # file_name = screenshot_path + f"\\{datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')}_{doc}.png"
        file_name = screenshot_path + f"\\{datetime.strftime(datetime.now(), '%m%d%H%M')}_{doc}.png"
        self.driver.save_screenshot(file_name)
        with open(file_name, mode='rb') as f:
            file = f.read()
        # 截图添加为allure报告的附件
        allure.attach(file, doc, allure.attachment_type.PNG)
        MyLog().info("截取屏幕完成，存放地址在{}".format(file_name))

    # 等待元素可见
    def wait_ele_visible(self, locator, doc="", times=30, poll_frequency=0.5):
        """
        :param locator: 元素定位表达式
        :param doc: 操作的模块名_页面名_操作名（用于异常时截图存储的截图图片名称）
        :param times:等待时间
        :param poll_frequency:轮询间隔时间
        """
        MyLog().info(f'等待元素{locator}可见')
        try:
            start_time = datetime.now() # 等待开始时间
            WebDriverWait(self.driver, times, poll_frequency).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            MyLog().info('等待元素失败.....')
            self.save_screenshot(doc) # 截图
            raise e
        end_time = datetime.now()  # 等待结束时间
        MyLog().info(f"等待结束，等待时长为: {(end_time - start_time).seconds}秒") # 求等待的差值,等待了多久

    # 元素是否可见，可见时返回True，不可见时返回False
    def is_ele_visible(self, locator, doc="", times=30, poll_frequency=0.5):
        """传参说明参考-->wait_ele_visible"""
        MyLog().info(f'等待元素{locator}可见')
        try:
            WebDriverWait(self.driver, times, poll_frequency).until(EC.visibility_of_element_located(locator))
            return True
        except Exception as e:
            self.save_screenshot(doc) # 截图
            MyLog().info(e)
            return False

    # 等待元素可点击
    def wait_element_to_be_click(self, loc, img_doc, timeout=20, frequency=0.5):
        '''
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        '''
        try:
            MyLog.info("开始等待页面元素<{}>是否可点击！".format(loc))
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.element_to_be_clickable(loc))
        except Exception as e:
            MyLog.error("页面元素<{}>等待可点击失败！".format(loc))
            self.save_screenshot(img_doc)
            raise e
        else:
            end_time = time.time()
            MyLog.info("页面元素<{}>等待可点击，等待时间: {}秒".format(loc, round(end_time - start_time, 2)))

    # 等待元素存在
    def wait_ele_exist(self, locator, doc="", times=30, poll_frequency=0.5):
        """传参说明参考-->wait_ele_visible"""
        MyLog().info('等待元素{}存在'.format(locator))
        try:
            start_time = datetime.now()   # 开始等待时间
            WebDriverWait(self.driver, times, poll_frequency).until(EC.presence_of_element_located(locator))
            # 结束等待时间
            end_time = datetime.now()  # 等待结束时间
            MyLog().info(f"等待结束，等待时长为: {(end_time - start_time).seconds}秒")  # 求等待的差值,等待了多久
        except:
            MyLog().info('等待元素失败.........')
            # 截图
            self.save_screenshot(doc)
            raise

    # 查找元素
    def get_element(self, locator, doc=""):
        MyLog().info('查找元素{}'.format(locator))
        try:
            time.sleep(2)
            ele = self.driver.find_element(*locator)
            # 返回元素对象，以便进行后续操作
            return ele
        except Exception as e:
            MyLog().info('查找元素失败........')
            self.save_screenshot(doc)
            raise e

    # 查找多个元素
    def get_elements(self, locator, doc=""):
        MyLog().info('查找元素{}'.format(locator))
        try:
            eles = self.driver.find_elements(*locator)
            return eles
        except:
            MyLog().info('查找元素失败........')
            self.save_screenshot(doc)  # 截图
            raise

    # 输入内容
    def input_text(self, locator, text, doc=""):
        # 先找到元素
        ele = self.get_element(locator, doc)
        MyLog().info('向元素{}输入文本: {}'.format(locator, text))
        try:
            ele.send_keys(text)
        except:
            MyLog().info('输入文本失败........')
            self.save_screenshot(doc)
            raise

    # 点击元素
    def click_element(self, locator, doc=""):
        # 先找到元素
        ele = self.get_element(locator, doc)
        MyLog().info('点击元素{}'.format(locator))
        try:
            ele.click()
        except:
            MyLog().info('点击元素失败........')
            self.save_screenshot(doc)
            raise

    # 定位表达式指向多个元素，输入点击的元素索引
    def click_elements(self, locator, index=0, doc=''):
        eles = self.get_elements(locator, doc)
        try:
            eles[index].click()
            MyLog().info('点击元素{}'.format(locator))
        except:
            MyLog().info('点击元素失败........')
            self.save_screenshot(doc)
            raise

    # 获取元素文本
    def get_text(self, locator, doc=""):
        # 先找到元素
        ele = self.get_element(locator, doc)
        MyLog().info('获取元素{}的文本内容'.format(locator))
        try:
            return ele.text
        except:
            MyLog().info('获取元素文本失败........')
            self.save_screenshot(doc)
            raise

    # 清空元素文本
    def clear_loc_text(self, locator, doc=""):
        ele = self.get_element(locator, doc)
        MyLog().info('清除元素{}的文本内容'.format(locator))
        try:
            ele.clear()
        except:
            MyLog().info('清除元素文本失败........')
            self.save_screenshot(doc)
            raise

    # 获取元素属性
    def get_ele_attribute(self, locator, attr, doc=""):
        # 先找到元素
        ele = self.get_element(locator, doc)
        MyLog().info('获取元素{}的属性'.format(locator))
        try:
            return ele.get_attribute(attr)
        except:
            MyLog.info('获取元素属性失败........')
            self.save_screenshot(doc)
            raise

    def get_element_text(self, loc, img_doc, timeout=20, poll_frequency=0.5):
        '''
        获取WebElement对象的文本值
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return: WebElement对象的文本值
        '''
        try:
            MyLog.info("在{}中获取元素<{}>的文本值".format(img_doc, loc))
            self.wait_ele_visible(loc, img_doc, timeout, poll_frequency)
            text = self.get_element(loc, img_doc).text
        except Exception as e:
            MyLog.error("在{}中获取元素<{}>的文本值失败！".format(img_doc, loc))
            self.save_screenshot(img_doc)
            raise e
        else:
            MyLog.info("获取到的元素文本值为：{}".format(text))
            return text

    def get_elements_text(self, loc, doc="", timeout=20, poll_frequency=0.5):
        '''
        获取WebElement对象的所有文本值
        :param loc: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return: WebElement对象的文本值的列表
        '''
        try:
            MyLog.info("在{}中获取元素<{}>的所有文本值".format(doc, loc))
            self.wait_ele_visible(loc, doc, timeout, poll_frequency)
            all_text = self.get_elements(loc, doc)
            text_list = []
            for one_text in all_text:
                text_list.append(one_text.text)
        except Exception as e:
            MyLog.error("在{}中获取元素<{}>的所有文本值失败！".format(doc, loc))
            self.save_screenshot(doc)
            raise e
        else:
            MyLog.info("获取到的元素文本值列表为：{}".format(text_list))
            return text_list

    # 鼠标操作(鼠标悬浮某元素)
    def move_to_over(self, locator):
        # 1、找到要操作的元素-->2、实例化ActionChains-->3、将要操作的元素添加到actions列表中-->4、调用perform来操作
       ActionChains(self.driver).move_to_element(locator).perform()

    '''页面滚动操作'''

    def my_srcoll(self):
        # self.driver.swipe(400,1500,400,0)

        i = 100
        while i > 0:
            # 获取滑动前页面元素
            before_swipe = self.driver.page_source
            # 滑动
            self.driver.swipe(400, 100, 400, 0)
            # 获取滑动后页面元素
            after_swipe = self.driver.page_source
            # 对比滑动前后的页面元素
            if before_swipe != after_swipe:
                # 若滑动前后页面元素不相同，继续滑动
                self.driver.swipe(400, 100, 400, 0)
                i += 1
                continue
            else:
                break

    def srcoll_to_find_ele(self, locator):
        ele = self.get_element(locator, doc="获取滑动前的元素")
        if not ele:
            i = 10
            while i > 0:
                self.driver.swipe(400, 100, 400, 20)
                # 获取滑动后页面元素
                ele = self.get_element(locator, doc="获取滑动后的元素")
                # 对比滑动前后的页面元素
                if not ele:
                    # 若滑动前后页面元素不相同，继续滑动
                    self.driver.swipe(400, 100, 400, 20)
                    i += 1
                    continue
                else:
                    break

    # 滚动元素“底端”与当前窗口的“底部”对齐
    def move_ele_to_baseOfWindow(self, locator, doc=''):
        ele = self.get_element(locator, doc)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", ele)

    # 滚动元素“底端”与当前窗口的“顶部”对齐
    def move_ele_to_topOfWindow(self, locator, doc=''):
        ele = self.get_element(locator, doc)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)

    # 滚动到页面底部
    def move_to_baseOfWindow(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # 滚动到页面顶部
    def move_to_topOfWindow(self):
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")

    # 页面定位到要查看的元素
    def move_to_element(self, locator):
        ele = self.driver.find_element(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    '''弹窗处理'''
    def accept_alert(self, times=30, poll_frequency=0.5, doc=''):
        try:
            WebDriverWait(self.driver, times, poll_frequency).until(EC.alert_is_present())
            self.driver.switch_to_alert.accept()
        except:
            MyLog.info('弹窗不存在........')
            self.save_screenshot(doc)
            raise

    def dismiss_alert(self, times=30, poll_frequency=0.5, doc=''):
        try:
            WebDriverWait(self.driver, times, poll_frequency).until(EC.alert_is_present())
            self.driver.switch_to_alert.dismiss()
        except:
            MyLog.info('弹窗不存在........')
            self.save_screenshot(doc)
            raise

    # 获取弹窗文本内容
    def get_alert_text(self, times=30, poll_frequency=0.5, doc=''):
        # 等待弹窗存在
        try:
            WebDriverWait(self.driver, times, poll_frequency).until(EC.alert_is_present())
            alert = self.driver.switch_to_alert()
            MyLog().info('弹窗存在，获取弹框的文本内容')
            try:
                return alert.text
            except:
                MyLog.info('获取弹框的文本内容失败.........')
                self.save_screenshot(doc)
                raise
        except:
            MyLog.info('弹窗不存在........')
            self.save_screenshot(doc)
            raise


    "APP页面操作类"

    # 获取toast提示信息
    def get_toastMsg(self, str):
        # xpath表达式，文本匹配
        loc = (MobileBy.XPATH, '//*[contains(@text,"{}")]'.format(str))
        try:
            WebDriverWait(self.driver, 10, 0.01).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc).text
        except:
            MyLog.info('没有找到匹配的toast.......')
            raise

    # 快速输入，需要与ADBKeyboard配合使用，提升小程序中的输入效率
    def quick_sendkeys(self, keys):
        time.sleep(2)
        com = 'adb shell am broadcast -a ADB_INPUT_TEXT --es msg \"%s\"' % keys
        os.system(com)

    # 模拟鼠标输入
    def action_chains_send_keys(self, locator, text, doc):
        """
        方法使用介绍：ActionChains创建鼠标事件,move_to_element鼠标移动到某个元素,click单击鼠标左键,
        send_keys发送某个键到当前焦点的元素,perform执行鼠标事件
        :param element: 查找的元素
        :param text: 需要输入的信息
        """
        a = self.driver.find_element(locator, doc)
        action_a = ActionChains(self.driver)
        action_a.move_to_element(a).click().send_keys(text).perform()

    # 对于app需要输入支付密码方法,使用系统键盘方法输入
    def input_code(self, pay_pwd):
        l1 = list(pay_pwd)
        dict_data = {'0': 7, '1': 8, '2': 9, '3': 10, '4': 11, '5': 12, '6': 13, '7': 14, '8': 15, '9': 16}
        for i in l1:
            if i:
                self.driver.press_keycode(dict_data[i])

    # 滑屏操作
    def sliding_screen(self, direction, img_doc):
        '''param direction: 滑屏方向：上-up；下-down；左-left；右-right'''
        size = self.driver.get_window_size()
        try:
            MyLog.info("开始向{}方向滑动".format(direction))
            if direction.lower() == 'up':
                self.driver.swipe(start_x = size['width'] * 0.5,
                                  start_y = size['height'] * 0.75,
                                  end_x = size['width'] * 0.5,
                                  end_y = size['height'] * 0.25,
                                  duration=200)
            elif direction.lower() == 'down':
                self.driver.swipe(start_x = size["width"] * 0.5,
                                  start_y = size["height"] * 0.25,
                                  end_x = size["width"] * 0.5,
                                  end_y = size["height"] * 0.75,
                                  duration=200)
            elif direction.lower() == 'left':
                self.driver.swipe(start_x = size["width"] * 0.75,
                                  start_y = size["height"] * 0.5,
                                  end_x = size["width"] * 0.25,
                                  end_y = size["height"] * 0.5,
                                  duration=200)
            elif direction.lower() == 'right':
                self.driver.swipe(start_x = size["width"] * 0.25,
                                  start_y = size["height"] * 0.5,
                                  end_x = size["width"] * 0.75,
                                  end_y = size["height"] * 0.5,
                                  duration=200)
            else:
                MyLog.error("方向选择错误！")
        except Exception as e:
            MyLog.error("向{}方向滑动屏幕失败！".format(direction))
            self.save_screenshot(img_doc)
            raise e

    # 切换到webview页面
    def switch_to_webview(self, loc, img_doc, timeout=20, frequency=0.5):
        '''
        :param loc: webview页面的元素
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        '''
        try:
            MyLog.info("等待元素{}可见，并进行webview切换".format(loc))
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
            cons = self.driver.contexts
            MyLog.info("开始切换到webview：{}".format(cons[-1]))
            self.driver.switch_to.context(cons[-1])
        except Exception as e:
            MyLog.error("切换webview失败！")
            self.save_screenshot(img_doc)
            raise e
        else:
            end_time = time.time()
            MyLog.info("切换到webview：{}成功，等待时间：{}秒".format(cons[-1], round(end_time - start_time, 2)))

    # 切换到app原生页面
    def switch_to_native_app(self, img_doc):
        '''
        :param img_doc: 截图说明
        '''
        try:
            MyLog.info("切换到app原生页面")
            self.driver.switch_to.context('NATIVE_APP')
        except Exception as e:
            MyLog.error("切换到app原生页面失败！")
            self.save_screenshot(img_doc)
            raise e

    # 应用切换
    def application_switching(self, package_name, activity_name, img_doc):
        '''
        :param package_name: 包名
        :param activity_name: 欢迎页面名
        :param img_doc: 截图说明
        '''
        try:
            MyLog.info("切换应用到{}".format(package_name))
            self.driver.start_activity(app_package=package_name, app_activity=activity_name)
        except Exception as e:
            MyLog.error("切换应用到{}失败！".format(package_name))
            self.save_screenshot(img_doc)
            raise e

     # --------------随机生成数据部分，用于注册、任意字符输入--------------------- #

    def create_CH_mobile(self):
        """随机生成中国电话号码 """
        num = '0123456789'
        code = ['13', '15', '18', '19']  # 中国
        mobile = random.choice(code) + ''.join(random.choice(num) for i in range(9))
        return mobile

    def create_VE_mobile(self):
        """随机生成委内瑞拉电话号码 """
        num = '0123456789'
        code = ['4120', '4123', '4124']  # 委内瑞拉
        mobile = random.choice(code) + ''.join(random.choice(num) for i in range(7))  # 委内瑞拉
        return mobile

    def create_email(self):
        """随机生成邮箱地址"""
        num = '0123456789'
        server = '@qq.com', '@163.com'  # 邮箱域名
        email = ''.join(random.choice(num) for i in range(8)) + random.choice(server)
        return email

    def create_number(size=8, chars=string.digits):
        """ 随机生成数字 """
        return ''.join(random.choice(chars) for _ in range(size))

    def create_string(size=8, chars=string.ascii_letters):
        """ 随机字符串 """
        return ''.join(random.choice(chars) for _ in range(size))

    def withraw_address_special_start(size=33):
        """特殊字符开头"""
        start = ['-', '_', '@', ' ', '$', '&', '*', '^', '/']  # 特殊字符!@#$%^&*()._+=-
        str = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return random.choice(start) + ''.join(random.choice(str) for i in range(size))

    def withraw_address_special_end(size=33):
        """特殊字符结束"""
        end = ['-', '_', '@', ' ', '$', '&', '*', '^', '/']  # 特殊字符!@#$%^&*()._+=-
        str = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return ''.join(random.choice(str) for i in range(size)) + random.choice(end)

    def withraw_address_special_between(size=20):
        """特殊字符在中间"""
        between = ['-', '_', '@', ' ', '$', '&', '*', '^', '/']  # 特殊字符!@#$%^&*()._+=-
        str = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return ''.join(random.choice(str) for i in range(13)) + random.choice(between) + ''.join(
            random.choice(str) for i in range(size))
