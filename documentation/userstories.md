# User stories


Nr. 1

	Käyttäjänä haluan listata kaikki katselulistani.

	SELECT * FROM Watchlist
	WHERE Account.id = nn

Nr. 2

	Käyttäjänä haluan listata katselulistani sisällön.
	
	SELECT * FROM Content
	JOIN Watchlist ON Content.watchlist_id = Watchlist.id
	WHERE Watchlist.id = nn
	
Nr. 3

	Käyttäjänä haluan tietää katselulistan ohjelmien yhteiskeston.
	
	SELECT SUM(Content.length) FROM Content
	JOIN Watchlist ON Content.watchlist_id = Watchlist.id
	WHERE Watchlist.id = nn
	
Nr. 4

	Käyttäjänä haluan tietää kaikkien katselulistojeni yhteiskeston.

	SELECT SUM(Content.length) FROM Content
	JOIN Watchlist ON Content.watchlist_id = Watchlist.id
	JOIN Account ON Watchlist.account_id = Account.id
	WHERE Account.id = nn
	
Nr. 5

	Käyttäjänä haluan nimetä katselulistani uudelleen.
	
	UPDATE Watchlist
	SET name='new name'
	WHERE id = nn
	
Nr. 6

	Käyttäjänä haluan poistaa katselulistaltani sisältöä.
	
	DELETE FROM Content
	WHERE id = nn

Nr. 7

	Käyttäjänä haluan päivittää katselulistan sisällön tietoja.
	
	UPDATE Content
	SET name='new name', length=nn, category='new category', cdn='new cdn'
	WHERE id = nn
	
Nr. 8

	Käyttäjänä haluan poistaa katselulistan ja sen sisällön järjestelmästä.
	
	DELETE FROM Content
	JOIN Watchlist ON Content.watchlist_id = Watchlist.id
	WHERE watchlist_id = nn
	
	DELETE FROM Watchlist
	WHERE id = nn

Nr. 8

	Käyttäjänä haluan lisätä järjestelmään katselulistan.
	
	INSERT INTO Watchlist
	VALUES (id, date_created, name, account_id)
	
Nr. 9

	Käyttäjänä haluan lisätä katselulistalleni sisältöä.
	
	INSERT INTO Content
	VALUES (id, date_created, date_modified, name, length, category, cdn, watchlist_id)
	

