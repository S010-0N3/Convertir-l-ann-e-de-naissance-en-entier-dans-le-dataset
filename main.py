import csv

f = open("legislator.csv")
legislator = csv.reader(f)
legislator = list(legislator)

gender=[]
for row in legislator:
  gender.append(row[3])

gender = set(gender[1:])


party =[]
for row in legislator:
  party.append(row[6])

party = set(party[1:])


for row in legislator:
  if row[6] == "":
    row[6] = "no party"
party =[]

for row in legislator:
  party.append(row[6])
party = set(party[1:])



for row in legislator:
  if row[3] == "":
    row[3] = "M"
gender =[]
for row in legislator:
  gender.append(row[3])
gender = set(gender[1:])

birth_year =[]

for row in legislator:
  list_row = []
  list_row.append(row[2])
  for x in list_row:
    list_row= x.split("-")
    birth_year.append(list_row[0])
birth_year = set(birth_year)


birth_years2 = []

for row in legislator:
  birthday = row[2]
  parts = birthday.split("-")
  birth_years2.append(parts[0])

birth_years2 = set(birth_years2)
##################ci dessu VOIR EXERCICE SUR SET######################

####EXERCICE Convertir l'année de naissance en entier dans le dataset####

for row in legislator:
  birthday = row[2]
  birth_year= birthday.split("-")[0]
  try:
    birth_year = int(birth_year)
  except Exception:
    birth_year = 0
  row.append(birth_year)

legislator[0][7]="birth_year"
print(legislator[0:10]) 