from  appium import  webdriver

def init():
    desired_caps = dict()
    # 需要连接的手机平台
    desired_caps['platformName'] = 'Android'
    # 连接手机版本版本号
    desired_caps['platformVersion'] = '5.1'
    # 连接手机的设备号  可以用adb devices 查看
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # 要启动程序的报名
    desired_caps['appPackage'] = 'com.android.contacts'
    # desired_caps['appPackage'] = 'com.android.quicksearchbox'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['noReset'] = True

    # 要启动程序的界名
    desired_caps['appActivity'] = '.activities.PeopleActivity '
    # desired_caps['appActivity'] = '.SearchActivity'
    # 连接appium 服务器

    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

