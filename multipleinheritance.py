class A:
    def __init__(self):
        print("inside A init")

    def feature1(self):
           print("feature1 is working")

    def feature2(self):
          print("feature2 is working")
class B:
    def __init__(self):
        print("inside B init")

    def feature3(self):
           print("feature3 is working")

    def feature4(self):
          print("feature4 is working")
class C(B,A):
   def __init__(self):
    super().__init__()
    print("inside C init")
juice=C()

