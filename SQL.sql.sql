SELECT DISTINCT title
FROM books
WHERE publication_year > 1990;


SELECT a.first_name, a.last_name, SUM(b.pages) AS total_pages
FROM authors a
JOIN books b ON a.author_id = b.author_id
GROUP BY a.author_id, a.first_name, a.last_name;

SELECT 
    FLOOR((publication_year / 100) + 1) AS century, 
    COUNT(*) AS book_count
FROM Books
GROUP BY century
ORDER BY century;


SELECT a.first_name, a.last_name
FROM authors a
LEFT JOIN books b ON a.author_id = b.author_id
WHERE b.book_id IS NULL;

