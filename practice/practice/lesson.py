# import json, request
#
#
# response = request.get("https://jsonplaceholder.typicode.com/users")
# print(response)


# string_json = '{"https://jsonplaceholder.typicode.com/users"}'
# obj = json.loads(string_json)
# print(obj)
# # print(obj['answer'])
#
# # if key in obj:
# #     print(obj[key])
# # else:
# #     print(f'ключа {key} в json нету')

# with open("text_file.txt", 'r', encoding="utf-8",) as file:
#     s = file.readlines()
#     s1 = (line for line in s)
#     try:
#         while True:
#             print(next(s1))
#     except StopIteration:
#         print('empty_item')
#     print(dir(s))
#     print(dir(file))
#     print(iter(file))
#     print(iter(file) is file)


def gen(n, k=0):
    while k < 40:
        k = n
        n += 2
        yield n
        if k == 40:
            break

print(gen(1))

# print(fn())
# print(gen())
generator = gen(5)
print(next(generator))

# print(next(generator))
# print(dir(gen))
for i in generator:
    print(i)