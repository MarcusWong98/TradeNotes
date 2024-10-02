from pydantic import BaseModel


class Role(BaseModel):
    name: str
    description: str = None
    enable_block: bool = False
    enable_reset_pwd: bool = False
    enable_sql: bool = False
    
