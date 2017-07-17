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

