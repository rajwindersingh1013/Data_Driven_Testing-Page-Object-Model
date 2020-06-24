from unittest import TestLoader, TestSuite, TextTestRunner
from Test.Scripts.test_RegistrationPage import Tests_RegistrationPage
from Test.Scripts.test_LoginPage import TestsLoginPage
import testtools as testtools


if __name__ == "__main__":

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(Tests_RegistrationPage),
        loader.loadTestsFromTestCase(TestsLoginPage)
        ))

#run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

