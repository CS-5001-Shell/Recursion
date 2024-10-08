# Practice with Recursion

This lab assignment requires the following concepts:
- Recursion

For this assignment, you will complete the following three programs:

## Print Triangle
Write a *recursive* Python program that prints the following output. You will
implement a function `print_triangle` that takes as input the length of the
longest row, in this case 5. You may use one or more helper methods. For full
credit, your solution may not use *any* loops.

```
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4
0 1 2 3
0 1 2
0 1
0
```

## End X
Write a *recursive* Python function that takes as a parameter a string and
recursively computes a new string where all the lowercase 'x' chars have been
moved to the end of the string. The function should take only one parameter and 
not use any loops.

```
endX('xxre') -> 'rexx'
endX('xxhixx') -> 'hixxxx'
endX('xhixhix') -> 'hihixxx'
```

## Sum Before
Implement a *recursive* Python function `sum_before` that takes as a
parameter a list of integers and returns True if there is a number in the list
that equals the sum of all numbers before it in the list and False otherwise.

For full credit your solution may not use any loops.

```
[1, 2, 3, 4] -> True
[1, 2, 2, 2] -> False
[] -> False
[0] -> True
```

## Assignment Submission

To earn credit for this assignment you must commit all of your changes to your GitHub repository prior to the deadline. It is strongly recommended that you commit your changes regularly. Do not wait until you complete all parts of the assignment to upload your (partial) solution.

Step 1 - *Stage Changes*: Select the Source Control icon in the VSCode left menu. In the Changes section, click the + to *Stage All Changes*.

Step 2 - Commit Message: In the text box that says Message enter a meaningful message that describes the change you just completed.

Step 3 - *Commit & Push*: Select the down arrow in the blue box that says Commit. Choose *Commit & Push*.

Step 4 - Verify: Visit the repository on GitHub to confirm that your changes were uploaded successfully
