from testing.testutils import Test, Tester
import datetime


from validation import Validator, ComplexValidator

class HandlerTest():
    def __init__(self, stub:bool=True):
        self._stub = stub
        pass
    
    @property
    def stub(self):
        return self._stub
    @stub.setter
    def stub(self, s: bool):
        self._stub = s

    def test(self)-> bool:
        return self.stub



class ValidateTest(Validator[HandlerTest], Test):
    def __init__(self, validate:bool = True):
        Test.__init__(self, name="Validator_validate_"+str(validate), testedMethod=self.validate, parameters=[], expectedResults=validate)
        Validator.__init__(self, HandlerTest(validate))

    def validate(self):
        return self.get_handler().test()

validator_tc =[
    ValidateTest(True),
    ValidateTest(False)
]

class ValidatorTester(Tester):
    def __init__(self):

        super().__init__("Class_Validator_Test", "This function tests the validator Class that provide a validate function", "./ValidatorTest_{}.log".format(datetime.datetime.today().strftime('%d-%m-%Y_%H-%M-%S')), listoftest=validator_tc)

validator_test = ValidatorTester()
validator_test.run_all_tests()