#encoding=utf-8

# 列表

bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0].title())
print(bicycles[-1])#负数索引，例如，索引-2返回倒数第二个列表元素，索引-1返回倒数第一个列表元素

bicycles = ['trek','cannondale','redline','specialized']
message = "My first bicycle was a "+bicycles[1].title()+"."
print(message)

#在列表中修改、添加、删除元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'yup'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)


#创建空列表，使用append()动态增加列表元素
motorcycles = []
motorcycles.append('honda')
print(motorcycles)
motorcycles.append('yamaha')
print(motorcycles)
motorcycles.append('yup')
print(motorcycles)

#删除元素使用del()函数
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
del motorcycles[1]

#使用pop()弹出元素

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

poppedmotorcycles = motorcycles.pop()
print(motorcycles)
print(poppedmotorcycles)

motorcycles = ['honda','yamaha','suzuki']
poppedmotorcycles = motorcycles.pop(0)
print(poppedmotorcycles)


#使用remove根据值删除元素
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)



#使用sort()对列表进行永久性排序
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse = True)   #永久性逆排序
print(cars)

cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

cars = ['bmw','audi','toyota','subaru']
length = len(cars)
print(length)
