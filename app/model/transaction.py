from typing import Union
from pydantic import BaseModel

class Transaction(BaseModel):
    name: str
    description: Union[str, None] = None