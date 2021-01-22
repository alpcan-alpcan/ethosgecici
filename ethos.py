
#coding: UTF-8


from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")




if __name__ == "__main__":   #bunu yazdığımızda kodlar yenilendiğinde (kaydetmeyle birlikte) server yayını kesmeye gerek kalmıyor.
    app.run(debug=True)