#!/usr/bin/python3
"""
Database Storage Engine Module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {'User': User, 'Place': Place,
           'State': State, 'City': City,
           'Review': Review, 'Amenity': Amenity
           }


class DBStorage:
    """Database class"""

    __engine = None
    __session = None

    def __init__(self):
        """init function for database storage"""
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")

        connection_sting = "mysql+mysqldb://{}:{}@{}/{}".format(
                        user, password, host, database)
        self.__engine = create_engine(connection_string, pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query the current database session for all objects of a class.
        """

        object_dict = {}

        if cls is None:
            classes_to_query = classes.values()
        else:
            classes_to_query = [cls]

        for queried_cls in classes_to_query:
            for obj in self.__session.query(queried_cls).all():
                obj_key = f"{queried_cls.__name__}.{obj.id}"
                object_dict[obj_key] = obj

        return object_dict

    def new(self, obj):
        """Adds object to database"""
        self.__session.add(obj)

    def save(self):
        """Saves object to database"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes object from database"""
        try:
            self._session.delete(obj)
        except:
            pass

    def reload(self):
        """Create current database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def close(self):
        """End seeson"""
        self.__session.remove()
