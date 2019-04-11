from core.generator import Generator

import json
import logging


class Parser:
    """
    A generic class for parsing different files.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def convert_fixed_width_to_csv(self, file_spec, input_file, output_file, delimiter):
        """
        parse a fixed width file and write to a csv file.

        :param file_spec:
        :param input_file:
        :param output_file:
        :param delimiter:
        :return:
        """
        try:
            with open(input_file) as file:
                lines = file.readlines()
        except FileNotFoundError as error:
            self.logger.error(error)
        data = self.parse_fixed_width_data(file_spec, lines, delimiter)
        self.write_file(data, output_file)

    def parse_fixed_width_data(self, file_spec, file_lines, delimiter):
        """
        This function parses the fixed width file and generates a csv file with comma as delimiter.

        :param file_spec: file spec.
        :type file_spec: string
        :param file_lines: lines of data
        :type file_lines: list
        :param delimiter: delimiter e.g. comma or pipe
        :type delimiter: char
        :return: none
        """

        column_names, offsets, include_header, input_encoding, output_encoding = Generator().get_file_spec(file_spec)

        header_processed = False
        content = ''
        for line in file_lines:
            if include_header.lower() == 'true' and not header_processed:
                header_processed = True
                index = 2
                for offset in offsets[:len(offsets) - 1]:
                    index += int(offset)
                    s = list(line)
                    s[index] = delimiter
                    line = "".join(s)
                    index += 2
            index = 2
            for offset in offsets[:len(offsets) - 1]:
                index += int(offset)
                n = list(line)
                n[index] = delimiter
                line = "".join(n)
                index += 2
            line = line.replace(' ', '')
            content += line

        return content

    def write_file(self, content, output_file):
        """
        write csv file to disk.

        :param content: data
        :type content: string
        :param output_file: output file
        :type output_file: string
        :return: none
        """
        with open(output_file, mode='w') as csv_file:
            csv_file.write(content)
            self.logger.info("The parsed csv file created in the following path: {}".format(output_file))
