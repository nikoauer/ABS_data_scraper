from flask import Flask

app = Flask(__name__)

@app.route("/SA2Code/<int:code>")
def hello_world(code):
    return f"Hello, {code}!</p>"
 
if __name__ == "__main__":
    app.run()