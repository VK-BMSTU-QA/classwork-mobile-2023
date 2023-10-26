import os

from appium.options.android import UiAutomator2Options
from selenium import webdriver


def capability_select(device_os):
    if device_os == 'web':
        capability = webdriver.ChromeOptions()
        capability.add_experimental_option("excludeSwitches", ["enable-logging"])
    elif device_os == 'mw':
        mobile_emulation = {"deviceName": "Pixel 2"}
        # если хотите задать конкретные хар-ки устройства
        # подробнее: https://chromedriver.chromium.org/mobile-emulation
        # mobile_emulation = {"deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        #                     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) "
        #                                  "AppleWebKit/535.19 (KHTML, like Gecko) "
        #                                  "Chrome/18.0.1025.166 Mobile Safari/535.19"}
        capability = webdriver.ChromeOptions()
        capability.add_experimental_option("mobileEmulation", mobile_emulation)
        capability.add_experimental_option("excludeSwitches", ["enable-logging"])
    elif device_os == 'android':
        capability = UiAutomator2Options()
        capability.load_capabilities(caps=dict(
                      platformName="Android",
                      platformVersion="13.0",
                      automationName="uiautomator2",
                      appPackage="org.wikipedia",
                      appActivity=".main.MainActivity",
                      app=os.path.abspath(os.path.join(os.path.dirname(__file__), '../stuff/Wikipedia_v2.7.50337.apk')),
                      orientation="PORTRAIT",
                      autoGrantPermissions="true")
        )
    else:
        raise ValueError("Incorrect device os type")
    return capability
