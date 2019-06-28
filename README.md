# Katselulistasovellus

Sovelluksen tarkoituksena on luoda työkalu eri suoratoistopalveluista löytyvien elokuvien ja sarjojen järjestämiseksi katselulistoiksi. Sovellus on siis suunnattu käyttäjille, jotka käyttävät useampaa palvelua. Palveluun kirjautunut käyttäjä voi luoda sovellukseen katselulistoja ja lisätä katselulistoilleen elokuvia ja sarjoja eri sisällöntarjoajilta. Sovelluksesta voi hakea sinne lisättyä tietoa ja saada tilastotietoja sinne lisätystä sisällöstä.

## Toiminnot

* Sovellukseen voi luoda käyttäjätunnuksen ja kirjautua. Käyttäjärooleja on vain yksi eli peruskäyttäjä.
* Kirjautunut käyttäjä voi luoda katselulistoja ja nähdä niiden listauksen.
* Kirjautunut käyttäjä voi lisätä katselulistoilleen sisältöä ja tarkastella, päivittää ja poistaa listojensa sisältöä.
* Kirjautunut käyttäjä voi nimetä listan uudelleen.
* Kirjautunut käyttäjä voi poistaa katselulistan sisältöineen.
* Katselulista-listausnäkymässä näytetään kaikkien käyttäjän katselulistojen yhteispituus minuutteina. Jokaisen katselulistan kohdalla näytetään listan sisällön yhteispituus minuutteina.
* Kirjautunut käyttäjä voi lisätä sovellukseen luokittelutyypin.

## Sovellus Herokussa

Sovellukseen kirjautumiseen tarvitaan käyttäjätunnus ja salasana.

Sovellukseen voi joko luoda uuden käyttäjän tai kokeilla sovellusta valmiilla tunnuksilla. Sovelluksessa on valmiiksi  käyttäjät 'Jaska Jokunen' (käyttäjätunnus: 'jaska', salasana: 'ressu') sekä 'Minni Hiiri' ('minni', 'juusto').

**[Katselulistasovellus](https://tranquil-tor-18309.herokuapp.com)**

## Sovelluksesta

### Tietoturva

Kaikki sovelluksen toiminnot käyttäjätunnuksen luomista lukuunottamatta ovat sallittuja vain kirjautuneille käyttäjille. Lisäksi käyttäjän id:llä varmistetaan, että kirjautuneella käyttäjällä on oikeus POST-pyyntöihin vain omiin listoihinsa ja sisältöihinsä ja niiden muokkaukseen polkujen kautta. Salasanat tallennetaan tietokantaan salattuina. Käyttäjän syöttämiä arvoja ei sijoiteta suoraan tietokantakyselyihin ja syöttöihin.

### Havaittuja puutteita ja sovelluksen jatkokehitys

* Kun sovellus otetaan ensimmäisen kerran käyttöön, luokittelulista on tyhjä. Jonkun käyttäjän täytyy siis lisätä genrejä, jotta voi lisätä sisältöä. Genrejä voisi toki lisätä ohjelmallisesti ensimmäisellä käyttökerralla taulujen luonnin yhteydessä, mutta tätä ei ole toteutettu. Tarkoituksena on lisätä sovellukseen ylläpitäjän rooli, jolloin tavallinen käyttäjä ei pääse lisäämään genrejä vaan niiden muokkaus on ylläpitäjän vastuulla. Tämä ominaisuus jäi toistaiseksi toteuttamatta.

* Myöskään genrejen poistoa ei ole toteuttu, koska ne ovat kaikille käyttäjille yhteisiä.

* Sovelluksessa jokainen listoille lisätty ohjelma on tietokannassa oma rivinsä, vaikka todellisuudessa sama ohjelma voisi olla useammallakin listalla (monesta moneen -yhteys). Sovelluksessa tätä ei toteutettu, vaan jokainen käyttäjä saa muokata ja poistaa vapaasti omalle listalleen lisäämiään ohjelmia, jotta yhden käyttäjän tekemät muutokset eivät vaikuta muiden käyttäjien listojen sisältöön.

* Jatkossa sovellukseen voi kehittää hakutoiminnallisuuksia, esimerkiksi ohjelmien haku genren tai palveluntarjoajan perusteella.

* Olisi mielenkiintoista päästä tarkastelemaan myös muiden käyttäjien katselulistoja. Niitä voisi siis merkitä julkisiksi tai yksityisiksi.

* Käyttäjäroolien lisäys, esimerkiksi ylläpitäjä genrejen ja sisällöntarjoajien valikon muokkaamiseen.

## Linkkejä

### [Tietokanta](https://github.com/skoskipaa/Katselulista/blob/master/documentation/database.md)

### [Asennus](https://github.com/skoskipaa/Katselulista/blob/master/documentation/installation.md)

### [Käyttöohje](https://github.com/skoskipaa/Katselulista/blob/master/documentation/instructions.md)

### [User stories](https://github.com/skoskipaa/Katselulista/blob/master/documentation/userstories.md)


