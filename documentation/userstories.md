# User stories

Nr. 1

	Käyttäjänä haluan rekisteröityä sovellukseen.

	INSERT INTO Account
	VALUES (id, name, username, password)

Nr. 2

	Käyttäjänä haluan lisätä järjestelmään katselulistan.
	
	INSERT INTO Watchlist
	VALUES (id, date_created, name, account_id)

Nr. 3

	Käyttäjänä haluan listata kaikki katselulistani.

	SELECT * FROM Watchlist
	WHERE Account.id = nn

Nr. 4

	Käyttäjänä haluan listata tietyn katselulistani sisällön.
	
	SELECT * FROM Content
	JOIN Watchlist ON Content.watchlist_id = Watchlist.id
	WHERE Watchlist.id = nn
	
Nr. 5

	Käyttäjänä haluan nimetä katselulistani uudelleen.
	
	UPDATE Watchlist
	SET name='new name'
	WHERE id = nn
	
Nr. 6

	Käyttäjänä haluan lisätä katselulistalleni sisältöä.
	
	INSERT INTO Content
	VALUES (id, date_created, date_modified, name, length, cdn, watchlist_id)
	
	INSERT INTO Content_Genre ('content_id', 'genre_id')  
	VALUES (nn, mm)
	
Nr. 7

	Käyttäjänä haluan tietää katselulistan ohjelmien yhteiskeston.
	
	SELECT SUM(Content.length) FROM Content
	JOIN Watchlist ON Content.watchlist_id = Watchlist.id
	WHERE Watchlist.id = nn
	
Nr. 8

	Käyttäjänä haluan tietää kaikkien katselulistojeni yhteiskeston.

	SELECT SUM(Content.length) FROM Content
	JOIN Watchlist ON Content.watchlist_id = Watchlist.id
	JOIN Account ON Watchlist.account_id = Account.id
	WHERE Account.id = nn
	
Nr. 9

	Käyttäjänä haluan poistaa katselulistaltani sisältöä.
	
	DELETE FROM Content
	WHERE id = nn
	
	DELETE FROM Content_Genre
	WHERE content_id = nn

Nr. 10

	Käyttäjänä haluan päivittää katselulistan sisällön tietoja.
	
	UPDATE Content
	SET name = 'new name', date_modified = date, length = nn, cdn = 'new cdn'
	WHERE id = nn
	
	UPDATE Content_Genre
	SET genre_id = mm
	WHERE content_id = nn
	
Nr. 11

	Käyttäjänä haluan poistaa katselulistan ja sen sisällön järjestelmästä.
	
	DELETE FROM Content_Genre
	WHERE content_id = mm
	
	DELETE FROM Content
	JOIN Watchlist ON Content.watchlist_id = Watchlist.id
	WHERE watchlist_id = nn
	
	DELETE FROM Watchlist
	WHERE id = nn
	
Nr. 12

	Käyttäjänä haluan lisätä järjestelmään uuden luokittelun.

	INSERT INTO Genre
	VALUES (id, name)
