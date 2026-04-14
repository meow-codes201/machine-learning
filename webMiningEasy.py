logs  = [
"home",
"products",
"home",
"about",
"contacts",
"about",
"home",
"home"
]

visits={}
for i in logs:
  if i in visits:
    visits[i] +=1
  else:
    visits[i] = 1

print("WEB MINING")
print("=======LOGS=======")
for i in visits:
  print(i,"->",visits[i])
  
max_c = max(visits,key=visits.get)
print("Max count is of:",max_c," - ", visits[max_c])
