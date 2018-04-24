# Appium
* Android启动多端口服务：
  <pre>
    appium -p 4723 -bp 4724 -U 22238e79 --command-timeout 600
    参数解释：
      -p Appium的主要端口
      -U 设备id
      -bp Appium bootstrap端口
      --chromedriver-port chromedriver端口（当使用了webviews或者chrome）
  </pre>
* IOS 貌似不能本地启动多个端口

# 若使用uiautomator2时，开启多服务端口会竞争需要设置systemport
systemPort If you are using appium-uiautomator2-driver, set a different system port for each Appium instanceset with systemPort capability since sometimes there can be a port conflict if different ports aren't used, such as in this issue.


