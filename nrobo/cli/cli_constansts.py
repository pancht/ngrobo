import os


class REPORT_TYPES:
    HTML = "html"
    ALLURE = "allure"
    REPORT_DIR = "results"
    HTML_REPORT_PATH = REPORT_DIR + os.sep + "report.html"


class nCLI:
    INSTALL = "install"
    APP = "app"
    URL = "url"
    USERNAME = "username"
    PASSWORD = "password"
    INSTANCES = "instances"
    RERUNS = "reruns"
    RERUNS_DELAY = "reruns-delay"
    REPORT = "report"
    TESTDIR = "testsdir"
    BROWSER = "browser"
    KEY = "key"

    ARGS = {
        INSTALL: "install",
        APP: "app",
        URL: "link",
        USERNAME: "username",
        PASSWORD: "password",
        INSTANCES: "instances",
        RERUNS: "rerun",
        REPORT: "report",
        TESTDIR: "testsdir",
        BROWSER: "browser",
        KEY: "key",
    }

    DEFAULT_ARGS = {
        '--cache-clear': ['--cache-clear'],
        '--color': ['--color', 'yes'],
        '-r': ['-r', 'fE'],
        '--code-highlight': ['--code-highlight', 'yes'],
        '--junit-xml': ['--junit-xml', REPORT_TYPES.REPORT_DIR + os.sep + f"junit-report.xml"]
    }


class PACKAGES:
    NROBO = "nrobo"
    CLI = "cli"
