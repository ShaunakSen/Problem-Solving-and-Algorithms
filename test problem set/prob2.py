import re

ERROR_CODE_MESSGAES = {
    -1 : 'String length out of limit',
    -2: 'The password must begin with a latin letter',
    -3: 'The password can consist of Latin letters, numbers, dot and minuses',
    -4: 'the password must end only with a latin letter or number',
    100: 'Password Successful'
}

def password_check_historical(test_string):
    all_errors = []
    if(1<=len(test_string)<=20):
        str_len=len(test_string)
        # first char check
        match_1=re.match("[À-Ö]",test_string[0])
        if(bool(match_1)==True):
            # all chars check
            match_2=re.fullmatch("[À-Ö0-9.-]*", test_string[1:str_len-1])
            if(bool(match_2)==True):
                # last char check
                match_3=re.match("[À-Ö0-9]",test_string[str_len-1])
                if(bool(match_3)==True):
                    return ERROR_CODE_MESSGAES[100]
                else:
                    all_errors.append(-4)
            else:
                all_errors.append(-3)
        else:
            all_errors.append(-2)
    else:
        all_errors.append(-1)
    return all_errors

def password_check(test_string):
    all_error_codes = []
    str_len=len(test_string)
    print (str_len)
    if not (str_len >=1 and str_len <=20):
        all_error_codes.append(-1)
    if str_len > 0:
        # first char check
        match_1=re.match("[À-Ö]",test_string[0])
        if not bool(match_1):
            all_error_codes.append(-2)
        # all chars check
        match_2=re.fullmatch("[À-Ö0-9.-]*", test_string[1:str_len-1])
        if not bool(match_2):
            all_error_codes.append(-3)
        # last char check
        match_3=re.match("[À-Ö0-9]",test_string[str_len-1])
        if not bool(match_3):
            all_error_codes.append(-4)
    
    ## check if any errors ocurred
    if len(all_error_codes) == 0:
        return all_error_codes, ERROR_CODE_MESSGAES[100].strip()
    else:
        message = ""
        for code_ in all_error_codes:
            message += ERROR_CODE_MESSGAES[code_]
            message += " | "
    return all_error_codes, message[:-2].strip()
    

print (password_check(''))