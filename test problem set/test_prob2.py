import prob2


### configure the test_strings to debug if the tests are working properly
test_scenarios = {
    'length_checker': {'test_sring': 'ÀÀÀÀ12-.34'},
    'last_character_check': {'test_sring': 'ÀÀÀÀ12-.34'},
    'first_character_check': {'test_sring': 'ÀÀÀÀ12-.34'},
    'input_type_check': {'test_sring': 'ÀÀÀÀ12-.34'}
}

def test_length(scenario='length_checker'):
    """
    Test to check if the length is within prescribed limits
    """
    
