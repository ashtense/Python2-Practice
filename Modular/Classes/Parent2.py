class Parent(object):

    def __init__(self):
        print "Parent method's constructor"

    def altered(self):
        print "Parent altered"


class Child(Parent):

    def __init__(self):
        print "Child method's constructor"
        super(Child, self).__init__()

    def altered(self):
        print "Child altered"
        # this is how we call a method from parent class.
        super(Child, self).altered()
        print "Child after parent alteration"


father = Parent()
son = Child()

son.altered()
