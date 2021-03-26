import argparse
from ele import App


if __name__ == "__main__":
    __version_info__ = ('0','1','0')
    __version__ = '.'.join(__version_info__)

    parser = argparse.ArgumentParser(prog="ele",
                                        description='KST elevation profiler',
                                        epilog='Pavol Hudák')
    parser.add_argument('-v', '--version', action='version',
                                version='%(prog)s ('+__version__+')')
    parser.add_argument('-c', '--config', dest='config_file_path',
                                action='store',
                                default="./ele/config.yml",
                                help='Path to config file (default: %(default)s)')
    parser.add_argument('-e', '--env', dest='ele_env',
                                action='store',
                                default="production",
                                help='Define execution environment (default: %(default)s)')

    app = App(__version__, parser.parse_args())
    app.run()
    app.finished()
    