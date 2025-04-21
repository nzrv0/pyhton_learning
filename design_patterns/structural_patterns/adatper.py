from abc import ABC, abstractmethod


class PngInterface(ABC):
    @abstractmethod
    def draw(self):
        pass


class PngImage(PngInterface):
    def __init__(self, png):
        self.png = png
        self.format = "raster"

    def draw(self):
        print("drawing" + self.get_image())

    def get_image(self):
        return "png"


class SvgImage:
    def __init__(self, svg):
        self.svg = svg
        self.format = "vector"

    def get_image(self):
        return "svg"


# with composition
class SvgAdapterComposition(PngInterface):
    def __init__(self, svg: SvgImage):
        self.svg = svg

    def restrize(self):
        return "restirezed" + self.svg.get_image()

    def draw(self):
        img = self.restrize()
        print("drawing" + img)


# with inhertiance
class SvgAdapterInheritance(PngInterface, SvgImage):
    def __init__(self, svg):
        super().__init__(svg)

    def restrize(self):
        return "restirezed" + self.get_image()

    def draw(self):
        img = self.restrize()
        print("drawing" + img)


regular_png = PngImage("some data")
regular_png.draw()

example_svg = SvgImage("some data")
example_adapter = SvgAdapterComposition(example_svg)

example_adapter = SvgAdapterInheritance(example_svg)
example_adapter.draw()
