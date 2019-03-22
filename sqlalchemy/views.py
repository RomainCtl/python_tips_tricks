from src.ext import db, ma
from .models import Child, Table1, Table2
from .schemas import ChildSchema
from sqlalchemy.sql import select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm, Table, MetaData
from marshmallow_sqlalchemy import TableSchema
from marshmallow import fields
import sqlalchemy_views

Base = declarative_base()
metadata = MetaData() # important to use different metadata that db.metadata (if not, these View are created as Table when 'db.create_all()' if called)

class View(Table):
    is_view = True

class CreateView(sqlalchemy_views.CreateView):
    def __init__(self, view):
        super().__init__(view.__table__, view.__definition__, or_replace=True)
        
class Cases(Base):
    __table__ = View(
        'cases', metadata,
        db.Column('foo', db.String(10), primary_key=True),
        db.Column('bar',  db.String(45))
    )
    
    __definition__ = select([
        Table1.foo, Table2.barrr.label('bar')
    ]).select_from(
        Table1.__table__ \
        .outerjoin(Table2, Table1.id == Table2.id)
    )
    
    # if you need fictive relationship
    childs = db.relationship(Child,
                             foreign_keys = [ __table__.foo ],
                             primaryjoin  = __table__.c.foo == Child.id,
                             uselist = True)
    
    def __repr__(self):
        return "<Cases %s>" % (self.foo)
        
# Schema with Marshmallow
class CasesSchema(TableSchema):
    childs = ma.Nested(ChildSchema, many=True)
    class Meta:
        table = Cases.__table__
        fields = ('foo', 'bar', 'childs')
        
        
## Creating the view
# after 'db.create_all()'
for view in [Cases]:
    db.engine.execute(CreateView(view))

## Mapping the view
# To allow access to column like basic db.Model ('Cases.foo')
for view in [Cases]:
    if not hasattr(view, '_sa_class_manager'):
        orm.mapper(view, view.__table__)
        
        
## Query a view
schema = CasesSchema(many=True)
datas = db.sessio.query(Cases).all()
json_datas = schema.dumps(datas).data

