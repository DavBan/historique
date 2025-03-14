from testing.testutils import Test, Tester, create_tc
import datetime


from validation import Validator, ComplexValidator


class ValidateTest(Validator):
    def __init__(self, validate:bool = True):
        self.valid = validate

    def validate(self):
        return self.valid

validator_tc =[
    ValidateTest(True),
    ValidateTest(False)
]

class ValidatorTester(Tester):
    def __init__(self):

        super().__init__("Class_Validator_Test", "This function tests the validator Class that provide a validate function", "./ValidatorTest_{}.log".format(datetime.datetime.today().strftime('%d-%m-%Y_%H-%M-%S')), listoftest=validator_tc)

validator_test = Tester(
    "Class_Validator_Test",
    "This function tests the validator Class that provide a validate function", 
    "./ValidatorTest_{}.log".format(datetime.datetime.today().strftime('%d-%m-%Y_%H-%M-%S')), 
    [
        create_tc(
            "Validator_validate_True",
            None,
            True,
            cls=ValidateTest,
            instance_init_param=[True]
        ),
        create_tc(
            "Validator_validate_False",
            None,
            False,
            cls=ValidateTest,
            instance_init_param=[False]
        )
    ]
)
complexxvalidator_test = Tester(
    "Class_Complexe_Validator_Test",
    desc="This Test tests the ComplexValidator Class that provide a validate function",
    logfile="./ComplexValidatorTest_{}.log".format(datetime.datetime.today().strftime('%d-%m-%Y_%H-%M-%S')),
    listoftest=[
        create_tc(
            "ComplexeValidator_validate_false_only",
            ComplexValidator.validate,
            False,
            [],
            ComplexValidator,
            [
                [
                    ValidateTest(False)
                ]
            ]
        ),
        create_tc(
            "ComplexeValidator_validate_true_only",
            ComplexValidator.validate,
            True,
            [],
            ComplexValidator,
            [
                [
                    ValidateTest(True)
                ]
            ]
        ),
        create_tc(
            "ComplexeValidator_validate_two_Validator_false_first",
            ComplexValidator.validate,
            False,
            [],
            ComplexValidator,
            [
                [
                    ValidateTest(False),
                    ValidateTest(True)
                ]
            ]
        ),
        create_tc(
            "ComplexeValidator_validate_two_Validator_false_second",
            ComplexValidator.validate,
            False,
            [],
            ComplexValidator,
            [
                [
                    ValidateTest(True),
                    ValidateTest(False)
                ]
            ]
        ),
        create_tc(
            "ComplexeValidator_validate_two_Validator_true",
            ComplexValidator.validate,
            True,
            [],
            ComplexValidator,
            [
                [
                    ValidateTest(True),
                    ValidateTest(True)
                ]
            ]
        ),
        create_tc(
            "ComplexeValidator_validate_two_Validator_false",
            ComplexValidator.validate,
            True,
            [],
            ComplexValidator,
            [
                [
                    ValidateTest(False),
                    ValidateTest(False)
                ]
            ]
        )
    ]
)

if __name__ == "__main__":
    validator_test.run_all_tests()
    complexxvalidator_test.run_all_tests()