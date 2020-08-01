import prob2


### configure the test_strings to debug if the tests are working properly
test_scenarios = {
    'length_checker': {'test_string': 'ÀÀÀÀ12-.34'},
    'last_character_check': {'test_string': 'ÀÀÀÀ12-.34'},
    'first_character_check': {'test_string': 'ÀÀÀÀ12-.34'},
    'all_characters_check': {'test_string': 'ÀÀÀÀ12-.34'},
    'input_type_check': {'test_string': 'ÀÀÀÀ12-.34'}
}

def test_length(scenario='length_checker'):
    """
    Test to check if the length is within prescribed limits
    """
    test_string = test_scenarios[scenario]['test_string']
    error_codes, message = prob2.password_check(test_string)
    assert -1 not in error_codes, prob2.ERROR_CODE_MESSGAES[-1]

def test_first_character(scenario='first_character_check'):
    """
    Test to check if the first character is valid
    """
    test_string = test_scenarios[scenario]['test_string']
    error_codes, message = prob2.password_check(test_string)
    assert -2 not in error_codes, prob2.ERROR_CODE_MESSGAES[-2]

def test_all_character(scenario='all_characters_check'):
    """
    Test to check if all characters are valid
    """
    test_string = test_scenarios[scenario]['test_string']
    error_codes, message = prob2.password_check(test_string)
    assert -3 not in error_codes, prob2.ERROR_CODE_MESSGAES[-3]

def test_last_character(scenario='last_character_check'):
    """
    Test to check if the last character is valid
    """
    test_string = test_scenarios[scenario]['test_string']
    error_codes, message = prob2.password_check(test_string)
    assert -4 not in error_codes, prob2.ERROR_CODE_MESSGAES[-4]

def test_input_type(scenario='input_type_check'):
    """
    Test to check if the input is of valid type
    """
    test_string = test_scenarios[scenario]['test_string']
    assert isinstance(test_string, str), "Input must be of type: string"