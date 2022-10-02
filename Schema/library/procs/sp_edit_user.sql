-- call library.sp_edit_user (@err, 1,1,'New First Name', null, null, null, null, null, null);
-- call library.sp_edit_user (@err, 1,null,'New First Name', null, 'superadmin@sglib.com', null, null, null, null);


DROP PROCEDURE IF EXISTS library.sp_edit_user;

DELIMITER $$
CREATE PROCEDURE library.sp_edit_user(OUT error_code INT
				       ,IN in_app_user_id INT                                       
				       ,IN in_user_id INT                                       
                                          ,IN in_first_name VARCHAR(100)
                                          ,IN in_last_name VARCHAR(100)
                                          ,IN in_email VARCHAR(100)
                                          ,IN in_password VARCHAR(100)
                                          ,IN in_phone_number VARCHAR(50)
                                          ,IN in_fees VARCHAR(100)			       
                                       ,IN in_status TINYINT)

BEGIN
SET error_code=-2;

UPDATE library.user 
SET 	
        first_name            = IFNULL(in_first_name,first_name),
        last_name             = IFNULL(in_last_name,last_name),
        password              = IFNULL(in_password,password),
        phone_number          = IFNULL(in_phone_number,phone_number),
        fees                  = IFNULL(in_fees,fees),
        status                = IFNULL(in_status, status),
        modified_id           = in_app_user_id
        
WHERE
        user_id = in_user_id
        OR
        email = in_email;

SET error_code=0;  

END$$
DELIMITER ;



