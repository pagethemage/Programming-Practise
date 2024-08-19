class customerManager:
    customerList:list = []## is equivalent to declaring as static variable in Java
                           ## ie. private static ArrayList<Customer> customerList = new ArrayList<>():
                           ## Variable is declared at top of class (inside of class is important)
                           ## This is called class level data/class level variables

    @classmethod
    def addCustomer(cls, customer):
        cls.customerList.append(customer)

    @classmethod
    def displayCustomers(cls): ## This has to be a @classmethod as it interacts with class level variables (in this case customerList)
        for index, customer in enumerate(cls.customerList, start = 1):
            print(f"{index} {customer}") 

    @classmethod
    def removeCustomer(cls, index): ## This also has to be @classmethod as it interacts with a class level variable, customerList
        cls.displayCustomers()
        if index.isdigit():
            index = int(index)
        cls.customerList.pop(index-1)
        print(f"Customer {index} has successfully been deleted. ")


    @classmethod
    def modifyCustomer(cls, index):
        cls.displayCustomers
        if index.isdigit():
            index = int(index)
        else:
            print("Invalid index. ")
            return
        
        if index <= 1 <= len(cls.customerList):
            print("Out of range. ")
            return
        
        customerToModify = cls.customerList[index-1]

        options:list = ["Change ID", "Change name", "Change branch"]
        for index, option in enumerate(options, start = 1):
            print(f"{index} {option}")

        choice = int(input("Which option would you like to modify? (enter number): "))

        if type(choice) is not int:
            print("Invalid choice.")

        if choice == 1:
            new_id = str(input("Enter new ID: "))
            customerToModify.setID(new_id)

        elif choice == 2:
            new_name = str(input("Please input new name: "))
            customerToModify.setName(new_name)

        elif choice == 3:
            new_branch = str(input("Please input new branch:"))
            customerToModify.setBranch(new_branch)


class customer:
    def __init__(self, ID, name, balance, branch):
        self.ID:int = ID
        self.name:str = name
        self.balance:float = balance
        self.branch:str = branch


    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getID(self):
        return self.ID
    
    def setID(self, ID):
        self.ID = ID

    def getBalance(self):
        return self.balance
    
    def setBalance(self, balance):
        self.balance = balance

    def getBranch(self):
        return self.branch
    
    def setBranch(self, branch):
        self.branch = branch
    


    def __str__(self):
        ## will need to iterate through customerList and get ID of customer you want to delete
        ## as they will all be named "new_customer" in list
        return(f"{self.getID()} {self.getName()} {self.getBalance()} {self.getBranch()}")

    

def main():
    while True:

        optionsList:list = ["display customers", "add customer", "remove customer", "modify customer", "exit"]
        for index, option in enumerate(optionsList, start = 1):
            print(f"{index} {option}")

        user_input:str = input("Please select an option: ")
        


        if user_input == "1" or user_input == "display customers":
            print("\nCurrent list of customers: ")
            customerManager.displayCustomers()

        elif user_input == "2" or user_input == "add customer":
            try:
                ncID = int(input("Please input customer's ID (integers only): "))
                ncName = str(input("Please input customer's name: "))
                ncBalance = float(input("Please input customers balance: $"))
                ncBranch = str(input("Please input customer's branch: "))
                new_customer = customer(ncID, ncName, ncBalance, ncBranch)
            except ValueError:
                print("\nNotice: Please ensure correct data types are provided.\n ")
                continue
            customerManager.addCustomer(new_customer)


        elif user_input == "3" or user_input == "remove customer":
            index:int = input("Please provide number corresponding to the customer you want to remove: ")
            customerManager.removeCustomer(index)

        elif user_input == "4" or user_input == "modify customer": ## Complete this method, likely requires iteration
            index:int = input("Please provide a number corresponding to the customer you would like to modify: ") 
            customerManager.modifyCustomer(index)

        elif user_input == "5" or user_input == "exit" or user_input == "quit":
            quit()

main()


## TODO: 
## 1. Fix printing objects (customers) returning gibberish, __str__ method may be wrong.  [COMPLETE] (18/08/24)
## 2. Fix error on line 68 (run code again to get report from compiler) [COMPLETE] (19/08/2024)
## 3. Fix modify customer method -> will likely require iterating through customerList based on ID


#Notes: 
# cls vs self:
#   - cls = class (class methods)
#   - cls equal to static methods in java
#   - dont need an instance of a class to be called to execute
#   - equivalent of writing methods in the public static void main(String args[]) segment of Java

#   - self = instance method
#   - self methods belong to the object and determine what the object will do
#   - For exampple, John.
#
## cls vs self methods:
## -    cls refers to class methods which are performed on class level variables
## -    eg. customerList will need cls methods to modify it

## -    self methods refer to a specific instance of the class (ie. John as an instance of Person)

## @classmethod is not just a tag, it will break code if in the wrong place. 