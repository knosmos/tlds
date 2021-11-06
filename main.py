from flask import Flask, render_template, request, redirect, url_for, flash, jsonify;
import convGcode
import ocr

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        print(request.files)
        print(request.form)
        file = request.files["file"]
        file.save("temp.jpg")
        equation = ocr.run("temp.jpg")
        convGcode.main(equation)
    return '''
<!doctype html>
<title>Upload new File</title>
<h1>Upload new File</h1>
<form method=post enctype=multipart/form-data>
    <input type=file name=file>
    <input type=submit value=Upload>
</form>
'''

if __name__ == "__main__":
    app.run("0.0.0.0",debug=False)