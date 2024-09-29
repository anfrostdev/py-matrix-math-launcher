class InputDataReader:

    def input_cfg(self, fileName, separator):
        try:
            with open(fileName, 'r') as f:
                cfgMatrix = f.readline().rstrip('\n').split(separator)
        except:
            raise Exception(f'Something wrong with open file: {fileName}')

        return cfgMatrix

    def input_matrix_data(self, fileName, cfgMatrix, separator):
        rows = cfgMatrix.get_count_rows()
        columns = cfgMatrix.get_count_columns()
        try:
            with open(fileName, 'r') as f:
                # Skip first line
                f.readline()
                dataMatrix = []
                countRows = 0
                temp = f.readline().rstrip('\n').split(separator)
                while temp != ['']:
                    countRows += 1
                    if countRows > rows:
                        raise Exception('there are more rows in the file than needed')

                    if len(temp) != columns:
                        raise Exception(f'there are more(less) values in the row#{countRows} than needed')

                    dataMatrix.append(temp)
                    temp = f.readline().rstrip('\n').split(separator)
                if countRows < rows:
                    raise Exception('there are less rows in the file than needed')
        except Exception as err:
            raise Exception(f'error with open file "{fileName}": {err}')

        return dataMatrix
