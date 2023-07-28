**About**

This is an alias to supplement [this Ring of Spell Storing alias](https://avrae.io/dashboard/workshop/610504a87f97753ef774c729) by MrBrown#6022. That workshop alias has not been updated to be able to store the new spells, like the Strixhazen spells or homebrew spells, to your ring of spell storing. This alias allows you to add those new spells.

See ``!help rss`` for more information on using that alias.

**Command:**

``!storerss <spell_name> [args]``
Stores a spell in the Ring of Spell Storing

**Arguments**

``spell_name`` - the name of the spell to be stored.

**Optional Arguments**
All default to the values of the active character if not included.
- ``-l <level>`` - specifies the level of the spell slot for the spell being stored. Levels below the minimum level of spell are stored as the minimum level. In other words, if you try to store a Fireball as a 1st level spell, it will instead store it as 3rd level spell. Unrecognized spells without the level argument will default to level 1 spells.
- ``-dc <dc>`` - specifies the DC for the spell being stored. Minimum 5, maximum 35
- ``-b <attack bonus>`` - specifies the spell attack bonus for the spell being stored. Minimum -3, maximum 27
