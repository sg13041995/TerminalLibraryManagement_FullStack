from configparser import ConfigParser
from mysql.connector import MySQLConnection, Error

#========================================================================================================
# credential parser
#========================================================================================================
def credential_parser():
    # this dict will store the parsed credentials
    credentials = {}
    
    # creating ConfigParser object
    parser = ConfigParser()

    # parser is reading the config file
    parser.read('config.ini')

    # storing the parsed credentials inside the dict
    if parser.has_section('mysql'):
        # returns a list of tuples
        # [('host', '127.0.0.1'), ('database', 'test_db'), ('user', 'root'), ('password', 'abcd')]
        credential_items = parser.items('mysql')

        # putting the credentials inside the dict
        # 0th element is key and 1st element is the value
        for item in credential_items:
            credentials[item[0]] = item[1]
        
        return credentials
    else:
        raise Exception(f"Failed to fetch the credentials")

#===========================================================================================================
# connect to database
#===========================================================================================================

def connect_db(credentials):
    # will store the final connection object
    connection_obj = {}
    cursor_obj = {}
    
    try:
        # trying to connect
        connection_obj = MySQLConnection(**credentials)
        
        # if connected successfully
        if connection_obj.is_connected():
            cursor_obj = connection_obj.cursor()
            
            return connection_obj, cursor_obj 
    except Error as e:
        raise Exception(f"{e}")
       
#===========================================================================================================
# fetch one or all or limited records
#===========================================================================================================

def get_records(cursor_obj, table_name, column_names = '*', where_clause = "1 = 1" , get_all = False, print_all = False):
    
    record_list = []
    
    try:       
        cursor_obj.execute(f"SELECT {column_names} FROM {table_name} WHERE {where_clause}")
        record = cursor_obj.fetchone()
        record_list.append(record)
        
        if (get_all == False):
            return record_list
        else:
            while record is not None:
                record = cursor_obj.fetchone()
                record_list.append(record)
        
        if (print_all == True):
            for record in record_list:
                print(record)
        else:
            pass
       
        return record_list

    except Error as e:
        raise Exception(f"{e}")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#===========================================================================================================
# fetch all or limited records
#===========================================================================================================

def get_all_records(cursor_obj, table_name, column_names = '*', where_clause = "1 = 1" , print_all = False):
       
    try:       
        cursor_obj.execute(f"SELECT {column_names} FROM {table_name} WHERE {where_clause}")
        record_list = cursor_obj.fetchall()
        
        if (print_all == True):
            for record in record_list:
                print(record)
        else:
            pass
       
        return record_list

    except Error as e:
        raise Exception(f"{e}")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#===========================================================================================================
# fetch n number of records
#===========================================================================================================

def get_n_records(cursor_obj, table_name, no_of_rows = 10, column_names = '*', where_clause = "1 = 1" , print_all = False):
       
    try:       
        cursor_obj.execute(f"SELECT {column_names} FROM {table_name} WHERE {where_clause}")
        record_list = cursor_obj.fetchmany(no_of_rows)
        
        if (print_all == True):
            for record in record_list:
                print(record)
        else:
            pass
       
        return record_list

    except Error as e:
        raise Exception(f"{e}")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#===========================================================================================================
# insert one record
#===========================================================================================================

def insert_one_record(connection_obj, cursor_obj, table_name, column_list, value_list):
    PERCENT_S = "%s, "
    column_names = ""
    values = ""
    value_tuple = tuple(value_list)
    
    for item in column_list:
        column_names += f"{item},"
    
    column_names = column_names[:len(column_names)-1]
    
    values = PERCENT_S*(len(value_list))
    values = values[:len(values)-2]

    sql_query = f"INSERT INTO {table_name}({column_names}) VALUES ({values})"
                  
    try:       
        cursor_obj.execute(sql_query,value_tuple)
        connection_obj.commit()

    except Error as e:
        raise Exception(f"{e}")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#===========================================================================================================
# insert multiple records
#===========================================================================================================

def insert_multiple_records(connection_obj, cursor_obj, table_name, column_list, values_list):
    PERCENT_S = "%s, "
    column_names = ""
    values = ""
    
    for item in column_list:
        column_names += f"{item},"
    
    column_names = column_names[:len(column_names)-1]
    
    each_record_length = len(values_list[0])
    
    values = PERCENT_S * each_record_length
    values = values[:len(values)-2]

    sql_query = f"INSERT INTO {table_name}({column_names}) VALUES ({values})"
                  
    try:       
        cursor_obj.executemany(sql_query,values_list)
        connection_obj.commit()

    except Error as e:
        raise Exception(f"{e}")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

