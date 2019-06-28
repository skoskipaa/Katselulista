# Tietokanta

Tietokannassa on neljä taulua: Account (käyttäjätili), Watchlist (katselulista), Content (sisältö) ja Genre (sisällön luokittelu). Koska sisältö voi kuulua moneen luokkaan (esim. toiminta ja komedia) ja samassa luokassa on monta sisältöä, näiden välillä on monesta moneen -yhteys. Tietokannassa on tätä yhteyttä varten vielä liitostaulu Content_Genre.

<p align="center"><img src="https://github.com/skoskipaa/Katselulista/blob/master/documentation/pictures/database.png"></p>

## Taulujen luonti eli CREATE TABLE -lauseet

### Account

    CREATE TABLE Account (
      id INTEGER NOT NULL,
      date_created DATETIME,
      date_modified DATETIME,
      name VARCHAR(60) NOT NULL,
      username VARCHAR(60) NOT NULL,
      password VARCHAR(60) NOT NULL,
      PRIMARY KEY (id),
      UNIQUE (username)
      )
    
### Watchlist

    CREATE TABLE Watchlist (
      id INTEGER NOT NULL,
      date_created DATETIME,
      name VARCHAR(200) NOT NULL,
      account_id INTEGER,
      PRIMARY KEY (id),
      FOREIGN KEY (account_id) REFERENCES Account (id)
      )
    
### Content

    CREATE TABLE Content (
      id INTEGER NOT NULL,
      date_created DATETIME,
      date_modified DATETIME,
      name VARCHAR(100) NOT NULL,
      length INTEGER,
      cnd VARCHAR(30) NOT NULL,
      watchlist_id INTEGER,
      PRIMARY KEY (id),
      FOREIGN KEY (watchlist_id) REFERENCES Watchlist (id)
      )
    
### Genre

    CREATE TABLE Genre (
      id INTEGER NOT NULL,
      name VARCHAR(50) NOT NULL,
      PRIMARY KEY (id),
      UNIQUE (name)
      )
    
### Content_Genre

    CREATE TABLE Content_Genre (
      content_id INTEGER NOT NULL,
      genre_id INTEGER NOT NULL,
      FOREIGN KEY (content_id) REFERENCES Content (id),
      FOREIGN KEY (genre_id) REFERENCES Genre (id)
      )

    
## Tietokannasta

Tietokannassa taulujen Watchlist ja Content välillä voisi olla myös monesta moneen -yhteys, eli sama ohjelma voisi olla useamallakin katselulistalla. Tämänhetkisessä toteutuksessa jokainen ohjelma on uniikki, eli todellisuudessa sama ohjelma voi olla syötettynä tietokantaan useaan kertaan. Mikäli monesta moneen -yhteys toteutettaisiin, pitäisi päättää, kuka ohjelman tietoja saa poistaa ja muokata, etteivät yhden käyttäjän tekemät muutokset vaikuttaisi muiden käyttäjien sisältöön epätoivotulla tavalla.

Genre eli ohjelman kategoria olisi voinut olla myös atribuuttina ohjelmalle (Content), mutta ohjelma voidaan luokitella useampaan genreen, kun genre on omana taulunaan.

Koska sovelluksessa ei ole monimutkaisia monen taulun hakukyselyitä, indeksointia ei ole erikseen toteutettu. Toiminnot ovat pääasiassa suoraviivaisia listauksia, joten indeksointiin riittää pääavaimen mukainen indeksointi.

