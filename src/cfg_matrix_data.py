class ConfigMatrixData:

    def __init__(self, rows = 0, columns = 0, typeVal = ''):
        self.countRows = rows
        self.countColumns = columns
        self.typeValues = typeVal

    def set_count_rows(self, value):
        self.countRows = value

    def set_count_columns(self, value):
        self.countColumns = value

    def set_count_type_val(self, value):
        self.typeValues = value

    def get_count_rows(self):
        return self.countRows

    def get_count_columns(self):
        return self.countColumns

    def get_type_val(self):
        return self.typeValues

    #ToDo: implements verbose output
    def print_config(self):
        return f'Rows: {self.countRows}; Colomns: {self.countColumns}; Type: {self.typeValues}'
