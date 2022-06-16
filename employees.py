#
#tarik
#


class Employee:
    
    # Defining method init method with a parameter
    def __init__(self,firstName,lastName):
       
        self.__firstName = firstName
        self.__lastName = lastName
    
    # Defining Mutator Method for firstName
    def set_firstName(self,firstName):
        self.__firstName = firstName
    
    # Defining Mutator Method for lastName
    def set_lasttName(self,lastName):
        self.__lastName = lastName

    # Defining Accessor Method for firstName
    def get_firstName(self):
        return self.__firstName
    
    # Defining Accessor Method for lastName
    def get_lastName(self):
        return self.__lastName

    def print_employee(self):
        print("First name:", self.get_firstName())
        print("Last name:", self.get_lastName())


class CommissionEmployee(Employee):

    # Defining method init method with a parameter
    def __init__(self,firstName, lastName, commission_rate, gross_sales):
        super().__init__(firstName, lastName)
        self.__commision_rate = commission_rate
        self.__gross_sales = gross_sales
    
    # Defining Mutator Method for commission_rate
    def set_commission_rate(self,commission_rate):
        self.__commision_rate = commission_rate
    
    # Defining Mutator Method for gross_sales
    def set_gross_sales(self,gross_sales):
        self.__gross_sales = gross_sales

    # Defining Accessor Method for commision_rate
    def get_commission_rate(self):
        return self.__commision_rate
    
    # Defining Accessor Method for gross_sales
    def get_gross_sales(self):
        return self.__gross_sales

    def print_employee(self):
        super().print_employee()
        print("Commission rate:", self.get_commission_rate())
        print("Gross sales:", self.get_gross_sales())

    def earnings(self):
        earnings = self.get_commission_rate() * self.get_gross_sales()
        
        return earnings

class BasePlusCommissionEmployee(CommissionEmployee):

    def __init__(self, firstName, lastName, commission_rate, gross_sales, base_salary):

        super().__init__(firstName, lastName, commission_rate, gross_sales)
        self.__base_salary = base_salary

    def set_base_salary(self, base_salary):
        self.__base_salary = base_salary

    def get_base_salary(self):
        return self.__base_salary

    def print_employee(self):
        super().print_employee()
        print("Base salary:", self.get_base_salary())

    def earnings(self):
        earnings = self.get_base_salary() + super().earnings()
        print("Earnings",earnings)

my_base_comm_employee = BasePlusCommissionEmployee("Tarik", "Soysal", 5000, 0.4, 300)
my_base_comm_employee.print_employee()
my_base_comm_employee.earnings()