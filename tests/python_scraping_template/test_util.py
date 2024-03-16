from python_scraping_template.util import parse_numbers_from_text, simple_format_time


class TestSimpleFormatTime:
    def test_zero_seconds(self):
        assert simple_format_time(0) == "0時間0分0秒"

    def test_under_one_minute(self):
        assert simple_format_time(30) == "0時間0分30秒"

    def test_one_minute(self):
        assert simple_format_time(60) == "0時間1分0秒"

    def test_over_one_minute(self):
        assert simple_format_time(90) == "0時間1分30秒"

    def test_one_hour(self):
        assert simple_format_time(3600) == "1時間0分0秒"

    def test_over_one_hour(self):
        assert simple_format_time(3660) == "1時間1分0秒"

    def test_multiple_hours_minutes_seconds(self):
        assert simple_format_time(5432) == "1時間30分32秒"

    def test_large_number_of_seconds(self):
        assert simple_format_time(86399) == "23時間59分59秒"


class TestParseNumbersFromText:
    def test_extract_single_number(self):
        assert parse_numbers_from_text("ここには100人います。") == "100"

    def test_extract_multiple_numbers(self):
        assert (
            parse_numbers_from_text("この部屋には10個の椅子と20個のテーブルがあります。") == "1020"
        )

    def test_extract_numbers_with_spaces(self):
        assert parse_numbers_from_text("合計で 2.5 時間かかりました。") == "2.5"

    def test_extract_numbers_mixed_with_letters(self):
        assert parse_numbers_from_text("Version 2.0.1がリリースされました。") == "2.01"

    def test_no_numbers_present(self):
        assert parse_numbers_from_text("ここには数値が含まれていません。") == ""

    def test_numbers_with_special_characters(self):
        assert parse_numbers_from_text("現在の支援総額12,345,678円です。") == "12345678"

    def test_empty_string(self):
        assert parse_numbers_from_text("") == ""
