class A:
    def show(self):
        print('Class A')
class B:
    def show(self):
        print('Class B')
class C(A):
    def show(self):
        super().show()
        print('Class C')

obj = C()
obj.show()
