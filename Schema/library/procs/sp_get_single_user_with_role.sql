
-- call library.sp_get_single_user_with_role(@err, 33);

DELIMITER $$

DROP PROCEDURE IF EXISTS library.sp_get_single_user_with_role$$

CREATE  PROCEDURE library.sp_get_single_user_with_role(OUT error_code INT
											   ,IN in_user_id INT)

BEGIN
SET error_code = -2;
SET @q = CONCAT('

select u.user_id, 
       u.first_name, 
       u.last_name,
       rt.role_type_name,
       u.email,
       u.password,
       u.phone_number,
       u.fees
        
  FROM 
        library.user u,
        library.user_role ur,
        library.role_type rt
        
     
 WHERE  u.status = 1
        AND u.user_id = ur.user_id
        AND ur.role_type_id = rt.role_type_id');
 
IF in_user_id IS NOT NULL THEN
SET @q = CONCAT(@q, " AND ur.user_id = ", in_user_id);
END IF;

 PREPARE stmt FROM @q;
 EXECUTE stmt;
 DEALLOCATE PREPARE stmt;
 
SET error_code = 0;
END$$

DELIMITER ;


