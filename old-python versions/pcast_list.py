<drac2>

subcommands = ["help", "set", "get", "show", "reset"]
msg = ""
if ("&1&" in subcommands):
    recievedCommand = "&1&"
elif len(&ARGS&) < 1:
    recievedCommand = subcommands[0]
else:
    msg = msg + "Not a valid subcommand"
    recievedCommand = ""
helpMsg = False
if recievedCommand == subcommands[1]:
    character().set_cvar_nx("prepListName", "prepared")
    oldCvar = character().get_cvar('prepListName')
    if len(&ARGS&) == 2:
        character().set_cvar("prepListName", "&2&")
        if character().get_cvar(character().get_cvar('prepListName')) != None:
            msg = msg + f"Your cvar of prepared spells is now: &2&"
        else:
            character().set_cvar("prepListName", oldCvar)
            msg = msg + f"Could not load new prepared spells cvar. See ``{ctx.prefix}{ctx.alias} help`` for rules on cvar names."
    else:
        msg = msg + "Invalid cvar name"
elif recievedCommand == subcommands[2]:
    character().set_cvar_nx("prepListName", "prepared")
    msg = msg + f"Your prepared spells are in cvar: {character().get_cvar('prepListName')}"
elif recievedCommand == subcommands[3]:
    character().set_cvar_nx("prepListName", "prepared")
    msg = msg + f"Your prepared spells cvar: {character().get_cvar(character().get_cvar('prepListName'))}"
elif recievedCommand == subcommands[-1]:
    character().delete_cvar("prepListName")
    msg = msg + "Your prep list name has been reset.    "
else:
    helpMsg = True
if not helpMsg:
    msg = f'embed -title "{name} checks their preparations data" -desc "{msg}" -footer "alias by @""Quincy#3650"'
else:
    msg = f"help {ctx.alias} list"
return msg

</drac2>
