"""work.py"""

class MainClass:
    def __init__(self, text=""):
        self.__text = text  

    def set_text(self, text=""):
        self.__text = text

    def get_text(self):
        return self.__text

    def display_data(self):
        print(f"Text: {self.get_text()}")


class DerivedClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self.__number = number  

    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number

    def display_data(self):
        print(f"Text: {self.get_text()}, Number: {self.get_number()}")


if __name__ == "__main__":
    main_obj = MainClass("Hello, world!")
    main_obj.display_data()
    main_obj.set_text("New text")
    main_obj.display_data()
    derived_obj = DerivedClass("Hello from derived class", 42)
    derived_obj.display_data()
    derived_obj.set_number(99)
    derived_obj.display_data()
