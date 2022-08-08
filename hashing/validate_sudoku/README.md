Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

<table>
    <tr>
        <td>5</td>
        <td>3</td>
        <td></td>
        <td></td>
        <td>7</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>6</td>
        <td></td>
        <td></td>
        <td>1</td>
        <td>9</td>
        <td>5</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>9</td>
        <td>8</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>6</td>
        <td></td>
    </tr>
    <tr>
        <td>8</td>
        <td></td>
        <td></td>
        <td></td>
        <td>6</td>
        <td></td>
        <td></td>
        <td></td>
        <td>3</td>
    </tr>
    <tr>
        <td>4</td>
        <td></td>
        <td></td>
        <td>8</td>
        <td></td>
        <td>3</td>
        <td></td>
        <td></td>
        <td>1</td>
    </tr>
    <tr>
        <td>7</td>
        <td></td>
        <td></td>
        <td></td>
        <td>2</td>
        <td></td>
        <td></td>
        <td></td>
        <td>6</td>
    </tr>
    <tr>
        <td></td>
        <td>6</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>2</td>
        <td>8</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td>4</td>
        <td>1</td>
        <td>9</td>
        <td></td>
        <td></td>
        <td>5</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>8</td>
        <td></td>
        <td></td>
        <td>7</td>
        <td>9</td>
    </tr>
</table>


The input corresponding to the above configuration :

["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
A partially filled sudoku which is valid.

Note:

A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem  

