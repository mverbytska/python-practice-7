import pandas as pd


def get_input_from_console():
    """
    Gets user's input from console using built-in function input(), and returns it.

    Returns:
        :return: User's value that was written into the input function as an argument.
        :rtype: str
    """
    text = input('Please write your text: ')
    return text


def input_using_built_in_funcs(filename: str):
    """
    Gets input from file, using Python's built-in file reader, of mentioned filename,
    and returns it.
    Args:
        param filename(str): String with file's name from which the input is read.
    Returns:
        :return:Text from input file.
        :rtype: str

    Raises:
        FileNotFoundError if input file does not exist or is not found.
    """
    try:
        with open(filename, 'r') as f:
            text = f.read()
            return text
    except FileNotFoundError:
        raise FileNotFoundError(f'File {filename} not found')


def input_using_pandas_lib(filename: str):
    """
    Gets input from file, using Pandas library, of mentioned filename,
    and returns it.

    Args;
        param filename(str): String with name of the file from which the input is read.
    Returns:
        :return: Text from input file.
        :rtype: str

    Raises:
        FileNotFoundError if input file does not exist or is not found.
    """
    try:
        data = pd.read_csv(filename)
        text = data.to_string(index=False, header=True)
        return text
    except FileNotFoundError:
        raise FileNotFoundError(f'File {filename} not found')



