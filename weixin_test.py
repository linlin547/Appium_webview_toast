from appium import webdriver
# -*- coding: UTF-8 -*-
import os,time,sys
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
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = 'd5a1bc96'
        # desired_caps['fullReset'] = 'false'
        desired_caps['chromeOptions'] = {
            'androidProcess': 'com.tencent.mm:appbrand3'
        }
        # if install app
        desired_caps['noReset'] = 'true'
        # run more device session
        # desired_caps['udid'] = '192.168.56.101:5555'
        # desired_caps['app'] = PATH(
        #     '../../../sample-code/apps/ContactManager/ContactManager.apk'
        # )
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = '.ui.LauncherUI'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}
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
        self.driver.find_element_by_id('com.tencent.mm:id/af9').click()
        time.sleep(3)
        print self.driver.contexts
        self.x = WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_id("com.tencent.mm:id/a35"))
        self.x.click()
        print self.driver.contexts
        time.sleep(5)
        self.driver.switch_to.context("WEBVIEW_com.tencent.mm:tools")
        print "switch ok"
        self.y = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_css_selector("input[type='tel']"))
        self.y.send_keys("13488834010")
        print "click ok"
        time.sleep(5)
        self.driver.quit()