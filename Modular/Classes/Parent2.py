class Parent(object):

    def altered(self):
        print "Parent altered"


class Child(Parent):

    def altered(self):
        print "Child altered"
        # this is how we call a method from parent class.
        super(Child, self).altered()
        print "Child after parent alteration"


father = Parent()
son = Child()

son.altered()
