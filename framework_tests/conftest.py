"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

conftest.py for running unit tests.

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""

# import sys, os
# sys.path.append(os.path.join(os.path.dirname(__file__),
# os.path.join(os.path.dirname(__file__), '')))
# print(sys.path)


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     test_fn = item.obj
#     docstring = getattr(test_fn, '__doc__')
#     if docstring:
#         report.nodeid = docstring  # replace __doc__ string with nodeid
