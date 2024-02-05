"""
nrobo conftest.py file.

Contains fixtures for nrobo framework
"""
import argparse

import pytest
from nrobo.cli.nglobals import __APP_NAME__, __USERNAME__, __PASSWORD__, __URL__


@pytest.fixture(autouse=True)
def url():
    # Global fixture returning app url
    return __URL__


@pytest.fixture(autouse=True)
def app():
    # Global fixture returning app name
    return __APP_NAME__


@pytest.fixture(autouse=True)
def username():
    # Global fixture returning admin username
    return __USERNAME__


@pytest.fixture(autouse=True)
def password():
    # Global fixture returning admin password
    return __PASSWORD__


@pytest.fixture(autouse=True)
def driver():
    # need implementation
    return 'driver'
