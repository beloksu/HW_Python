import pytest
from string_utils import StringUtils


class TestStringUtils:

    @pytest.fixture
    def utils(self):
        return StringUtils()

    @pytest.mark.parametrize("input_str, expected", [
        ("skypro", "Skypro"),
        ("sKYPRO", "Skypro"),
        ("", ""),
        ("  whitespace", "  whitespace")
    ])
    def test_capitalize(self, utils, input_str, expected):
        assert utils.capitalize(input_str) == expected

    @pytest.mark.parametrize("input_str, expected", [
        ("   skypro", "skypro"),
        ("skypro   ", "skypro   "),
        ("   ", ""),
        ("", "")
    ])
    def test_trim(self, utils, input_str, expected):
        assert utils.trim(input_str) == expected

    @pytest.mark.parametrize("input_str, delimiter, expected", [
        ("a,b,c,d", ",", ["a", "b", "c", "d"]),
        ("1:2:3", ":", ["1", "2", "3"]),
        ("", ",", []),
        ("a,,b", ",", ["a", "", "b"])
    ])
    def test_to_list(self, utils, input_str, delimiter, expected):
        assert utils.to_list(input_str, delimiter) == expected

    @pytest.mark.parametrize("input_str, symbol, expected", [
        ("SkyPro", "S", True),
        ("SkyPro", "k", True),
        ("SkyPro", "U", False),
        ("", "A", False)
    ])
    def test_contains(self, utils, input_str, symbol, expected):
        assert utils.contains(input_str, symbol) is expected

    @pytest.mark.parametrize("input_str, symbol, expected", [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("SkyPro", "Z", "SkyPro"),
        ("", "A", "")
    ])
    def test_delete_symbol(self, utils, input_str, symbol, expected):
        assert utils.delete_symbol(input_str, symbol) == expected

    @pytest.mark.parametrize("input_str, symbol, expected", [
        ("SkyPro", "S", True),
        ("SkyPro", "P", False),
        ("", "S", False),
        ("Hello", "", True)
    ])
    def test_starts_with(self, utils, input_str, symbol, expected):
        assert utils.starts_with(input_str, symbol) is expected

    @pytest.mark.parametrize("input_str, symbol, expected", [
        ("SkyPro", "o", True),
        ("SkyPro", "y", False),
        ("", "o", False),
        ("Hello", "", True)
    ])
    def test_ends_with(self, utils, input_str, symbol, expected):
        assert utils.ends_with(input_str, symbol) is expected

    @pytest.mark.parametrize("input_str, expected", [
        ("", True),
        ("   ", True),
        ("SkyPro", False),
        ("  a  ", False)
    ])
    def test_is_empty(self, utils, input_str, expected):
        assert utils.is_empty(input_str) is expected

    @pytest.mark.parametrize("input_list, joiner, expected", [
        ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
        (["Sky", "Pro"], ", ", "Sky, Pro"),
        ([], "-", ""),
        (["A", "B", "C"], " - ", "A - B - C")
    ])
    def test_list_to_string(self, utils, input_list, joiner, expected):
        assert utils.list_to_string(input_list, joiner) == expected


if __name__ == "__main__":
    pytest.main()
