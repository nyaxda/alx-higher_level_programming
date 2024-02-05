# 0x0A. Python - Inheritance

In this directory, the learning objectives were as follows:

-   Why Python programming is awesome
-   What is a superclass, baseclass or parentclass
-   What is a subclass
-   How to list all attributes and methods of a class or instance
-   When can an instance have new attributes
-   How to inherit class from another
-   How to define a class with multiple base classes
-   What is the default class every class inherit from
-   How to override a method or attribute inherited from the base class
-   Which attributes or methods are available by heritage to subclasses
-   What is the purpose of inheritance
-   What are, when and how to use  `isinstance`,  `issubclass`,  `type`  and  `super`  built-in functions

## Files in the Directory:

1. 0-lookup.py - function that returns the list of available attributes and methods of an object:
2. 1-my_list.py - class  `MyList`  that inherits from  `list`, public instance method:  `def print_sorted(self):`  that prints the list, but sorted (ascending sort)
3. 2-is_same_class.py - function that returns `True` if the object is _exactly_ an instance of the specified class ; otherwise `False`.
4. 3-is_kind_of_class.py - function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.
5. 5-base_geometry.py - empty class `BaseGeometry`.
6. 6-base_geometry.py - class  `BaseGeometry`  (based on  `5-base_geometry.py`).
			-   Public instance method:  `def area(self):`  that raises an  `Exception`  with the message  `area() is not implemented`
7.  7-base_geometry.py - class  `BaseGeometry`  (based on  `6-base_geometry.py`).

			-   Public instance method:  `def area(self):`  that raises an  `Exception`  with the message  `area() is not implemented`
			-   Public instance method:  `def integer_validator(self, name, value):`  that validates  `value`
8. 8-rectangle.py - class  `Rectangle`  that inherits from  `BaseGeometry`  (`7-base_geometry.py`).
			-   Instantiation with  `width`  and  `height`:  `def __init__(self, width, height):`
			-   `width`  and  `height`  must be private. No getter or setter
			-   `width`  and  `height`  must be positive integers, validated by  `integer_validator`
9. 9-rectangle.py - class  `Rectangle`  that inherits from  `BaseGeometry`  (`7-base_geometry.py`). (task based on  `8-rectangle.py`)

			-   Instantiation with  `width`  and  `height`:  `def __init__(self, width, height):`:
				-   `width`  and  `height`  must be private. No getter or setter
				-   `width`  and  `height`  must be positive integers validated by  `integer_validator`
			-   the  `area()`  method must be implemented
			-   `print()`  should print, and  `str()`  should return, the following rectangle description:  `[Rectangle] <width>/<height>`
10. 10-square.py - class  `Square`  that inherits from  `Rectangle`  (`9-rectangle.py`):
			-   Instantiation with  `size`:  `def __init__(self, size):`:
			    -   `size`  must be private. No getter or setter
			    -   `size`  must be a positive integer, validated by  `integer_validator`
			-   the  `area()`  method must be implemented
11. 11-square.py - class  `Square`  that inherits from  `Rectangle`  (`9-rectangle.py`). (task based on  `10-square.py`).
-   Instantiation with  `size`:  `def __init__(self, size):`:
    -   `size`  must be private. No getter or setter
    -   `size`  must be a positive integer, validated by  `integer_validator`
-   the  `area()`  method must be implemented
-   `print()`  should print, and  `str()`  should return, the square description:  `[Square] <width>/<height>`
12. 100-my_int.py - class  `MyInt`  that inherits from  `int`:
			-   `MyInt`  is a rebel.  `MyInt`  has  `==`  and  `!=`  operators inverted
13. 101-add_attribute.py - function that adds a new attribute to an object if it’s possible:
			-   Raise a  `TypeError`  exception, with the message  `can't add new attribute`  if the object can’t have new attribute
			-   You are not allowed to use  `try/except`