from sqlalchemy import Column, Integer, String
from app.main import Base
from sqlalchemy import Table, Column, Float, Integer, String, DateTime

class Remote(Base):
    __tablename__ = 'remote'
    id = Column('id', Integer, primary_key=True, autoincrement= True)
    command = Column('command', String, nullable=False)
    remote_name =  Column('remote_name',String, nullable=False)

    def __init__(self, id, command, remote_name):
        self.id = id
        self.command = command
        self.remote_name = remote_name