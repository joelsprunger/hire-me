from website import app
from os import environ

# app.config["SECRET_KEY"] = environ.get("SECRET_KEY")
app.config["SECRET_KEY"] = "mysecretkey"

if __name__ == "__main__":
    app.run(debug=True)