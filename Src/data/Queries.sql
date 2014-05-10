

--To find the red cards or yellow cards given to the countries who have won the world cup finals

SELECT Player,Card,Country FROM cards WHERE Country='France' AND Card LIKE "%red%" AND Country IN (SELECT Country FROM Overview);

--Countries that made qualification rounds or didn't make past qualification rounds
SELECT COUNT(Country),Country FROM Group_Results WHERE Qualification='Yes' GROUP BY Country;
