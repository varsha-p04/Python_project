from enum import Enum
from typing import List, Optional
from uuid import UUID
from pydantic import conint,conlist, BaseModel, Field, field_validator
from datetime import datetime


class Size(Enum):
    small = 'small'
    medium = 'medium'
    big = 'big'


class Status(Enum):
    created = 'created'
    progress = 'progress'
    cancelled = 'cancelled'
    dispatched = 'dispatched'
    delivered = 'delivered'

class OrderItemSchema(BaseModel):
    product: str
    size: Size
    quantity: Optional[int] = Field(1, ge=1 , strict=True)
    @field_validator('quantity')
    def quantity_non_nullabable(cls, value):
        if value is None:
            raise ValueError('quantity many not be none')
        return value
    



class CreatedOrderSchema(BaseModel):
    order: List[OrderItemSchema] = Field(..., min_items=1)

class GetOrderSchema(CreatedOrderSchema):
    id: UUID
    created: datetime
    Status: Status

class GetOrdersSchema(BaseModel):
    orders: List[GetOrderSchema]