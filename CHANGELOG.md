# nRoBo Test Automation Video Tutorials are available on [YouTube Channel](https://t.ly/FhJzy)

[//]: <> (## Change Log)
[//]: <> (All notable changes to this project will be documented in this file.)
[//]: <> (The format is based on Keep a Changelog keepachangelog.com/)
[//]: <> (and this project adheres to Semantic Versioning semver.org/)

### [2024.7.1] -  On 2024.02.18
#### Added
- Added YouTube channel link to PyPi project page

### [2024.7.0] -  On 2024.02.18, Fully tested release.
#### Added
- Few more unit tests

### [2024.6.10 - 2024.6.15] -  On 2024.02.18
#### Fixes
- Issue of repeated test run fixed

### [2024.6.1] -  On 2024.02.14
#### Fixes
- Issue with upgrade.
- Issue with demo pages and tests.
- Fix the issue of host packages not searchable.
#### Added
- More unit tests to ensure quality of the framework.
- Added feature to check if internet connectivity is there while upgrade.
- [Internal] Publishing feature changes.
- [Internal] Added ability to run tests in parallel in the internal test framework.

### NOTE: Below releases are removed, however, features in respective removed releases are included in the latest release.
### [2024.5.2] -  On 2024.02.12

#### Changes
- Smoothen nRoBo exit when using switch `--report allure`, "Press Ctrl+C to exit nRoBo."
- Handle system exit verbose when closing the allure report server by pressing Ctrl+C.
- Improved nRoBo console
#### Added
- Feature to show user information that an update is available. Without visiting PyPi.org. nRoBo will check if there is an update on start of each test/test-suite run. and if any update found, it will ask user to update or skip. It is good to suppress prompt when the test-suite is integrated into CI/CD pipeline. Other than that keeping it enabled will be a good help. Isn't it? 
- New command line switches:
    - Suppress
      - Usage: `nrobo --supress`
    - VERSION
      - Usage: `nrobo --VERSION`
      - Show version of nRoBo on your system
    - target
      - Usage: `nrobo --target`
      - To supply information of report name to nRoBo
- Added 61 critical component tests to ensure that baseline functionalities are up and running as expected. A lot is still need to be worked upon though.


###
###
### [2024.5.1] -  On 2024.02.10

#### Fixed
- Fix nRoBo launcher error [BLOCKER ISSUE]

### [2024.5.0] - On 2024.02.10

#### Added
nRoBo revamped at its core and loaded now with more power, yet, it's easy to learn and leverage benefit of using test automation. The previous versions of nRoBo framework are removed from the primary python package index([PyPi.org](https://pypi.org/)).
To share more details of nRoBo features, examples, practicals in the form of videos are available on dedicated YouTube channel.

- Rich Browser Support (Chrome, Headless Chrome, Edge, Safari, Firefox, FireFox Headless, IE) - By [SeleniumWebdriver](https://www.selenium.dev/documentation/webdriver/)
- Rich Platform Support (Unix, Linux, Mac, Windows) - By [PyTest](https://docs.pytest.org/), [Selenium](https://www.selenium.dev/) and [nRoBo](https://pypi.org/project/nrobo/)
- Wrapper classes for Webdriver, WebElement, and other selenium webdriver classes for saving a lot of typing. Thus, great readability of code. - By [nRoBo](https://pypi.org/project/nrobo/)
- Ready to use framework loaded with power of PyTest, Selenium and other tools. By [nRoBo](https://pypi.org/project/nrobo/)
- Well-structured inbuilt setup and tear down processes. Just focus on testing! Not on maintaining framework. - By [nRoBo](https://pypi.org/project/nrobo/)
- Inbuilt support for distributed testing over Grid infrastructure - Inherited from [PyTest](https://docs.pytest.org/)
- Inbuilt support for test parameterization - Inherited from [PyTest](https://docs.pytest.org/)
- Screenshot capture at the end of test - Inherited from [Selenium](https://www.selenium.dev/)
- Support for capturing test logs in reports - Inherited from [PyTest](https://docs.pytest.org/)
- Next Generation Test Reports (Backed by [Allure](https://allurereport.org/docs/pytest/) Reports and [pytest-html-reports](https://pytest-html.readthedocs.io/en/latest/user_guide.html))
- Support for cool tweaks in the standard reports - By [nRoBo](https://pypi.org/project/nrobo/)
- Command line Support to trigger tests that can be integrate with CI/CD pipeline or any DevOps tech. - By [nRoBo](https://pypi.org/project/nrobo/)
- Easy to use framework - By [nRoBo](https://pypi.org/project/nrobo/)
- Well Defined Directory Structure - By [nRoBo](https://pypi.org/project/nrobo/)
- Support grouping of tests. Supported groups are sanity, ui, regression, nogui, api at present. - By [PyTest](https://docs.pytest.org/), [nRoBo](https://pypi.org/project/nrobo/)


By [NamasteyDigitalIndia.com]