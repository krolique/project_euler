

Divisibility Rules
------------------
Easily test if one number can be evenly divided by another



The following table summarizes divisibility rules for numbers. Some of these
rules can be recurse such that if you apply the first operation and you're
still left with the same number you can apply the rule again. Example:
number 1629 would be 1 + 6 + 2 + 9 = 18, apply again 1 + 8 = 9. 


+------------------------+--------------------------------------------+
|         Number         | Condition                                  |
+========================+============================================+
|           2            | The last digit is even (0,2,4,6,8)         | 
+------------------------+--------------------------------------------+
|           3            | The sum of the digits is divisible by 3    |
+------------------------+--------------------------------------------+
|           4            | The last 2 digits are divisible by 4       |
+------------------------+--------------------------------------------+
|           5            | The last digit is 0 or 5                   |
+------------------------+--------------------------------------------+
|                        | If you double the last digit and subtract  | 
|           7            | it from the rest of the number and the     |
|                        | answer is: 0, or divisible by 7 (recursive)|
+------------------------+--------------------------------------------+
|           8            | The last three digits are divisible by 8   |
+------------------------+--------------------------------------------+
|           9            | The sum of the digits is divisible by 9    |
|                        | (recursive)                                |
+------------------------+--------------------------------------------+
|           10           | The number ends in 0                       |
+------------------------+--------------------------------------------+
|                        | If you sum every second digit and then     |
|           11           | subtract all other digits and the answer   |
|                        | is: 0, or divisible by 11                  |
+------------------------+--------------------------------------------+
|           12           | The number is divisible by both 3 and 4    |
+------------------------+--------------------------------------------+

