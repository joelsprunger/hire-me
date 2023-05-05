from website import app
from os import environ

app.config["SECRET_KEY"] = environ.get("SECRET_KEY")

if __name__ == "__main__":
    app.run()