from core.parser import Parser
from core.generator import Generator

import logging.config
import configparser


class Runner:
    """
    This class takes care of initialization of program and ruuning the tasks.
    """

    def __init__(self):
        logging.config.fileConfig('logging.ini')
        self.logger = logging.getLogger(__name__)

        self.config = configparser.ConfigParser()
        self.config.read('./config/config.ini')

    def run(self):
        """
        Entry point for the program.

        :return: none
        """
        self.logger.info("Fixed width file generator is starting ...")
        generator = Generator()
        generator.generate_fixed_width_file(self.config['FILE']['SPEC_FILE'],
                                            int(self.config['FILE']['NO_OF_RECORDS']),
                                            self.config['FILE']['FIXED_WIDTH_FILE'])

        self.logger.info("Fixed width file parser is starting ...")
        parser = Parser()
        parser.convert_fixed_width_to_csv(self.config['FILE']['SPEC_FILE'],
                                          self.config['FILE']['FIXED_WIDTH_FILE'],
                                          self.config['FILE']['CSV_FILE'],
                                          self.config['FILE']['DELIMITER'])


if __name__ == "__main__":
    runner = Runner()
    runner.run()
