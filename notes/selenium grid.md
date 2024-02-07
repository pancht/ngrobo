#selenium grid doc
https://www.selenium.dev/documentation/grid/getting_started/

# Example:
https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/drivers/test_remote_webdriver.py

Prerequisites
-------------
- Java 11 or higher installed
- Browser(s) installed
- Browser driver(s)
  - Selenium Manager will configure the drivers automatically if you add --selenium-manager true.
  - Installed and on the PATH
- Download the Selenium Server jar file from the latest release 
- Start the Grid
  - java -jar selenium-server-<version>.jar standalone
- Point* your WebDriver tests to http://localhost:4444
- (Optional) Check running tests and available capabilities by opening your browser at http://localhost:4444

* Wondering how to point your tests to http://localhost:4444? Check the RemoteWebDriver section.

To learn more about the different configuration options, go through the sections below.


Commands
---------
# Following did not work
java -jar selenium-server-4.17.0.jar standalone --selenium-manager true 

# Following works
java -jar selenium-server-4.17.0.jar standalone

python test-nrobo-framework.py --browser safari --rootdir nrobo/ --grid http://192.168.1.6:4444