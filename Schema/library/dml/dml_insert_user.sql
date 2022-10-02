INSERT INTO library.user

(
    user_id, 
    first_name, 
    last_name,
    email,
    password,
    phone_number,
    fees,
    status, 
    created_id, 
    created_dtm, 
    modified_id, 
    modified_dtm
) 

VALUES 
(
    1, 
    'Super', 
    'Admin',
    'superadmin@sglib.com',
    '12345678',
    '9999898985',
    NULL, 
    1, 
    1, 
    CURRENT_TIMESTAMP, 
    1,
    CURRENT_TIMESTAMP
);



