import unittest
from app.io import input


error_filepath = './my_static_data/error_file'


class TestInputWithBuiltInFunctions(unittest.TestCase):
    def test_input_string_using_built_func_check_file_existing(self):
        with self.assertRaises(FileNotFoundError):
            input.input_using_built_in_funcs(error_filepath)


if __name__ == '__main__':
    unittest.main()
