# request potrafi odczytywac metody htmla
# render renderuje htmla od razu do strony
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')  # dodajemy dekorator. jak zawsze we flasku strona glowna
def index():
    # zwroci nam nasz html i zredneruje go jako homepage
    return render_template("frontend.html")


# kolejna sciezka, ktora prowadzi nas do success, z deklaracja, ze jest tam uzywana metoda POST
@app.route('/success', methods=["POST"])
def success():
    # Jezeli methoda w route bedzie "POST", a nie "GET"
    if request.method == "POST":
        # zapisz w zmiennej email informacje z htmlu z input email,
        # ktory byl w form, dlatego request.FORM
        email = request.form["email_name"]
        # zapis z inputa height, name height
        height = request.form["height"]
        print(email)
        print(height)
    return render_template("success.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
