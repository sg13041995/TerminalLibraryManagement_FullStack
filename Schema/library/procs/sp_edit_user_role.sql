-- call library.sp_edit_user_role (@err, 1,3,null,null,0);


DROP PROCEDURE IF EXISTS library.sp_edit_user_role;

DELIMITER $$
CREATE PROCEDURE library.sp_edit_user_role(OUT error_code INT
				       ,IN in_app_user_id INT
                                       ,IN in_user_role_id INT                                       
                                       ,IN in_user_id INT
                                       ,IN in_role_type_id INT			       
                                       ,IN in_status TINYINT)

BEGIN
SET error_code=-2;

UPDATE library.user_role 
SET 	
        user_id         = IFNULL(in_user_id,user_id),
        role_type_id            = IFNULL(in_role_type_id,role_type_id),
        status        = IFNULL(in_status, status),
        modified_id   = in_app_user_id
        
WHERE
        user_role_id = in_user_role_id;

SET error_code=0;  

END$$
DELIMITER ;



