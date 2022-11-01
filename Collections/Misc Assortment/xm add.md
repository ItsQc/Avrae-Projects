Adds a new x-multi command or overwrites an existing one.

Format
``!xm add <xm name> <minimum arguments for this xm> [<default argument 1> <default argument 1>]  <Avrae command 1> [addtional Avrae commands]``

Simple Example:
``!xm add 'ftmisty' '0' 'cc "Fey Touched (Intelligence): Misty Step" -1' 'cast "Misty Step" -i'``

Advanced Examples:
``!xm add 'gjoin' '2' 'Belnir' 'Scribe' 'char <1>' 'i join -group <2> <x>'``

- Spaces separate arguments, inclose arugments with quotation marks if they contain spaces.
	- Be careful when using multiple quotations, like with commands that use quotations themselves
- Minimum arguments must be a number greater than or equal to 0
- Default arguments
	- The number of default arguments must be greater than or equal to the minimum arguments.
	- Must be listed in order.
	- The the default arguments are only added until the argument minimum is reached, only replacing missing arguments of the same place. In effect, all arguments for using your x-multi command are optional.
		- For example, if the x-multi is called with 1 arguemnt and the minimum is 3, the argument is kept and only the default arguments 2 and 3 are added as default arguments.
- For Avrae commands, omit the command prefix (the character used to start a command). For most servers, the prefix is ``!``
- To pass arguments from your call to your x-multilline command, insert a pair of angled brackets containing a one of the options below. You will need a separate pair of brackets for each passing of arguments, as seen in the advanced example above the bullet points.
	- A number. This passes argument 1, 2, 3 etc. from when you use the x-multi command. 
		- Example avrae command including a passed numbered argument: ``"attack shortsword -t <1>"``.
		- It must a number be between 1 and the x-multi's minimum arguments
		- The order given when using the x-multi command does not have to match the order they appear in your Avrae commands
		- You pass the same numbered argument to multiple Avrae commands and multiple times to the same commands 
	- The character ``x``. This passes the excess arguments, all the arguments after the minimum. Useful for spellcasting arguments or passing snippets for your attack.
		- Example avrae command including passed excessa arguments: ``cast fireball <x>``
		- This can be passed to multiple avrae commands. You can pass it multiple times to the same Avrae command, but doing so is not reccomended.