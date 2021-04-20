import pokepy


def fetch_type(api, pkm):
    ans = ''
    try:
        pika = api.get_pokemon(pkm)
    except:
        try:
            pikasp = api.get_pokemon_species(pkm)
            pid = pikasp.id
            pika = api.get_pokemon(pid)
        except:
            ans = "Seems like that ain't a valid Pokemon name.."
            return ans
    ptypeList = pika.types
    typeList = []
    for t in ptypeList:
        typeList.append(api.get_type(t.type.name))
    dmg0 = []
    dmgh = []
    dmg2 = []
    if len(typeList) > 1:
        ans = ans + 'Type : '
    first = 1
    for t in typeList:
        if len(typeList) > 1:
            if first:
                first = 0
                ans = ans + t.name.capitalize()
            else:
                ans = ans + ' | ' + t.name.capitalize()
        else:
            ans = ans + 'Type : ' + t.name.capitalize()
        s1list = []
        s2list = []
        s3list = []
        for tn in t.damage_relations.no_damage_from:
            s1list.append(tn.name)
        for tn in t.damage_relations.half_damage_from:
            s2list.append(tn.name)
        for tn in t.damage_relations.double_damage_from:
            s3list.append(tn.name)
        dmg0.append(s1list)
        dmgh.append(s2list)
        dmg2.append(s3list)
    ans = ans + '\n'
    d0 = {}
    d25 = {}
    d50 = {}
    d200 = {}
    d400 = {}
    if len(typeList) > 1:
        d0 = set(dmg0[0]) | set(dmg0[1])
        d25 = set(dmgh[0]) & set(dmgh[1])
        d400 = set(dmg2[0]) & set(dmg2[1])
        d50 = ((set(dmgh[0]) - set(dmg2[1])) | (set(dmgh[1]) - set(dmg2[0]))) - d0 - d25 - d400
        d200 = ((set(dmg2[0]) - set(dmgh[1])) ^ (set(dmg2[1]) - set(dmgh[0]))) - d0 - d25 - d400
    else:
        d0 = set(dmg0[0])
        d50 = set(dmgh[0])
        d200 = set(dmg2[0])

    if d0:
        st = ''
        for t in d0:
            st = st + (t.capitalize() + ', ')
        st = st[:-2]
        ans = ans + 'No Damage from ' + st + '\n'
    if d25:
        st = ''
        for t in d25:
            st = st + (t.capitalize() + ', ')
        st = st[:-2]
        ans = ans + '1/4th Damage from ' + st + '\n'
    if d50:
        st = ''
        for t in d50:
            st = st + (t.capitalize() + ', ')
        st = st[:-2]
        ans = ans + 'Half Damage from ' + st + '\n'
    if d200:
        st = ''
        for t in d200:
            st = st + (t.capitalize() + ', ')
        st = st[:-2]
        ans = ans + 'Double Damage from ' + st + '\n'
    if d400:
        st = ''
        for t in d400:
            st = st + (t.capitalize() + ', ')
        st = st[:-2]
        ans = ans + '4x Damage from ' + st + '\n'
    return ans
