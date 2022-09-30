INSERT INTO library.book

(
    book_id, 
    user_id, 
    book_name, 
    book_desc,
    book_author,
    publication_company,
    isbn,
    is_rented,
    rented_on,
    status, 
    created_id, 
    created_dtm, 
    modified_id, 
    modified_dtm
) 

VALUES 
(
    1,
    1, 
    'Python for Beginners', 
    'This is a beginner friendly Python language book',
    'Adam Stewart',
    'Stewart Publications',
    '99999999', 
    0,
    NULL,
    1, 
    1, 
    CURRENT_TIMESTAMP, 
    1,
    CURRENT_TIMESTAMP
);



