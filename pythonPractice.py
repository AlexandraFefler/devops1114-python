# nums = [1,2,3,4,5]
# squares = []
# for i in range(0,len(nums)):
#     squares.append(nums[i]**2)
# print (squares)



# fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# counter = 0
# for i in range(0,len(fruits)):
#     if "apple" == fruits[i]:
#         counter += 1
# print (f"There are {counter} apples in the list")



# colors = ['red', 'blue', 'green', 'yellow', 'blue']
# def is_there_green(list):
#     for i in range(0,len(list)):
#         if list[i] == 'green':
#             return i
#     return 0

# print (is_there_green(colors))



# list1 = [1,2,3]
# list2 = [4,5,6]
# list1.extend(list2)
# print(list1)

########################last my version
# def remove_all(lst, value):
#     result_lst = lst
#     for i in range(0,len(lst)):
#         if lst[i] == value:
#             result_lst.remove(result_lst[i])
#     return result_lst

# def remove_all(lst,value):
#     i = 0
#     while value in lst:
#         if lst[i] == value:
#             lst.remove(lst[i])
#         i += 1
#     return lst

# def remove_all(lst,value):
#     lst_of_places = []
#     for i in range(0,len(lst)):
#         if lst[i] 


##############Yeb tvoyu mat' za nogu sukaaaaaaaaaaaaaaaaa blyaaaaaaaaaaaaaaaaaat' yobaniy v rot nahuy 
# def remove_all(lst, value):
#     while value in lst:
#         lst.remove(value)
#     return lst

# numbers1 = [1,2,2,3,4,2]
# print(remove_all(numbers1,2))

def sortAsc(nums):
    for i in range(0,len(nums)):
        if i > 0:
            for j in range(0,i):
                if nums[j] >= nums[i]:
                    nums.insert(j,nums[i])
                    # nums.pop(nums[i+1])
                    del nums[i+1]  #pushed all eyvarim to their position + 1, so the nums[i] i found to be out of order here, has moved +1 too
    return nums

nums = [33,55,1,2,3,78,130,3,0,-2,-90]
print (sortAsc(nums))
#nice