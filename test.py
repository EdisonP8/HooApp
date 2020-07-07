from appium import webdriver
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






if __name__ == "__main__":
    login()