class Model:
    def __init__(self, cn, cs):
        # storing the connection and cursor object
        self.cn = cn
        self.cs = cs
    
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
            self.cs.callproc(procname=proc_name, args=proc_args)
            self.cn.commit()
            # on success
            return "200"
        except Exception:
            # on failure
            return "404"
        
