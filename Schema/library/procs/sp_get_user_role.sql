-- call library.sp_get_user_role(@err,null,null);

DELIMITER $$

DROP PROCEDURE IF EXISTS library.sp_get_user_role$$

CREATE  PROCEDURE library.sp_get_user_role(OUT error_code INT
                                          ,IN in_user_id INT
                                          ,IN in_role_type_id INT
                                   )
BEGIN
SET error_code = -2;
SET @q = CONCAT('

select  user_role_id,
        user_id,
        role_type_id, 
        status,
        created_id,
        created_dtm,
        modified_id,
        modified_dtm
        
  FROM 
        library.user_role
     
 WHERE  1 = 1  ');
 
 IF in_user_id IS NOT NULL THEN
 SET @q = CONCAT(@q,' AND user_id = ',in_user_id);
 END IF;

 IF in_role_type_id IS NOT NULL THEN
 SET @q = CONCAT(@q,' AND role_type_id = ',in_role_type_id);
 END IF;
 
 SET @q = CONCAT(@q,' AND status = 1');
 -- SELECT @q;
 PREPARE stmt FROM @q;
 EXECUTE stmt;
 DEALLOCATE PREPARE stmt;
 
SET error_code = 0;
END$$

DELIMITER ;


