from datetime import datetime

class Model:
    # constructor
    def __init__(self, cn, cs, super_admin_id):
        # storing the connection and cursor object
        self.cn = cn
        self.cs = cs
        self.super_admin_id = super_admin_id
        self.librarian_id = 1
        self.client_id = 2
        
    
    # user existence checking and then signup
    def signup(self, role : str, credential_dict : dict) -> None:        
        # existence checking
        user_exists = True
        
        try:
            proc_name = "sp_get_user"
            proc_args = [0,
                        None,
                        credential_dict["email"],
                        None,
                        None]
            
            # calling the procs
            self.cs.callproc(proc_name, proc_args)
            # getting all user details
            # if user is there we will get the details but if user not there then we will get None
            user_details = [r.fetchone() for r in self.cs.stored_results()]
                        
            if (None not in user_details):
                user_exists = True
                return ["401", user_exists]
            else:
                user_exists = False                                                           
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
                    print("signup exception")
                    user_credentials = None
                    return ["500", user_credentials]
        except Exception:
            # on failure of checking the user existence
            user_exists = True
            return ["500", user_exists]
        
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
            print("assign role exception")
            role_insert_status = None
            return ["500", role_insert_status]
    
    # handle the user credential checking along with the proper associated role
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
            # otherwise the user exist and we have already received the details of the user
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
    
    # check whether the corresponding role is valid/assigned for/to the given user id
    # this method is called from check_user_existence_role method internally
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
    
    # get all the available details of all the books books
    def get_all_details_all_books(self, query_flag = 0):
        all_books = ""
        try:
            proc_name = "sp_get_book"
            proc_args = [0,
                         None,
                         None,
                         None,
                         None,
                         None,
                         None,
                         None,
                         None]
            
            # calling the procs
            self.cs.callproc(proc_name, proc_args)
            # getting all user details
            all_books = [r.fetchall() for r in self.cs.stored_results()]
        
            return ["200", all_books]
        except Exception:
            all_books = None
            return ["500", all_books]

    
    # same method will be used for 1 - book issue and return
    def book_issue(self, app_user_id, book_id, user_id):
        try:
            # checking whether book id exist and also available for renting
            sql_query = f"SELECT book_id, book_name FROM book WHERE is_rented=0 AND status=1 AND book_id={book_id};"
            
            self.cs.execute(sql_query)
            query_result = self.cs.fetchone()
            
            # if book id exist and available for renting
            if (query_result != None):                      
                now = datetime.now()
                sql_now = now.strftime('%Y-%m-%d %H:%M:%S')
                proc_name = "sp_edit_book"
                proc_args = [0,
                            app_user_id,
                            book_id,
                            user_id,
                            None,
                            None,
                            None,
                            None,
                            None,
                            1,
                            sql_now,
                            None]
                
                self.cs.callproc(proc_name, proc_args)
                self.cn.commit()
                return ["200"]
            else:
                return ["500"]
        except Exception:
            return ["500"]
    
    # same method will be used for - 3, 4, 5
    # get all books, get rented books, get rentable books
    def get_all_books(self,
                      column_names='*',
                      table_name="book",
                      where_clause='1=1',
                      no_of_rows=10,
                      all=True,
                      rows=False):
        try:       
            self.cs.execute(f"SELECT {column_names} FROM {table_name} WHERE status=1 AND {where_clause}")
            if (all == True):
                record_all_list = self.cs.fetchall()
                print(record_all_list)
                return ["200", record_all_list]
            elif (all == False):  
                record_n_list = self.cs.fetchmany(no_of_rows)
                return ["200", record_n_list]
        except Exception:
            record_all_list = None
            return ["500", record_all_list]