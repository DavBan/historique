
from typing import TypeVar, Generic
from copy import copy

T = TypeVar('T')
class HandlerBase(Generic[T]):
    def __init__(self, handler: T):
        self._handler:T=handler
    
    def set_handler(self, nHandler: T):
        self._handler = nHandler

    def get_handler(self) -> T:
        return self._handler


        
    