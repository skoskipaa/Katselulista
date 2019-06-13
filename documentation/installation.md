# Asennusohje

* Lataa GitHubista ohjelmakoodi ZIP-pakettina linkistä **Clone or download -> Download ZIP**
* Pura paketti haluamaasi uuteen kansioon omalla koneellasi.
* Mene sovelluksen juureen, eli kansioon **~/katselulista**
* Luo kansioon virtuaaliympäristö komennolla **python3 -m venv venv**
* Aktivoi virtuaaliympäristö komennolla **source venv/bin/activate**
* Tuo sovelluksen käyttöön tarvittavat riippuvuudet komennolla **pip install -r requirements.txt**
(Asennetaan siis kaikki tiedostossa requirements.txt luetellut kirjastot paikalliseen ympäristöön)
* Nyt sovelluksen voi ajaa (juurikansiossa) komennolla **python run.py**
* Sovelluksen käynnistyttyä sen voi avata selaimessa osoitteessa **localhost:5000**
* Sovelluksen saa sammutettua painamalla terminaalissa **CTRL + C**
