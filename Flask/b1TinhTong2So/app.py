from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    tong = None
    ds = []
    if request.method == "POST":
        a = int(request.form["a"])
        b = int(request.form["b"])
        ds = request.form["ds"]
        tong = a + b

    # tong --> index.html voi ten la kq
    # return render_template("index.html", kq=tong)
    items = ["Táo", "Cam", "Chuối"]

    return render_template("index.html", kq_tong=tong, hoaqua=items, game=ds)


if __name__ == "__main__":
    app.run(debug=True)
