from src.ext import db
from sqlalchemy.sql import select
from sqlalchemy import orm, Table, MetaData
from marshmallow_sqlalchemy import TableSchema
from marshmallow import fields
import sqlalchemy_views

metadata = MetaData() # important to use differente metadata that db.metadata (if not, these View are created as Table)

class View(Table):
    is_view = True

class CreateView(sqlalchemy_views.CreateView):
    def __init__(self, view):
        super().__init__(view.__view__, view.__definition__, or_replace=True)
        
class Cases:
    __view__ = View(
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
    
    def __repr__(self):
        return "<Cases %s>" % (self.numero)
        
# Schema with Marshmallow
class CasesSchema(TableSchema):
    class Meta:
        fields = ('foo', 'bar')
        
        
## Creating the view
# after create_all()
for view in [Cases]:
    db.engine.execute(CreateView(view))
    
## Mapping the view
for view in [Cases]:
    if not hasattr(view, '_sa_class_manager'):
        orm.mapper(view, view.__view__)
        
        
## Query a view
schema = CasesSchema(many=True)
datas = db.sessio.query(Cases).all()
json_datas = schema.dumps(datas).data

