class MatrixDataConverter:

    def __is_valid_list_size(self, listValues, value):
        return len(listValues) == value

    def __conversion_matrix_data_to_int(self, config, listData):
        rows = config.get_count_rows()
        columns = config.get_count_columns()

        for i in range(rows):
            if len(listData[i]) != columns:
                raise Exception(f'there are more or less values in the row#{i} than needed')

            for j in range(columns):
                try:
                    listData[i][j] = int(listData[i][j])
                except Exception:
                    raise Exception (f'not integer number in position row {i}, column {j}')

        return True

    def __conversion_matrix_data_to_float(self, config, listData):
        rows = config.get_count_rows()
        columns = config.get_count_columns()

        for i in range(rows):
            if len(listData[i]) != columns:
                raise Exception(f'there are more or less values in the row#{i} than needed')

            for j in range(columns):
                try:
                    listData[i][j] = float (listData[i][j])
                except Exception:
                    raise Exception (f'not number in position row {i}, column {j}')

        return True

    def convert(self, cfgMatrix, listMatrixData):
        if not self.__is_valid_list_size(listMatrixData, cfgMatrix.get_count_rows()):
             raise Exception('matrix have incorrect count of rows')

        typeVal = cfgMatrix.get_type_val()
        if typeVal == 'int':
            self.__conversion_matrix_data_to_int(cfgMatrix, listMatrixData)

        if typeVal == 'double':
            self.__conversion_matrix_data_to_float(cfgMatrix, listMatrixData)

        return listMatrixData
