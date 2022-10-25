# slicing is creating  a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]

# step: indicates the index space between each extracted character

name = "Albert Smith"
name_changed = name[1:8:2]

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice_format = slice(7, -4)
# as you can see it's very useful using minus!


print(name_changed)
print(website1[slice_format])
print(website2[slice_format])
