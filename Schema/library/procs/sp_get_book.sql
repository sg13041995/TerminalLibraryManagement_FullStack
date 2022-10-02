-- call library.sp_get_book(@err,null,null,null,null,null,null,null,null);

DELIMITER $$

DROP PROCEDURE IF EXISTS library.sp_get_book$$

CREATE  PROCEDURE library.sp_get_book(OUT error_code INT
				              ,IN in_book_id INT
				              ,IN in_user_id INT
                                      ,IN in_book_name VARCHAR(100)
                                      ,IN in_book_author TEXT
                                      ,IN in_publication_company VARCHAR(100)
                                      ,IN in_isbn VARCHAR(100)
                                      ,IN in_is_rented TINYINT
                                      ,IN in_rented_on DATETIME
                                   )
BEGIN
SET error_code = -2;
SET @q = CONCAT('

select  book_id, 
       user_id, 
       book_name, 
       book_desc,
       book_author,
       publication_company,
       isbn,
       rented_on,
        status,
        created_id,
        created_dtm,
        modified_id,
        modified_dtm
        
  FROM 
        library.book
     
 WHERE  1 = 1  ');
 
 IF in_book_id IS NOT NULL THEN
 SET @q = CONCAT(@q,' AND book_id = ',in_book_id);
 END IF;

 IF in_user_id IS NOT NULL THEN
 SET @q = CONCAT(@q,' AND user_id = ',in_user_id);
 END IF;
 
 IF in_book_name IS NOT NULL THEN
 SET @q = CONCAT(@q,' AND UPPER (book_name) = ', "'",UPPER(in_book_name),"'"); 
 END IF;

 IF in_book_author IS NOT NULL THEN
 SET @q = CONCAT(@q,' AND UPPER (book_author) = ', "'",UPPER(in_book_author),"'"); 
 END IF;

 IF in_publication_company IS NOT NULL THEN
 SET @q = CONCAT(@q,' AND UPPER (publication_company) = ', "'",UPPER(in_publication_company),"'"); 
 END IF;

 IF in_isbn IS NOT NULL THEN
 SET @q = CONCAT(@q,' AND UPPER (isbn) = ', "'",UPPER(in_isbn),"'"); 
 END IF;

 IF in_is_rented IS NOT NULL THEN
 SET @q = CONCAT(@q,' AND UPPER (is_rented) = ', "'",UPPER(in_is_rented),"'"); 
 END IF;

 IF in_rented_on IS NOT NULL THEN
 SET @q = CONCAT(@q,' AND  (rented_on) = ', "'",(in_rented_on),"'"); 
 END IF;
 
 SET @q = CONCAT(@q,' AND status = 1');
 -- SELECT @q;
 PREPARE stmt FROM @q;
 EXECUTE stmt;
 DEALLOCATE PREPARE stmt;
 
SET error_code = 0;
END$$

DELIMITER ;


