# Find 'Em All
A full stack application challenging users to see how well they know characters from TV series Pokémon.

# Background
I took on this personal project primarily to learn SQL, which I find is pertinent to web development. I had no prior knowledge of SQL. The point of the challenge is simple; name as many Pokémon(1st Generation only) in the TV Series Pokémon as you know. See if you can Find 'Em All!

# How it Works
All SQL queries and interactions with the database are handled through python backend structure. There are two tables in the database. The first is the table with all the correct answers, i.e. all the different Pokémon to be entered by the user. The second table is the user's progress; which of the entries entered by the user were correct. For each Pokémon name entered by the user, the solution table is cross-referenced and if it contains the same entry, the user table is updated with value inputted. Otherwise, an error message is shown.

At any tume, the user may display all their progress or clear it. Displaying will show all values in the user table, while clear will delete all values in the table.

# Challenges Faced
While taking on this project, many obstacles and issues came up. Since, it was my first time learning SQL and using the MySQL workbench, it was initially difficult to set up the database. With sufficient research and instructions, I was successfully able to initalize a database, make tables, and add values to it.

All SQL queries used were also learned for this project so there was a lot of reading forums and undrstanding tutorials.

Another issue I faced was checking if what the user entered was in a table in the database. This was resolved by converting the table into a list and searching through the list for the value entered by the user.  
