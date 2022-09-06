### Booming Blade Automation**
Follow the instructions below to be able to cast your favorite gish cantrip and make the attack all in one easy command.  (After a tiny bit of one-time set up)

1. Using the [template yaml file](https://github.com/ItsQc/Avrae-Projects/blob/86ef6f069b356b702bf91b5ed261f0e24e50ca8c/automations/boomingBlade_template.yaml), change the text in the code in angle brackets ``<example>`` to the information correct for your character. __Leave no spaces in the attackBonus and damage__
3. Check that you have the correct character active, then paste the code into a botspam appropriate channel and hit enter.
You're set!

Now you can use it with ``!a`` followed by the name you gave it, like any other attack, and any arguments or snippets that you put on your weapon attacks. If your attack hits, there will be a button that appears on the monsters turn for you to press if the monster moves, it will deal the additional thunder damage.

[Here](https://github.com/ItsQc/Avrae-Projects/blob/86ef6f069b356b702bf91b5ed261f0e24e50ca8c/automations/boomingBlade_example.yaml) I have an example set up for a character using a +1 rapier with dexterity who decided to call it "bb" because they hate typing.

Examples of use in initiative:

``!a bb -t EvilGuy1 adv``

``!a bb -t EvilGuy2 crusher reckless``
