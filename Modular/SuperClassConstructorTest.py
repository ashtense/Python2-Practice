class Parent_class(object):

    def __init__(self, parent_class_variable):
        self.parent_class_incomming_variable = parent_class_variable
        print self.parent_class_incomming_variable

    def experimental_method(self):
        print "Inside the experimental method in parent class"


class Child_class(Parent_class):

    # Inside the functions in a class, self is a variable \
    # for the instance/object being accessed.
    def __init__(self):
        print "First you're inside the child class"
        parent_class_variable = "Hello darling, my first experiment \
with python constructors"
        super(Child_class, self).__init__(parent_class_variable)
        print "This is the end of the child class"
        # this way I can access methods of parent class. but still I\
        # need them parameterized with self. not liking it.
        super(Child_class, self).experimental_method()
        # this way I can even make an object of parent_class and just like java
        # constructor will first work on object instantiation. Still not using
        # inheritance is a fucked up thing in itself.
        parent_class_object = Parent_class(parent_class_variable)
        parent_class_object.experimental_method()


thing = Child_class()
