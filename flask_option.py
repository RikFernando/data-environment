# pylint: disable=missing-docstring

import os

def start():
    """returns the right message"""
    # print(os.getenv("FLASK_ENV"))
    statement = os.getenv("FLASK_ENV", default = "empty")
    return f"Starting in {statement} mode..."

if __name__ == "__main__":
    print(start())
