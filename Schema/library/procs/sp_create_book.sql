-- call library.sp_create_book (@err,1,'Book Name','Book Desc','Book Author','Publication Company',123456789,NULL,@aid);

DROP PROCEDURE IF EXISTS library.sp_create_book;

DELIMITER $$
CREATE PROCEDURE library.sp_create_book(OUT error_code INT
				              ,IN in_app_user_id INT
                                          ,IN in_book_name VARCHAR(100)
                                          ,IN in_book_desc VARCHAR(500)
                                          ,IN in_book_author TEXT
                                          ,IN in_publication_company VARCHAR(100)
                                          ,IN in_isbn VARCHAR(100)
                                          ,IN in_rented_on DATETIME
                                          ,OUT out_book_id INT
                                          )
BEGIN

SET error_code=-2;

INSERT INTO library.book
       (
       book_id, 
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
       )
VALUES
       (NULL,
       1, 
       in_book_name, 
       in_book_desc,
       in_book_author,
       in_publication_company,
       in_isbn,
       in_rented_on,
        1,
        in_app_user_id,
        CURRENT_TIMESTAMP,
        in_app_user_id,
        CURRENT_TIMESTAMP
       );
       
SET out_book_id=LAST_INSERT_ID();

SET error_code=0;
 
END$$
DELIMITER ;


