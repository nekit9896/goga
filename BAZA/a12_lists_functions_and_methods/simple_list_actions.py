#  внутри списка может лежать списко как элемент списка
nums = [1, 3, 4, "ggwp", 1, "", True, ["ggwp", 1, ""]]
#  заменить элемент по индексу
nums[0] = 10.0
print(nums, nums[-1], nums[7])
print(nums[-1], nums[7])
#  получить элемент из списка, который является элементом списка
print(nums[-1][1], "\n")

nums1 = [1, 3, 4]
#  добавить 1 элемент в конец списка
nums1.append(100)
nums1.append(True)
print(nums1, "\n")
#  добавить 1 элемент в список по индексу
nums1.insert(1, True)
print(nums1)
#  добавить список в список
nums1.extend([True, "gg", 1])
print(nums1)
#  отзеркалить список
nums1.reverse()
print("отзеркалить", nums1)
#  удалить последний элемент
nums1.pop()
print(nums1)
#  удалить элемент по индексу
nums1.pop(2)  # больше не работает
print("удален 3 элемент", nums1)
#  удалить элемент равный по значению
nums1.remove("gg")
print("удален элемент gg", nums1)
#  посчитать количество элемент совпадающих с чем либо
print("количество элементов True", nums1.count(True))
#  посчитать длину списка
print(len(nums1))
#  удалить весь список
nums1.clear()
