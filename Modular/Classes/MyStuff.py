class MyStuff(object):

    def __init__(self):
        # below is a way split lines of code
        print "This entering init method by itself. \
without any explicit calls to it. Like a constructor"
        self.tangerine = "And now we have an inner variable"

    def apple(self):
        print "I Am class apples."


thing = MyStuff()
thing.apple()
print thing.tangerine
