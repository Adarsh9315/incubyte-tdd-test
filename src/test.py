from main import StringCalculator

# Step 1: empty string returns 0
def test_empty_string_returns_0():
    sc = StringCalculator()
    assert sc.add("") == 0


# Step 2: single number returns its value
def test_single_number_returns_value():
    sc = StringCalculator()
    assert sc.add("1") == 1
