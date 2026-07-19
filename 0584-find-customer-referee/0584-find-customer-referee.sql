-- Write your PostgreSQL query statement below
Select name From Customer
Where referee_id != 2 OR referee_id is NULL;