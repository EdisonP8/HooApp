import os
from HooApp.Common.read_config import ReadConfig,config_file_path

platformName = ReadConfig(config_file_path, 'Device_info', 'platformName')
apppackage = ReadConfig(config_file_path, 'Device_info', 'apppackage')
appActivity = ReadConfig(config_file_path, 'Device_info', 'appActivity')

class Android:

    @property
    def get_device_version(self):
        """获取安卓版本"""
        with os.popen('adb shell getprop ro.build.version.release', 'r') as f:  # 获取安卓版本
            android_version = f.read().replace('\n', '')
            # print('设备的版本为:', android_version)
        return android_version

    @property
    def get_device_name(self):
        """获取连接到电脑的安卓设备名称"""
        with os.popen('adb devices', 'r') as f:
            device_name = f.read().split('\n')[1].replace('\tdevice', '') # 取出第一个设备名称
            # print('连接的设备名称为:', device_name)
        return device_name

    @property
    def get_app_package(self):
        """获取待测目标app的包名"""
        with os.popen(f'adb shell "pm list packages | grep {apppackage}"', 'r') as f:
            app_package = f.read().replace('package:', '').replace('\n', '')  # app包名
            # print('查找的app包名为:', app_package)
        return app_package

    @property
    def get_app_Activity(self):
        """获取app的启动页Activity"""
        app_activity = appActivity  # 启动页Activity
        # print(f'启动页Activity:', app_activity)
        return app_activity

class setup_method():
    '''启动会话装置'''
    an = Android()  # 初始化设备数据
    driver_caps = {'platformName': platformName,
                   'platformVersion': an.get_device_version,
                   'deviceName': an.get_device_name,  # 默认第一个设备
                   'appPackage': an.get_app_package,
                   'appActivity': an.get_app_Activity,
                   "noReset": True,  # 默认不清空数据
                   "automationName": "Uiautomator2"}

if __name__ == '__main__':
    print(setup_method().driver_caps)
    # print(Android().get_device_name)