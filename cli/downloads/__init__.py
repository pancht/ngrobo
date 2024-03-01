"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

This module has methods to get download stats.

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""
from datetime import datetime
from pathlib import Path


def downloads():
    """Displays downloads count of nRoBo pypi project

       Doc: https://pypi.org/project/pypinfo/
       Example: https://github.com/ofek/pypinfo"""
    from nrobo import console, terminal, NROBO_CONST, Python
    from nrobo.util.common import Common

    command = [Python.PYPINFO, '--auth', 'key/nrobo-statistics-214a0f5d2c1b.json']
    terminal(command=command)

    result = terminal([Python.PYPINFO, NROBO_CONST.NROBO, 'country'], debug=True, text=True, capture_output=True)
    console.print(f"{result.stdout}")

    download_stat_file_path = Path('key') / \
                              'download-stats' / \
                              f'{datetime.today().strftime("%Y-%m-%d_%H_%M")}' \
                              f'_{Common.generate_random_numbers(1000, 9999)}.md'
    Common.write_text_to_file(download_stat_file_path, result.stdout)


