profile = {'name': 'arif', 'age': 18, 'location' : 'chittagong', 'country' : 'Bangladesh' }

# print(len(profile.keys()))

values = list(profile.values())
element = list(profile.keys())

# var = [elm for elm in profile.keys()]

table = f'<table border="1"><tr><td>{((element)[0])}</td><td>{((values)[0])}</td></tr>' \
         f'<tr><td>{((element)[1])}</td><td>{((values)[1])}</td></tr>' \
         f'<tr><td>{((element)[2])}</td><td>{((values)[2])}</td></tr>' \
         f'<tr><td>{((element)[3])}</td><td>{((values)[3])}</td></tr></table>'

print(table)

