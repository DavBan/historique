from action import Action
from _historic_settings import config, ConfigsEnum

class _historique():
    def __init__(self, size:int =config[ConfigsEnum.HISTORY_SIZE]):
        self._max_size=size
        self._history:list[Action]=[]
    
    def _is_history_full(self):
        if(self._max_size > 0):
            return False
        return len(self._history) == self._max_size

    def push_action(self, action:Action):
        if( self._is_history_full() ):
            self._history.pop(0)
        self._history.append(action)
    
    def cancel_last_action(self):
        action = self._history.pop()
        action.cancel_action()

historique_global=_historique()