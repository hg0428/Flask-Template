from flask import Flask, render_template, send_file, request
# If you are going all-async, use this instead:
# from Quart import Quart, render_template, send_file, request

app = Flask(__name__)
app.config[
    "TEMPLATES_AUTO_RELOAD"] = True  # Always show the latest changes. Turn off if you wouldn't like you changes to apply instantly


@app.route('/', methods=["GET"])
def homepage():
    print(request.method)  # GET
    print(type(request.args))
    # request.args is a dict-like object containing all the query parameters in the url.
    # So in "https://example.com/page?key=value&key2=value2", request.args would be {"key": "value", "key2": "value2"}
    return render_template("index.html", value="Try changing this in main.py."
                           )  # Sends templates/index.html to the client


@app.route('/other-static-file')
def other_static_file():
    # All files in the static directory will appear under /static/ on your website. But you can use send_file to send other static files.
    return send_file("path-to-file")


@app.route("/@<username>/profile")
def user_profiles(username):
    # Special routes allow you to do cool things like this.
    return f"<h1>Username: {username}</h1>"


@app.after_request
def add_headers(response):
    # Set your headers and stuff here
    response.headers["Content-Security-Policy"] = "base-uri 'self'"
    return response


app.run("0.0.0.0", 8080)  # Run it!
