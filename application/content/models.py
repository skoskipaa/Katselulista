from application import db
from application.lists.models import Watchlist

from sqlalchemy.sql import text



class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    name = db.Column(db.String(100), nullable=False)
    length = db.Column(db.Integer)
    category = db.Column(db.String(30), nullable=False)
    cdn = db.Column(db.String(30), nullable=False)

    watchlist_id = db.Column(db.Integer, db.ForeignKey('watchlist.id'))


    def __init__(self, name, length, category, cdn): 
        self.name = name
        self.length = length
        self.category = category
        self.cdn = cdn

    @staticmethod
    def total_length_of_a_watchlist(id):
        stmt = text("SELECT SUM(Content.length) FROM Content"
                    " JOIN Watchlist ON Content.watchlist_id = Watchlist.id"
                    " WHERE Watchlist.id = :id").params(id=id)
        
        res = db.engine.execute(stmt)

        return res.scalar()

    @staticmethod
    def total_length_for_a_user(id):
        stmt = text("SELECT SUM(Content.length) FROM Content"
                    " JOIN Watchlist ON Content.watchlist_id = Watchlist.id"
                    " JOIN Account ON Watchlist.account_id = Account.id"
                    " WHERE Account.id = :id").params(id=id)
        
        res = db.engine.execute(stmt)

        return res.scalar()

    
