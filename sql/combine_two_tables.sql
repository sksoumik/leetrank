-- https://leetcode.com/problems/combine-two-tables/
-- MySQL

SELECT Person.FirstName, Person.LastName, Address.City, Address.State 
FROM Person NATURAL LEFT JOIN Address;

