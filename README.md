**TuringMachine is a simple text-based Turing machine emulator in python made for testing simple formal descriptions.**

I made it simply because a friend needed such a tool, and now it'd be a pity for it to just get forgotten, buried somewhere on my local drive :)


Since this is supposed to be a general machine, all the instructions can be loaded from a Turing Machine (TMC) text file using the parser module.
Users can also input their own data inside python, and that allows for a little more versability;
the machine is made to be completely functional on any tape that can take the form of a list of character-strings, 
however these can, as of today, only be inserted directly inside python, as for obvious reasons it'd be harder to format them inside a text file alongside other parameters.

A future version may introduce functionality allowing for reading the tape from a separate file.
