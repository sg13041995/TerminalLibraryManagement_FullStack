-- call library.sp_create_user (@err, 1, 'First Name', 'Last Name', 'hello@sglib.com', 'pass123','7896589636', 0, @aid);

DROP PROCEDURE IF EXISTS library.sp_create_user;

DELIMITER $$
CREATE PROCEDURE library.sp_create_user(OUT error_code INT
				              ,IN in_app_user_id INT
                                          ,IN in_first_name VARCHAR(100)
                                          ,IN in_last_name VARCHAR(100)
                                          ,IN in_email VARCHAR(100)
                                          ,IN in_password VARCHAR(100)
                                          ,IN in_phone_number VARCHAR(50)
                                          ,IN in_fees VARCHAR(100)
                                          ,OUT out_user_id INT
                                          )
BEGIN

SET error_code=-2;

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
       (NULL,
       in_first_name, 
       in_last_name,
       in_email,
       in_password,
       in_phone_number,
       in_fees,
        1,
        in_app_user_id,
        CURRENT_TIMESTAMP,
        in_app_user_id,
        CURRENT_TIMESTAMP
       );
       
SET out_user_id=LAST_INSERT_ID();

SET error_code=0;
 
END$$
DELIMITER ;


