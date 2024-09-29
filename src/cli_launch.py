from input_data_reader import InputDataReader
from cfg_builder import ConfigBuilder
from matrix_data_converter import MatrixDataConverter
import MatrixMath 

class CliLaunch:

    def __init__(self):
        self.CONFIG_SEPARATOR = ';'
        self.DATA_SEPARATOR = ';'
        self.inputReader = InputDataReader()
        self.configBuilderMatrix = ConfigBuilder()
        self.matrixDataConverter = MatrixDataConverter()

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

        print(f'Open file "{fileNameOne}" and read matrix one data...', end = ' ')
        dataMatrixOne = self.matrixDataConverter.convert(
            configMatrixOne,
            self.inputReader.input_matrix_data(
                fileNameOne,
                configMatrixOne,
                self.DATA_SEPARATOR
            )
        )
        print('Ok')

        print(f'Open file "{fileNameTwo}" and read matrix two data...', end = ' ')
        dataMatrixTwo = self.matrixDataConverter.convert(
            configMatrixTwo,
            self.inputReader.input_matrix_data(
                fileNameTwo,
                configMatrixTwo,
                self.DATA_SEPARATOR
            )
        )
        print('Ok')

        print('Start multiply...', end = ' ')
        configMatrixResult = []
        dataMatrixResult = []
        MatrixMath.multiply_two_matrix(
            (
                self.configBuilderMatrix.build_cfg_to_list(configMatrixOne),
                dataMatrixOne,
                self.configBuilderMatrix.build_cfg_to_list(configMatrixTwo),
                dataMatrixTwo,
                configMatrixResult,
                dataMatrixResult
            )
        )
        print('Ok')

        print('Done')

        return True
