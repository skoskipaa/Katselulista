# User stories


Nr. 1

	Käyttäjänä haluan listata kaikki katselulistat.

	SELECT * FROM Katselulista

Nr. 2

	Käyttäjänä haluan etsiä katselulistaltani sisältöä suoratoistopalvelun perusteella perusteella.

	SELECT * FROM Ohjelma
	JOIN OhjelmaKatselulista ON OhjelmaKatselulista.ohjelma_id = Ohjelma.id
	JOIN Katselulista ON Katselulista.id = OhjelmaKatselulista.katselulista_id
	WHERE Ohjelma.nimi = 'haettava_ohjelma'

