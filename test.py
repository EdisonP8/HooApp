from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
desired_caps = {
    'platformName':'Android',
    'deviceName':'e4c6c8d7',
    'appPackage':'com.hufu.qianbao',
    'appActivity':'.activitys.SplashActivity',
    'autoGrantPermissions': True,  # 获取默认权限
    "noReset": True
    }

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


def login():
    time.sleep(5)
    # print(drivr.page_source)
    driver.find_element_by_id("tv_login_register").click()
    time.sleep(1)
    driver.find_element_by_id('et_input_phone').send_keys('13632543087')
    driver.find_element_by_id('et_input_pwd').send_keys('Abc123456')  # 输入登陆密码
    time.sleep(1)
    driver.find_element_by_id('bt_login').click()  # 点击登陆
    time.sleep(1)
    # a = driver.find_element_by_id('tv_0')
    action_a = ActionChains(driver)
    action_a.move_to_element(driver.find_element_by_id('tv_0')).click().send_keys(456320).perform()
    aa = driver.find_element_by_id('tv_0').click()  # 点击登陆
    aa.send_keys('456320')

    # driver.find_element_by_id('et_input_phone').send_keys('13236925899')
    # driver.find_element_by_id('tv_phonecode').click()
    # driver.find_element_by_id('tv_phonecode').click()
    # driver.find_element_by_id('tv_phonecode').click()
    # driver.find_element_by_id('tv_phonecode').click()
    # driver.find_element_by_id('et_input_code').send_keys('456321')
    # driver.find_element_by_id('bt_login').click()  # 点击下一步
    # time.sleep(2)
    # driver.find_element_by_id('et_input_pwd').send_keys('Abc123456')
    # driver.find_element_by_id('et_input_pwd2').send_keys('Abc123456')
    # driver.find_element_by_id('bt_login').click()  # 点击完成
    # time.sleep(2)
    # source = driver.page_source  # 打印当前页面全部的元素
    # if '设置密码成功' in source:
    #     return 3232323
    # else:
    #     print('找不到该元素...')
    #     return False

    time.sleep(20)

if __name__ == "__main__":
    login()