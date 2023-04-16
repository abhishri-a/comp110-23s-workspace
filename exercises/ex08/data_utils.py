__author__ = "730554082"

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read csv file and return as a list of dicts with a header key"""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header"""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str,str]]) -> dict[str,list[str]]:
    """Reformats data so that it's a dictionary with a column header as keys"""
    result: dict[str,list[str]] = {}
    #loop through keys of one row of table
    first_row: dict[str,str] = table[0]
    for key in first_row:
        # for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], count: int) -> dict[str, list[str]]:
    """Let's the user pick out 'n' amount of rows """
    result: dict[str,list[str]] = {}
    # loop through each column name in the first row
    for column_name in table.keys():
        # extract the first N items in the column
        column_values = table[column_name][:count]
        result[column_name] = column_values      
    return result


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Gives new column which is a subset of the original."""
    result: dict[str, list[str]] = {}
    # loop through each specified column name
    for column_name in columns:
        result[column_name] = table[column_name]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Returns a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    # loop through each column in the first table
    for column_name in table1:
        result[column_name] = table1[column_name]
    # loop through each column in the second table
    for column_name in table2:
        # check to see if the column is already in the last one
        if column_name in result:
            result[column_name].extend(table2[column_name])
        else:
            result[column_name] = table2[column_name]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Returns a dictionary of the counts of each item in the input list"""
    result = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result