# Asennusohje

## Sovelluksen asennus paikallisesti

Vaatimuksena Python (vähintään versio 3.5) asennettuna.

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

## Sovelluksen asennus Herokuun

Vaatimuksena Heroku-käyttäjätili, jolle on kirjauduttu (esimerkiksi selaimella).

* Mikäli sovellusta ei ole liitetty versionhallintaan, tee se komennolla **git init** juurikansiossa
(Tee myös commit ja poista ylimääräiset tiedostot versionhallinnasta.)
* Luo Herokuun uusi sovellus komennolla **heroku create** 
(voit antaa sovellukselle myös valitsemasi nimen komennolla **heroku create _nimi_**. Mikäli nimeä ei määritellä, Heroku nimeää sovelluksen automaattisesti satunnaisella nimellä.)
* Sovelluksen kansiossa luo yhteys versionhallintaan komennolla **git remote add heroku _sovelluksenosoiteherokussa_**
* Lähetä sovellus herokuun komennolla **git push heroku master**
* Luo Herokuun ympäristömuuttuja HEROKU komennolla **heroku config:set HEROKU=1**
* Lisää Herokuun tietokanta komennolla **heroku addons:add heroku-postgresql:hobby-dev**
* Nyt sovellus on käytettävissä Herokussa sille luodussa osoitteessa.
