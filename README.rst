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
`YouTube Channel <https://t.ly/FhJzy>`_

.. Pre-requisites

Pre-requisites
--------------

Following pre-requisites needs to be installed in order to run ***nRoBo*** framework.

    0. Install Python (3.11 or higher)
        - `Check install guide for Python <https://www.python.org/downloads/>`_

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
        - Check `Install guide <https://docs.qameta.io/allure/#_installing_a_commandline>`_
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

    nrobo

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
                            *chrome*, *chrome_headless*, *edge*, *edge_headless*,
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


    * Rich Browser Support (Chrome, Headless Chrome, Edge, Safari, Firefox, FireFox Headless, IE) - By `SeleniumWebdriver <https://www.selenium.dev/documentation/webdriver/>`_
    * Rich Platform Support (Unix, Linux, Mac, Windows) - By `PyTest <https://docs.pytest.org/>`_, `Selenium <https://www.selenium.dev/>`_ and `nRoBo <https://pypi.org/project/nrobo/>`_
    * Wrapper classes for Webdriver, WebElement, and other selenium webdriver classes for saving a lot of typing. Thus, great readability of code. - By `nRoBo <https://pypi.org/project/nrobo/>`_
    * Ready to use framework loaded with power of `PyTest <https://docs.pytest.org/>`_, `Selenium <https://www.selenium.dev/>`_ and other tools. By `nRoBo <https://pypi.org/project/nrobo/>`_
    * Well structured inbuilt setup and tear down processes. Just focus on testing! Not on maintaining framework. - By `nRoBo <https://pypi.org/project/nrobo/>`_
    * Inbuilt support for distributed testing over Grid infrastructure - Inherited from `PyTest <https://docs.pytest.org/>`_
    * Inbuilt support for test parameterization - Inherited from `PyTest <https://docs.pytest.org/>`_
    * Screenshot capture at the end of test - Inherited from `Selenium <https://www.selenium.dev/>`_
    * Support for capturing test logs in reports - Inherited from `PyTest <https://docs.pytest.org/>`_
    * Next Generation Test Reports (Backed by `Allure <https://allurereport.org/docs/pytest/>`_ Reports and `pytest-html-reports <https://pytest-html.readthedocs.io/en/latest/user_guide.html>`_)
    * Support for cool tweaks in the standard reports - By `nRoBo <https://pypi.org/project/nrobo/>`_
    * Command line Support to trigger tests that can be integrate with CI/CD pipeline or any DevOps tech. - By `nRoBo <https://pypi.org/project/nrobo/>`_
    * Easy to use framework - By `nRoBo <https://pypi.org/project/nrobo/>`_
    * Well Defined Directory Structure - By `nRoBo <https://pypi.org/project/nrobo/>`_
    * Support grouping of tests. Supported groups are sanity, ui, regression, nogui, api at present. - By `PyTest <https://docs.pytest.org/>`_, `nRoBo <https://pypi.org/project/nrobo/>`_


.. Tools and Libraries

-----------------
Tools & Libraries
-----------------

1. `Next Generation Test Automation Framework for Python <https://docs.pytest.org/en/7.2.x/contents.html>`_
    2. pytest plugins
        1. `pytest-metadata <https://pypi.org/project/pytest-metadata/>`_ - pytest plugin that provides access to test session metadata
        2. `pytest-xdist <https://pypi.org/project/pytest-xdist/>`_ - The pytest-xdist plugin extends pytest with new test execution modes, the most used being distributing tests across multiple CPUs to speed up test execution.
        3. `pytest-forked <https://pypi.org/project/pytest-forked/>`_ - Run tests in isolated forked subprocesses
        4. `pytest-rerunfailures <https://pypi.org/project/pytest-rerunfailures/>`_ - pytest plugin to re-run tests to eliminate flaky failures
        5. `virtualenv <https://pypi.org/project/virtualenv/>`_ - Virtual Python Environment builder
        6. `PyYAML <https://pypi.org/project/PyYAML/>`_ - YAML parser and emitter for Python
        7. `py <https://pypi.org/project/py/>`_ - library with cross-python path, ini-parsing, io, code, log facilities
2. `Selenium Webdriver 4 <https://www.selenium.dev/documentation/webdriver/getting_started/upgrade_to_selenium_4/>`_ - Browser Automation Tool (Open Source)
3. `Webdriver Manager <https://pypi.org/project/webdriver-manager/>`_ - Selenium Webdriver Manager
4. `Allure Framework <https://docs.qameta.io/allure/>`_ - Next Generation Test Report Framework
5. `pytest-html <https://pypi.org/project/pytest-html/>`_ - Simple HTML Test Report Plugin