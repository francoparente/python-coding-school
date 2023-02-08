import unittest


class ExtendedTestCase(unittest.TestCase):
    def assert_raises_and_verify(self, a_lambda_to_try, exception_type, error_description, assertions):
        try:
            a_lambda_to_try()
            self.fail()
        except exception_type as error:
            self.assertEqual(error_description, str(error))
            assertions()

    def assert_raises(self, a_lambda_to_try, exception_type, error_description):
        self.assert_raises_and_verify(a_lambda_to_try, exception_type, error_description, lambda: None)


if __name__ == '__main__':
    unittest.main()
