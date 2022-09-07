<drac2>
IDs = load_yaml(get_gvar("e808cf94-12fb-45c4-9fd1-dcaa0d39c841"))
args = &ARGS&
spN = "&1&"
cArgs = ' '.join([f'"{x}"' if ' ' in x else str(x) for x in args[1:] ]) if args else ''
ch = character()
sb = character().spellbook
spN.lower()
l = ["and", "an", "the", "a", "to"]
w = spN.split(" ")
for i in range(len(w)):
    if w[i] not in l:
        w[i] = w[i].capitalize()
spN = " ".join(w)
msg = f'{name} failed to cast a prepared spell'
sLvl = 1
stC = f"Spell Slots\n{sb.slots_str(sLvl)}"
scc = False
empty = False
ig = False
ch.set_cvar_nx("prepListName", "prepared")
ch.set_cvar_nx(ch.get_cvar("prepListName"), [])
preps = ch.get_cvar(ch.get_cvar("prepListName"))
if preps != None:
    if spN in IDs:
        if "-l" in args:
            sLvl = f'{args[args.index("-l") + 1]}'[0]
            cArgs = cArgs.replace(f" -l {sLvl}", '')
        else:
            sLvl = IDs[spN]['L']
        if "-i" in cArgs:
            ig = True
            cArgs = cArgs.replace("-i", "'")
        if (sb.get_slots(sLvl) > 0) or ig:
            cArgs = {cArgs.lstrip(spN)}
            if sb.can_cast(spN, sLvl)  or ig:
                if (spN in preps) or ig:
                    msg = f"""cast "{spN}" -i -l {sLvl} {cArgs}" " """
                    if not ig:
                        sb.use_slot(int(sLvl))
                        stC = f"Spell Slots\n{sb.slots_str(sLvl)}(- 1)"
                    scc = True
                else:
                    msg = f"You don't have {spN} prepared!"
            else:
                msg = f"{spN} is not a spell you know!"
        else:
            empty = True
            msg = f"No level {sLvl} spell slots left!"
    else:
        msg = f'"{spN}" spell not recognized!'
else:
    msg = f'{name} has not prepared any spells!'
md = f"embed  -color {color} -thumb {image} -desc "
stC = f'{md}"{stC}"'
ft = f' -footer "Cast spells prepared using {ctx.prefix}{ctx.alias}. Alias by @""Quincy#3650"'
if spN.lower() == "help":
    msg = f'{md}"Casting: `{ctx.prefix}{ctx.alias} <spell name> [!cast args]`"'
elif not scc:
    msg = f'{md}"{msg}" -title "{name} failed to cast {spN}!"'
out = ["", msg, stC]
if (not scc) or ig:
    out.pop(-1)
    out[1] = out[1] + ft
else:
    out[-1] = out[-1] + ft
return f'{ctx.prefix}'.join(out)
</drac2>
