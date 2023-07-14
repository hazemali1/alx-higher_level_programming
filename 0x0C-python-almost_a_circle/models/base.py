#!/usr/bin/python3
"""
define class named base
"""
import json


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        nameoffile = cls.__name__ + ".json"
        with open(nameoffile, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                x = []
                for i in list_objs:
                    x.append(i.to_dictionary())
                f.write(json.dumps(x))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                s = cls(1, 1)
            else:
                s = cls(1)
            s.update(**dictionary)
            return s

    @classmethod
    def load_from_file(cls):
        nameoffile = str(cls.__name__) + ".json"
        try:
            with open(nameoffile, "r") as f:
                z = Base.from_json_string(f.read())
                return [cls.create(**d) for d in z]
        except IOError:
            return []
