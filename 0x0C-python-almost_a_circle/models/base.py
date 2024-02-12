#!/usr/bin/python3
"""Defines a base class for all models in the project."""
import json


class Base:
    """Represents the BaseModel class."""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def reset_nb_objects(cls):
        cls.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        else:
            list_objs = [obj.to_dictionary() for obj in list_objs]

        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        cls.update(dummy, **dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding='utf-8') as file:
                list_dicts = cls.from_json_string(file.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
