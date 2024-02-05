import os


class nCLI:
    INSTALL = "install"
    APP = "app"
    URL = "url"
    USERNAME = "username"
    PASSWORD = "password"
    INSTANCES = "instances"
    RERUN = "rerun"
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
        RERUN: "rerun",
        REPORT: "report",
        TESTDIR: "testsdir",
        BROWSER: "browser",
        KEY: "key",
    }


class REPORT_TYPES:
    HTML = "html"
    ALLURE = "allure"
    REPORT_DIR = "results"
    HTML_REPORT_PATH = REPORT_DIR + os.sep + "report.html"


class PACKAGES:
    NROBO = "nrobo"
    CLI = "cli"
