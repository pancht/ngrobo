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
import os
from datetime import datetime
from pathlib import Path


def downloads() -> str:
    """Displays downloads count of nRoBo pypi project

       Doc: https://pypi.org/project/pypinfo/
       Example: https://github.com/ofek/pypinfo"""
    from nrobo import console, terminal, NROBO_CONST, Python, NROBO_PATHS
    from nrobo.util.common import Common
    from nrobo.util.filesystem import move
    import re

    today_date = re.match(r'([\d]+_[\d]+_[\d]+)', f'{datetime.today().strftime("%Y_%m_%d_%H_%M")}')[1]
    key_path = Path("key")
    download_status_dir = key_path / "download-stats"

    download_stats_present_for_the_day = False
    existing_status_file_path = None
    existing_status_file_date = None
    for path in download_status_dir.iterdir():
        if path.is_file() and re.match(r'([\d]+_[\d]+_[\d]+)', str(path.name)):
            existing_status_file_path = path
            existing_status_file_date = re.match(r'([\d]+_[\d]+_[\d]+)', str(path.name))[1]
            if today_date == existing_status_file_date:
                download_stats_present_for_the_day = True  # change status to True
                break  # no further processing is needed at this point, thus break loop!

    # move the previous download stat file to its folder
    # if folder is not present then create it else just move the file
    existing_stat_file_date_and_today_date_matches = (existing_status_file_date == today_date)
    existing_stat_file_date_folder_exists = \
        (download_status_dir / existing_status_file_date).exists() if existing_status_file_date is not None else None

    if existing_status_file_date is not None \
            and not existing_stat_file_date_and_today_date_matches\
            and not existing_stat_file_date_folder_exists:
        os.mkdir(download_status_dir / existing_status_file_date)

    if existing_status_file_date is not None \
            and not existing_status_file_date == re.match(r'([\d]+_[\d]+_[\d]+)', today_date)[1]:
        # move file
        move(existing_status_file_path, download_status_dir / existing_status_file_date / existing_status_file_path.name)

    if download_stats_present_for_the_day:
        # download stats are present for today
        # thus, no need to re-download status to save BigQuery API usage.
        # Just return.
        return

    # add auth key
    command = [Python.PYPINFO, '--auth', 'key/nrobo-statistics-214a0f5d2c1b.json']
    terminal(command=command)

    # Get download stats
    result = terminal([Python.PYPINFO, NROBO_CONST.NROBO, 'country'], debug=True, text=True, capture_output=True)
    console.print(f"{result.stdout}")

    # save download stats
    download_stat_file_path = download_status_dir / f'{today_date}_{Common.generate_random_numbers(1000, 9999)}.md'
    Common.write_text_to_file(download_stat_file_path, result.stdout)

    output = result.stdout

    # test output conversion

    # strip off header
    output = re.sub(r'(Served from cache:[ a-zA-Z:\d.$\n]*)', '', output, count=1)
    # strip off pipes and spaces
    output = output.replace('|', '').replace(' ', '').replace('-','')
    output = """.. list-table:: **Download Statistics**\n   :widths: 25 25\n   :align: center\n   :header-rows: 1""" + output
    output = output.replace('countrydownload_count\n', '')
    output = output.replace(':header-rows: 1', ':header-rows: 1\n\n   * - Country\n     - Download Count')

    matches = re.findall(r'([A-Za-z]+[\d,]+)', output)
    for m in matches:
        _country = re.findall(r'([a-zA-Z]+)', m)
        _count = re.search(r'([\d,]+)', m)
        _repl = f'   * - **{_country[0]}**\n     - **{_count[0]}**' if _country[0] == 'Total' else f'   * - {_country[0]}\n     - {_count[0]}'
        output = output.replace(m, _repl)

    # Read README.rst file
    readme_file_content = Common.read_file_as_string(NROBO_PATHS.README_RST_FILE)
    # Remove previous download stats section
    readme_file_content = re.sub(r'(\n.. list-table:: [*]+Download Statistics[*]+[\n, :a-z *A-Z\d-]*)', '', readme_file_content, count=1)
    # Append new download stats section
    readme_file_content = f"{readme_file_content}\n{output}"
    # Write back to README.rst file
    Common.write_text_to_file(NROBO_PATHS.README_RST_FILE, readme_file_content)

    console.rule(f"Added download statistics to README.rst")

