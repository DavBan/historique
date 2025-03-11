from typing import Callable, Any, Type
from testutils import Test


def _create_tc_class_from_object(cls: Type, instance_init_param:list|dict=[])-> Type[Test]:
    class _test(Test):
        _instance_cls=cls
        _instance_init_param=instance_init_param
        def __init__(self, name, tested_method:Callable, params:list|dict=[], expected_res:Any|None=None):
            if isinstance(self._instance_init_param, list):
                instance = self._instance_cls(*self._instance_init_param)
            else:
                instance = self._instance_cls(**self._instance_init_param)
            self._instance=instance
            super().__init__(name, getattr(self._instance, tested_method.__name__), params, expectedResults=expected_res)
    return _test
        



def create_tc(name:str, tested_method:Callable, expected_res:Any|None=None, params:list|dict=[], cls: type|None = None, instance_init_param:list|dict=[])-> Test:
    test_cls = Test
    if(cls is not None):
        test_cls = _create_tc_class_from_object(cls, testedMethod=tested_method, instance_init_param=instance_init_param)
        return test_cls(name, tested_method, params, expected_res)
    return test_cls(name, tested_method, params, expected_res)

        



