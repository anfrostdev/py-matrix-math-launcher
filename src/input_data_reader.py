class InputDataReader:

    def input_cfg(self, fileName, separator):
        try:
            with open(fileName, 'r') as f:
                cfgMatrix = f.readline().rstrip('\n').split(separator)
        except:
            raise Exception(f'Something wrong with open file: {fileName}')

        return cfgMatrix
