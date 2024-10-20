from pydantic import BaseModel
from typing import List


class RuleBase(BaseModel):
    rule_string: str


class RuleCreate(RuleBase):
    pass


class RuleUpdate(RuleBase):
    pass


class RuleInDB(RuleBase):
    id: int
    ast: str

    class Config:
        from_attributes = True





class RuleList(BaseModel):
    id: int
    rule_string: str





class RuleCombine(BaseModel):
    rule_ids: List[int]

from pydantic import BaseModel

class RuleEvaluate(BaseModel):
    rule_id: int
    data: dict

