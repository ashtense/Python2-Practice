class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now we have an inner variable"

    def apple(self):
        print "I Am class apples."


thing = MyStuff()
thing.apple()
print thing.tangerine
