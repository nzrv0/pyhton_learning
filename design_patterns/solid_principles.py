# Single-responsibility principle (SRP)
"""
A class should have only one reason to change.
"""

from pathlib import Path
from zipfile import ZipFile
from abc import ABC, abstractmethod


# instead of creating all of the methods in the filemanager we can split its responsibilts to other classes, and normal file manager will have only one responsibilty coressponding to its class
class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)


class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()


# Open–closed principle (OCP)
"""
Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.
"""
from math import pi


# we can put every shape and their spesific calculation into the shape object which will cause problem as we move on to create new shapes, besides from that it would cause headeache of gettin each values for shapes. Or we can create seperate objects with its properties
class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


# Liskov substitution principle (LSP)
"""
Subtypes must be substitutable for their base types
"""


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side**2


# Interface segregation principle (ISP)
"""
Clients should not be forced to depend upon methods that they do not use. Interfaces belong to clients, not to hierarchies.
"""


# instead of creating all of the methdos in printer would produce requried methods to be used even if we do not want, we can spereate these futures to seperate classes order to get not depend on the interface
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")


class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")


# Dependency inversion principle (DIP)
"""
Abstractions should not depend upon details. Details should depend upon abstractions.
"""


# instead of getting data from frontend class we can seperate source of the data and how it comes into the seperate objects rather than depending on them
class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)


class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass


class Database(DataSource):
    def get_data(self):
        return "Data from the database"


class API(DataSource):
    def get_data(self):
        return "Data from the API"
