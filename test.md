# Testing the Program

The user will be able to test the functionality of the entire program by answering all of the questions on the command line. The questions could look something like this.

> Would you like to use the simple or advanced search?  
> *Simple*   
> Do you want to search by artist, difficulty, key, or tuning?  
> *Artist*   
> Please input the name of the artist
> *Adele*

If the artist they input is not in the database, they will get back an "invalid response" message. If the artist is in the database, their results will print like this.

> Adele - Turning Tables, Intermediate, Key: Db, Capo: 1st fret, Tuning: E A D G B E  
> Adele - Hello, Novice, Key: Em, Capo: 1st Fret, Tuning: E A D G B E  
> Adele - Someone Like You, Intermediate, Key: A, Capo: No Capo, Tuning: E A D G B E  
> Adele - Rolling in the Deep, Intermediate, Key: Db, Capo: No Capo, Tuning: E A D G B E  
> Adele - When We Were Young, Novice, Key: C, Capo: 3rd fret, Tuning: E A D G B E

The advanced search will have more questions that will allow the user to decide the difficulty, key, and tuning of the songs.  

At the end of each printed section, the program will ask "Would you like more suggestions?" If the user says yes, it will print out more recommendations.
