import json


class SearchByTag:

    def __init__(self, data_file, query_tag):
        with open(data_file) as data_file:
            self._data = json.load(data_file)
        self.query = query_tag

    def search(self):
        for item in self._data.get("items", []):
            if self.query in item.get("tags", []):
                yield item

    def first(self):
        for item in self.search():
            return item
        raise StopIteration("No matching item found")

# Example usage:
search_1 = SearchByTag("interview-stuff\interviews-2023\movies.json", 'crime')
first_result = search_1.first()
# print(first_result)

data = search_1.search()
for d in data:
    print(d)
# print(data)
# Call the first method
# try:
#     first_result = search_1.first()
#     print(first_result)
# except StopIteration as e:
#     print(e)
    
print("====================")

data_1 = {
    "items":[
        {"name":"The shawshank Reemption", "tags":["90s","drama"]},
        {"name": "The Godfather", "tags" :["70s", "drama","crime"]}
    ]
}
def gen(data_1):
    for i in data_1.get("items",[]):
        if 'crime' in i.get("tags"):
            yield i
d1 = gen(data_1)
for j in d1:
    print(j)

"""
class SearchByTag:

    def __init__(self, data_file, query_tag):
        with open(data_file) as data_file:
            self._data = json.load(data_file)
        self.query = query_tag

    def search(self):
        pass

    def first(self):
        pass
"""
    