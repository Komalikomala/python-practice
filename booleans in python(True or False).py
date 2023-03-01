Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # PYTHON - BOOL DATATYPES IN PYTHON TRUE OR FALSE IN PYTHON BOOLEANS
>>> print(True)
True
>>> print(False)
False
>>> print(Dare)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(Dare)
NameError: name 'Dare' is not defined
>>> print("Dare")  # WE CAN ADD SINGLE OR DOUBLE QUOTES STRINGS
Dare
>>> print(bool('24'))
True
>>> print(type(True))
<class 'bool'>
>>> print(bool("komala"))
True
>>> print(type(true))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(type(true))
NameError: name 'true' is not defined
>>> # BECAUSE WE R ADDING SMALL LETTER t THATS A REASON ture is not define
>>> print(type(True))
<class 'bool'>
>>> 
>>> # NOW WE CAN SEE THE FALSE VALUES
>>> print(bool())
False
>>> #BECAUSE WE NO MENTION ANY VALUES AND NAMES VARIABLES THATS A REASON FALSE ARE COMIMG
>>> # IF ANY CONDITION WE R TAKING 0(ZERO) VALUE THAT IS FALSE
>>> print(bool(0))
False
>>>  #05
>>> name = "komala L bhovi"
>>> print('komala in name)
      
SyntaxError: EOL while scanning string literal
>>> print('komala' in name)
True
>>> # WE R TAKING ANY NAME OR WORD IN THAT ADHU STRINGS METHOD NALLI EDHRE ADHU DEFINE AGUTTE TRUE ANTHA
>>> # 06
>>> name = "komala L bhovi"
>>> print('bhovi' is name)
False
>>> # BECAUSE WE R USING (IS) SOO FALSE
>>> print('bhovi' in name)
True
>>> #07 Example
>>> my_age = 22
>>> your_age = 18
>>> print(22 > 18)
True
>>> print(18 > 22)
False
>>> print(18 < 22)
True
>>> print(22 = 22)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> print(22=22)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> print(22 = = 22)
SyntaxError: invalid syntax
>>> print(18 = = 22)
SyntaxError: invalid syntax
>>> print(my_age > your_age)
True
>>> print(my_age < your_age)
False
>>> 