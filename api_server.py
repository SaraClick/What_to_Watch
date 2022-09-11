from flask import Flask, render_template, request
import webbrowser

app = Flask(__name__, template_folder='templates', static_folder='static')


# ROUTES TO EACH WEBPAGE
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/genre")
def genre():
    return render_template("genre.html")


@app.route("/decade")
def decade():
    return render_template("decade.html")


@app.route("/movie")
def movie():
    return render_template("movie.html")


@app.route("/streaming")
def streaming():
    return render_template("streaming.html")


# ->TO CONTINUE WITH TUTORIAL: https://www.youtube.com/watch?v=9MHYHgh4jYc


### GENRE USER SELECTION
@app.route("/", methods=["POST", "GET"])
def main_to_genre():
    if request.method == "GET":
        return render_template("/genre")
    else:
        return

### DECADE SELECTION


### MOVIES OUTPUT


### STREAMINGS AVAILABLE


### LINK TO STREAMING PLATFORM


if __name__ == "__main__":
    app.run(debug=True)  # debug=True avoids having to re run server every time after making changes
