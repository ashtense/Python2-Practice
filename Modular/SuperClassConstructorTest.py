class Parent_class(object):

    def __init__(self, parent_class_variable):
        self.parent_class_incomming_variable = parent_class_variable
        print self.parent_class_incomming_variable

    def experimental_method():
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
        # below piece of code doesn't work. maybe my understanding is
        # a bit wrong. lets see if the book provides such a solution
        super(Child_class, self).experimental_method


thing = Child_class()
