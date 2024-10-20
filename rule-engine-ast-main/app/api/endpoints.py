from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session
from app.schemas.rule_schema import RuleCreate, RuleEvaluate, RuleCombine
from app.services.rule_service import RuleService


router = APIRouter()


# Create a new rule
@router.post("/rules/create")
async def create_rule(rule: RuleCreate, session: AsyncSession = Depends(get_session)):
    rule_service = RuleService(session)
    return await rule_service.create_rule(rule)


# Combine multiple rules by IDs
@router.post("/rules/combine")
async def combine_rules(rule_combine: RuleCombine, session: AsyncSession = Depends(get_session)):
    print(rule_combine)  
    rule_service = RuleService(session)
    return await rule_service.combine_rules(rule_combine.rule_ids)




# Evaluate a specific rule
from fastapi import HTTPException

@router.post("/rules/evaluate")
async def evaluate_rule(rule_eval: RuleEvaluate, session: AsyncSession = Depends(get_session)):
    try:
        rule_service = RuleService(session)
        return await rule_service.evaluate_rule(rule_eval.rule_id, rule_eval.data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


