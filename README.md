## My Solution

My idea was create a dictionary where each line is:

```
key = a word that exist in at least one title

value = list of objects that represents the titles that have this key word and the number of times that this word appeared
```
This dictionary is create in the begin of the program, as soon as the file is read. The list of values are create not sorted,
I'm just appending the new title that contains the word in the order as the title is in the file. 

When receive a word to search, the search is directly, no need process anything more, just access the dictionary by the word
will bring the list of titles. The first you search by a word the list will not be sorted, then before return the titles, the list
is sorted based on how many times the word appeared in the title and this sorted list is updated so the next time will not be
necessary sort again, just return the titles.


## Execute the program
```bash
python run.py
```

1 - Enter a file name where should be titles or press enter to start the program with the file `files/news_titles`

2 - Enter the word that you desire to search the titles. Note the program is not case sensitive, so if you type `House` will bring the same results as `house`

## Run tests

```bash
python setup.py test --pytest-args='--junitxml=junit.xml'
```

It will show the results in the console and also save them in the file `junit.xml`. 
Opening the file is possible to check the tests results with a bit more details, such as the time to execute each test. 