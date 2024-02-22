__About__: Tracking thrown weapons is is not called out for "collect half" like ammunition is, so how it is handled by vary by DM.
This alias simply tracks weapons thrown and will tell you how many you lose after what you've retrieved. It does not interact with your bags or rests.

**__Alias__**

**Syntax:** ``!retrieve <amount> <weapon name>``
Examples ``!retrieve all dag``  ``!retrieve 3 javelin`` ``!retrieve max rocks`` ``!retrieve half rocks``


- ``<amount>`` must be either a number, "max"/"all" if you want to collect all the unretrieved weapons of the counter, or "half" if you want to collect half.
- ``<weapon name>`` must be at least 3 letters and supports partial matching.
- The thrown weapon name argument is option if you only have one thrown weapon counter.
- Omit the "Thrown " part of the counter name, just include the weapon name.
- This reset the custom counter to zero. It prints an embed that tells you how many you have lost. One use case is when your DM tells you how many javelins you got back from the fight, you use the alias and then use your preferred bag/inventory alias to remove the number weapons you've lost.

__**Snippet**__

**Syntax:** ``throw [weapon name]``  
Examples ``!a shuriken throw dag``   ``!a javelin throw``

- Uses custom counters to track the number weapons you've thrown. You can specify after the snippet if the name is different than the name of the ation/weapon of the ``!action`` command.
- "Smart" matches the weapon name. Allows for partial matches if you enter as least 3 letters.
- If you omit the tracking name optional argumnet or the given one isn't named the same as a standard phb weapon, it will create one for you. You can type the name after the snippet if you want to specify. It does its best to make the best choice given the command used witht he action command, your existing thrown weapon counters, and the standard phb weapons.
- Automatically negates the rage bonus damage for melee attacks if you're raging and omitted the "norage" snippet
