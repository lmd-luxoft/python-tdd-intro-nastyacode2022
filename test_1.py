

def setup():
    print('basic setup into module')
def teardown():
    print('basic teardown')
def setup_modul():
    print('modul setup')
def teardown_module():
    print('module teardown')
def setup_function(f):
    print(f'dunction {f} setup')
def teardown_function(f):
    print(f'function {f} terminated')

def test_add_2_3_should_be_5():
    a = 2
    b = 3
    expected = 5
    print(f'{a}+{b}={expected}')

    actual = a+b

    assert expected == actual

def test_mul_2_2_should_be_4():

    a = 2
    b = 2
    expected = 4

    print(f'test {a}*{b}={expected}')

    actual = a*b

    assert expected == actual