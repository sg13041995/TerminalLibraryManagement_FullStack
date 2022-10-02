-- call library.sp_edit_book (@err, 1,2,1,'Book Name','Book Desc','Book Author','Publication Company',123456789,0, NULL,0);


DROP PROCEDURE IF EXISTS library.sp_edit_book;

DELIMITER $$
CREATE PROCEDURE library.sp_edit_book(OUT error_code INT
				       ,IN in_app_user_id BIGINT
                                       ,IN in_book_id INT                                       
				        ,IN in_user_id INT
                                        ,IN in_book_name VARCHAR(100)
                                        ,IN in_book_desc VARCHAR(500)
                                        ,IN in_book_author TEXT
                                        ,IN in_publication_company VARCHAR(100)
                                        ,IN in_isbn VARCHAR(100)
                                        ,IN in_is_rented TINYINT
                                        ,IN in_rented_on DATETIME			       
                                       ,IN in_status TINYINT)

BEGIN
SET error_code=-2;

UPDATE library.book 
SET 	
        user_id                      = IFNULL (user_id, user_id),
        book_name                    = IFNULL (in_book_name, book_name),
        book_desc                    = IFNULL (in_book_desc, book_desc),
        book_author                  = IFNULL (in_book_author, book_author),
        publication_company          = IFNULL (in_publication_company, publication_company),
        isbn                         = IFNULL (in_isbn, isbn),
        is_rented                    = IFNULL (in_is_rented, is_rented),
        rented_on                    = IFNULL (in_rented_on, rented_on),
        status                       = IFNULL(in_status, status),
        modified_id                  = in_app_user_id
        
WHERE
        book_id = in_book_id;

SET error_code=0;  

END$$
DELIMITER ;



