from abc import ABC, abstractmethod
from collections.abc import Callable
from __future__ import annotations

from historique import historique_global
from handler import HandlerBase
from validation import Validator

class Action(ABC, HandlerBase):
    def __init__(self, handler: T, validator:Validator|None, actionhook:Callable[[Action], None]=historique_global.push_action):
        super(Action, self).__init__(handler=handler)
        self._valid = validator
        self._action_hook= actionhook
    
    def set_validator(self, nvalid:Validator):
        self._valid = nvalid
    
    def has_validator(self):
        return self._valid != None
    

    def __call__(self, *args, **kwds):
        self.do_action(args, kwds)
    
    def do_action(self, *args, **kwargs):
        if self.has_validator() and not self._valid():
            self.cancel_action()
            return
        self._action_hook(self)

    @abstractmethod
    def cancel_action(self):
        pass