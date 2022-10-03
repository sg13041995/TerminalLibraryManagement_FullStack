def name_validator(fname : str, lname : str) -> bool:
    validation_status = False
    validator_list = []
    if ((fname != '') and (lname != '')):
        validator_list.append(True)
    else:
        validator_list.append(False)
                    
    if ((len(fname) >= 3) and (len(lname) >= 3)):
        validator_list.append(True)
    else:
        validator_list.append(False)
    
    if (False in validator_list):
        validation_status = False
    else:
        validation_status = True
    
    return validation_status

def email_validator(email : str) -> bool:
    validation_status = False
    validator_list = []
    if (email != ''):
        validator_list.append(True)
    else:
        validator_list.append(False)
    
    if (False in validator_list):
        validation_status = False
    else:
        validation_status = True
    
    return validation_status
        
def password_validator(pass1 : str, pass2 : str) -> bool:
    validation_status = False
    validator_list = []
    if ((pass1 != '') and (pass2 != '')):
        validator_list.append(True)
    else:
        validator_list.append(False)

    if ((len(pass1) >= 8) and (len(pass2) >= 8)):
        validator_list.append(True)
    else:
        validator_list.append(False)
        
    if (pass1 == pass2):
        validator_list.append(True)
    else:
        validator_list.append(False)
                    
    if (False in validator_list):
        validation_status = False
    else:
        validation_status = True
    
    return validation_status

def ph_no_validator(ph_no):
    validation_status = False
    validator_list = []
    if (ph_no != ''):
        validator_list.append(True)
    else:
        validator_list.append(False)

    if ((len(ph_no) >= 10) and (len(ph_no) <= 15)):
        validator_list.append(True)
    else:
        validator_list.append(False)
                    
    if (False in validator_list):
        validation_status = False
    else:
        validation_status = True
    
    return validation_status