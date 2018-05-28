class Parent(object):

    def altered(self):
        print "Parent altered"


class Child(Parent):

    def altered(self):
        print "Child altered"
        super(Child, self).altered()
        print "Child after parent alteration"


father = Parent()
son = Child()

son.altered()
