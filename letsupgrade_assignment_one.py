class ArithemeticOperations:
    def floor_division(self,a,b):
        if a>b :
            res = a//b
        else:
            res = b//a
        return res

    def power_of_a(self,a,b):
        return a**b

    def check_equal(self,a,b):
        if a==b :
            return True
        else:
            return False

    def run_functions(self):
        a = int(input('Enter first number: '))
        b = int(input('Enter the second number: '))
        print('Floor division: ',self.floor_division(a,b))
        print('Power of first  number: ',self.power_of_a(a,b))
        print('Entered numbers are equal: ',self.check_equal(a,b))
    
operations = ArithemeticOperations()
operations.run_functions()
