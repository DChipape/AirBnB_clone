seModel."""

import models

from uuid import uuid4

from datetime import datetime





class BaseModel:

        """The BaseModel class for the Airbnb clone project."""



            def __init__(self, *args, **kwargs):

                    """Initialize the attributes of a new BaseModel.



                            Args:

                                            *args (any): Unused.

                                                        **kwargs (dict): Key/value pairs of attributes.

                                                                """

                                                                        tform = "%Y-%m-%dT%H:%M:%S.%f"

                                                                                self.id = str(uuid4())

                                                                                        self.created_at = datetime.today()

                                                                                                self.updated_at = datetime.today()

                                                                                                        if len(kwargs) != 0:

                                                                                                                    for k, v in kwargs.items():

                                                                                                                                    if k == "created_at" or k == "updated_at":

                                                                                                                                                        self.__dict__[k] = datetime.strptime(v, tform)

                                                                                                                                                                        else:

                                                                                                                                                                                            self.__dict__[k] = v

                                                                                                                                                                                                    else:

                                                                                                                                                                                                                models.storage.new(self)



                                                                                                                                                                                                                    def save(self):

                                                                                                                                                                                                                            """Update instance of updated_at with the current datetime and save the file."""

                                                                                                                                                                                                                                    self.updated_at = datetime.today()

                                                                                                                                                                                                                                            models.storage.save()



                                                                                                                                                                                                                                                def to_dict(self):

                                                                                                                                                                                                                                                        """Return the dict of the BaseModel instance with the string format.



                                                                                                                                                                                                                                                                Includes the key/value pair __class__ representing

                                                                                                                                                                                                                                                                        the class name of the object.

                                                                                                                                                                                                                                                                                """

                                                                                                                                                                                                                                                                                        rdict = self.__dict__.copy()

                                                                                                                                                                                                                                                                                                rdict["created_at"] = self.created_at.isoformat()

                                                                                                                                                                                                                                                                                                        rdict["updated_at"] = self.updated_at.isoformat()

                                                                                                                                                                                                                                                                                                                rdict["__class__"] = self.__class__.__name__

                                                                                                                                                                                                                                                                                                                        return rdict



                                                                                                                                                                                                                                                                                                                            def __str__(self):

                                                                                                                                                                                                                                                                                                                                    """Return the str info of the BaseModel instance."""

                                                                                                                                                                                                                                                                                                                                            clname = self.__class__.__name__

                                                                                                                                                                                                                                                                                                                                                    return "[{}] ({}) {}".format(clname, self.id, self.__dict__)




