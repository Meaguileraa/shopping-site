"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customers in console."""

        return f"Customer: {self.first_name} {self.last_name}, {self.email}, {self.password}"


def read_customer_info_from_file(filepath):
    """Read customer info data and populate a dictionary with info. 
        Dictionary format will be: {email : Customer(....)}"""   

    customer_info = {}

    with open(filepath) as file:
        for line in file:
            (first_name,
             last_name,
             email,
             password) = line.strip().split("|")


            customer_info[email] = Customer(first_name, last_name, email, password)
  
    return customer_info

# def get_all():
#     """Returns a list of all customers and their info."""

#     return list(customer_info.values())


def get_by_email(email):
    """Gets a Customer object by email address and returns it"""

    return customer_info[email] #get an error here "Get_by_email not defined"




customer_info = read_customer_info_from_file("customers.txt")

