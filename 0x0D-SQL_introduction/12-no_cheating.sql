-- updates the score of Bob to 10 in the table second_table.
UPDATE `second_table`
SET `score` = 10
WHERE `id` =        
        (SELECT `id`
            FROM `second_table`
            WHERE `name` = 'Bob');