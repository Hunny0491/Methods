# list methods

v1 = [[1,'Sachin',45,'cricket'],
      [2,'virat',35,'cricket'],
      [3,'rohit',37,'cricket'],
      [4,'sunil',38,'football'],
      [5,'rakul',25,'astist'],
      [6,'rahul',35,'cricket'],
      [7,'sumit',37,'cricket'],
      [8,'akshar',38,'football'],
      [9,'ishan',45,'Cricket'],
      [10,'tony',35,'cricket'],
      [11,'arvind',37,'student'],
      [12,'abhishek',38,'football'],
      [13,'ronit',28,'Cricket'],
      [14,'rupam',35,'cricket'],
      [15,'viraj',37,'cricket'],
      [16,'akshat',25,'football'],
      [17,'vivek',45,'Cricket'],
      [18,'salman',35,'cricket'],
      [19,'shahrukh',37,'cricket'],
      [20,'amir',38,'student'],
      [21,'sanju',28,'astist'],
      [22,'akshay',35,'cricket'],
      [23,'shraddha',37,'astist'],
      [24,'astha',19,'student'],
      [25,'mukesh',45,'Cricket'],
      [25,'donald',35,'student'],
      [26,'barakh',37,'cricket'],
      [27,'ritesh',28,'football'],
      [28,'pranay',37,'cricket'],
      [29,'ankit',38,'football'],
      [30,'ajay',24,'astist'],
      [31,'pranit',35,'cricket'],
      [32,'shroff',37,'cricket'],
      [33,'siraj',38,'football'],
      [34,'mahesh',24,'Cricket'],
      [35,'shubman',35,'student'],
      [36,'yashashvi',37,'cricket'],
      [37,'nitish',38,'astist'],
      [38,'harshit',24,'Cricket'],
      [39,'akash',35,'cricket'],
      [40,'sagar',37,'cricket'],
      [41,'dinesh',38,'astist'],
      [42,'vijay',45,'Cricket'],
      [43,'yash',35,'cricket'],
      [44,'prajwal',37,'cricket'],
      [45,'shreya',24,'student'],
]
print(v1)

print()

## 1.append
print('APPEND method',)
v1 = [43,'yash',35,'cricket']
v1.append("suraj")
print(v1)

print()

## 2.clear
print('CLEAR method')
v1 = [43,'yash',35,'cricket']
v1.clear()
print(v1)

print()

## 3.copy
print('COPY method')
v1 = [9,'ishan',45,'Cricket']
c = v1.copy()
print(c)

print()

## 4.sort
print('SORT method')
v1 = [38]
v1.sort()
print(v1)

print()

## 5.count
print('COUNT method')
v1 = [1,'Sachin',45,'cricket',
      2,'virat',35,'cricket',
      3,'rohit',37,'cricket',
      4,'sunil',38,'football',
      5,'rakul',25,'astist',
]
x = v1.count('cricket')
print(x)

print()

## 6.pop
print('POP method')
v1 = [2,'virat',35,'cricket',3,'rohit',37,'cricket',]
v1.pop(4)
print(v1)

print()

## 7.remove
print('REMOVE method')
v1 = [1,'Sachin',45,'cricket',
      2,'virat',35,'cricket',
      3,'rohit',37,'cricket',
      4,'sunil',38,'football',
      5,'rakul',25,'astist',]
v1.remove("cricket")
print(v1)

print()

## 8.reverse
print('REVERSE method')
v1 = [1,'Sachin',45,'cricket',
      2,'virat',35,'cricket',
      3,'rohit',37,'cricket',
      4,'sunil',38,'football',
      5,'rakul',25,'astist',
      6,'rahul',35,'cricket',
      7,'sumit',37,'cricket',
      8,'akshar',38,'football',
      9,'ishan',45,'Cricket',
      10,'tony',35,'cricket',
      11,'arvind',37,'student',
      12,'abhishek',38,'football',
      13,'ronit',28,'Cricket',
      14,'rupam',35,'cricket',
      15,'viraj',37,'cricket',
      16,'akshat',25,'football',
      17,'vivek',45,'Cricket',
      18,'salman',35,'cricket',
      19,'shahrukh',37,'cricket',
      20,'amir',38,'student',
      ]
v1.reverse()
print(v1)

print()

## 9.insert
print('INSERT method')
v1 = ['akshat',25,]
v1.insert(1, "male")
print(v1)

print()

## 10.extend
print('EXTEND method')
v1 = [20,'amir',38,'student']
v2 = ['male','topper']
v1.extend(v2)
print(v1)

print()