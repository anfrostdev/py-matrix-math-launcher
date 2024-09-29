import pytest
from cfg_builder import ConfigBuilder
from cfg_matrix_data import ConfigMatrixData

testDataInvalid = [
    #size list config
    ([], 'Config have incorrect count of items'),
    (['3'], 'Config have incorrect count of items'),
    (['3', 'int'], 'Config have incorrect count of items'),
    (['3', '4', 'int', '5'], 'Config have incorrect count of items'),
    #count rows is not integer
    (['', '4', 'int'], 'Count rows is not integer number'),
    (['value', '4', 'int'], 'Count rows is not integer number'),
    (['3.5', '4', 'int'], 'Count rows is not integer number'),
    #count rows <= 0
    (['0', '4', 'int'], 'Count rows <= 0'),
    (['-3', '4', 'int'], 'Count rows <= 0'),
    #count columns is not integer
    (['3', '', 'int'], 'Count columns is not integer number'),
    (['3', 'value', 'int'], 'Count columns is not integer number'),
    (['3', '4.9', 'int'], 'Count columns is not integer number'),
    #count columns <= 0
    (['3', '0', 'int'], 'Count columns <= 0'),
    (['3', '-4', 'int'], 'Count columns <= 0'),
    #invalid type value
    (['3',' 4', ''], 'Invalid type value'),
    (['3', '4', 'value'], 'Invalid type value') 
    ]

testIdsInvalid = [
    # size list config
    'invalid size list config (empty)',
    'invalid size list config (1 argument)',
    'invalid size list config (2 arguments)',
    'invalid size list config (4 arguments)',
    #count rows is not integer
    'count rows is not integer number (empty)',
    'count rows is not integer number (string)',
    'count rows is not integer number (double)',
    #count rows <= 0
    'count rows <= 0 (zero)',
    'count rows <= 0 (negative)',
    #count columns is not integer
    'count columns is not integer number (empty)',
    'count columns is not integer number (string)',
    'count columns is not integer number (double)',
    #count columns <= 0
    'count columns <= 0 (zero)',
    'count columns <= 0 (negative)',
    #invalid type value
    'invalid type value (empty)',
    'invalid type value (incorrect value)'
    ]

@pytest.mark.parametrize('list_values, expMsg', testDataInvalid, ids = testIdsInvalid)
def test_build_cfg_matrix_data_invalid_args(list_values, expMsg):
    with pytest.raises(Exception, match = expMsg):
        ConfigBuilder().build_cfg_matrix_data(list_values)

@pytest.mark.parametrize(
    'list_values, rows, columns, typeVal',
    [(['3', '4', 'int'], 3, 4, 'int'), (['5', '2', 'double'], 5, 2, 'double')]
)
def test_build_cfg_matrix_data_valid_args(list_values, rows, columns, typeVal):
    config = ConfigBuilder().build_cfg_matrix_data(list_values)
    assert isinstance(config, ConfigMatrixData)
    assert config.get_count_rows() == rows
    assert config.get_count_columns() == columns
    assert config.get_type_val() == typeVal
