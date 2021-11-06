from flask import Flask, render_template, request, redirect, url_for, flash, jsonify;
import convGcode
import ocr2

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        print(request.files)
        print(request.form)
        file = request.files["file"]
        file.save("temp.jpg")
        equation = ocr2.run("temp.jpg")
        convGcode.main(equation)
    return render_template("index.html")

if __name__ == "__main__":
    app.run("0.0.0.0",debug=False)