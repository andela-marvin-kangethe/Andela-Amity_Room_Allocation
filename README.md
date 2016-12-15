[![Build Status](https://travis-ci.org/andela-marvin-kangethe/Andela-Amity_Room_Allocation.svg?branch=develop)](https://travis-ci.org/andela-marvin-kangethe/Andela-Amity_Room_Allocation)

[![Coverage Status](https://coveralls.io/repos/github/andela-marvin-kangethe/Andela-Amity_Room_Allocation/badge.svg?branch=develop)](https://coveralls.io/github/andela-marvin-kangethe/Andela-Amity_Room_Allocation?branch=develop)

[![Code Climate](https://codeclimate.com/github/andela-marvin-kangethe/Andela-Amity_Room_Allocation/badges/gpa.svg)](https://codeclimate.com/github/andela-marvin-kangethe/Andela-Amity_Room_Allocation)

[![Test Coverage](https://codeclimate.com/github/andela-marvin-kangethe/Andela-Amity_Room_Allocation/badges/coverage.svg)](https://codeclimate.com/github/andela-marvin-kangethe/Andela-Amity_Room_Allocation/coverage)

[![Issue Count](https://codeclimate.com/github/andela-marvin-kangethe/Andela-Amity_Room_Allocation/badges/issue_count.svg)](https://codeclimate.com/github/andela-marvin-kangethe/Andela-Amity_Room_Allocation)

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d8f495a7f1d64cdda55984b43ae6614a)](https://www.codacy.com/app/marvin-kangethe/Andela-Amity_Room_Allocation?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=andela-marvin-kangethe/Andela-Amity_Room_Allocation&amp;utm_campaign=Badge_Grade)

# Andela-Amity_Room_Allocation

Amity has rooms which can be offices or living spaces. An office can occupy a maximum of 6 people. A living space can inhabit a maximum of 4 people.

This is a console application that allocates offices and living spaces at Amity to Andela employees

## Installation

Clone this repo 

```
git clone https://github.com/andela-marvin-kangethe/Andela-Amity_Room_Allocation.git
```

Navigate to the folder

```cd Andela-Amity_Room_Allocation```

Fetch the develop branch.

```git pull origin develop```

Set up a virtualenv then Install packages required

```pip install  -r requirements.txt```

## Launching the Program

```python dojo.py -i```

## Running the tests

Run ``` nosetests --exe --with-coverage --cover-erase --cover-package=tests/ ```


## Usage

1. ```create_room (<room_name> <room_type>)...``` Create a new room or several new rooms, with the specified room type. You must specify whether it is a living space or an office as well as the room name. The room type can be either 'o' for office or 'l' for livingspace. Example: ``` create_room Hogwarts o Valhalla l Krypton o ```

2. ```add_person <first_name> <last_name> <role> [<wants_accomodation>]``` Add a new person. You must specify their first name, last name and whether they are a fellow or staff member.You can use 's' for STAFF and 'f' for FELLOW. Optionally, you can indicate whether or not they want space with "Y" or "N". If you indicate that the person wants space, they are automatically allocated a room. Staff members can only be allocated an office while fellows can only be allocated a living space and office space using this command. If there are no rooms in the system, the person will not be added. Example: ```add_person Ada Lovelace f y```

3. ```reallocate_person <person_id> <new_room_name>``` Using this command, you can allocate an already allocated person another room. You must specify the person's id number which he/she will be given when being added to the system, as well as the room to be allocated. Note that staff members cannot be allocated living spaces, while fellows can be allocated offices using this command. Example: ```reallocate_person 1234 Hogwarts```


4. ```load_people <filename>``` This command allows the user to specify a text file containing people's information. The people are then added to the system. See ```data.txt``` for sample data.

6. ```print_allocated [<filename>]``` Print a list of occupants per room to the screen, and optionally to a text file.

7. ```print_unallocated [<filename>]``` Print a list of unallocated people to the screen, and optionally to a text file.

8. ```print_room <room_name>``` Print a list of people occupying a particular room. Example: ```print_room Hogwarts```

9. ```save_state [sqlite_database]``` Save all the data stored in the application in a database. Optionally, you can specify the name of the database. Example: ```save_state Amity.db```

10. ```load_state <sqlite_database>``` Load data into the application from a specified database. Example: ```load_state Amity.db```


# Testing
To run the test cases files, use the command 

nosetests --exe --with-coverage --cover-erase --cover-package=tests/


