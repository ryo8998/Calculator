

from curses.ascii import isdigit

class Parser:
    valid_num_symbol = ["0","1","2","3","4","5","6","7","8","9",".","+","-","/","*","%"]
    @staticmethod
    def parse(expression):
        #remove space from original expression
        expression = expression.replace(" ","")
        for i in range(len(expression)):
            if expression[i] not in Parser.valid_num_symbol:
                return False, expression
        #return if this expression is valid and space removed expression
        return True, expression

class Status:
    def __init__(self, status):
        self.status = status.lower()

    def set_status(self,status):
        self.status = status.lower()
    
    def get_status(self):
        return self.status

class Calculator:
    operators = ["+","-","/","*","%"]
    #the greater the number is, the greater the priority is
    operatorPriority = { "+":1,
                         "-":1,
                         "*":2,
                         "/":2,
                         "%":2
                                }
    #include period for float value
    valid_num_symbol_to_calc = ["0","1","2","3","4","5","6","7","8","9","."]

    
    def __init__(self,expression):
        self.operand_stack = []
        self.operator_stack = []
        self.expression = expression
        self.result = None
    
    def get_result(self):
        if self.result == None :
            print("No result")
        else:
            return self.result
    
    def calc_total(self):
        expression = self.expression;
        #loop until expression is empty strings

        while(expression != ""):
            #check if first character is digit
            if isdigit(expression[0]):
                #take number from get_num method especiall for more than 1 digit (ex: 10,200)
                num, index = self.get_num(expression)
                self.operand_stack.append(num)
                #remove the number from expression and update 
                expression = expression[index:]
            #if first char is not digit, must be an operator and when operator stack is empty, simply push
            elif len(self.operator_stack) == 0:
                self.operator_stack.append(expression[0])
                #remove the operator from expression and update
                expression = expression[1:]
            #compare upcoming operator and stack top and if upcoming operator priority is higher, simply push    
            elif Calculator.operatorPriority[expression[0]] > Calculator.operatorPriority[self.operator_stack[len(self.operator_stack)-1]]:
                self.operator_stack.append(expression[0])
                expression = expression[1:]
            # case upcoming operator is lower, start calculating 
            # until operator stack is not empty or upcoming operator priority is higher than 
            else:
                while(len(self.operator_stack) != 0):
                    if Calculator.operatorPriority[expression[0]] > Calculator.operatorPriority[self.operator_stack[len(self.operator_stack)-1]]:
                        break
                    self.operand_stack.append(self.calculate(self.operator_stack,self.operand_stack))
                self.operator_stack.append(expression[0])
                expression = expression[1:]
        #calculate remaining stack 
        while len(self.operator_stack) != 0:
            self.operand_stack.append(self.calculate(self.operator_stack,self.operand_stack))
            self.result = self.operand_stack[0]

    def get_num(self,expression):
        #flag for judge if expression has a period(if expression has a float number)
        hasPeriod = False
        index = 0
        #loop until not number or not period emerge 
        while index < len(expression) and expression[index] in Calculator.valid_num_symbol_to_calc :
            if expression[index] == "." :
                hasPeriod = True
            index+=1
        if hasPeriod :
            return float(expression[:index]), index
        else:
            return int(expression[:index]), index

    def calculate(self, operator_stack, operand_stack):
        num1 = operand_stack.pop()
        num2 = operand_stack.pop()
        operator = operator_stack.pop()
        if operator == "+": return num2 + num1
        if operator == "-": return num2 - num1
        if operator == "*": return num2 * num1
        if operator == "/": return num2 / num1
        if operator == "%": return num2 % num1

def main():
    status = Status("waiting")
    while status.get_status() == "waiting":

        #Take User Input
        expression = input("Your expression here ; ")

        if expression == "exit":
            status.set_status("exit")
            break

        #Parse User Input
        is_valid, parsed_expression = Parser.parse(expression)
        if not is_valid:
            print("Invalid expression Please input again")
        else:
            #Calculate parsed expression
            c = Calculator(parsed_expression)
            try:
                c.calc_total()
                result = c.get_result()
                print("Result is " + str(result))
            except ZeroDivisionError:
                print("Zero Division happened. Plaease input again")

if __name__ == "__main__":
    main()




