"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""

import json
import os.path as path
import string
import sys
import random
from pathlib import Path
from time import time
from typing import Union

import yaml


class Common:
    """Customized Selenium WebDriver class which contains all the useful methods that can be re used.
    These methods _help to in the following cases:
    To reduce the time required to write automation script.
    To take the screenshot in case of test case failure.
    To log to provide waits"""

    @staticmethod
    def read_file_as_string(file_path: Union[str, Path], encoding=None):
        """
        Read file as string

        :param file_path:
        :param encoding:
        :return:
        """

        try:
            if encoding is None:
                with open(file_path, "r") as f:
                    content = f.read()
                    return content
            else:
                with open(file_path, "r", encoding=encoding) as f:
                    content = f.read()
                    return content
        except FileNotFoundError as file_not_found_error:
            print("No such file or directory found: " + file_path)
            raise file_not_found_error

    @staticmethod
    def write_text_to_file(file_path: Union[str, Path], content, encoding=None):
        """
        Write text to file

        :param file_path:
        :param content:
        :param encoding:
        :return:
        """
        if isinstance(file_path, str):
            file_path = Path(file_path)

        try:
            if encoding is None:
                with open(file_path, 'w') as f:
                    f.write(content)
            else:
                with open(file_path, 'w', encoding=encoding) as f:
                    f.write(content)

        except FileNotFoundError as file_not_found_error:
            print("No such file or directory found: " + str(file_path))

    @staticmethod
    def append_text_to_file(file_path: Union[str, Path], content, encoding=None):
        """
        Write text to file

        :param file_path:
        :param content:
        :param encoding:
        :return:
        """
        if isinstance(file_path, str):
            file_path = Path(file_path)

        try:
            if encoding is None:
                with open(file_path, 'a') as f:
                    f.write(content)
            else:
                with open(file_path, 'w', encoding=encoding) as f:
                    f.write(content)

        except FileNotFoundError as file_not_found_error:
            print("No such file or directory found: " + str(file_path))

    @staticmethod
    def read_json(file_path: Union[str, Path]):
        """
        Read Json

        :param file_path:
        :return:
        """

        try:

            with open(file_path) as f:
                data = json.load(f)
                return data

        except FileNotFoundError as file_not_found_error:
            print("No such file or directory found: " + file_path)

    @staticmethod
    def write_json(file_path: Union[str, Path], dictionary):
        """
        Write dictionary data to file

        :param file_path: Path of file where dictionary date is going to be stored
        :param dictionary: Dictionary of data
        :return:
        """

        with open(file_path, 'w') as file:  # Open given file in write mode
            json.dump(dictionary, file, sort_keys=True, indent=4)

    @staticmethod
    def is_file_exist(file_path: Union[str, Path]):
        """
        Checks if given file exists or not.

        :param file_path: Path of file
        :return: True if file exists else return False
        """
        return path.exists(file_path)

    @staticmethod
    def read_yaml(file_path: Union[str, Path], /, *, fail_on_failure=True) -> Union[str, None]:
        """
        Read yaml file at given path

        :param fail_on_failure: create file if TRUE though file is not present_release to read.
        :param file_path: Path of file
        :return: Content of yaml file -> dict()
        """

        if not path.exists(file_path) and not fail_on_failure:
            """if file does not exist, then let's create it first"""

            with open(file_path, 'w') as file:
                """Create a file"""

                # initialize file with empty dictionary
                yaml.dump({}, file)

        if not path.exists(str(file_path)) and fail_on_failure:
            """file does not exist"""
            raise Exception(f"File {file_path} does not exist!")
        else:
            """Do Nothing as file exists"""
            pass

        # Read the file
        with open(r'{0}'.format(file_path)) as file:
            # The FullLoader parameter handles the conversion from YAML
            # scalar values to Python the dictionary format
            data = yaml.load(file, Loader=yaml.SafeLoader)

            # return with data as dictionary
            return data

    @staticmethod
    def write_yaml(file_path: Union[str, Path], dictionary):
        """
        Write dictionary data to given file path in yaml format

        :param file_path: Path of file where dictionary data needs to be stored
        :param dictionary: Dictionary data
        :return: Nothin
        """

        with open(file_path, 'w') as file:  # Open given file in write mode
            yaml.dump(dictionary, file)

    @staticmethod
    def generate_random_numbers(min, max):
        """
        Generate and return a random number in given range denoted by min and max

        :param min:
        :param max:
        :return:
        """
        """
        Returns a random string of given length

        @Returns string a random string
        """
        random_number = random.randint(min, max)

        return random_number

    @staticmethod
    def save_as_pdf(file_content_as_string, path: [str, Path] = None):
        """Save as pdf to given path"""

        import base64

        if path is None:
            path = "downloads/temp.pdf"

        if isinstance(path, Path):
            path = str(path)

        with open(path, 'wb') as theFile:
            theFile.write(base64.b64decode(file_content_as_string))

    @staticmethod
    def save_base64string(file_content_as_string, path: [str, Path] = None):
        """Save base64string as given path"""

        import base64

        if path is None:
            path = "downloads/temp.pdf"

        if isinstance(path, Path):
            path = str(path)

        with open(path, 'wb') as theFile:
            theFile.write(base64.b64decode(file_content_as_string))

    @staticmethod
    def save_bytes_to_file(bytes, path: [str, Path] = None):
        """Save bytes to given path"""

        import base64

        if path is None:
            path = "temp.jpg"

        if isinstance(path, Path):
            path = str(path)

        with open(path, 'wb') as theFile:
            theFile.write(bytes)
