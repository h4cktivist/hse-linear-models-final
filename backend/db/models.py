from sqlalchemy import Column, Integer, Float
from .init import Base


class Record(Base):
    __tablename__ = 'data'

    id = Column(Integer, primary_key=True, name='id')
    target = Column(Integer)
    age = Column(Integer)
    gender = Column(Integer)
    child_total = Column(Integer)
    dependants = Column(Integer)
    socstatus_work_fl = Column(Integer)
    socstatus_pens_fl = Column(Integer)
    fl_presence_fl = Column(Integer)
    own_auto = Column(Integer)
    family_income = Column(Integer)
    personal_income = Column(Float)
    loan_num_total = Column(Integer)
    loan_num_closed = Column(Integer)
    last_credit = Column(Float)
    term = Column(Integer)
    fst_payment = Column(Float)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
