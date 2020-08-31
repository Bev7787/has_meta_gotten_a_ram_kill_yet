from flask import Flask, render_template
app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True)

@app.route("/")
def hello():
    return render_template('home.html')
@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-cache"
    return response

if __name__ == "__main__":
    app.run()