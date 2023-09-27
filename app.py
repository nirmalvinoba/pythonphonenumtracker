from flask import Flask,render_template,request
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

app = Flask(__name__)

# number = "+917358335581"
@app.route('/', methods = ["GET","POST"])
def home():
    if request.method == "POST":

        number = request.form.get("track")
        
        num = phonenumbers.parse(number)
        country = geocoder.description_for_number(num,"en")
        print(geocoder.description_for_number(num, "en"))

        num1 = phonenumbers.parse(number)
        sim = carrier.name_for_number(num1,"en")
        print(carrier.name_for_number(num1,"en"))

        return render_template ("index.html", box = country, bag = sim )
    return render_template ("index.html")

if __name__ == "__main__":
    app.run(debug=True)