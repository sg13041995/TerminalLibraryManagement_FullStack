class Model:
    # constructor
    def __init__(self, cn, cs):
        # storing the connection and cursor object
        self.cn = cn
        self.cs = cs
    
    # user creation
    def signup(self, role : str, credential_dict : dict) -> None:        
        # proc to create the user 
        try:
            proc_name = "sp_create_user"
            proc_args = [0,
                        1,
                        credential_dict["fname"],
                        credential_dict["lname"],
                        credential_dict["email"],
                        credential_dict["pass1"],
                        credential_dict["ph"],
                        None,
                        0]
            user_id = self.cs.callproc(procname=proc_name, args=proc_args)[8]
            self.cn.commit()
            
            # creating/ inserting user role into database
            self.assign_user_role(role, user_id)
            
            # on success
            return ["200", user_id]
        except Exception:
            # on failure
            user_id = None
            return ["500", user_id]
        
    # user role creation
    def assign_user_role(self, role, user_id):
        role_type_id = 2
        # selecting role type id based on the role selected by the user
        if (role == "Client"):
            role_type_id = 2
        elif (role == "Librarian"):
            role_type_id = 1
            
        # proc to create user role or assign user role 
        try:
            proc_name = "sp_create_user_role"
            proc_args = [0,
                        user_id,
                        user_id,
                        role_type_id,
                        0]
            insert_status = self.cs.callproc(procname=proc_name, args=proc_args)[0]
            self.cn.commit()
            # on success
            return ["200", insert_status]
        except Exception:
            # on failure
            insert_status = None
            return ["500", insert_status]
        
        
