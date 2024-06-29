.. Project Description
.. Project Log

.. Logo

.. image:: http://www.namasteydigitalindia.com/connect/wp-content/uploads/2023/01/Artboard-1.png
    :alt: nRobo image not found!
    :height: 200
    :width: 200
    :align: center

=======================================
nRoBo (An Automated Testing Framework )
=======================================

For Web Developers, QAs and Testers
***********************************

.. Project Status

--------------
Project Status
--------------
**Active**

.. Online Tutorials

----------------
Online Tutorials
----------------
VISIT and SUBSCRIBE to `nRoBo YouTube Channel <https://www.youtube.com/@nrobotestautomationframework/playlists>`_

.. Pre-requisites

Pre-requisites
--------------

Following pre-requisites needs to be installed in order to run ***nRoBo*** framework.

    0. Install Python (3.11 or higher)
        - `Check install guide for Python <https://www.python.org/downloads/>`_

        - Notes on Python Installation on Windows:
            - Go to "Control Panel > Add Or Remove Programs" and make sure that there are not multiple versions of Python are installed.
            - While installing Python, make sure following options to check as mentioned in the screenshots:


        .. image:: http://www.namasteydigitalindia.com/connect/wp-content/uploads/2024/03/Screenshot_1.png
            :alt: Install Python on Windows Screenshot 1
            :height: 200
            :width: 33%


        .. image:: http://www.namasteydigitalindia.com/connect/wp-content/uploads/2024/03/Screenshot_2.png
            :alt: Install Python on Windows Screenshot 2
            :height: 200
            :width:  33%

        .. image:: http://www.namasteydigitalindia.com/connect/wp-content/uploads/2024/03/Screenshot_3.png
            :alt: Install Python on Windows Screenshot 3
            :height: 200
            :width: 33%


        .. code-block:: bash

            python --version
            # or
            python --version

    1. Install Java (11  or higher)
        - `Check install guide for Java <https://www.java.com/en/download/manual.jsp>`_
        - Run the following command to check if java is installed

        .. code-block:: bash

            java --version

    2. Install allure command line tool.
        - Check `Install guide <https://allurereport.org/docs/gettingstarted-installation/>`_
        - Run the following command to check if allure cli is installed

        .. code-block:: bash

            allure --version

    3. Install Target Browsers on testing systems
        - `Chrome <https://www.google.com/chrome/>`_
        - `Edge <https://www.microsoft.com/en-us/edge/download>`_
        - `IE <https://www.selenium.dev/downloads/>`_
        - `Safari <https://support.apple.com/downloads/safari>`_
        - `Firefox <https://www.mozilla.org/en-US/firefox/new/>`_

.. Installation

Installation
------------

**On Windows machine**, Run Command Prompt and/or Python IDE of your choice should be run in Administrator mode and execute the following commands.
(To run in administrator mode, Right click on the tool and select 'Run As Administrator' option)

0. Make a directory for automation project

.. code-block:: bash

    mkdir <project-name>

- Example:
    If you want to develop autotests for the project, *Dream*.
    You can create directory and change directory to *dream* as following:

.. code-block:: bash

    mkdir dream
    cd dream

1. Install **virtualenv** package

.. code-block:: bash

    pip install virtualenv

2. Create virtual environment - .venv

.. code-block:: bash

    virtualenv .venv

3. Activate virtual environment

    - Unix/Mac/Linux

    .. code-block:: bash

        source .venv/bin/activate

    - Windows

    .. code-block:: bash

        .\\.venv\\Scripts\\activate

4. Install *nrobo*

.. code-block:: bash

    pip install nrobo --require-virtualenv

5. Install & run framework in single command

.. code-block:: bash

    nrobo --instances 10

.. note:: If there are any errors, run the upgrade command, pip install --upgrade nrobo

6. Run tests
    A. Minimal switches

    .. code-block:: bash

        nrobo --browser chrome_headless --report allure

    B. Typical usage

    .. code-block:: bash

        nrobo --app <app-name> --url <test-url> --username <username> --password <password> --instances <number-of-parallel-tests> --reruns <number-of-retries-to-rerun-failed-tests> --browser chrome_headless --report allure

    - Example:

    .. code-block:: bash

        nrobo --app Lotus --url https://www.google.com --username shiv --password tandav --instances 10 --reruns 2 --browser chrome_headless --report allure


    Above command instructs nrobo to do the following actions:
        - Launch the tests of Lotus application from the default test directory, <project-root-dir>, and its subdirectories and generate both, html (plain) and allure (rich) reports for displaying test results with following additional test parameters:

            #. Test url (--url switch)
            #. Credential: (username, password)=(shiv, tandav)
            #. Run bunch of 10 tests at once (--instances switch)
            #. Rerun addition 2 times the tests which got failed (--reruns switch)
            #. Target browser = Headless Chrome (--browser switch)

Notes for running -b=anti_bot_chrome:
    - `When running from a datacenter (even smaller ones), chances are large you will not pass! Also, if your ip reputation at home is low, you won't pass! <https://pypi.org/help/#description-content-type>`_
    - anti_bot_chrome will not work with --grid switch!

.. Command Line Switches

Command Line Switches
---------------------
This section enlists list of nRoBo-command-line-switches (nCLI) that it supports.
nCLI shadows every PyTest-command-line-switches (PyTestCLI) for backward compatibility with pytest.

Thus, nCLI switches are being categorized into three types:
    A. Pure-nCLI-switches
        - Only nCLI specific switches. Non-PyTest CLI switches.
    B. nCLI shadowing switches
        - These are PyTest switches overriden by nCLI with a new long or short name. These are at core, pure PyTest switches.
    C. Pure-PyTest-CLI-switches
        - As the name suggests, it is self explanatory that these switches are pure PyTest switches and maintained by them.

Below is a list of switches including all the three types categorically.

A. Pure nCLI Switches

    -i, --install           Install nRoBo requirements and framework on host system
    --app                   Name of application under test.
                            Name should not include special chars and it should only having alphanumeric values.
    --url                   Application url under test.
    --username              Username for login.
    --password              Password for login.
    -n, --instances         Number of parallel tests to reduce test-run-time.
                            Default value is 1. Meaning single test at a time in sequence.
    --report                Defines type of test report. Two types are supported, Simple HTML or Rich Allure report.
                            Options are <html> or <allure>. Default is <html>
    -b, --browser           Target browser. Default is **chrome**.
                            Following is a list of browser options support in nRoBo.
                            *chrome*, *chrome_headless*, *anti_bot_chrome*, *edge*, *edge_headless*,
                            *safari*, *firefox*, *firefox_headless*, *ie*
    --browser-config        Path of browser-config-file containing additional options that is/are needed to be applied
                            before browser instantiation. Each line in file should contain one option only.

                            For example: You want to apply, --start-maximized, chrome switch for chrome browser.
                            and if the browser-config-file is names as 'chrome_config.txt', then
                            the content of file would be as following:

                                --start-maximized

                            There will be no conversion taking place by nRoBo!
                            The browser switches will be applied to the browser instance.
    --grid                  Remote Grid server url.
                            Tests will be running on the machine when Grid server is running pointed by Grid url.

B. nCLI Shadowing Switches

    -k, --key               Only run tests that match the given substring
                            expression. An expression is a python resolvable
                            expression where all names are substring-matched
                            against test names and their parent classes.

                            Example:
                                -k 'test_method or test_other' matches all test.yaml functions and
                                classes whose name contains 'test_method' or 'test_other',
                                while -k 'not test_method' matches those
                                that don't contain 'test_method' in their names. -k 'not test_method
                                and not test_other' will eliminate the matches.
                                Additionally keywords are matched to classes
                                and functions containing extra names in their 'extra_keyword_matches' set,
                                as well as functions which have names assigned directly to them.
                                The matching is case-insensitive.

                            Note: --key switch is shadowing -k switch of PyTest for the sake of readability.
    -m, --marker            Only run tests matching given mark expression.
                            For example:
                            -m 'mark1 and not mark2'

C. Pure PyTest CLI Switches

    --reruns                Retries to rerun the failed tests n times specified by --reruns switch.
    --reruns-delay          Delay time in second(s) before a rerun for a failed test. Default is 1 second.
    --markers               Show markers (builtin, plugin and per-project ones).
    --junit-xml             --junit-xml=path. create junit-xml style report file at given path.
    --rootdir               --rootdir=ROOTDIR. Define root directory for tests.
                            Can be relative path: 'root_dir', './root_dir','root_dir/another_dir/'; absolute path:'/home/user/root_dir'; path with variables: '$HOME/root_dir'.
    --co, --collect-only     only collect tests, don't execute them.

    Note:
        * Full list of PyTest switches are enlisted and explained at the following web address: `Pure PyTest CLI Switches <https://docs.pytest.org/en/6.2.x/reference.html#command-line-flags>`_
        * Full list of all switches can be seen by running the following nrobo cli:

            .. code-block:: bash

                nrobo -h
                #or
                nrobo --help

        * nRoBo shadows all the PyTest switches, so no need to worry about. We can use each of them within the nRoBo framework. Isn't it great!

Personalization
---------------

.. note:: This section will be updated soon!

Reports
-------

Support for two kinds of test reports:

1. Lightweight HTML Report (*Best for sharing test results*)
    - Go to *<results>* dir and Double click on <report.html> file to view the simple html report.
2. Rich Allure Pytest Report (*Best for visualization*)
    - *Make sure *allure-pytest* command line tool is installed!*
        - To check, run the command:

        .. code-block:: bash

            allure --version

        - If not installed, please go through `Pre-requisites` section above.
    - Run the following command:

    .. code-block:: bash

        allure serve results/allure

.. Video Tutorials

------
Videos
------

.. note:: This section will be updated soon!

.. Features

--------
Features
--------

.. topic:: @ @


    * Easy and standard install - By `nRoBo <https://pypi.org/project/nrobo/>`_
    * Easy to learn and use - By `nRoBo <https://pypi.org/project/nrobo/>`_
    * Simple and Well Defined Automation Directory Structure - By `nRoBo <https://pypi.org/project/nrobo/>`_
    * Report Customization - By `nRoBo <https://pypi.org/project/nrobo/>`_
    * Rich Command Line Support that helps integration with CI/CD pipeline or any DevOps tech. - By `nRoBo <https://pypi.org/project/nrobo/>`_
    * Shipped with rich set of examples along with install. Thus, speedup learning. - By `nRoBo <https://pypi.org/project/nrobo/>`_
    * VISIT and SUBSCRIBE to Dedicated `nRoBo YouTube channel <https://www.youtube.com/@nrobotestautomationframework/playlists>`_ with a collection of video tutorials. Thus, speedup learning. - By `nRoBo <https://pypi.org/project/nrobo/>`_
    * Ready to use framework loaded with power of PyTest, Selenium Webdriver 4, HTML Report, Rich Allure Report and other tools. By `nRoBo <https://pypi.org/project/nrobo/>`_
    * Ability to organize tests in Groups. Inbuilt groups are sanity, ui, regression, nogui, api at present. - By `PyTest <https://docs.pytest.org/>`_ and `nRoBo <https://pypi.org/project/nrobo/>`_
    * Rich Browser Support (Chrome, Headless Chrome, Anti Bot Chrome, Edge, Safari, Firefox, FireFox Headless, IE) - By `SeleniumWebdriver <https://www.selenium.dev/documentation/webdriver/>`_
    * Rich Platform Support (Unix, Linux, Mac, Windows) - By `PyTest <https://docs.pytest.org/>`_, `SeleniumWebdriver <https://www.selenium.dev/documentation/webdriver/>`_ and `nRoBo <https://pypi.org/project/nrobo/>`_
    * nRoBo selenium wrapper classes and methods that saves lot of key presses. Thus, leveraging benefits of compact, readable and manageable of code. - By `nRoBo <https://pypi.org/project/nrobo/>`_
    * Well-structured thread-safe inbuilt setup and tear down processes. Thus, You can keep focus on testing! Not on maintaining framework. - By `nRoBo <https://pypi.org/project/nrobo/>`_
    * Test Parallelization - Inherited from `PyTest <https://docs.pytest.org/>`_
    * Distributed testing over Grid infrastructure - Inherited from `SeleniumWebdriver <https://www.selenium.dev/documentation/webdriver/>`_
    * Test parameterization - Inherited from `PyTest <https://docs.pytest.org/>`_
    * Screenshot-capture at the end of each test - Inherited from `SeleniumWebdriver <https://www.selenium.dev/documentation/webdriver/>`_
    * Capture webdriver logs, console logs and screenshots in reports - Inherited from `PyTest <https://docs.pytest.org/>`_
    * Inbuilt integration with NxGen Rich Allure Report (Backed by `Allure <https://allurereport.org/docs/pytest/>`_ Reports and `pytest-html-reports <https://pytest-html.readthedocs.io/en/latest/user_guide.html>`_)

.. list-table:: **Download Statistics**
   :widths: 33 33 33
   :align: center
   :header-rows: 1

   * - Country
     - Percent
     - Download Count