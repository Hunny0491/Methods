information = {
1 : {'player_id' : '139','player_name' : 'Sachin','age' : '19','profession' : 'artist','gender' : 'female'},
2 : {'player_id' : '101','player_name' : 'sahil','age' : '45','profession' : 'cricket','gender' : 'male'},
3 : {'player_id' : '102','player_name' : 'subodh','age' : '25','profession' : 'artist','gender' : 'male'},
4 : {'player_id' : '103','player_name' : 'rohit','age' : '35','profession' : 'student','gender' : 'female'},
5 : {'player_id' : '104','player_name' : 'virat','age' : '25','profession' : 'football','gender' : 'male'},
6 : {'player_id' : '105','player_name' : 'mahi','age' : '36','profession' : 'volleyball','gender' : 'female'},
7 : {'player_id' : '106','player_name' : 'rachin','age' : '28','profession' : 'soccer','gender' : 'male'},
8 : {'player_id' : '107','player_name' : 'shraddha','age' : '30','profession' : 'Chess','gender' : 'female'},
9 : {'player_id' : '108','player_name' : 'aditi','age' : '31','profession' : 'Cycling','gender' : 'male'},
11 :{'player_id' : '109','player_name' : 'sagar','age' : '21','profession' : 'throwball','gender' : 'male'},
12 :{'player_id' : '110','player_name' : 'akash','age' : '22','profession' : 'student','gender' : 'female'},
13 :{'player_id' : '111','player_name' : 'Sachin','age' : '37','profession' : 'football','gender' : 'male'},
14 :{'player_id' : '112','player_name' : 'jadeja','age' : '58','profession' : 'artist','gender' : 'female'},
15 :{'player_id' : '113','player_name' : 'sanika','age' : '48','profession' : 'Chess','gender' : 'female'},
16 :{'player_id' : '114','player_name' : 'mahesh','age' : '33','profession' : 'student','gender' : 'male'},
17 :{'player_id' : '115','player_name' : 'mukesh','age' : '36','profession' : 'artist','gender' : 'female'},
18 :{'player_id' : '116','player_name' : 'donald','age' : '34','profession' : 'soccer','gender' : 'male'},
19 :{'player_id' : '117','player_name' : 'barakh','age' : '39','profession' : 'football','gender' : 'male'},
20 :{'player_id' : '118','player_name' : 'bear','age' : '21','profession' : 'soccer','gender' : 'female'},
21 :{'player_id' : '119','player_name' : 'ankit','age' : '28','profession' : 'artist','gender' : 'male'},
22 :{'player_id' : '120','player_name' : 'shantanu','age' : '29','profession' : 'cricket','gender' : 'female'},
23 :{'player_id' : '121','player_name' : 'aakanksha','age' : '28','profession' : 'throwball','gender' : 'female'},
24 :{'player_id' : '122','player_name' : 'devanshu','age' : '29','profession' : 'artist','gender' : 'male'},
25 :{'player_id' : '123','player_name' : 'alia','age' : '22','profession' : 'football','gender' : 'female'},
26 :{'player_id' : '124','player_name' : 'kirti','age' : '24','profession' : 'student','gender' : 'male'},
27 :{'player_id' : '125','player_name' : 'kiara','age' : '49','profession' : 'artist','gender' : 'male'},
28 :{'player_id' : '126','player_name' : 'nora','age' : '45','profession' : 'throwball','gender' : 'male'},
29 :{'player_id' : '127','player_name' : 'rahman','age' : '47','profession' : 'soccer','gender' : 'female'},
30 :{'player_id' : '128','player_name' : 'tamanna','age' : '36','profession' : 'throwball','gender' : 'female'},
31 :{'player_id' : '129','player_name' : 'shreya','age' : '18','profession' : 'football','gender' : 'female'},
32 :{'player_id' : '130','player_name' : 'himanshu','age' : '14','profession' : 'student','gender' : 'female'},
33 :{'player_id' : '131','player_name' : 'harshit','age' : '40','profession' : 'cricket','gender' : 'male'},
34 :{'player_id' : '132','player_name' : 'shubman','age' : '49','profession' : 'throwball','gender' : 'female'},
35 :{'player_id' : '133','player_name' : 'yashasvi','age' : '42','profession' : 'artist','gender' : 'male'},
36 :{'player_id' : '134','player_name' : 'sanju','age' : '44','profession' : 'artist','gender' : 'female'},
37 :{'player_id' : '135','player_name' : 'abhiskek','age' : '35','profession' : 'cricket','gender' : 'male'},
38 :{'player_id' : '136','player_name' : 'yuvika','age' : '46','profession' : 'football','gender' : 'male'},
39 :{'player_id' : '137','player_name' : 'prince','age' : '27','profession' : 'cricket','gender' : 'female'},
40 :{'player_id' : '138','player_name' : 'narendra','age' : '51','profession' : 'Cycling','gender' : 'female'}
}
print(information)

print()
print()
print()

# 1.update
information = {
  'player_id' : '111',
 'player_name' : 'Sachin',
 'age' : '37',
 'profession' : 'football',
 'gender' : 'male'
  }
information.update({"debut": "2005"})
print(information)
print()
print()
print()
# 2.values
information = {
  'player_id' : '111',
 'player_name' : 'Sachin',
 'age' : '37',
 'profession' : 'football',
 'gender' : 'male'
}
A = information.values()
print(A)
print()
print()
print()
# 3.set default
information = {
 'player_id' : '111',
 'player_name' : 'Sachin',
 'age' : '37',
 'profession' : 'football',
 'gender' : 'male'
}
A = information.setdefault('age', "39")
print(A)
print()
print()
print()
# 4.popitem
information = {
  'player_id' : '111',
 'player_name' : 'Sachin',
 'age' : '37',
 'profession' : 'football',
 'gender' : 'male'
}
information.popitem()
print(information)
print()
print()
print()
# 5.pop
information = {
 'player_id' : '111',
 'player_name' : 'Sachin',
 'age' : '37',
 'profession' : 'football',
 'gender' : 'male'
}
information.pop('player_name')
print(information)
print()
print()
print()
# 6.keys
information = {
  'player_id' : '111',
 'player_name' : 'Sachin',
 'age' : '37',
 'profession' : 'football',
 'gender' : 'male'
}
A = information.keys()
print(A)
print()
print()
print()
# 7.items
information = {
  'player_id' : '111',
 'player_name' : 'Sachin',
 'age' : '37',
 'profession' : 'football',
 'gender' : 'male'
}
A = information.items()
print(A)
print()
print()
print()
# 8.get
information = {
  'player_id' : '111',
 'player_name' : 'Sachin',
 'age' : '37',
 'profession' : 'football',
 'gender' : 'male'
}
A = information.get('profession')
print(A)
print()
print()
print()
# 9.copy
information = {
  'player_id' : '111',
 'player_name' : 'Sachin',
 'age' : '37',
 'profession' : 'football',
 'gender' : 'male'
}
A = information.copy()
print(A)
print()
print()
print()
# 10.clear
information =	{
 'player_id' : '111',
 'player_name' : 'Sachin',
 'age' : '37',
 'profession' : 'football',
 'gender' : 'male'
}
information.clear()
print(information)