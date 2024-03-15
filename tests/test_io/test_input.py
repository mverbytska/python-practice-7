import unittest
from app.io import input


error_filepath = './error_file.txt'


class TestInputWithBuiltInFunctions(unittest.TestCase):
    def test_input_string_using_built_func_check_non_existing_file_(self):
        with self.assertRaises(FileNotFoundError):
            input.input_using_built_in_funcs(error_filepath)

    def test_input_string_using_built_func_with_existing_file(self):
        with open('./temp_file.txt', '+w') as temp_write_file:
            temp_write_file.write('Let\'s test this function!')

        test_result = input.input_using_built_in_funcs('./temp_file.txt')
        self.assertEqual(test_result, 'Let\'s test this function!')


class TestInputWithPandasLibrary(unittest.TestCase):

    def test_input_using_pandas_with_non_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            input.input_using_pandas_lib(error_filepath)



if __name__ == '__main__':
    unittest.main()
