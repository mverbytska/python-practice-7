from app.io import input


def main():
    console_value = input.get_input_from_console()
    file_reader_value = input.input_using_built_in_funcs('./my_static_data/simple_text.txt')
    pandas_reader_value = input.input_using_pandas_lib('./my_static_data/addresses.csv')
    print(console_value, '\n', file_reader_value, '\n', pandas_reader_value)

    with open('./my_static_data/output_file', 'w+') as writer_file:
        writer_file.write(f'{console_value}\n')
        writer_file.write(f'{file_reader_value}\n')
        writer_file.write(pandas_reader_value)


if __name__ == '__main__':
    main()
