class OutputDataWriter:

    def output_matrix(self, fileName, cfgMatrix, cfgSeparator, dataMatrix, dataSeparator):
        try:
            with open(fileName, 'w') as fileOut:
                fileOut.write(cfgSeparator.join(list(map(str, cfgMatrix))) + '\n')
                for row in dataMatrix: 
                    fileOut.write(dataSeparator.join(list(map(str, row))) + '\n')
        except:
            raise Exception('Something wrong with open file result')

        return True
