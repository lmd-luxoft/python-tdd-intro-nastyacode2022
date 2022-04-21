from add import add

def test_2_3_1_should_be_6():
    expression = '2,3,1'
    expected = 6

    actual = add(expression)

    assert actual == expected

def test_should_be_error_blank():
    expression = ''
    expected = -1

    actual = add(expression)

    assert actual == expected, f"Error"


def test_should_be_error_wrong_input():
    expression = 'thfhhft'
    expected = -1

    actual = add(expression)

    assert actual == expected, f"Error"


def test_should_be_error_one_digit():
    expression = '333'
    expected = -1

    actual = add(expression)

    assert actual == expected, f"Error"



