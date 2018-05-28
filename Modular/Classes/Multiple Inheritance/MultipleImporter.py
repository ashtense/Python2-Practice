import Child
import Geronimo


class MultipleImporter(Child, Geronimo):

    def __init__(self):
        child_object = Child()
        geronimo_object = Geronimo()
        child_object.child_method()
        geronimo_object.geronimo_method()


thing = MultipleImporter()
