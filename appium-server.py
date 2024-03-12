import os
os.environ["JAVA_HOME"] = "/usr/libexec/java_home"
os.environ["ANDROID_HOME"] = f"{os.environ['HOME']}/Library/Android/sdk"
os.environ["PATH"] = f'{os.environ["PATH"]}:' \
                     f'{os.environ["ANDROID_HOME"]}/platform-tools:' \
                     f'{os.environ["ANDROID_HOME"]}/tools:' \
                     f'{os.environ["ANDROID_HOME"]}/tools/bin:' \
                     f'{os.environ["ANDROID_HOME"]}/emulator:' \
                     f'{os.environ["ANDROID_HOME"]}/adb'
print(os.environ["ANDROID_HOME"])
os.system("echo $PATH")
os.system("adb devices")
# os.system("adb uninstall io.appium.uiautomator2.server")
# os.system("adb uninstall io.appium.uiautomator2.server.test")
os.system("appium --allow-cors")