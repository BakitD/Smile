import os


DEBUG = False if os.getenv("DEBUG") == "False" else True
