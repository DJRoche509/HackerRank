 /*
Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. The output column headers should be Doctor, Professor, Singer, and Actor, respectively.

Note: Print NULL when there are no more names corresponding to an occupation.

Input Format
The OCCUPATIONS table is described as follows:

 *      +----------+---------+
 *      | Column   | Type    |
 *      +----------+---------+
 *      | Name     | String  |
 *      |Occupation| String  |
 *      +----------+---------+
 * 
 *  Occupation will only contain one of the following values: Doctor, Professor, Singer or Actor.
 *
 *  Sample Input:
 *      +--------+----------+
 *      |  Name  |Occupation|
 *      +--------+----------+
 *      |  Sam   |   Doctor |
 *      |  Jul   |Professor |
 *      |  Mar   |   Actor  |
 *      |  Pri   |  Singer  |
 *      |  Mel   |  Doctor  |
 *      |  Chris | Professor|
 *      |  Jane  |   Actor  |
 *      +--------+----------+
 * 
 *
 * Sample Output: 
 *       Jenny    Ashley     Meera  Jane
 *       Samantha Christeen  Priya  Julia
 *       NULL     Ketty      NULL   Maria
 *
 * Explanation
 * 
 * The first column is an alphabetically ordered list of Doctor names.
 * The second column is an alphabetically ordered list of Professor names.
 * The third column is an alphabetically ordered list of Singer names.
 * The fourth column is an alphabetically ordered list of Actor names.
 * The empty cell data for columns with less than the maximum number of names per occupation (in this case, the Professor and Actor columns) are filled with NULL values.
 * 
 */


 SELECT 
    MAX(CASE WHEN Occupation = 'Doctor' THEN Name ELSE NULL END) Doctor,
    MAX(CASE WHEN Occupation = 'Professor' THEN Name ELSE NULL END) Professor,
    MAX(CASE WHEN Occupation = 'Singer' THEN Name ELSE NULL END) Singer,
    MAX(CASE WHEN Occupation = 'Actor' THEN Name ELSE NULL END) Actor
FROM (
    SELECT Name, Occupation, ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) rn
    FROM OCCUPATIONS) RANKED
GROUP BY rn
ORDER BY rn;


/*
Explaination:   In this query
  - The inner subquery assigns a row number (rn) to each name within its occupation group, ordered alphabetically.
  - The CASE statements pivot the Occupation column into separate columns for Doctor, Professor, Singer, and Actor, using the MAX() function to display the names. MAX() is used here only to ensure that NULL values are displayed for missing names. It doesn't affect the result because there's only one non-NULL value for each occupation in each row.
  - The outer query groups the results by the row number (rn) and orders the output based on rn. This ensures that the names are displayed in alphabetical order under their respective occupations.
  - NULL values will be displayed when there are no more names corresponding to a specific occupation.
*/