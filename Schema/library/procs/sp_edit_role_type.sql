-- call library.sp_edit_role_type (@err, 1,3,null,null,0);


DROP PROCEDURE IF EXISTS library.sp_edit_role_type;

DELIMITER $$
CREATE PROCEDURE library.sp_edit_role_type(OUT error_code INT
				       ,IN in_app_user_id INT                                       
                                       ,IN in_role_type_id INT
                                       ,IN in_role_type_name VARCHAR(50)
                                       ,IN in_role_type_desc VARCHAR(500)				       
                                       ,IN in_status TINYINT)

BEGIN
SET error_code=-2;

UPDATE library.role_type 
SET 	
        role_type_name     = IFNULL(in_role_type_name, role_type_name),
        role_type_desc     = IFNULL(in_role_type_desc, role_type_desc),
        status        = IFNULL(in_status, status),
        modified_id   = in_app_user_id
        
WHERE
        role_type_id = in_role_type_id;

SET error_code=0;  

END$$
DELIMITER ;



