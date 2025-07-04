my_dict={"name":"zaman","age":21,"place":"kochi",1:3}

my_dict.update({"name":"athul"})
print(my_dict)
my_dict.update({"number":100})
print(my_dict)

my_dict.pop("place")
print(my_dict)
a=my_dict.pop("house","not found")
print(a)

