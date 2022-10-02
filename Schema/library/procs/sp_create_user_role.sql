-- call library.sp_create_user_role (@err, 1, 1, 1,@aid);

DROP PROCEDURE IF EXISTS library.sp_create_user_role;

DELIMITER $$
CREATE PROCEDURE library.sp_create_user_role(OUT error_code INT
				              ,IN in_app_user_id INT
                                          ,IN in_user_id INT
                                          ,IN in_role_type_id INT
                                          ,OUT out_user_role_id INT
                                          )
BEGIN

SET error_code=-2;

INSERT INTO library.user_role 
       (
       user_role_id,
       user_id,
        role_type_id, 
        status,
        created_id,
        created_dtm,
        modified_id,
        modified_dtm
       )
VALUES
       (NULL,
       in_user_id,
        in_role_type_id, 
        1,
        in_app_user_id,
        CURRENT_TIMESTAMP,
        in_app_user_id,
        CURRENT_TIMESTAMP
       );
       
SET out_user_role_id=LAST_INSERT_ID();

SET error_code=0;
 
END$$
DELIMITER ;


