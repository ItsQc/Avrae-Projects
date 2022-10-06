``!pcast`` works by referencing a cvar containing the list of your character's prepared spells. The default cvar, and the one set by the ``!prep`` alias, is named "prepared".
The ``list`` command and it's subcommands are for chaning which cvar ``!pcast`` references. These are settings for enhanced compatability that most will not need.

Cvar (character variable) names:
- Cvar names must be identifiers (only contain a-z, A-Z, 0-9, _ , and not start with a number).
- The list must be stored in the cvar in the format of a python list.
  - In other words, a pair of square brackets "[ ]" containing a comma separated list of quoted strings.
  - Example: ``["Shield", "Absorb Elements", "Web"]``
- See ``!help cvar`` for further information.

Subcommands:

  - ``help``  You're looking at it :)
  - ``set``   Select the cvar that contains your character's spell preps
  - ``get``   Show the name of your current spell prep cvar
  - ``show``  Show the contents of your spell prep cvar
  - ``reset`` Reset the use the default cvar, "prepared", for spell preps