from cli_launch import CliLaunch
from cfg_builder import ConfigBuilder
from input_data_reader import InputDataReader
from output_data_writer import OutputDataWriter
from matrix_data_converter import MatrixDataConverter
import MatrixMath

import pytest

testDataInvalid = [
    (
    #size list (config)
    [[], []],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    False,
    [],
    'Config have incorrect count of items'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [[], []],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [],
    False,
    [],
    'Config have incorrect count of items'
    ),
    ([[], []],
    [[], []],
    [],
    [],
    False,
    [],
    'Config have incorrect count of items'
    ),
    #count rows is not integer (config)
    ([['', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    False,
    [],
    'Count rows is not integer number'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [],
    False,
    [],
    'Count rows is not integer number'
    ),
    ([['', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [],
    False,
    [],
    'Count rows is not integer number'
    ),
    ([['value', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    False,
    [],
    'Count rows is not integer number'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['value', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [],
    False,
    [],
    'Count rows is not integer number'
    ),
    ([['value', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['value', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [],
    False,
    [],
    'Count rows is not integer number'
    ),
    ([['3.2', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    False,
    [],
    'Count rows is not integer number'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2.6', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [],
    False,
    [],
    'Count rows is not integer number'
    ),
    ([['0.3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2.5', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [],
    False,
    [],
    'Count rows is not integer number'
    ),
    #count rows <= 0 (config)
    ([['0', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    False,
    [],
    'Count rows <= 0'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['0', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [],
    False,
    [],
    'Count rows <= 0'
    ),
    ([['0', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['0', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [],
    False,
    [],
    'Count rows <= 0'
    ),
    ([['-3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    False,
    [],
    'Count rows <= 0'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['-2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [],
    False,
    [],
    'Count rows <= 0'
    ),
    ([['-3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['-2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [],
    False,
    [],
    'Count rows <= 0'
    ),
    #count columns is not integer (config)
    ([['3', '', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    False,
    [],
    'Count columns is not integer number'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [],
    False,
    [],
    'Count columns is not integer number'
    ),
    ([['3', '', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [],
    False,
    [],
    'Count columns is not integer number'
    ),
    ([['3', 'value', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    False,
    [],
    'Count columns is not integer number'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', 'value', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [],
    False,
    [],
    'Count columns is not integer number'
    ),
    ([['3', 'value', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', 'value', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [],
    False,
    [],
    'Count columns is not integer number'
    ),
    ([['3', '2.5', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    False,
    [],
    'Count columns is not integer number'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '0.4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [],
    False,
    [],
    'Count columns is not integer number'
    ),
    ([['3', '2.9', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4.5', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [],
    False,
    [],
    'Count columns is not integer number'
    ),
    #count columns <= 0 (config)
    ([['3', '0', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    False,
    [],
    'Count columns <= 0'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '0', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [],
    False,
    [],
    'Count columns <= 0'
    ),
    ([['3', '0', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '0', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [],
    False,
    [],
    'Count columns <= 0'
    ),
    ([['3', '-2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    False,
    [],
    'Count columns <= 0'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '-4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [],
    False,
    [],
    'Count columns <= 0'
    ),
    ([['3', '-2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '-4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [],
    False,
    [],
    'Count columns <= 0'
    ),
    #invalid type value (config)
    ([['3', '2', ''], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    False,
    [],
    'Invalid type value'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', ''], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [],
    False,
    [],
    'Invalid type value'
    ),
    ([['3', '2', ''], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', ''], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [],
    False,
    [],
    'Invalid type value'
    ),
    ([['3', '2', '8'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    False,
    [],
    'Invalid type value'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', '2'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [],
    False,
    [],
    'Invalid type value'
    ),
    ([['3', '2', '7'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', '5'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [],
    False,
    [],
    'Invalid type value'
    ),
    ([['3', '2', 'float'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    False,
    [],
    'Invalid type value'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'float'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [],
    False,
    [],
    'Invalid type value'
    ),
    ([['3', '2', 'float'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'float'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [],
    [],
    False,
    [],
    'Invalid type value'
    ),
    #can't multiply: matrix size mismatch
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['5', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    False,
    [],
    'Can\'t multiply'
    ),
    #count rows (matrix)
    ([['3', '2', 'int'], []],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], []],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    True,
    [],
    'matrix have incorrect count of rows'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], []],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [[2, 4, 'int'], []],
    True,
    [],
    'matrix have incorrect count of rows'
    ),
    ([['3', '2', 'int'], []],
    [['2', '4', 'int'], []],
    [[3, 2, 'int'], []],
    [[2, 4, 'int'], []],
    True,
    [],
    'matrix have incorrect count of rows'
    ),
     ([['3', '2', 'int'], [['-3', '5'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], []],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    True,
    [],
    'matrix have incorrect count of rows'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [[2, 4, 'int'], []],
    True,
    [],
    'matrix have incorrect count of rows'
    ),
     ([['3', '2', 'int'], [ ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], []],
    [[2, 4, 'int'], []],
    True,
    [],
    'matrix have incorrect count of rows'
    ),
     ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2'], ['-6', '-8']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], []],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    True,
    [],
    'matrix have incorrect count of rows'
    ),
     ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0'],  ['-3', '15', '9', '-8']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [[2, 4, 'int'], []],
    True,
    [],
    'matrix have incorrect count of rows'
    ),
     ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2'], ['-6', '-8']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0'], ['-3', '15', '9', '-8']]],
    [[3, 2, 'int'], []],
    [[2, 4, 'int'], []],
    True,
    [],
    'matrix have incorrect count of rows'
    ),
    #count varues in row (matrix)
    ([['3', '2', 'int'], [['-3', '5'], ['3'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], []],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    True,
    [],
    'there are more or less values in the row#1 than needed'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '0']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [[2, 4, 'int'], []],
    True,
    [],
    'there are more or less values in the row#1 than needed'
    ),
    ([['3', '2', 'int'], [['3'], ['-3', '5'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], []],
    [[2, 4, 'int'], []],
    True,
    [],
    'there are more or less values in the row#0 than needed'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '-6', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], []],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    True,
    [],
    'there are more or less values in the row#2 than needed'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '5', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [[2, 4, 'int'], []],
    True,
    [],
    'there are more or less values in the row#0 than needed'
    ),
    ([['3', '2', 'int'], [['-3', '5', '0'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0', '15']]],
    [[3, 2, 'int'], []],
    [[2, 4, 'int'], []],
    True,
    [],
    'there are more or less values in the row#0 than needed'
    ),
    #not integer number (matrix)
    ([['3', '2', 'int'], [['-3', '5'], ['3', ''], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], []],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    True,
    [],
    'not integer number in position row 1, column 1'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [[2, 4, 'int'], []],
    True,
    [],
    'not integer number in position row 0, column 2'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['', '2']]],
    [['2', '4', 'int'], [['3', '5', '', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], []],
    [[2, 4, 'int'], []],
    True,
    [],
    'not integer number in position row 2, column 0'
    ),
    ([['3', '2', 'int'], [['-3', '5.5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], []],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    True,
    [],
    'not integer number in position row 0, column 1'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0.5']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [[2, 4, 'int'], []],
    True,
    [],
    'not integer number in position row 1, column 3'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3.1', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3.5', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], []],
    [[2, 4, 'int'], []],
    True,
    [],
    'not integer number in position row 1, column 0'
    ),
    ([['3', '2', 'int'], [['value', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], []],
    [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
    True,
    [],
    'not integer number in position row 0, column 0'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
    [['2', '4', 'int'], [['3', '5', '3', 'value'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
    [[2, 4, 'int'], []],
    True,
    [],
    'not integer number in position row 0, column 3'
    ),
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', 'value']]],
    [['2', '4', 'int'], [['3', 'value', '3', '-8'], ['-6', '-8', '2', '0']]],
    [[3, 2, 'int'], []],
    [[2, 4, 'int'], []],
    True,
    [],
    'not integer number in position row 2, column 1'
    ),
    #not a number (matrix)
    ([['3', '2', 'double'], [['-3', '5.5'], ['', '-8.9'], ['-0.8', '2']]],
    [['2', '4', 'double'], [['3', '-5.5', '0.3', '-8.5'], ['-6.5', '-8.4', '2.1', '0']]],
    [[3, 2, 'double'], []],
    [[2, 4, 'double'], [[3.0,  -5.5, 0.3, -8.5], [-6.5, -8.4, 2.1,  0.0]]],
    True,
    [],
    'not number in position row 1, column 0'
    ),
    ([['3', '2', 'double'], [['-3', '5.5'], ['3.3', '-8.9'], ['-0.8', '2']]],
    [['2', '4', 'double'], [['3', '', '0.3', '-8.5'], ['-6.5', '-8.4', '2.1', '0']]],
    [[3, 2, 'double'], [[-3.0,  5.5], [ 3.3, -8.9], [-0.8,  2.0]]],
    [[2, 4, 'double'], []],
    True,
    [],
    'not number in position row 0, column 1'
    ),
    ([['3', '2', 'double'], [['-3', '5.5'], ['3.3', '-8.9'], ['-0.8', '']]],
    [['2', '4', 'double'], [['', '-5.5', '0.3', '-8.5'], ['-6.5', '-8.4', '2.1', '0']]],
    [[3, 2, 'double'], []],
    [[2, 4, 'double'], []],
    True,
    [],
    'not number in position row 2, column 1'
    ),
    ([['3', '2', 'double'], [['value', '5.5'], ['3.3', '-8.9'], ['-0.8', '2']]],
    [['2', '4', 'double'], [['3', '-5.5', '0.3', '-8.5'], ['-6.5', '-8.4', '2.1', '0']]],
    [[3, 2, 'double'], []],
    [[2, 4, 'double'], [[3.0,  -5.5, 0.3, -8.5], [-6.5, -8.4, 2.1,  0.0]]],
    True,
    [],
    'not number in position row 0, column 0'
    ),
    ([['3', '2', 'double'], [['-3', '5.5'], ['3.3', '-8.9'], ['-0.8', '2']]],
    [['2', '4', 'double'], [['3', '-5.5', '0.3', '-8.5'], ['-6.5', '-8.4', '2.1', 'value']]],
    [[3, 2, 'double'], [[-3.0,  5.5], [ 3.3, -8.9], [-0.8,  2.0]]],
    [[2, 4, 'double'], []],
    True,
    [],
    'not number in position row 1, column 3'
    ),
    ([['3', '2', 'double'], [['-3', '5.5'], ['value', '-8.9'], ['-0.8', '2']]],
    [['2', '4', 'double'], [['3', '-5.5', '0.3', '-8.5'], ['-6.5', '-8.4', 'value', '0']]],
    [[3, 2, 'double'], []],
    [[2, 4, 'double'], []],
    True,
    [],
    'not number in position row 1, column 0'
    ),
    ([['3', '2', 'double'], [['-3', '5.5'], ['3.3', '-8,9'], ['-0.8', '2']]],
    [['2', '4', 'double'], [['3', '-5.5', '0.3', '-8.5'], ['-6.5', '-8.4', '2.1', '0']]],
    [[3, 2, 'double'], []],
    [[2, 4, 'double'], [[3.0,  -5.5, 0.3, -8.5], [-6.5, -8.4, 2.1,  0.0]]],
    True,
    [],
    'not number in position row 1, column 1'
    ),
    ([['3', '2', 'double'], [['-3', '5.5'], ['3.3', '-8.9'], ['-0.8', '2']]],
    [['2', '4', 'double'], [['3', '-5.5', '0,3', '-8.5'], ['-6.5', '-8.4', '2.1', '0']]],
    [[3, 2, 'double'], [[-3.0,  5.5], [ 3.3, -8.9], [-0.8,  2.0]]],
    [[2, 4, 'double'], []],
    True,
    [],
    'not number in position row 0, column 2'
    ),
    ([['3', '2', 'double'], [['-3', '5.5'], ['3.3', '-8.9'], ['-0,8', '2']]],
    [['2', '4', 'double'], [['3', '-5,5', '0.3', '-8.5'], ['-6.5', '-8.4', '2.1', '0']]],
    [[3, 2, 'double'], []],
    [[2, 4, 'double'], []],
    True,
    [],
    'not number in position row 2, column 0'
    ),
    ]

testIdsInvalid = [
    #size list (config)
    'invalid size list config (empty matrix one)',
    'invalid size list config (empty matrix two)',
    'invalid size list config (empty both matrix)',
    #count rows is not integer (config)
    'count rows is not integer number (empty matrix one)',
    'count rows is not integer number (empty matrix two)',
    'count rows is not integer number (empty both matrix)',
    'count rows is not integer number (string matrix one)',
    'count rows is not integer number (string matrix two)',
    'count rows is not integer number (string both matrix)',
    'count rows is not integer number (double matrix one)',
    'count rows is not integer number (double matrix two)',
    'count rows is not integer number (double both matrix)',
    #count rows <= 0 (config)
    'count rows <= 0 (zero matrix one)',
    'count rows <= 0 (zero matrix two)',
    'count rows <= 0 (zero both matrix)',
    'count rows <= 0 (negative matrix one)',
    'count rows <= 0 (negative matrix two)',
    'count rows <= 0 (negative both matrix)',
    #count columns is not integer (config)
    'count columns is not integer number (empty matrix one)',
    'count columns is not integer number (empty matrix two)',
    'count columns is not integer number (empty both matrix)',
    'count columns is not integer number (string matrix one)',
    'count columns is not integer number (string matrix two)',
    'count columns is not integer number (string both matrix)',
    'count columns is not integer number (double matrix one)',
    'count columns is not integer number (double matrix two)',
    'count columns is not integer number (double both matrix)',
    #count columns <= 0 (config)
    'count columns <= 0 (zero matrix one)',
    'count columns <= 0 (zero matrix two)',
    'count columns <= 0 (zero both matrix)',
    'count columns <= 0 (negative matrix one)',
    'count columns <= 0 (negative matrix two)',
    'count columns <= 0 (negative both matrix)',
    #invalid type value (config)
    'invalid type value (empty matrix one)',
    'invalid type value (empty matrix two)',
    'invalid type value (empty both matrix)',
    'invalid type value (number matrix one)',
    'invalid type value (number matrix two)',
    'invalid type value (number both matrix)',
    'invalid type value (incorrect value matrix one)',
    'invalid type value (incorrect value matrix two)',
    'invalid type value (incorrect value both matrix)',
    #can't multiply: matrix size mismatch
    'can\'t multiply: matrix size mismatch',
    #count rows (matrix)
    'invalid count rows (empty matrix one)',
    'invalid count rows (empty matrix two)',
    'invalid count rows (empty both matrix)',
    'invalid count rows (less matrix one)',
    'invalid count rows (less matrix two)',
    'invalid count rows (less both matrix)',
    'invalid count rows (more matrix one)',
    'invalid count rows (more matrix two)',
    'invalid count rows (more both matrix)',
    #count varues in row (matrix)
    'invalid count values in row (less matrix one)',
    'invalid count values in row (less matrix two)',
    'invalid count values in row (less both matrix)',
    'invalid count values in row (more matrix one)',
    'invalid count values in row (more matrix two)',
    'invalid count values in row (more both matrix)',
    #not integer number (matrix)
    'not integer number (empty matrix one)',
    'not integer number (empty matrix two)',
    'not integer number (empty both matrix)',
    'not integer number (double matrix one)',
    'not integer number (double matrix two)',
    'not integer number (double both matrix)',
    'not integer number (string matrix one)',
    'not integer number (string matrix two)',
    'not integer number (string both matrix)',
    #not a number (matrix)
    'not number (empty matrix one)',
    'not number (empty matrix two)',
    'not number (empty both matrix)',
    'not number (string matrix one)',
    'not number (string matrix two)',
    'not number (string both matrix)',
    'not number (\',\' in number matrix one)',
    'not number (\',\' in number matrix two)',
    'not number (\',\' in number both matrix)',
    ]

testDataValid = [
    #int to int
    ([['3', '2', 'int'], [['-3', '5'], ['3', '-8'], ['-8', '2']]],
     [['2', '4', 'int'], [['3', '5', '3', '-8'], ['-6', '-8', '2', '0']]],
     [[3, 2, 'int'], [[-3,  5], [ 3, -8], [-8,  2]]],
     [[2, 4, 'int'], [[3,  5, 3, -8], [-6, -8, 2,  0]]],
     True,
     [[3, 4, 'int'], [[-39, -55, 1, 24], [ 57, 79, -7, -24], [-36, -56, -20, 64]]]
     ),
     #double to double
     ([['3', '2', 'double'], [['-3', '5.5'], ['3.3', '-8.9'], ['-0.8', '2']]],
     [['2', '4', 'double'], [['3', '-5.5', '0.3', '-8.5'], ['-6.5', '-8.4', '2.1', '0']]],
     [[3, 2, 'double'], [[-3.0,  5.5], [ 3.3, -8.9], [-0.8,  2.0]]],
     [[2, 4, 'double'], [[3.0,  -5.5, 0.3, -8.5], [-6.5, -8.4, 2.1,  0.0]]],
     True,
     [[3, 4, 'double'], [[-44.75, -29.7, 10.65, 25.5], [ 67.75, 56.61, -17.7, -28.05], [-15.4, -12.4, 3.96, 6.8]]]
     )
    ]

@pytest.mark.parametrize('strlistOne, strlistTwo, listOne, listTwo, valid, listRes, expMsg', testDataInvalid, ids = testIdsInvalid)
def test_launch_invalid_args(monkeypatch, strlistOne, strlistTwo, listOne, listTwo, valid, listRes, expMsg):
    def mock_input_cfg(self, fileName, separator = ';'):
        if fileName == 'one.txt':
            return strlistOne[0]
        elif fileName == 'two.txt':
            return strlistTwo[0]
        else:
            raise Exception(f'Bad file name {fileName}')

    def mock_validate_possibility_multiply_matrix(configMatrices):
        if configMatrices[0] == listOne[0] and configMatrices[1] == listTwo[0]:
            return valid

        raise Exception('Can\'t multiply')  

    def mock_input_matrix_data(self, fileName, cfgMatrix, separator = ';'):
        if fileName == 'one.txt':
            return strlistOne[1]
        elif fileName == 'two.txt':
            return strlistTwo[1]
        else:
            raise Exception(f'Bad file name {fileName}')

    def mock_multiply_two_matrix(listMatrices):
        print(listMatrices)
        if (listMatrices[0] == listOne[0] and listMatrices[1] == listOne[1]
            and listMatrices[2] == listTwo[0] and listMatrices[3] == listTwo[1]
        ):
            listMatrices[4].append(listRes[0])
            listMatrices[5].append(listRes[1])

            return

        raise Exception('Bad input arg')

    def mock_output_matrix(self, fileName, cfgMatrix, separatorCfg, listMatrix, separatorMtr):
        if cfgMatrix == [listRes[0]] and listMatrix == [listRes[1]]:
            return True

        raise Exception('Multiply bad')

    monkeypatch.setattr(InputDataReader, 'input_cfg', mock_input_cfg)    
    monkeypatch.setattr(InputDataReader, 'input_matrix_data', mock_input_matrix_data)    
    monkeypatch.setattr(MatrixMath, 'validate_possibility_multiply_matrix', mock_validate_possibility_multiply_matrix)
    monkeypatch.setattr(MatrixMath, 'multiply_two_matrix', mock_multiply_two_matrix)
    monkeypatch.setattr(OutputDataWriter, 'output_matrix', mock_output_matrix) 

    with pytest.raises(Exception, match = expMsg):
       CliLaunch().launch('one.txt', 'two.txt', 'res.txt')

@pytest.mark.parametrize('strlistOne, strlistTwo, listOne, listTwo, valid, listRes', testDataValid)
def test_launch_valid_args(monkeypatch, strlistOne, strlistTwo, listOne, listTwo, valid, listRes):
        
    def mock_input_cfg(self, fileName, separator = ';'):
        if fileName == 'one.txt':
            return strlistOne[0]
        elif fileName == 'two.txt':
            return strlistTwo[0]
        else:
            raise Exception(f'Bad file name {fileName}')

    def mock_validate_possibility_multiply_matrix(configMatrices):
        if configMatrices[0] == listOne[0] and configMatrices[1] == listTwo[0]:
            return valid

        raise Exception('Can\'t multiply')  

    def mock_input_matrix_data(self, fileName, cfgMatrix, separator = ';'):
        if fileName == 'one.txt':
            return strlistOne[1]
        elif fileName == 'two.txt':
            return strlistTwo[1]
        else:
            raise Exception(f'Bad file name {fileName}')

    def mock_multiply_two_matrix(listMatrices):
        print(listMatrices)
        if (listMatrices[0] == listOne[0] and listMatrices[1] == listOne[1]
            and listMatrices[2] == listTwo[0] and listMatrices[3] == listTwo[1]
        ):
            listMatrices[4].append(listRes[0])
            listMatrices[5].append(listRes[1])

            return

        raise Exception('Bad input arg')

    def mock_output_matrix(self, fileName, cfgMatrix, separatorCfg, listMatrix, separatorMtr):
        if cfgMatrix == [listRes[0]] and listMatrix == [listRes[1]]:
            return True

        raise Exception('Multiply bad')

    monkeypatch.setattr(InputDataReader, 'input_cfg', mock_input_cfg)    
    monkeypatch.setattr(InputDataReader, 'input_matrix_data', mock_input_matrix_data)    
    monkeypatch.setattr(MatrixMath, 'validate_possibility_multiply_matrix', mock_validate_possibility_multiply_matrix)
    monkeypatch.setattr(MatrixMath, 'multiply_two_matrix', mock_multiply_two_matrix)
    monkeypatch.setattr(OutputDataWriter, 'output_matrix', mock_output_matrix) 

    assert CliLaunch().launch('one.txt', 'two.txt', 'res.txt')
