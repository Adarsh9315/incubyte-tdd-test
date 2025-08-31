from main import StringCalculator

def test_empty_string_returns_0():
    sc = StringCalculator()
    assert sc.add("") == 0
