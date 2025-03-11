from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from copy import copy

T = TypeVar('T')

from handler import HandlerBase


class Validator(ABC,HandlerBase[T]):
    def __init__(self, handler:T):
        super().__init__(handler=handler)
    
    def __call__(self):
        return self.validate()
    
    @abstractmethod
    def validate(self) -> bool:
        pass


class ComplexValidator(Validator[None]):
    def __init__(self, ValidatorsList:list[Validator]=[]):
        super().__init__(None)
        self._valid_list=ValidatorsList
        self._validator=iter(self._valid_list)
        self._last_failing_validator = None

    def addValidator(self, validator: Validator):
        self._valid_list.append(validator)
    
    def __iter__(self):
        self._validator=iter(self._valid_list)
        return self
    
    def __next__(self):
        validator = next(self._validator)
        return validator.validate()
    
    def validate(self)->bool:
        if False in self:
            return False
        return True