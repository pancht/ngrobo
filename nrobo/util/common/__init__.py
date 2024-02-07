import json
import os.path as path
import string
import sys
import random
from time import time
import yaml


class Common:
    """
    Customized Selenium WebDriver class which contains all the useful methods that can be re used.
    These methods _help to in the following cases:
    To reduce the time required to write automation script.
    To take the screenshot in case of test case failure.
    To log to provide waits
    """

    @staticmethod
    def read_file_as_string(file_path, encoding=None):
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

    @staticmethod
    def write_text_to_file(file_path, content, encoding=None):
        """
        Write text to file

        :param file_path:
        :param content:
        :param encoding:
        :return:
        """

        try:
            if encoding is None:
                with open(file_path, 'w') as f:
                    f.write(content)
            else:
                with open(file_path, 'w', encoding=encoding) as f:
                    f.write(content)

        except FileNotFoundError as file_not_found_error:
            print("No such file or directory found: " + file_path)

    @staticmethod
    def read_json(file_path):
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
    def write_json(file_path, dictionary):
        """
        Write dictionary data to file

        :param file_path: Path of file where dictionary date is going to be stored
        :param dictionary: Dictionary of data
        :return:
        """

        with open(file_path, 'w') as file:  # Open given file in write mode
            json.dump(dictionary, file, sort_keys=True, indent=4)

    @staticmethod
    def is_file_exist(file_path):
        """
        Checks if given file exists or not.

        :param file_path: Path of file
        :return: True if file exists else return False
        """
        return path.exists(file_path)

    @staticmethod
    def read_yaml(file_path):
        """
        Read yaml file at given path

        :param file_path: Path of file
        :return: Content of yaml file -> dict()
        """

        if not path.exists(file_path):
            """if file does not exist, then let's create it first"""

            with open(file_path, 'w') as file:
                """Create a file"""

                # initialize file with empty dictionary
                yaml.dump({}, file)
        else:
            """Do Nothing as file exists"""

        # Read the file
        with open(r'{0}'.format(file_path)) as file:
            # The FullLoader parameter handles the conversion from YAML
            # scalar values to Python the dictionary format
            data = yaml.load(file, Loader=yaml.SafeLoader)

            # return with data as dictionary
            return data

    @staticmethod
    def write_yaml(file_path, dictionary):
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
