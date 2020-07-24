# input_str = "Hi,I'm charan"
# check_str = "charan"
# index = input_str.find(check_str)
# print(input_str[index:index + len(check_str)])
# print(input_str.split())

map_value = {"name": "charan",
             "password": "value"}

if "name" in map_value:
    with open("file.txt", "a+") as f:
        val = f.read()
        val = val + "\n" + map_value["name"]
        f.write(val)
        f.close()
    print(map_value["name"])
