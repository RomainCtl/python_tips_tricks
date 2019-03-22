from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import synonym
from src.ext import db
from datetime import datetime

IN_DATE_FORMAT = '%Y/%m/%d %H:%M:%S' # 2014/09/02 00:00:00 exemple of input date (format can easy change)
OUT_DATE_FORMAT = '%H:%M:%S %d/%m/%Y'

# exemple with MySQL DB
TABLE_ARGS = {'mysql_engine':'InnoDB','mysql_charset':'utf8','mysql_collate':'utf8_general_ci'}

class User(db.Model):
    __table__ = 'user'
    __table_args__ = TABLE_ARGS
    # Columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(45))
    lastname = db.Column(db.String(45))
    
    # Create new property
    @hybrid_property
    def fullname(self):
        return self.firstname + " " + self.lastname

class Blog(db.Model):
    __table__ = 'blog'
    __table_args__ = TABLE_ARGS
    # Columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.String(128), default="")
    _entry_date = db.Column('entry_date', db.DateTime, default=datetime.utcnow)
    
    # other way to do rather than create '@hybrid_property' (i already get some problem with hyprid_property and Date type)
    @property
    def entry_date(self):
        return self._entry_date.strftime(OUT_DATE_FORMAT)
    
    @entry_date.setter
    def entry_date(self, date):
        self._entry_date = datetime.strptime(date, IN_DATE_FORMAT)
    
    entry_date = synonym('_entry_date', descriptor=entry_date)
    
    
    
    
