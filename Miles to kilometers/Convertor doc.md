# Convertor.py documentation.

*convertor* function solves the next problem:

Convert miles to kilometers in given sentence.

*сonvertor* function takes one argument - a *sentence* to transform.

- All available miles are in range between one mile and thousand miles, so a list *numbers* is generated according mentioned miles range;
- Then two numerals lists, *names_miles* and *names_km*, are declared. *names_miles* consists of numerals used with miles only, the same is right about *names_km* content;
- Two dictionaries, *miles_words_to_numbers* and *km_numbers_to_words* are made from corresponding lists to convert words into numbers and numbers into words;
- Different numbers require different forms of *mile* and *kilometer* words. *key_words_miles* and *key_words_km* are lists specify these words forms variety;
- *left* - a part of *sentence* which is located before word *mile* or one of *mile* word forms. *left* is a list of strings. *right* - a part of *sentence* past word *mile* or past one of *mile* word forms. *right* - is a string. *miles* - a numerical value of very miles named in the *sentence*;
- Since all possible word *mile* forms in russian have the same length (4 symbols), a four symbols slice of *sentence* is compared with *keywords_miles* list. Once a match has been found, the *sentence* is broken into two parts, *left* and *right* to analyze *left* in further. **rsplit(maxsplit=3)** instruction splits sentence slice into 3 parts only, because here is miles less than thousand. This split is done from the end of the slice;
- **while** loop transforms numerals into numbers via *miles_words_to_numbers* dictionary;
- Then some magic happens:
1. *miles*  is converted into kilometers via quite understandable function *miles_to_kilometers*;
2. kilometers are converted into string;
3. string is broken into lone digits (str() instruction within list() instruction);
4. all list elements are converted into integers via map() and stored in list via list().
- Finally, kilometers are translated into words via *km_numbers_to_words* dictionary according some specific cases;
- Last instructions make up final redacted string.

> **Note:**: It is implied that word *mile* occurs one time in *sentence*. 
