

--To find the red cards or yellow cards given to the countries who have won the world cup finals
SELECT Player,Card,Country FROM cards WHERE Country='France' AND Card LIKE "%red%" AND Country IN (SELECT Country FROM Overview);

--Countries that made qualification rounds or didn't make past qualification rounds
SELECT COUNT(Country),Country FROM Group_Results WHERE Qualification='Yes' GROUP BY Country;

--Number of the time the world cup winning teams havent made it past the qualifying stages.
SELECT COUNT(Country),Country FROM Group_Results WHERE Qualification='No' AND Country in (SELECT DISTINCT Country FROM Overview) GROUP BY Country;

-- Suggested queries
-- 1.  Number of red/yellow cards given to the winning team of the event
-- 2.  Who won the most matches in the world cup history.
-- 3.  Who lost most of the matches in the world cup history.
-- 4.  Highest margin of victory.
-- 5.  Highest margin of defeat;
-- 6.  Players with the most number of cards.
-- 7.  Players with the most number of red cards/yellow cards.
-- 8.  Cards for the team which haven't gone beyond the qualifying rounds.
-- 9.  Who lost most number of quarter/semi finals.
-- 10. Who won most number of quarter/semi finals.
--
--
--

