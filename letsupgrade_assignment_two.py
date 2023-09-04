class AreaOfSquare:

    def area(self,side) :
        area = side * side
        return area
    
    def run_program(self) :
        
        side = float(input('Enter the value of one side of the square: '))
        print('Area of the square is: ',self.area(side))

square_area = AreaOfSquare()

square_area.run_program()