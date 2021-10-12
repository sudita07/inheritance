# classA is the parent/super class
class A:
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")
# classB is the child/sub class
# class B(A) inheriting A into B
class B(A):
    def feature3(self):
        print("feature3 is working")
    def feature4(self):
        print("feature4 is working")
class C(B):
    def feature5(self):
        print("feature5 is working")
    def feature6(self):
        print("feature6 is working")
queen=A()
king=B()
prince=C()

queen.feature1()
queen.feature2()

king.feature3()
king.feature4()
king.feature1()

prince.feature5()
prince.feature6()

