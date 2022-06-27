from documentary import Documentary
m = Documentary()
m._add_movie('My Octopus Techer',2020,'Documentary')
m.add_channel('NetFliex')
m._get_movie()
print(f'Tital:{m._tital}')