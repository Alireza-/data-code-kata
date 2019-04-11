from string import ascii_letters
from random import choice, randint

import json
import logging


class Generator:
    """
    A generic class for creating file in different format.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def generate_fixed_width_file(self, file_spec, record_no, output_file):
        data = self.generate_fixed_width_rows(file_spec, record_no)
        self.write_file(data, output_file)

    def get_file_spec(self, file):
        """
        read and return file spec.

        :param file: file spec
        :type file: string
        :return: list
        """

        try:
            with open(file) as json_file:
                data = json.load(json_file)
                column_names = data['ColumnNames'].split(',')
                offsets = data['Offsets'].split(',')
                include_header = data['IncludeHeader']
                input_encoding = data['InputEncoding']
                output_encoding = data['OutputEncoding']
        except FileNotFoundError as error:
            self.logger.error(error)

        return column_names, offsets, include_header, input_encoding, output_encoding

    def generate_fixed_width_rows(self, file_spec, record_no):
        """
        Generate a fixed width file as per the provided spec.

        :param file_spec: a json file that defines the spec for the output file.
        :type file_spec: string
        :param record_no: number of records in file.
        :type record_no: int
        :param output_file: output file name and path.
        :type output_file: string
        :return: fixed width rows
        :rtype string
        """

        column_names, offsets, include_header, input_encoding, output_encoding = self.get_file_spec(file_spec)

        content = ''
        if include_header.lower() == 'true':
            for offset, column_name in zip(offsets, column_names):
                column_name = column_name.strip()
                column_name += ' ' * (int(offset) - len(column_name) + 1)
                content = content + ' ' + column_name
            content += '\n'

        for i in range(record_no, 0, -1):
            random_string = ''
            for offset in offsets:
                random_string = random_string + ' ' + self.random_string_generator(int(offset)) + ' '
            content += random_string
            content += '\n'

        return content

    def write_file(self, content, output_file):
        """
        write the data to a file.

        :param data: data
        ":type data: string
        :return: none
        """
        try:
            with open(output_file, 'w') as file:
                file.write(content)
            self.logger.info("The expected file created in the following path: {}".format(output_file))
        except EnvironmentError as error:
            self.logger.error(error)

    def random_string_generator(self, length):
        """
        Generate a random strings.

        :param length: output string length.
        :type length: int
        :return: string
        """
        return "".join(choice(ascii_letters) for x in range(randint(length, length)))
