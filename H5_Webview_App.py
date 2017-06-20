# -*- coding: utf-8 -*-
import os
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        # desired_caps['automationName'] = 'Uiautomator2'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '87c5c497'
        # desired_caps['fullReset'] = 'false'
        # desired_caps['chromeOptions'] = {
        #     'androidProcess': 'com.tencent.mm:appbrand3'
        # }
        # if install app
        desired_caps['noReset'] = 'true'
        # run more device session
        # desired_caps['udid'] = '192.168.56.101:5555'
        # desired_caps['app'] = PATH(
        #     '../../../sample-code/apps/ContactManager/ContactManager.apk'
        # )
        desired_caps['appPackage'] = 'com.cafintech.insurer'
        desired_caps['appActivity'] = '.activity.MainActivity'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    def tearDown(self):
        self.driver.quit()
    def _find_toast(self, message, timeout, poll_frequency, driver):
        """
        # appium find toast
        # message: get except toast
        # timeout: total time
        # poll_frequency: The time interval
        """
        self.message = '//*[@text=\'{}\']'.format(message)
        self.element = WebDriverWait(driver, timeout, poll_frequency).until(
            expected_conditions.presence_of_element_located((By.XPATH,message)))
        print self.element
    def test_add_contacts(self):
        self.driver.implicitly_wait(10)
        print self.driver.contexts
        # 切换到webview上
        self.driver.switch_to.context("WEBVIEW_com.cafintech.insurer")
        # 打印当前切换到的webview
        print self.driver.current_context
        # 输入手机号
        self.driver.find_elements_by_class_name("mint-field-core")[0].send_keys("123452312312")
        self.driver.quit()