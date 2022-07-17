from enum import Enum


class RegEx(Enum):
    BRAND = (
        r'^[a-zA-Z]{2,100}$',
        'only letters min 2 max 100 char'
    )

    def __init__(self,pattern:str,msg:str|list[str]):
        self.pattern = pattern
        self.msg = msg
        
