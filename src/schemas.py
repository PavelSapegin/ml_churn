from typing import List, Literal

from pydantic import BaseModel, Field


class Customer(BaseModel):
    customer_id: int
    credit_score: int = Field(ge=300, le=850)
    country: Literal["France", "Germany", "Spain"]
    gender: Literal["Male", "Female"]
    age: int = Field(ge=18, le=100)
    tenure: int = Field(ge=0, le=10)
    balance: float = Field(ge=0, le=1_000_000)
    products_number: int = Field(ge=1)
    credit_card: bool
    active_member: bool
    estimated_salary: float = Field(ge=0)


class BatchRequest(BaseModel):
    customers: List[Customer]
