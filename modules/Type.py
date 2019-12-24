import pokepy

def fetch_type(api,pkm):
	ans = ''
	try:
		pika = api.get_pokemon(pkm)
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
	for t in typeList:
		# print('Type : ' + t.name)
		ans = ans + 'Type : ' + t.name.capitalize() + '\n'
		s1list = []
		s2list = []
		s3list = []
		# s1 = ''
		for tn in t.damage_relations.no_damage_from:
			# s1 = s1 + (tn.name+' ')
			s1list.append(tn.name)
		# if s1 == '':
			# s1 = '-'
		# print('No Damage from '+s1)
		# s2 = ''
		for tn in t.damage_relations.half_damage_from:
			# s2 = s2 + (tn.name+' ')
			s2list.append(tn.name)
		# if s2 == '':
			# s2 = '-'
		# print('1/2 Damage from '+s2)
		# s3 = ''
		for tn in t.damage_relations.double_damage_from:
			# s3 = s3 + (tn.name+' ')
			s3list.append(tn.name)
		# if s3 == '':
			# s3 = '-'
		# print('2x Damage from '+s3)
		# print('')
		dmg0.append(s1list)
		dmgh.append(s2list)
		dmg2.append(s3list)
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
			st = st + (t.capitalize()+', ')
		st = st[:-2]
		# print('No Damage from '+st)
		ans = ans + 'No Damage from ' + st + '\n'
	if d25:
		st = ''
		for t in d25:
			st = st + (t.capitalize()+', ')
		st = st[:-2]
		# print('1/4th Damage from '+st)
		ans = ans + '1/4th Damage from ' + st + '\n'
	if d50:
		st = ''
		for t in d50:
			st = st + (t.capitalize()+', ')
		st = st[:-2]
		# print('Half Damage from '+st)
		ans = ans + 'Half Damage from ' + st + '\n'
	if d200:
		st = ''
		for t in d200:
			st = st + (t.capitalize()+', ')
		st = st[:-2]
		# print('Double Damage from '+st)
		ans = ans + 'Double Damage from ' + st + '\n'
	if d400:
		st = ''
		for t in d400:
			st = st + (t.capitalize()+', ')
		st = st[:-2]
		# print('4x Damage from '+st)
		ans = ans + '4x Damage from ' + st + '\n'
	return ans
