from simple import commandManager
from simple import create_app

from simple.extensions import app


if __name__ == "__main__":
    create_app(app)
    commandManager.run()
