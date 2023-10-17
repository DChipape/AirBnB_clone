ce class."""

from models.base_model import BaseModel





class Place(BaseModel):

        """Inherits from the BaseModel.



            Attributes:

                    city_id (str): The City.id.

                            user_id (str): The User.id.

                                    name (str): The name of the place.

                                            description (str): The description of the place.

                                                    number_rooms (int): 0

                                                            number_bathrooms (int): 0

                                                                    max_guest (int): 0

                                                                            price_by_night (int): 0

                                                                                    latitude (float): 0.0

                                                                                            longitude (float): 0.0

                                                                                                    amenity_ids (list): A list of Amenity ids

                                                                                                        """



                                                                                                            city_id = ""

                                                                                                                user_id = ""

                                                                                                                    name = ""

                                                                                                                        description = ""

                                                                                                                            number_rooms = 0

                                                                                                                                number_bathrooms = 0

                                                                                                                                    max_guest = 0

                                                                                                                                        price_by_night = 0

                                                                                                                                            latitude = 0.0

                                                                                                                                                longitude = 0.0

                                                                                                                                                    amenity_ids = []





