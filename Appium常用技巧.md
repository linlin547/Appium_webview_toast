# Appium常用技巧
* 测试微信准备(android)：
<pre><code>
        1.打开微信debug，微信进入debugx5.qq.com这个地址，打开后，点击页面上"信息"页，勾选是否打开TBS内核Inspector调试功能。
        2.需要找到进入公众号的路径，此部分为native
        3.切换到webview后，可以在chrome中打开"chrome://inspect/#devices"，查看当前webview的元素，方便后续定位
</pre></code>
* 测试WebView App(一般为H5包个安卓／苹果的壳，或者混合型app)
<pre><code>
        1.H5封壳的app一般需要测试的话，在打包时，开启webkit的debug模式，这样driver.contexts方法才能打印出webview名称，便于appium切换
        2.这里有一个坑，注意这个坑比较乱：
            坑1：运行中会出现appium的chromedriver的版本和chrome版本不一致错误，导致切不到webview
            坑2：运行过程中会出现不能执行二进制文件，这个一般是执行chromedriver包的错误，也是导致切不到webview
            android为例解决办法：
                1.进入手机设置-应用程序-全部-Android System webView中看下webView的版本(可以理解为chrome的版本)
                2.找到运行中报错的chromedriver版本--确认下是否不匹配
                3.网上找一下chromedriver对应的chrome版本，下载对应的chromedriver版本
                4.将步骤3中下载的chromedriver，替换appium自带的chromedriver
                ps：
                    mac为例，appium的chromedriver路径：
                        1./Users/用户名/Documents/node_modules/appium-chromedriver/chromedriver/mac/chromedriver
                        2./usr/local/lib/node_modules/appium/node_modules/.2.10.0@appium-chromedriver/chromedriver/mac/chromedriver
        3.切换到webview后，可以在chrome中打开"chrome://inspect/#devices"，查看当前webview的元素，方便后续定位
</pre></code>
* ![feature](https://github.com/linlin547/Appium/blob/master/image/chrome-chromedriver.png)
* 每次运行测试，app都会重新安装:
<pre><code>
        1.1 在case里不要设置app的安装路径，只要设置desired_caps['appPackage']（app的包名）和 desired_caps['appActivity']（启动时的activity）即可
        1.2 在case中desired_caps['noReset'] = 'true'
    </pre></code>
* 等待操作:
<pre><code>
        2.1 尽量不要使用sleep方法
        2.2 使用implicitly_wait(1000)方法，隐性等待/如果一个无素没有出现都会默认等待你所设定的时间，直到超时或者元素出现
        2.3 WebDriverWait()，同样也是 webdirver 提供的方法。在设置时间内，默认每隔一段时间检测一次当前。页面元素是否存在，如果超过设置时间检测不到则抛出异常。
        from selenium.webdriver.support.ui import WebDriverWait
        element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(“someId”))
        is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).
        until_not(lambda x: x.find_element_by_id(“someId”).is_displayed())
</pre></code>
* 元素无法定位:
<pre><code>
        3.1 使用元素坐标点定位，有两种点击方法:
            一种是tap([(100, 20), (100, 60), (100, 100)], 500)
            另一种是使用swipe(630, 320, 630, 320, 500)方法
        3.2 使用class_name来定位：
            # 获取页面class_name为android.widget.CheckBox的所有元素，形成一个list
            checkboxes = self.driver.find_elements_by_class_name('android.widget.CheckBox')
   </pre></code>
* 指定元素进行操作:
<pre><code>
        checkboxes[0].click()
        checkboxes[1].click()
        </pre></code>
* 长按操作:
<pre><code>
        action1 = TouchAction(self.driver)
        el_3 = self.driver.find_element_by_id('cn.highing.hichat:id/topic_voice_send')
        action1.long_press(el_3).wait(10000).perform()
        
        action2 = TouchAction(self.driver)
        el_3 = self.driver.find_element_by_id('cn.highing.hichat:id/topic_voice_send')
        action2.moveTo(el_3).release().perform()
        </pre></code>
* 异常处理
<pre><code>
        if self.driver.current_activity == ".ui.GuideActivity":
            try:
                做x这件事
            except:
                x失败的话，做这里的事
                </pre></code>
* appium设置输入法:
<pre><code>
        des.setCapability("unicodeKeyboard", "True")
        des.setCapability("resetKeyboard", "True")
        </pre></code>
* 拖动操作解析:
<pre><code>
        public void DragAndDrop(By dragElement, By dropElement)
            dragElement 起点元素，不要用输入框，尽量用不可点击的显示型元素
            dropElement 终点元素，不要用输入框，尽量用不可点击的显示型元素
            </pre></code>

* 滑动操作:
<pre><code>
    python:
        def swipe_to_up(self):
            """
            从下往上滑动
            :return: None
            """
            window_size = self.get_size()
            width = window_size.get("width")
            height = window_size.get("height")
            self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)
</pre></code>
<pre><code>
    java:
        public void SwipeToUp(int during) {
            int width = driver.manage().window().getSize().width;
            int height = driver.manage().window().getSize().height;
            driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, during);
            logger.info("向上滑动屏幕的3/4");
</pre></code>
* Appium（客户端版）解决每次运行Android，都安装Appium Setting和Unlock的方法
<pre><code>
    Appium Setting安装包路径:
    /usr/local/lib/node_modules/appium/node_modules/appium-android-driver/node_modules/io.appium.settings/bin/settings_apk-debug.apk
    Unlock安装包路径:
    /usr/local/lib/node_modules/appium/node_modules/appium-android-driver/lib/android-helpers.js
    解决方法，修改下面两个文件
    文件1地址：
    /usr/local/lib/node_modules/appium/node_modules/appium-android-driver/lib/android-helpers.js
    修改文件位置：
    helpers.initDevice = async function (adb, opts) {
      await adb.waitForDevice();
      await helpers.ensureDeviceLocale(adb, opts.language, opts.locale);
      await adb.startLogcat();
      let defaultIME;
      if (opts.unicodeKeyboard) {
        defaultIME = await helpers.initUnicodeKeyboard(adb);
      }
    //  await helpers.pushSettingsApp(adb);                                         # 注释掉
    //  await helpers.pushUnlock(adb);                                              # 注释掉
      return defaultIME;
    };
    
    文件2地址：
    /usr/local/lib/node_modules/appium/node_modules/appium-android-driver/build/lib/android-helpers.js
    修改文件位置：
    helpers.initDevice = function callee$0$0(adb, opts) {
      var defaultIME;
      return _regeneratorRuntime.async(function callee$0$0$(context$1$0) {
        while (1) switch (context$1$0.prev = context$1$0.next) {
          case 0:
            context$1$0.next = 2;
            return _regeneratorRuntime.awrap(adb.waitForDevice());
          case 2:
            context$1$0.next = 4;
            return _regeneratorRuntime.awrap(helpers.ensureDeviceLocale(adb, opts.language, opts.locale));
          case 4:
            context$1$0.next = 6;
            return _regeneratorRuntime.awrap(adb.startLogcat());
          case 6:
            defaultIME = undefined;
            if (!opts.unicodeKeyboard) {
              context$1$0.next = 11;
              break;
            }
            context$1$0.next = 10;
            return _regeneratorRuntime.awrap(helpers.initUnicodeKeyboard(adb));
          case 10:
            defaultIME = context$1$0.sent;
          case 11:
            context$1$0.next = 13;
            return _regeneratorRuntime.awrap(helpers.pushSettingsApp(adb));
            // return context$1$0.abrupt('return', defaultIME);                     # 添加新的 return，相当于跳过该步骤
          case 13:
            context$1$0.next = 15;
            return _regeneratorRuntime.awrap(helpers.pushUnlock(adb));
            // return context$1$0.abrupt('return', defaultIME);                     # 添加新的 return，相当于跳过该步骤
          case 15:
            return context$1$0.abrupt('return', defaultIME);
          case 16:
          case 'end':
            return context$1$0.stop();
        }
      }, null, this);
    };
</pre></code>
