-- call library.sp_create_role_type (@err, 1,'Super Admin','This is Super Admin Role',@aid);

DROP PROCEDURE IF EXISTS library.sp_create_role_type;

DELIMITER $$
CREATE PROCEDURE library.sp_create_role_type(OUT error_code INT
				              ,IN in_app_user_id INT
				              ,IN in_role_type_name VARCHAR(100)
                                          ,IN in_role_type_desc VARCHAR(250)
                                          ,OUT out_role_type_id INT
                                          )
BEGIN

SET error_code=-2;

INSERT INTO library.role_type 
       (
        role_type_id, 
        role_type_name, 
        role_type_desc, 
        status,
        created_id,
        created_dtm,
        modified_id,
        modified_dtm
       )
VALUES
       (NULL,
        in_role_type_name,
        in_role_type_desc,
        1,
        in_app_user_id,
        CURRENT_TIMESTAMP,
        in_app_user_id,
        CURRENT_TIMESTAMP
       );
       
SET out_role_type_id=LAST_INSERT_ID();

SET error_code=0;
 
END$$
DELIMITER ;


