import heapq

numbers = [1, 4, 2, 100, 20, 750, 50, 32, 150, 8]
print(type(numbers))
result = heapq.nlargest(3, numbers)
print(result)  
print(type(result))

numbers = tuple(numbers)
print(type(numbers))
result = heapq.nsmallest(3, numbers)
print(result)  
print(type(result))

print()

data = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1]
# copy = data[:]

# heapq.heapify(data)
# print(data)
# print(heapq.heappop(data))
# print(data)
# heapq.heapify(data)
# print(data)
# print()
# heapq.heapify(copy)
# print(copy)
# print(copy.pop(0))
# print(copy)
# heapq.heapify(copy)
# print(copy)

heapq.heapify(data)
print(data)
print(heapq.heappop(data))
print(data)
heapq.heappush(data, 4)
heapq.heappush(data, 19)
heapq.heappush(data, 21)
print(data)
print()

tasks = []
heapq.heappush(tasks, (5, 'write code'))
heapq.heappush(tasks, (7, 'release product'))
heapq.heappush(tasks, (1, 'write spec'))
heapq.heappush(tasks, (3, 'create tests'))
print(tasks)
print(heapq.heappop(tasks))
print(tasks)



