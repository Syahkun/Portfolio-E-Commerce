from blueprints import db
from flask_restful import fields
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import text
from datetime import datetime
from sqlalchemy.orm import relationship


class ReviewProduk(db.Model):
    __tablename__ = "table_review_produk"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gambar = db.Column(db.String(255))
    review = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    transaction_detail_id = db.Column(
        db.Integer, db.ForeignKey('transaction_detail.id'))

    response_fields = {
        'id': fields.Integer,
        'gambar': fields.String,
        'review': fields.String,
        'created_at': fields.DateTime,
        'updated_at': fields.DateTime,
        'transaction_detail_id': fields.Integer
    }

    def __init__(self, gambar, review):
        self.gambar = gambar
        self.review = review

    def __repr__(self):
        return '<ReviewProduk %r>' % self.id
