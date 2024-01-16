from pydantic import BaseModel


class RecordSchema(BaseModel):
    id: int
    target: int
    age: int
    gender: int
    child_total: int
    dependants: int
    socstatus_work_fl: int
    socstatus_pens_fl: int
    fl_presence_fl: int
    own_auto: int
    family_income: int
    personal_income: float
    loan_num_total: int
    loan_num_closed: int
    last_credit: float
    term: int
    fst_payment: float


class UserDataSchema(BaseModel):
    age: int
    gender: int
    child_total: int
    dependants: int
    socstatus_work_fl: int
    socstatus_pens_fl: int
    fl_presence_fl: int
    own_auto: int
    family_income: int
    personal_income: float
    loan_num_total: int
    loan_num_closed: int
    last_credit: float
    term: int
    fst_payment: float
