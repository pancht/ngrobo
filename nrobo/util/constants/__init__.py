"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================


Definitions of CONSTANTS.

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""


class CONST(object):
    """
    Collection of CONSTANTS
    """
    NEWLINE = "\n"

    SINGLE_INVERTED_COMMA = "'"
    EMPTY = ""
    EQUAL = "="
    BLANK = EMPTY
    SPACE = " "
    STAR = "*"
    ASTERISK = STAR
    UNDERSCORE = "_"
    FORWARD_SLASH = "/"
    MINUS = "-"
    HYPHEN = MINUS
    TILD = "~"
    CARET = "`"
    QUESTION = "?"
    EXCLAMATION = "!"
    HASH = "#"

    # Brackets & PROGRAMING LANGUAGES
    PARENTHESIS_OPEN = "("
    PARENTHESIS_CLOSE = ")"
    CURLY_BRACE_OPEN = "{"
    CURLY_BRACE_CLOSE = "}"
    SQUARE_BRACKET_OPEN = "["
    SQUARE_BRACKET_CLOSE = "]"
    SCOPE_RESOLUTION_OPERATOR = "::"

    # Web and browser
    HTTPS = "https://"
    HTTP = "http://"
    DOT = "."
    COLON = ":"
    ADDRESS_OF = "@"
    AT_THE_RATE = ADDRESS_OF

    # Day, Date and Time
    HOURS_PER_DAY = 24
    MINUTES_PER_HOUR = 60
    SECONDS_PER_MINUTE = 60
    PERCENTAGE = '%'

    # Currencies
    DOLLAR = "$"
    RUPEE = u'\u20B9'

    # Greetings
    FOLDED_HAND = '\uF09F\u998F'
    HEART_RED = '\u2764\ufe0f'

    # Path seperators
    SLASH = FORWARD_SLASH
    BACKSLASH = u'\u005C'


class EXT:
    """Constants for various extensions."""

    YAML = ".yaml"
    PY = ".py"
    PYC = ".pyc"
