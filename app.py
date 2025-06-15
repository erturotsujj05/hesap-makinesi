import os
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
    port = int(os.environ.get("PORT", 5000))  # Render portu veya varsayılan 5000
    app.run(host="0.0.0.0", port=port, debug=True)
import os
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
    port = int(os.environ.get("PORT", 5000))  # Render tarafından sağlanan portu al, yoksa 5000 kullan
    app.run(host="0.0.0.0", port=port, debug=True)
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hesapla', methods=['POST'])
def hesapla():
    sayi1 = float(request.form['sayi1'])
    islem = request.form['islem']
    sayi2 = float(request.form['sayi2'])
    sonuc = None
    if islem == '+':
        sonuc = sayi1 + sayi2
    elif islem == '-':
        sonuc = sayi1 - sayi2
    elif islem == '*':
        sonuc = sayi1 * sayi2
    elif islem == '/':
        if sayi2 != 0:
            sonuc = sayi1 / sayi2
        else:
            sonuc = "Hata: Sıfıra bölünemez!"
    return render_template('index.html', sonuc=sonuc)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hesapla', methods=['POST'])
def hesapla():
    try:
        sayi1 = float(request.form['sayi1'])
        sayi2 = float(request.form['sayi2'])
        islem = request.form['islem']

        if islem == '+':
            sonuc = sayi1 + sayi2
        elif islem == '-':
            sonuc = sayi1 - sayi2
        elif islem == '*':
            sonuc = sayi1 * sayi2
        elif islem == '/':
            if sayi2 == 0:
                sonuc = 'Sıfıra bölünemez!'
            else:
                sonuc = sayi1 / sayi2
        else:
            sonuc = 'Geçersiz işlem!'

        return render_template('index.html', sonuc=sonuc)

    except Exception as e:
        return render_template('index.html', sonuc='Hata: ' + str(e))

if __name__ == '__main__':
    app.run(debug=True, port=10000)


