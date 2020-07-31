import prob1

test_scenarios = {
    'equal_lengths': {'keys': list(range(1, 10)), 'values': list(range(1,10))},
    'more_keys': {'keys': list(range(1, 10)), 'values': list(range(1,5))},
    'more_values': {'keys': list(range(1, 10)), 'values': list(range(1,20))}
}


def test_equal_lengths(scenario='equal_lengths'):
    """
    Test to check if no of keys and values in final dict is same as those of the keys and values passed into the function
    """
    key_list = test_scenarios[scenario]['keys']
    values_list = test_scenarios[scenario]['values']
    final_dict = prob1.create_dict(key_list, values_list)
    assert len(final_dict.keys()) == len(final_dict.values()) == len(key_list) == len(values_list), f"Lengths of keys and values should be same in scenario: {scenario}"

def test_no_null_values(scenario='equal_lengths'):
    """
    Test to check that no None values present in keys or values of the resulting dict
    """
    key_list = test_scenarios[scenario]['keys']
    values_list = test_scenarios[scenario]['values']
    final_dict = prob1.create_dict(key_list, values_list)
    null_in_keys = None in list(final_dict.keys())
    null_in_values = None in list(final_dict.values())
    assert not null_in_keys and not null_in_values, f"No None values should be present in keys or values in scenario: {scenario}"

def test_all_values_present(scenario="more_keys"):
    """
    If there are more keys, all the values should be present in the final dict
    """
    key_list = test_scenarios[scenario]['keys']
    values_list = test_scenarios[scenario]['values']
    final_dict = prob1.create_dict(key_list, values_list)
    values_in_dict = list(final_dict.values())
    print (final_dict, values_in_dict, values_list, values_list in values_in_dict)
    assert all([value_ in values_in_dict for value_ in values_list]), f"All values should be present in scenario: {scenario}"

def test_count_null_values(scenario="more_keys"):
    """
    If there are more keys, None values will be present that that will equal to the diff bw no of keys and values
    """
    key_list = test_scenarios[scenario]['keys']
    values_list = test_scenarios[scenario]['values']
    final_dict = prob1.create_dict(key_list, values_list)
    values_in_dict = list(final_dict.values())
    count_null = sum([1 if value_ is None else 0 for value_ in values_in_dict])
    print (final_dict, count_null)
    assert count_null == len(key_list) - len(values_list), f"Number of values which are None should be equal to difference in no of keys and values in scenario: {scenario}"
    

def test_all_keys_present_and_no_null_values(scenario="more_values"):
    """
    If motre values, these will be ignored, so no None values
    Also all keys should be present in final dict
    """
    key_list = test_scenarios[scenario]['keys']
    values_list = test_scenarios[scenario]['values']
    final_dict = prob1.create_dict(key_list, values_list)
    values_in_dict = list(final_dict.values())
    keys_in_dict = list(final_dict.keys())
    count_null = sum([1 if value_ is None else 0 for value_ in values_in_dict])

    assert count_null == 0 and all(key_ in keys_in_dict for key_ in key_list), f"No None values and all keys should be present in scenario: {scenario}"
    
