def create_dict(keys_list, values_list):
    final_dict = {}
    ## CASE 1: if we have more keys than values
    if len(keys_list) > len(values_list):
        ## assign all the values
        for idx in range(len(values_list)):
            final_dict[keys_list[idx]] = values_list[idx]
        ## for the remaining keys assign the value of None
        for idx2 in range(idx+1, len(keys_list)):
            final_dict[keys_list[idx2]] = None
    ## CASE: equal keys and values OR more values than keys; either way we only assign the keys to values and for the rest we ignore
    else: 
        for idx, key_ in enumerate(keys_list):
            final_dict[key_] = values_list[idx]
    return final_dict


def main():
    keys_list = list(range(1,10))
    values_list = list(range(100, 109))
    final_dict = create_dict(keys_list, values_list)

    print (final_dict)

if __name__=="__main__":
    main()

"""
TEST 1 : if more keys all values should be there
TEST 2: no of None == diff in lengths of keys and values

"""