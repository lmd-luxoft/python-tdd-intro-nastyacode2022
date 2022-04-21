from add import add

def test_2_3_1_should_be_6():
    expression = '2,3,1'
    expected = 6

    actual = add(expression)

    assert actual == expected
