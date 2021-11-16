import configparser

parser = configparser.ConfigParser()
parser.read("config.ini")

BASE_URL = parser.get("saucedemo", "base_url")

STANDARD_USER_USERNAME = parser.get("users", "standard_user_username")
STANDARD_USER_PASSWORD = parser.get("users", "standard_user_password")
STANDARD_USER_INCORRECT_PASSWORD = parser.get("users", "standard_user_incorrect_password")
LOCKED_OUT_USER_USERNAME = parser.get("users", "locked_out_user_username")
LOCKED_OUT_USER_PASSWORD = parser.get("users", "locked_out_user_password")
PROBLEM_USER_USERNAME = parser.get("users", "problem_user_username")
PROBLEM_USER_PASSWORD = parser.get("users", "problem_user_password")
PERFORMANCE_GLITCH_USER_USERNAME = parser.get("users", "performance_glitch_user_username")
PERFORMANCE_GLITCH_USER_PASSWORD = parser.get("users", "performance_glitch_user_password")
NON_EXISTING_USER = parser.get("users", "non_existing_user")
NON_EXISTING_USER_PASSWORD = parser.get("users", "non_existing_user_password")

BROWSER_NAME = parser.get("driver", "browser_name").lower()
