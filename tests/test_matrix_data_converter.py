from matrix_data_converter import MatrixDataConverter
from cfg_matrix_data import ConfigMatrixData
import pytest

testDataInvalid = [
    # count rows
    (3, 2, 'int', [],
    'matrix have incorrect count of rows'),
    (3, 2, 'int', [['-3', '5'], ['3', '-8']],
    'matrix have incorrect count of rows'),
    (3, 2, 'int', [['3', '5'], ['3', '-8'], ['-6', '-8'], ['2', '0']],
    'matrix have incorrect count of rows'),
    # count varues in row
    (3, 4, 'int', [['3', '5', '-5', '9'], ['-3', '6', '9'], ['6', '8', '-8', '6']],
    'there are more or less values in the row#1 than needed'),
    (3, 4, 'int', [['3', '-5', '5', '9', '0'], ['3', '6', '9', '-5'], ['6', '-8', '8', '6']],
    'there are more or less values in the row#0 than needed'),
    # not integer number
    (3, 4, 'int', [['3', '5', '', '9'], ['-3', '6', '9', '-5'], ['6', '8', '-8', '6']],
    'not integer number in position row 0, column 2'),
    (3, 4, 'int', [['3', '5', '-7', '9'], ['-3', '6.5', '9', '-5'], ['6', '8', '-8', '6']],
    'not integer number in position row 1, column 1'),
    (3, 4, 'int', [['3', '5', '-7', '9'], ['-3', '6', '9', '-5'], ['6', 'value', '-8', '6']],
    'not integer number in position row 2, column 1'),
    # not a number
    (3, 4, 'double', [['3.5', '5.8', '', '9.5'], ['-3', '0.6', '2.9', '-5.9'], ['6.5', '8.2', '-8.0', '6']],
    'not number in position row 0, column 2'),
    (3, 4, 'double', [['3.5', '5.8', '0.6', '9.5'], ['-3', 'value', '2.9', '-5.9'], ['6.5', '8.2', '-8.0', '6']],
    'not number in position row 1, column 1'),
    (3, 4, 'double', [['3.5', '5.8', '0.6', '9.5'], ['-3', '0.6', '2.9', '-5.9'], ['6,5', '8.2', '-8.0', '6']],
    'not number in position row 2, column 0')
    ]

testIdsInvalid = [
    # count rows
    'invalid count rows (empty)', 'invalid count rows (less)', 'invalid count rows (more)',
    # count varues in row
    'invalid count values in row (less)', 'invalid count values in row (more)',
    # not integer number
    'not integer number (empty)', 'not integer number (double)', 'not integer number (string)',
    # not a number
    'not number (empty)', 'not number (string)', 'not number (\',\' in number)'
]

testDataValid = [
    # int to int
    (3, 4, 'int', [['3', '5', '-5', '9'], ['-3', '6', '9', '9'], ['6', '8', '-8', '6']],
                 [[3, 5, -5, 9], [-3, 6, 9, 9], [6, 8, -8, 6]]),
    # int to double
    (3, 4, 'double', [['3', '5', '-5', '9'], ['-3', '6', '9', '9'], ['6', '8', '-8', '6']],
                    [[3.0, 5.0, -5.0, 9.0], [-3.0, 6.0, 9.0, 9.0], [6.0, 8.0, -8.0, 6.0]]),
    # double to double
    (3, 4, 'double', [['3.5', '5.8', '0.6', '9.5'], ['-3.1', '0.6', '2.9', '-5.9'], ['6.5', '8.2', '-8.0', '6.3']],
                    [[3.5, 5.8, 0.6, 9.5], [-3.1, 0.6, 2.9, -5.9], [6.5, 8.2, -8.0, 6.3]]),
]

testIdsValid =  [ 'int to int', 'int to double', 'double to double']

@pytest.mark.parametrize('row, column, typeVal, list_values, expMsg', testDataInvalid, ids = testIdsInvalid)
def test_convert_invalid_args(row, column, typeVal, list_values, expMsg):
    with pytest.raises(Exception, match = expMsg):
        config = ConfigMatrixData(row, column, typeVal)
        MatrixDataConverter().convert(config, list_values)

@pytest.mark.parametrize('row, column, typeVal, list_values, list_answers', testDataValid, ids = testIdsValid)
def test_convert_valid_args(row, column, typeVal, list_values, list_answers):
    config = ConfigMatrixData(row, column, typeVal)
    assert MatrixDataConverter().convert(config, list_values) == list_answers
