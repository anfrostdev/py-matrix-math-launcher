from cfg_matrix_data import ConfigMatrixData

class ConfigBuilder:

    def __init__(self):
        self.CFG_INDEX_ROWS = 0
        self.CFG_INDEX_COLUMNS = 1
        self.CFG_INDEX_TYPE_VAL = 2
        self.CFG_TYPE_VALUE = ['int', 'double']

    def __is_positive(self, value):
        return int(value) > 0

    def __is_integer(self, value):
        try:
            value = int(value)
        except ValueError:
            return False

        return True

    def __is_valid_list_size(self, listValues, value):
        return len(listValues) == value

    def __get_row_num(self, listConfigValues):
        return listConfigValues[self.CFG_INDEX_ROWS] 

    def __get_column_num(self, listConfigValues):
        return listConfigValues[self.CFG_INDEX_COLUMNS] 

    def __get_type_val(self, listConfigValues):
        return listConfigValues[self.CFG_INDEX_TYPE_VAL] 

    def __validate_cfg_matrix(self, listConfigValues):
        if not self.__is_valid_list_size(listConfigValues, 3):
             raise Exception('Config have incorrect count of items')

        row = self.__get_row_num(listConfigValues)
        column = self.__get_column_num(listConfigValues)
        typeVal = self.__get_type_val(listConfigValues)
        if not self.__is_integer(row):
            raise Exception('Count rows is not integer number')

        if not self.__is_positive(row):
            raise Exception('Count rows <= 0')

        if not self.__is_integer(column):
            raise Exception('Count columns is not integer number')

        if not self.__is_positive(column):
            raise Exception('Count columns <= 0')

        if typeVal not in self.CFG_TYPE_VALUE:
            raise Exception('Invalid type value')

        return True

    def build_cfg_matrix_data(self, listConfigValues):
        self.__validate_cfg_matrix(listConfigValues)

        return ConfigMatrixData(
            int(self.__get_row_num(listConfigValues)),
            int(self.__get_column_num(listConfigValues)),
            self.__get_type_val(listConfigValues)
        )

    def build_cfg_to_list(self, configMatrixData):
        return [
            configMatrixData.countRows,
            configMatrixData.countColumns,
            configMatrixData.typeValues
        ]
