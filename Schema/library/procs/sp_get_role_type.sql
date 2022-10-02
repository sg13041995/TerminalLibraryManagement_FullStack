-- call library.sp_get_role_type(@err,null,null);

DELIMITER $$

DROP PROCEDURE IF EXISTS library.sp_get_role_type$$

CREATE  PROCEDURE library.sp_get_role_type(OUT error_code INT
                                   ,IN in_role_type_id INT
                                   ,IN in_role_type_name VARCHAR(50)
                                   )
BEGIN
SET error_code = -2;
SET @q = CONCAT('

select  role_type_id, 
        role_type_name, 
        role_type_desc, 
        status,
        created_id,
        created_dtm,
        modified_id,
        modified_dtm
        
  FROM 
        library.role_type
     
 WHERE  1 = 1  ');
 
 IF in_role_type_id IS NOT NULL THEN
 SET @q = CONCAT(@q,' AND role_type_id = ',in_role_type_id);
 END IF;
 
 IF in_role_type_name IS NOT NULL THEN
 SET @q = CONCAT(@q,' AND UPPER (role_type_name) = ', "'",UPPER(in_role_type_name),"'"); 
 END IF;
 
 SET @q = CONCAT(@q,' AND status = 1');
 -- SELECT @q;
 PREPARE stmt FROM @q;
 EXECUTE stmt;
 DEALLOCATE PREPARE stmt;
 
SET error_code = 0;
END$$

DELIMITER ;


