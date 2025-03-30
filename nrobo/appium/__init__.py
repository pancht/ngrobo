# pylint: disable=R0401
"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

appium module holds nRoBo settings needed for
working with appium framework.

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""

from dataclasses import dataclass


@dataclass
class Capability:
    """Capability class."""

    AUTOMATION_NAME = "automationName"


@dataclass
class AutomationNames:
    """Possible appium capabilities for automationName"""

    UI_AUTOMATION2 = "uiautomator2"
    XCUITEST = "XCUITest"
