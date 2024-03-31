# nRoBo Test Automation Video Tutorials are available on [YouTube Channel](https://www.youtube.com/@nrobotestautomationframework/playlists)

[//]: <> (## Change Log)
[//]: <> (All notable changes to this project will be documented in this file.)
[//]: <> (The format is based on Keep a Changelog keepachangelog.com/)
[//]: <> (and this project adheres to Semantic Versioning semver.org/)

### [2024.36.0] - On 2024.03.31

### Added
- Added notes for installing python on Windows machine with screenshots.

### [2024.35.0] - On 2024.03.24

#### Fixed
- Issue in update


### [2024.34.0] - On 2024.03.24

#### Added
- More sample examples to quickly learn nRoBo Framework
- Support for project specific dependencies through requirements.txt
- Added support for `appium` lib. Examples and sample videos will be published once `appium` support will complete.

#### Fixed
- Issue in handling multiple windows

### [2024.25.7] - On 2024.03.06

#### Fixed
- [Issue with upgrade](https://github.com/pancht/ngrobo/issues/87) 

### [2024.25.0] - On 2024.03.04

#### Added
- Introduced a new nRoBo command line switch, --title. If supplied, sets a [custom report title of HTML report](https://youtu.be/Qq49PwXP4bE?si=GMT61kFaOo0KJLiJ).
- Added feature to run tests from specific [modules](https://youtu.be/FR0G-ifr_a4?si=kv553Qb2gMNkHSJl), [classes](https://youtu.be/F5lrKKJhd84?si=Gf-fhBc46C2HpANI) and [packages](https://youtu.be/clUgVfoPZUc?si=8RBiP_Vk21A_6BJB). 

### [2024.24.0] - On 2024.03.01

#### Added
- Added --fullpagescreenshot nRoBo cli switch. That is when applied, it takes full page screenshot instead of only visible window rect by default. However, this switch only works with chrome_headless browser. nRoBo overrides the --browser switch with chrome_headless or adds --browser chrome_headless if fullpagescreenshot is requested. 

### [2024.21.3] - On 2024.03.01

#### Added
- Added GoogleBigQuery to get download statistics

### [2024.21.0] - On 2024.03.01

#### Added
- Added new browser support for anti bot chrome. -b=anti_bot_chrome. Basically this is achieved by instantiating driver instance from [undetected_chromedriver](https://pypi.org/project/undetected-chromedriver/).

### [2024.19.1] - On 2024.02.25

#### Added
- Ability to add define and add custom markers from browserConfigs/markers.yaml file

### [2024.16.0] - On 2024.02.23

#### Added
nRoBo revamped at its core and loaded now with more power, yet, simplicity to learn, use and leverage benefit of using test automation. The previous versions of nRoBo framework are removed from the primary python package index([PyPi.org](https://pypi.org/)).
To share more details of nRoBo features, examples, practicals in the form of videos are available on following [YouTube Channel](https://t.ly/FhJzy).

- Easy and standard install - By [nRoBo](https://pypi.org/project/nrobo/)
- Easy to learn and use - By [nRoBo](https://pypi.org/project/nrobo/)
- Simple and Well Defined Automation Directory Structure - By [nRoBo](https://pypi.org/project/nrobo/)
- Ability to organize tests in Groups. Inbuilt groups are sanity, ui, regression, nogui, api at present. - By [PyTest](https://docs.pytest.org/), [nRoBo](https://pypi.org/project/nrobo/)
- Rich Browser Support (Chrome, Headless Chrome, Anti-Bot-Chrome, Edge, Safari, Firefox, FireFox Headless, IE) - By [SeleniumWebdriver](https://www.selenium.dev/documentation/webdriver/)
- Rich Platform Support (Unix, Linux, Mac, Windows) - By [PyTest](https://docs.pytest.org/), [Selenium](https://www.selenium.dev/) and [nRoBo](https://pypi.org/project/nrobo/)
- nRoBo selenium wrapper classes and methods that saves lot of key presses. Thus, leveraging benefits of compact, readable and manageable of code. - By [nRoBo](https://pypi.org/project/nrobo/)
- Ready to use framework loaded with power of PyTest, Selenium Webdriver 4, HTML Report, Rich Allure Report and other tools. By [nRoBo](https://pypi.org/project/nrobo/)
- Well-structured thread-safe inbuilt setup and tear down processes. Thus, You can keep focus on testing! Not on maintaining framework. - By [nRoBo](https://pypi.org/project/nrobo/)
- Test Parallelization - Inherited from [PyTest](https://docs.pytest.org/)
- Distributed testing over Grid infrastructure - Inherited from [Selenium](https://www.selenium.dev/)
- Test parameterization - Inherited from [PyTest](https://docs.pytest.org/)
- Screenshot-capture at the end of each test - Inherited from [Selenium](https://www.selenium.dev/)
- Capture webdriver logs, console logs and screenshots in reports - Inherited from [PyTest](https://docs.pytest.org/) and [nRoBo](https://pypi.org/project/nrobo/)
- Inbuilt integration with NxGen Rich Allure Report (Backed by [Allure](https://allurereport.org/docs/pytest/) Reports and [pytest-html-reports](https://pytest-html.readthedocs.io/en/latest/user_guide.html))
- Report Customization - By [nRoBo](https://pypi.org/project/nrobo/)
- Rich Command Line Support that helps integration with CI/CD pipeline or any DevOps tech. - By [nRoBo](https://pypi.org/project/nrobo/)


Developed by **Team nRoBo** at [NamasteyDigitalIndia.com](NamasteyDigitalIndia.com)