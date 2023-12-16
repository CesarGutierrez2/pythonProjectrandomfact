# defining the class named "Person"
class Person:
    def __init__(self, name, address, telephone):  # defining the attributes for this class
        self.name = name
        self.address = address
        self.telephone = telephone


# creating the class named "Customer" which is a subclass of Person
class Customer(Person):
    def __init__(self, name, address, telephone, customer_number, on_mailing_list):  # attributes for this class
        super().__init__(name, address,
                         telephone)  # this calls the constructor of the superclass to inherit the attributes from
        # the superclass
        self.customer_number = customer_number
        self.on_mailing_list = on_mailing_list

    def __str__(
            self):  # this calls the __str__ method of the superclass that is used to convert the object into a string
        mailing_list_status = "Yes" if self.on_mailing_list else "No"  # this checks if the customer is on the
        # mailing list or not
        return f"Customer Information: \nName: {self.name}\nAddress: {self.address}\nTelephone: {self.telephone}\nCustomer Number: {self.customer_number}\nWish to be on the mailing list: {mailing_list_status}\n"


# the line above is used to print the object into a formattable string

customer1 = Customer("Phil Dunphy", "123 Main Avenue", "210-123-4567", "P1234567890", True)
# this line creates an instance of the 'customer' class with information and assigns it to the variable 'customer1'
print(customer1)
# this line prints the information by calling the __str__ method of the 'customer' class which is line 16
