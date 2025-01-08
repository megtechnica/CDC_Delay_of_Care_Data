import pandas as pd
# import libs


# check that the expected numeric columns are numeric
def type_check_numeric_columns(data) -> tuple:
    valid = ('All', True)
    if data.PANEL_NUM.dtype != 'int64':
        valid = ('PANEL_NUM', False)
    if data.UNIT_NUM.dtype != 'int64':
        valid = ('UNIT_NUM', False)
    if data.STUB_NAME_NUM.dtype != 'int64':
        valid = ('STUB_NAME_NUM', False)
    if data.STUB_LABEL_NUM.dtype != 'float64':
        valid = ('STUB_LABEL_NUM', False)
    if data.YEAR.dtype != 'int64':
        valid = ('YEAR', False)
    if data.AGE_NUM.dtype != 'float64':
        valid = ('AGE_NUM', False)
    if data.ESTIMATE.dtype != 'float64':
        valid = ('ESTIMATE', False)
    if data.SE.dtype != 'float64':
        valid = ('SE', False)
    return valid


def compare_nulls_against_threshold(data) -> bool:
    # set the threshold for acceptable nulls at 75 percent of the
    # total row count, this would probably be unacceptable otherwise
    # I just want to make a graph
    null_threshold = len(data.index) * .75
    acceptable_null_ratio = True
    for column in data:
        nulls_in_column = data[column].isna().sum()
        if null_threshold < nulls_in_column:
            acceptable_null_ratio = False
            break
    return acceptable_null_ratio
