multiline
<drac2>

out = [""]

keys = ["Lookup", "Name", "School", "Rarity"]
rarity = ["varies", "common", "uncommon", "rare", "very rare"]
schools = ["None", "Abjuration", "Conjuration", "Divination", "Enchantment", "Evocation",
           "Illusion", "Necromancy", "Transmutation"]
books = [{keys[0]: "Arcane Grimoire", keys[1]: "Arcane Grimoire", keys[2]: "None", keys[3]: rarity[0]},
         {keys[0]: "Crystalline", keys[1]: "Crystalline Chronicle", keys[2]: "None", keys[3]: rarity[4]},
         {keys[0]: "Protective Verses", keys[1]: "Protective Verses", keys[2]: "Abjuration", keys[3]: rarity[3]},
         {keys[0]: "Codex", keys[1]: "Planecaller's Codex", keys[2]: "Conjuration", keys[3]: rarity[3]},
         {keys[0]: "Atlas of Endless Horizons", keys[1]: "Atlas of Endless Horizons", keys[2]: "Conjuration", keys[3]: rarity[3]},
         {keys[0]: "Astromancy Archive", keys[1]: "Astromancy Archive", keys[2]: "Divination", keys[3]: rarity[3]},
         {keys[0]: "Heart Weaver", keys[1]: "Heart Weaver's Primer", keys[2]: "Enchantment", keys[3]: rarity[3]},
         {keys[0]: "Fulminating Treatise", keys[1]: "Fulminating Treatise", keys[2]: "Evocation", keys[3]: rarity[3]},
         {keys[0]: "Duplicitous Manuscript", keys[1]: "Duplicitous Manuscript", keys[2]: "Illusion", keys[3]: rarity[3]},
         {keys[0]: "Libram", keys[1]: "Libram of Souls and Flesh", keys[2]: "Necromancy", keys[3]: rarity[3]},
         {keys[0]: "Alchemical Compendium", keys[1]: "Alchemical Compendium", keys[2]: "Transmutation", keys[3]: rarity[3]}]

def select(inputList):
    matches = []
    for input in inputList:
        found = False
        if input.capitalize() in schools:
            matches.append(input.capitalize())
        elif input.lower() in rarity:
            matches.append(input.lower())
        else:
            found = False
            for school in schools:
                if input.lower()[0:2] == school.lower()[0:2]:
                    found = True
                    matches.append(school)
                    break
            if not found:
                for rating in rarity:
                    if input.lower()[0:2] == rating.lower()[0:2]:
                        matches.append(rating)
                        break
    return matches

args = &ARGS&
if len(args) == 0:
    out.append("embed -desc 'TODO: Help text'")
elif args[0].lower() == "all":
    for book in books:
        out.append(f"item {book[keys[0]]}")
elif (len(args) > 0) and (len(args) <= len(keys[2:])):
    results = []
    if args[0].lower() == "list":
        results = books
    else:
        selection = select(args)
        if len(selection) > 0:
            for i in range(len(selection)):
                for book in books:
                    if selection[i] in schools:
                        keyMatch = keys[2]
                    else:
                        keyMatch = keys[3]

                    if (book[keyMatch] == selection[i]) and (book not in results):
                        results.append(book)

    if len(results) > 0:
        text = ""
        for result in results:
            info = ""
            for key in keys[2:]:
                info = info + f"{key}: {result[key]}\n"
            info.rstrip('\n')
            text = text + f'-f "{result[keys[1]]}|{keys[0]}: ``{ctx.prefix}item {result[keys[0]]}``\n{info}" '
    else:
        text = f'''-desc "No categories matching '&*&' found."'''
    out.append(f'embed {text} -footer "{ctx.prefix}help {ctx.alias} | Quincy#3650"')

return f'\n{ctx.prefix}'.join(out)
</drac2>
