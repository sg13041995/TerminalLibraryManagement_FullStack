-- call library.sp_get_user(@err,null,null, null, null);

DELIMITER $$

DROP PROCEDURE IF EXISTS library.sp_get_user$$

CREATE  PROCEDURE library.sp_get_user(OUT error_code INT
                                   ,IN in_user_id INT
                                    ,IN in_email VARCHAR(100)
                                    ,IN in_password VARCHAR(100)
                                    ,IN in_phone_number VARCHAR(50)
                                   )
BEGIN
SET error_code = -2;
SET @q = CONCAT('

select user_id, 
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
        
  FROM 
        library.user
     
 WHERE  1 = 1  ');
 
 IF in_user_id IS NOT NULL THEN
 SET @q = CONCAT(@q,' AND user_id = ',in_user_id);
 END IF;
 
 IF in_email IS NOT NULL THEN
 SET @q = CONCAT(@q,' AND UPPER (email) = ', "'",UPPER(in_email),"'"); 
 END IF;

  IF in_password IS NOT NULL THEN
 SET @q = CONCAT(@q,' AND UPPER (password) = ', "'",UPPER(in_password),"'"); 
 END IF;

 IF in_phone_number IS NOT NULL THEN
 SET @q = CONCAT(@q,' AND phone_number = ',in_phone_number);
 END IF;
 
 SET @q = CONCAT(@q,' AND status = 1');
 -- SELECT @q;
 PREPARE stmt FROM @q;
 EXECUTE stmt;
 DEALLOCATE PREPARE stmt;
 
SET error_code = 0;
END$$

DELIMITER ;


