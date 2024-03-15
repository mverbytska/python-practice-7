import unittest
import os
from app.io import input


tests_script_dir = os.path.dirname(os.path.abspath(__file__))
my_static_data_dir = os.path.join(tests_script_dir, '..', '..', 'my_static_data')
error_filepath = os.path.join(my_static_data_dir, 'error_file.txt')


class TestInputWithBuiltInFunctions(unittest.TestCase):
    def test_input_string_using_built_func_check_not_existing_file_(self):
        with self.assertRaises(FileNotFoundError):
            input.input_using_built_in_funcs(error_filepath)

    def test_input_string_using_built_func_with_existing_file(self):
        with open('./temp_file.txt', '+w') as temp_write_file:
            temp_write_file.write('Let\'s test this function!')

        test_result = input.input_using_built_in_funcs('./temp_file.txt')
        self.assertEqual(test_result, 'Let\'s test this function!')


if __name__ == '__main__':
    unittest.main()
