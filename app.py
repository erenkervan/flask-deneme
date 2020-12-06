from flask import Flask, request, jsonify, render_template
# Flask: uygulamayi olusturmak icin
# request: gelen veriyi almak icin
# jsonify: JSON formatinda cikti dondurmek icin
# render_template: HTML sayfasi "render"lamak icin
#from sklearn.externals import joblib # Pickle ile deserialization
import joblib
app = Flask(__name__) # uygulama olustur
clr = joblib.load("rf_model.pkl") # modeli oku

@app.route('/predict', methods=["POST"])
def predict():
    # modeli predict icinde okursaniz
    # her istek geldiginde dosyadan yeni bir model olusturulacak
    # bunu engellemek icin global tanimladik
    global clr
    data = request.form # form verisini al
    data = [data["data_1"],data["data_2"],data["data_3"],data["data_4"],data["data_5"],data["data_6"],data["data_7"],data["data_8"]] # form verisi
    # Burada gelen veriyi "sanitize" etmeniz sizin faydaniza olur.
    # Kullanici girdisine asla guvenmeyin.
    res = int(clr.predict([data]))
    # veriyi [ [..degerler] ] seklinde modele verip tahmin aldik
    #return jsonify([res]) # JSON formatinda dondurelim
    return render_template('web.html', prediction_text='Sonuç {}'.format(res))

@app.route('/', methods=["GET"])
def home():
    # arayuzu koddan ayiralim
    return render_template("web.html")

if __name__ == "__main__":
    app.run(debug=True)