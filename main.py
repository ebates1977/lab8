def csv2list(filepath):
  file = open(filepath)
  first = True

  L = []
  for line in file:
    if first:
      first = False
      continue

    L.append(line.strip().split(","))
  return L

people = csv2list('people.csv')

def createEmail(people):
  emails = []
  for person in people:
    