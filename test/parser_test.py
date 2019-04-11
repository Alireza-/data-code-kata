from core.parser import Parser

import pytest


class TestParser():

    @pytest.fixture
    def parser(self):
        return Parser()

    def test_input_file_not_exist(self, parser):
        with pytest.raises(Exception) as e:
            parser.convert_fixed_width_to_csv('./fixed-width/spec.json', 'non-exist-file.txt', 'output_file',',')

    def test_generated_csv_structure(self, parser, mocker):
        mocker.patch('core.generator.Generator.get_file_spec', return_value=[['f1', 'f2'], ['2', '3'], 'false', '', ''])
        data = parser.parse_fixed_width_data('./fixed-width/spec.json', [' ll  mOD '], '|')
        assert 'll|mOD' == data

    def test_parse_fixed_width_data_with_header(self, parser, mocker):
        mocker.patch('core.generator.Generator.get_file_spec', return_value=[['f1', 'f2'], ['2', '3'], 'true', '', ''])
        data = parser.parse_fixed_width_data('./fixed-width/spec.json', ['  f1  f2 \n ll  mOD '], '|')
        assert 2 == len(data.split('\n'))


    def test_parse_fixed_width_data_without_header(self, parser, mocker):
        mocker.patch('core.generator.Generator.get_file_spec', return_value=[['f1', 'f2'], ['2', '3'], 'false', '', ''])
        data = parser.parse_fixed_width_data('./fixed-width/spec.json', [' ll  mOD '], '|')
        assert 1 == len(data.split('\n'))