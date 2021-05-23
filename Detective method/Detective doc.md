# Detective.py documentation

The Detective.py has a purpose to solve follwing problem:

A square table of certain size is given (**NxN**). Rows are some characters, columns - some places. Each place has one character only. Also no place remains without a character. A number of characters is **N**. Some cells of the table are filled with **1**, the rest of them filled  with **0**. **1** means a character can't take place, **0** - a character can take such place. One has to define a number of different character placements if **N** and a table are given. 

> **Note**: each place is able to hold 1 character or no character.

To solve claimed problem a recursive function **all_different_variants** has been built.

This function takes the following arguments:

- *matrix* - a matrix the problem provides. It is represented as a list of **N** ordinary lists each among them has size **N**;
- *answer* - a list filled with *1*. Program uses a list instead of a counter, because Python doesn't allow to change numerical variables after passing them into a function. the sum of *answer* elements is the answer for a certain table;
- *used_place* - a set of places which have been already taken.

Algorithm which rules **all_different_variants**:

1. Take next level of the given table (recursive call of **all_different_variants**);
2. Loop through places of the level;
3. Go back to 1st step of the algorithm, if current place can be taken (matrix[len(used_place)][place] != 1) and it is free (place not in used_place). Before taking the next level mark current place busied (used_place.add(place));
4. If the table last level was reached (len(used_place) == len(matrix) - 1) and the last character turned to be placeble, add **1** to the *answer* list (answer.append(1)) then go back to the previous level (return);
5. If a character can't be placed on some level, go back (return) to the previous one to choose the next place for previous character. One has to vanish previous character place from *used_place*, because this place is freed.

> **Note**: a size of *used_place* and level number are incremented simultaneously. So the instruction matrix[len(used_place)][place] != 1, which checks a place availability, comes clear.

Correctness of the algorithm seems to be apparent, because **all_different_variants** checks each place of each level and tries to place a character. If it placed all the characters it appends **1** to the *answer* list, otherwise it tries the next place. The programm checks different placement variants only, because a place of a certain level has a gradually increasing number.


The rest code describes instructions to scan input data.

Instructions:

  matrix_size, M, ans = int(input()), [], []
  
provide *matrix_size* (which is **N**) and declare *M* for a table and *ans* for answer.


A *for* loop:

  for string in range(matrix_size):
      M.append(list(map(int, input().split())))
      
fills matrix *M* with rows (M.append(list())) each their element converted to int (map(int, input.split())).

Then an answer is printed:
  print(sum(ans))

