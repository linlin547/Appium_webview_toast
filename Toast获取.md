* appium1.6.3新增Uiautomator2获取toast：
    * 1.安装Uiautomator2 driver：
        * npm install appium-uiautomator2-driver
    * 2.启动参数增加:
        * desired_caps['automationName'] = 'Uiautomator2'
* 坑 坑 坑:
    * 运行后手机会装如下两个apk
        * io.appium.uiautomator2.server
        * io.appium.uiautomator2.server.test
        * 但是......运行基本会报错，有个地方很关键：
            * 本地android-sdk的tools文件中必须要有文件：zipalign
            * 没有的话需要升级下sdk的版本(比如升到android6.0)，一般都会生成上面这个文件
