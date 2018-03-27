class MyStuff(object):

    def __init__(self):
        print "init method gets called first"
        self.tangerine = "And now we have a class"

    def apple(self):
        print "This is the method apple."


thing = MyStuff()
thing.apple()
print thing.tangerine
