from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hesapla", methods=["POST"])
def hesapla():
    try:
        sayi1 = float(request.form["sayi1"])
        sayi2 = float(request.form["sayi2"])
        islem = request.form["islem"]

        if islem == "+":
            sonuc = sayi1 + sayi2
        elif islem == "-":
            sonuc = sayi1 - sayi2
        elif islem == "*":
            sonuc = sayi1 * sayi2
        elif islem == "/":
            if sayi2 == 0:
                sonuc = "Hata: Bir sayı sıfıra bölünemez."
            else:
                sonuc = sayi1 / sayi2
        else:
            sonuc = "Geçersiz işlem"
    except Exception as e:
        sonuc = f"Hata: {str(e)}"

    return render_template("index.html", sonuc=sonuc)

if __name__ == "__main__":
    app.run(debug=True)
