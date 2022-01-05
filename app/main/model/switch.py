from sqlalchemy import Column, Integer, String
from app.main import Base
from sqlalchemy import Table, Column, Float, Integer, String, DateTime. ForeignKey

class Switch(Base):
    __tablename__ = 'switch'
    switchID = Column(Integer, primary_key=True, autoincrement= True)
    name = Column( String(100), nullable=False)
    status =  Column(Integer, nullable=False)
    userID = Column(Integer, ForeignKey('user.userID'), nullable=False)


    def __init__(self, switchID, name, status, userID):
        self.switchID = switchID
        self.name = name
        self.status = status
        self.userID = userID

    