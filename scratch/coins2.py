Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> number_of_coins = 200
>>> print number_of_coins
SyntaxError: Missing parentheses in call to 'print'
>>> print(number_of_coins)
200
>>> found_coins = 20
>>> magic_coins = 10
>>> stolen_coins =3
>>> found-coins + magic_coins *365 -stolen_coins * 52
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    found-coins + magic_coins *365 -stolen_coins * 52
NameError: name 'found' is not defined
>>> found_coins + magic_coins * 365 - stolen_coins * 52
3514
>>> stolen_coins
3
>>> found_coins + magic_coins * 365 - stolen_coins * 52
3514
>>> stolen_coins = 2
>>> found_coins + magic_coins * 365 - stolen_coins * 52
3566
>>> magic_coins = 50
>>> found_coins = 30
>>> found_coins + magic_coins * 365 - stolen_coins * 52
18176
>>> 
