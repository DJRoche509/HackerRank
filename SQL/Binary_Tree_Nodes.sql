/**
 * You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.
 * 
 * The TRIANGLES table is described as follows:
 * 
 *    +--------+---------+
 *    | Column | Type    |
 *    +--------+---------+
 *    |    N   | Integer |
 *    |    P   | Integer |
 *    +--------+---------+
 * 
 * Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node: 
 *    Root: If node is root node.
 *    Leaf: If node is leaf node.
 *    Inner: If node is neither root nor leaf node.
 * 
 * Sample Input:
 *    +--------+---------+
 *    |    N   |    P    |
 *    +--------+---------+
 *    |    1   |    2    |
 *    |    3   |    2    |
 *    |    6   |    8    |
 *    |    9   |    8    |
 *    |    2   |    5    |
 *    |    8   |    5    |
 *    |    5   |   null  |
 *    +--------+---------+
 *         
 * 
 * Sample Output:
 *    1 Leaf
 *    2 Inner
 *    3 Leaf
 *    5 Root
 *    6 Leaf
 *    8 Inner
 *    9 Leaf
 * 
*/

-- Working platform:- MySQL, DB2, Oracle, MS SQL Server

SELECT N, 
    CASE 
        WHEN P IS NULL THEN 'Root' 
        WHEN(SELECT COUNT(*) FROM BST WHERE P = B.N) > 0 THEN 'Inner'
        ELSE 'Leaf'
    END
FROM BST B
ORDER BY N;