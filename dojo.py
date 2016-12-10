#!/usr/bin/env python

"""
This file uses docopt with the built in cmd module to
run the application in interactive mode.

Usage:
    Dojo CREATE_ROOM <room_name>...
    Dojo ADD_PERSON <first_name> <last_name> <role> [<wants_accomodation>]
    Dojo REALLOCATE_PERSON <person_identifier> <new_room_name>
    Dojo LOAD_PEOPLE <filename>
    Dojo PRINT_ALLOCATED [<filename>]
    Dojo PRINT_UNALLOCATED [<filename>]
    Dojo PRINT_ROOM <room_name>
    Dojo SAVE_STATE [<sqlite_database>]
    Dojo LOAD_STATE <sqlite_database>
    Dojo (-i | --interactive)
    Dojo (-h | --help | --version)

Options:
    -i, --interactive   Interactive Mode
    -h, --help          Show this screen and exit.
"""

import sys
import cmd
from doc.docopt import docopt, DocoptExit
from app.amity import Amity


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to my interactive program!' \
        + ' (type help for a list of commands.)'
    prompt = '>>> '
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: CREATE_ROOM <room_name>..."""

        List = args["<room_name>"]
        for rooms in range(len(List)):
            if type(rooms) is int:
                amity.createRoom(List[rooms])

    @docopt_cmd
    def do_add_person(self, args):
    	"""Usage: ADD_PERSON <first_name> <last_name> <role> [<wants_accomodation>]"""


        fname = args["<first_name>"]
        lname = args["<last_name>"]
        name = str(fname)+" "+str(lname)
        job = args["<role>"]

        #if len(args) > 3:
        #    wants_accomodation = args["<wants_accomodation>"]
        #else:
        #    wants_accomodation = "NO" 

        wants_accomodation = args["<wants_accomodation>"] or "NO"       
    	
        #Convert F to Fellow and S to Staff.
        if job.upper() == "F":
            job = "FELLOW"
        elif job.upper() == "S":
            job = "STAFF"
        else:
            job = job

        #check the role is fellow or staff
        if not lname.upper() in ["FELLOW","STAFF","F","S"]:
            if job.upper() in ["FELLOW","STAFF","F","S"]:
                amity.allocateRoom(name.upper(), job, wants_accomodation)
            else:
                print "Job can only be Staff or Fellow. Not case sensitive."    
        else:
            print "Please use both first and last names."    
                
    @docopt_cmd
    def do_reallocate_person(self, args):
        """Usage: REALLOCATE_PERSON <person_identifier> <new_room_name>
        """

        id_no = args["<person_identifier>"]
        new_room = args["<new_room_name>"]

        amity.reallocate_person(id_no, new_room)

    @docopt_cmd
    def do_print_unallocated(self, args):
        """
        Usage: 
            PRINT_UNALLOCATED [<filename>]
        """
        filename = args["<filename>"] or ""
        amity.unallocated_people(filename)

    @docopt_cmd
    def do_print_allocated(self, args):
        """
        Usage: 
            PRINT_ALLOCATED [<filename>]
        """
        filename = args["<filename>"] or ""
        amity.allocated_people(filename)

    @docopt_cmd
    def do_print_room(self, args):
        """
        Usage: PRINT_ROOM <room_name>
        """
        room = args["<room_name>"]
        amity.print_rooms(room)
    
    @docopt_cmd
    def do_load_people(self, args):
        """
        Usage: LOAD_PEOPLE <filename>
        """
        filename = args["<filename>"]
        amity.load_people(filename)

    @docopt_cmd
    def do_load_state(self, args):
        """
        Usage: LOAD_STATE <sqlite_database>
        """
        db = args["<sqlite_database>"]
        amity.load_state(db)
    
    @docopt_cmd
    def do_save_state(self, args):
        """
        Usage: 
            SAVE_STATE [<sqlite_database>]
        """
        db = args["<sqlite_database>"] or ""
        amity.save_state(db)
        
    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    amity = Amity()
    MyInteractive().cmdloop()

print(opt)
