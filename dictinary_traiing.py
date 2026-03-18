a = {1.3: [5, 2, "a"], "ar": "ho"}
print(a.get(1.3))
print(1 in a)
new_keys = [1.3, "ar"]
a_new_keys = a.fromkeys(new_keys, ["ls"])
print(a_new_keys)
