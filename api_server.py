from flask import Flask, render_template
import webbrowser

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

### GENRE USER SELECTION


### DECADE SELECTION


### MOVIES OUTPUT


### STREAMINGS AVAILABLE


### LINK TO STREAMING PLATFORM


if __name__ == "__main__":
    app.run()
