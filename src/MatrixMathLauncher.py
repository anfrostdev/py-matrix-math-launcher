import sys
from cli_launch import CliLaunch

class Main:

    def main():
        try:
            if len(sys.argv) != 4:
                raise Exception('Incorrect amount agruments')

            CliLaunch().launch(sys.argv[1], sys.argv[2], sys.argv[3])
        except Exception as e:
            print('Error: ', e, file = sys.stderr)

            return 1

        return 0

exit(Main.main())
