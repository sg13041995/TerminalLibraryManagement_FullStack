class Model:
    # constructor
    def __init__(self, cn, cs, super_admin_id):
        # storing the connection and cursor object
        self.cn = cn
        self.cs = cs
        self.super_admin_id = super_admin_id
        self.librarian_id = 1
        self.client_id = 2
        
    
    # user creation
    def signup(self, role : str, credential_dict : dict) -> None:        
        # proc to create the user 
        try:
            proc_name = "sp_create_user"
            proc_args = [0,
                        self.super_admin_id,
                        credential_dict["fname"],
                        credential_dict["lname"],
                        credential_dict["email"],
                        credential_dict["pass1"],
                        credential_dict["ph"],
                        None,
                        0]
            user_credentials = self.cs.callproc(procname=proc_name, args=proc_args)
            self.cn.commit()
            
            # creating/ inserting user role into database
            self.assign_user_role(role, user_credentials[8])
            
            # on success
            return ["200", user_credentials]
        except Exception:
            # on failure
            user_credentials = None
            return ["500", user_credentials]
        
    # user role creation
    def assign_user_role(self, role, user_id):
        role_type_id = None
        role_insert_status = None
        
        # selecting role type id based on the role selected by the user
        if (role == "Client"):
            role_type_id = self.client_id
        elif (role == "Librarian"):
            role_type_id = self.librarian_id
            
        # proc to create user role or assign user role 
        try:
            proc_name = "sp_create_user_role"
            proc_args = [0,
                        user_id,
                        user_id,
                        role_type_id,
                        0]
            role_insert_status = self.cs.callproc(procname=proc_name, args=proc_args)[0]
            self.cn.commit()
            # on success
            return ["200", role_insert_status]
        except Exception:
            # on failure
            role_insert_status = None
            return ["500", role_insert_status]
    
    def check_user_existence_role(self, email, password, role):
        user_details = None
        is_valid_role = None
                
        try:
            proc_name = "sp_get_user"
            proc_args = [0,
                        None,
                        email,
                        password,
                        None]
            
            # calling the procs
            self.cs.callproc(proc_name, proc_args)
            # getting all user details
            user_details = [r.fetchone() for r in self.cs.stored_results()]
            
            # if no records found for the user
            # 404, no user found(None), no question of role validity(None)
            if (None in user_details):
                user_details = None
                return ["404", user_details, is_valid_role]
            else:
                role_type_id = None
                # initially invalid role
                
                # selecting role type id based on the role selected by the user
                if (role == "Client"):
                    role_type_id = self.client_id
                elif (role == "Librarian"):
                    role_type_id = self.librarian_id
                
                # getting user id
                user_id = user_details[0][0]
                
                # calling role validation checking function
                role_validity_response = self.validate_user_id_role(user_id, role_type_id)
                
                # 404, has user details, but wrong role selected(false)
                if (None in role_validity_response[1]):
                    is_valid_role = False
                    return ["404", user_details, is_valid_role]
                else:
                    # 200, has user details, correct role selected(true)
                    is_valid_role = True
                    return ["200", user_details, is_valid_role]
                     
        except Exception:
            # on failure
            user_details = None
            is_valid_role = None
            return ["500", user_details, is_valid_role]             
    
    def validate_user_id_role(self, user_id, role_type_id):
        try:
            proc_name = "sp_get_user_role"
            proc_args = [0,
                        user_id,
                        role_type_id]
            
            # calling the procs
            self.cs.callproc(proc_name, proc_args)
            # getting all user details
            role_validity_details = [r.fetchone() for r in self.cs.stored_results()]
            
            return ["200", role_validity_details]
        except Exception:
            # on failure
            role_validity_details = None
            return ["500", role_validity_details]