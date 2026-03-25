

#dict = {k:v} key может быть что угодно кроме списка

person = {
    'name' : 'Влад',
    'age' : 27,
    20 : "двадцать",
    1 : "Манго",
    2.7 : 20
    }

# dict_sample = {
#     True: "Mango",
#     False: "Coco"
# }

dict_sample = {
      None: "Mango",
      None: "Coco"
 }



#kitchen = {}     #== kitchen = dict()
# kitchen = dict(friedge="LG")
# print(kitchen)


print(type((person)))
print(person)
print(dict_sample)

#kitchen = dict(friedge="LG", mocrowave="samsung")

kitchen = {
        "friedge": "LG",
        "microwave": "samsung", 
        10: "ten"
}

#kitchen = {}

kitchen["friedge"] = "Hunday"

kitchen_copy = kitchen
# kitchen_copy["microwave"] = "LG"

# print(kitchen["microwave"]) #обязательно кавычки! friedge это ключ!!!
# print(kitchen_copy)

print(kitchen)

#del kitchen["friedge"] удаление из списка

#print("friedge" in kitchen) #будет ТРУ

#print(len(kitchen)) будет 1

#print(type(sorted(kitchen)))

#print(type([{"friedge": "LG"}, {10:"ten"}][0]))

for k, v in kitchen.items():  #items это пара k:v
    print(f"ключ: {k}, значение: {v}")


# kitchen.clear()
print(kitchen.get("friedge2", "арбуз")) #ищем по значению. в нашем случае выведет арбуз, тк friedge2 нету.

print(kitchen.items()) #[] list, {} словарь, () кортеж

list1 = [1, 3, 5] 
dict2 = dict.fromkeys(list1)
print(dict2)

item = dict2.pop(3)
print(dict2, item)

