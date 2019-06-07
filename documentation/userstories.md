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
	


