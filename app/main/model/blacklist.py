from sqlalchemy import Column, Integer, String, DateTime
import datetime
from app.main import sessionLoader, Base
from sqlalchemy import Table, Column, Float, Integer, String, DateTime

class BlacklistToken(Base):
    """
    Token Model for storing JWT tokens
    """
    __tablename__ = 'blacklist_tokens'

    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String, unique=True, nullable=False)
    blacklisted_on = Column(DateTime, nullable=False)

    def __init__(self, id, token):
        self.id = id
        self.token = token
        self.blacklisted_on = datetime.datetime.now()

    # def __repr__(self):
    #     return '<id: token: {}'.format(self.token)

    @staticmethod
    def check_blacklist(auth_token):
        session = sessionLoader()
        res = session.query(BlacklistToken).filter(BlacklistToken.token==str(auth_token)).first()
        if res: return True
        return False