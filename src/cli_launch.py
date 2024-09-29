from input_data_reader import InputDataReader 

class CliLaunch:

    def __init__(self):
        self.CONFIG_SEPARATOR = ';'
        self.DATA_SEPARATOR = ';'
        self.inputReader = InputDataReader()

    def launch(self, fileNameOne, fileNameTwo, fileNameRes):
        print(f'Open file "{fileNameOne}" and read config matrix one...', end = ' ')
        self.inputReader.input_cfg(fileNameOne, self.CONFIG_SEPARATOR)
        print('Ok')

        print(f'Open file "{fileNameTwo}" and read config matrix two...', end = ' ')
        self.inputReader.input_cfg(fileNameTwo, self.CONFIG_SEPARATOR)
        print('Ok')

        print('Done')

        return True
