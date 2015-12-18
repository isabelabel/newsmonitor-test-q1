## My Solution

My idea was create a dictionary where each line is:

```
key = a word that exist in at least one title

value = list of objects that represents the titles that have this key word and the number of times that this word appeared
```

This dictionary is create in the begin of the program, as soon as the file is read. According with the following logic:

1. For each title:
  1. Split the title into words
  2. Created a dictionary with these words and the number of times that each word appears in this title:
     - Ex: 
     ```
     {
      'a': 3,
      'another': 1
     }
     ```
  3. Iterate over this dictionary, adding this entry to a "global" dictionary:
    1. If the word already exist in the "global" words dictionary, includes in your list, the index for the title and how many times this word appeard in the current title
    2. If not, create a new entry in this dictionary with the word as the key and in the value create a list putting the index for the title and how many times this word appeard in the current title
    3. Ex:
    ```
    {
      'a': [(0, 3)],
      'another': [(0, 1)]
    }
    ```
3. Finished the previously step for all the titles, we have a dictionary that represents all the titles. However, since each item in the list was just appended at the end, the list of titles for each word is not sorted. So in this step each list for each word is sorted by the title where the word appeared more times

When receive a word to search, the search is directly, no need process anything more, just access the dictionary by the word will bring the list of titles. The first title will be the one that the word appeared more times.


## Execute the program
```bash
python run.py
```

  1. Enter a file name that contains the titles or press enter to start the program with the file `files/news_titles`
  2. Enter the word that you desire to search the titles. Note the program is not case sensitive, so if you type `House` will bring the same results as `house`

## Run tests

```bash
python setup.py test --pytest-args='--junitxml=junit.xml'
```

It will show the results in the console and also save them in the file `junit.xml`. 
Opening the file is possible to check the tests results with a bit more details, such including the time of execution to each test. 
