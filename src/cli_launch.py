from input_data_reader import InputDataReader
from cfg_builder import ConfigBuilder
import MatrixMath 

class CliLaunch:

    def __init__(self):
        self.CONFIG_SEPARATOR = ';'
        self.DATA_SEPARATOR = ';'
        self.inputReader = InputDataReader()
        self.configBuilderMatrix = ConfigBuilder()

    def launch(self, fileNameOne, fileNameTwo, fileNameRes):
        print(f'Open file "{fileNameOne}" and read config matrix one...', end = ' ')
        configMatrixOne = self.configBuilderMatrix.build_cfg_matrix_data(
            self.inputReader.input_cfg(fileNameOne, self.CONFIG_SEPARATOR)
        )
        print('Ok')

        print(f'Open file "{fileNameTwo}" and read config matrix two...', end = ' ')
        configMatrixTwo = self.configBuilderMatrix.build_cfg_matrix_data(
            self.inputReader.input_cfg(fileNameTwo, self.CONFIG_SEPARATOR)
        )
        print('Ok')

        if not MatrixMath.validate_possibility_multiply_matrix(
            (
                self.configBuilderMatrix.build_cfg_to_list(configMatrixOne),
                self.configBuilderMatrix.build_cfg_to_list(configMatrixTwo)
            )
        ):
            raise Exception('Can\'t multiply: matrix size mismatch')

        print('Matrices of corresponding dimensions, can multiply')

        print('Done')

        return True
