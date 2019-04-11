from core.generator import Generator

import pytest


class TestGenerator():

    @pytest.fixture
    def generator(self):
        return Generator()

    def test_spec_file_not_exist(self, generator):
        with pytest.raises(Exception) as e:
            generator.get_file_spec('non-exist-file.txt')

    def test_random_string_generator(self, generator):
        assert 15 == len(generator.random_string_generator(15))
        assert 0 == len(generator.random_string_generator(0))

    def test_generate_fixed_width_rows_with_header(self, generator, mocker):
        mocker.patch('core.generator.Generator.get_file_spec', return_value=[['f1', 'f2'], ['2', '3'], 'true', '', ''])
        data = generator.generate_fixed_width_rows('./fixed-width/spec.json', 10)
        # 10 records + header + a new line in the end = 12
        assert 12 == len(data.split('\n'))

    def test_generate_fixed_width_rows_without_header(self, generator, mocker):
        mocker.patch('core.generator.Generator.get_file_spec', return_value=[['f1', 'f2'], ['2', '3'], 'false', '', ''])
        data = generator.generate_fixed_width_rows('./fixed-width/spec.json', 10)
        # 10 records + a new line in the end = 11
        assert 11 == len(data.split('\n'))

    def test_generate_fixed_width_rows_width(self, generator, mocker):
        mocker.patch('core.generator.Generator.get_file_spec', return_value=[['f1', 'f2'], ['2', '3'], 'false', '', ''])
        data = generator.generate_fixed_width_rows('./fixed-width/spec.json', 2)
        # 9 length =  2 + 3 for each feaild plus two white spaces for each
        assert 9 == len(data.split('\n')[0])
