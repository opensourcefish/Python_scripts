'''
Compare two lists of accession codes using sets.
'''

# read old database release
old_db = set()
for line in open("list_old.txt"):
    accession = line.strip()
    old_db.add(accession)

# read new database release
new_db = set()
for line in open("list_new.txt"):
    accession = line.strip()
    new_db.add(accession)

# report differences
new_entries = new_db.difference(old_db)
print ("new entries"), list(new_entries)
old_entries = old_db.difference(new_db)
print ("deprecated entries"), list(old_entries)
unique_entries = new_db.symmetric_difference(old_db)
print ("unique entries"), list(unique_entries)
