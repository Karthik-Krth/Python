Hin_to_eng = { "accha" : "Good", "Burra":"bad","Kaun" :"Who","Kya":"What"}

wrd = input("Enter the Word to translate in english : ")
Hin_to_eng.update({"Paisa": "Money"})
print(Hin_to_eng.get(wrd))

print(Hin_to_eng.items())

print(Hin_to_eng.keys())

