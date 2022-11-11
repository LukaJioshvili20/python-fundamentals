inv_names = ["book", "pen", "pencil", "NegroMan"]
inv_ids = [32, 54, 75, 86]
combined_list = list(zip(inv_ids, inv_names))

# sort by ids
# get the item number 1 in tuple
sorted_inv_ids = sorted(combined_list, key=lambda inv_tuple: inv_tuple[0])
print(sorted_inv_ids)
# sort by length of the names
sorted_inv_names = sorted(combined_list, key=lambda inv_tuple: len(inv_tuple[1]))
print(sorted_inv_names)
