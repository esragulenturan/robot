class Robot:
    def __init__(self, name, build_year, type, category):
        """Constructor of the class. It takes 4 values and keeps them in private attributes"""
        self.__name = name
        self.__build_year = build_year
        self.__type = type
        self.__category = category

    @property
    def name(self):
        """This is a property, which gets the name of any Robot object"""
        print("Getting name...")
        return self.__name

    @name.setter
    def name(self, name):
        """This is a property setter, which sets the name of any Robot object"""
        print(f"Setting name {name}...")
        self.__name = name

    @property
    def build_year(self):
        """This is a property, which gets the build year of any Robot object"""
        print("Getting build year...")
        return self.__build_year

    @build_year.setter
    def build_year(self, build_year):
        """This is a property setter, which sets the build year of any Robot object"""
        print(f"Setting build year {build_year}...")
        self.__build_year = build_year

    @property
    def type(self):
        """This is a property, which gets the type of any Robot object"""
        print("Getting type...")
        return self.__type

    @type.setter
    def type(self, type):
        """This is a property setter, which sets the type of any Robot object"""
        print(f"Setting type {type}...")
        self.__type = type

    @property
    def category(self):
        """This is a property, which gets the category of any Robot object"""
        print("Getting category...")
        return self.__category

    @category.setter
    def category(self, category):
        """This is a property setter, which sets the category of any Robot object"""
        print(f"Setting category {category}...")
        self.__category = category

    def speak(self):
        """This method prints out the attribute values of Robot objects"""
        print("-----------------------------------")
        print(f"My name is {self.__name}")
        print(f"I was built in {self.__build_year}")
        print(f"My type is {self.__type}")
        print(f"My category is {self.__category}")
        print("-----------------------------------\n\n")


if __name__ == "__main__":
    x = Robot("Chappie", 2022, "Mobile", "Humanoide Roboter")
    y = Robot("Wall-E", 2012, "Parallelkinematik", "Serviceroboter")
    x.speak()
    y.speak()
    
    x.name = "01"
    x.type = "Controller"
    x.speak()
