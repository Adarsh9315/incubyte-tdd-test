from main import StringCalculator
import pytest

# Step 1: empty string returns 0
def test_empty_string_returns_0():
    sc = StringCalculator()
    assert sc.add("") == 0

# Step 2: single number returns its value
def test_single_number_returns_value():
    sc = StringCalculator()
    assert sc.add("1") == 1

# Step 3: two numbers separated by comma
def test_two_numbers_return_sum():
    sc = StringCalculator()
    assert sc.add("1,2") == 3

# Step 4: unknown amount of numbers
def test_many_numbers_return_sum():
    sc = StringCalculator()
    assert sc.add("1,2,3,4,5") == 15

# Step 5: support newline as delimiter
def test_newline_as_delimiter():
    sc = StringCalculator()
    assert sc.add("1\n2,3") == 6

# Step 6: custom single-character delimiter
def test_custom_delimiter():
    sc = StringCalculator()
    assert sc.add("//;\n1;2") == 3

# Step 7: negative numbers throw exception
def test_negatives_raise_exception():
    sc = StringCalculator()
    with pytest.raises(ValueError) as err:
        sc.add("1,-2,3")
    assert "negatives not allowed" in str(err.value).lower()
    assert "-2" in str(err.value)

# Step 8: ignore numbers bigger than 1000
def test_ignore_bigger_than_1000():
    sc = StringCalculator()
    assert sc.add("2,1001") == 2
    assert sc.add("1000,1") == 1001

# Step 9: delimiters of any length
def test_multi_char_delimiter():
    sc = StringCalculator()
    assert sc.add("//[***]\n1***2***3") == 6

# Step 10: multiple delimiters
def test_multiple_delimiters():
    sc = StringCalculator()
    assert sc.add("//[*][%]\n1*2%3") == 6

# Step 11: multiple multi-char delimiters
def test_multiple_multi_char_delimiters():
    sc = StringCalculator()
    assert sc.add("//[**][%%]\n1**2%%3") == 6