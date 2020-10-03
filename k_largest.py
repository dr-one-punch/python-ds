import heapq

l = [12, 5, 787, 1, 23, 43, 11]
k = 2
x = [] 

for i in l:
    
    heapq.heappush(x,i)
    # x.append(i)  #don't use append it does not work use heappush
    if len(x)>k:
        heapq.heappop(x)

    # print(x)

print(f"{k} largest: ",x)