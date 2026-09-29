def strings_to_list_of_lists(str_list):
    result = map(list, str_list)
    return list(result)

colors = ["Red", "Green", "Black", "Orange"]

print("Original list of strings:")
print(colors)

print("\nConvert the said list of strings into list of lists:")
print(strings_to_list_of_lists(colors))