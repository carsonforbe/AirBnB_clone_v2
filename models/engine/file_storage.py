#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """serializes instances to a JSON file and desirialize back to instances"""

    #string path to jsonfile
    __file_path = "file.json"
    #dictonary - empty but will store all objects by <class anme>.id
    __objects = {}

    def all(self, cls=None):
        """returns the __object dictionary"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects
    
    def new(self, obj):
        """sets in __objects with key <>obj class name>.id"""
        if obj is not None:
            key = obj.__class__.name + "." + obj.id
            self.__objects[key] = obj
    
    def save(self):
        """serializes __objects to yje json file"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """desirializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load()
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """calls the reload method after deserialization"""
        self.reload()