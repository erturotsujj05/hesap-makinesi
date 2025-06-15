from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hesapla", methods=["POST"])
def hesapla():
    sayi1 = float(request.form["sayi1"])
    sayi2 = float(request.form["sayi2"])
    islem = request.form["islem"]

    sonuc = 0
    try:
        if islem == "+":
            sonuc = sayi1 + sayi2
        elif islem == "-":
            sonuc = sayi1 - sayi2
        elif islem == "*":
            sonuc = sayi1 * sayi2
        elif islem == "/":
            sonuc = sayi1 / sayi2
    except Exception as e:
        sonuc = f"Hata: {str(e)}"

    return render_template("index.html", sonuc=sonuc)

if __name__ == "__main__":
    app.run(debug=True)
