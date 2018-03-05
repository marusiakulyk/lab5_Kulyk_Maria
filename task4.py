def get_valid_input(input_string, valid_options):
    """
    Function is used in classes to receive data
    with formatted input_string
    :param input_string: str in input
    :param valid_options: added to input_string to show valid options
    :return: str input
    """
    input_string += "({})".format(", ".join(valid_options))
    response = input(input_string)
    return response


class Property:
    """
    Is a parent class of House and Apartment
    """
    def __init__(self, square_feet='', beds='',
                 baths='', **kwargs):
        """
        Initializes class
        :param square_feet:(float) area of property
        :param beds:(int) number of beds
        :param baths: (int) number of bathes
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        Prints info about property
        :return: None
        """
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """

        :return: dict with values that has to be inputted
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter a number of bedrooms: "),
                    baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    """
    Is a sub-class of Property
    """
    valid_laundries = ('coin', 'ensuite', 'none')
    valid_balconies = ('yes', 'no', 'solarium')

    def __init__(self, balcony='', laundry='', **kwargs):
        """

        :param balcony:(str) info about balcony
        :param laundry: (str) info about laundry
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        Prints info about apartment as property + info
        about laundry and balcony
        :return: None
        """
        super().display()
        print("APARTMENT DETAILS")
        print('laundry: %s' % self.laundry)
        print('has balcony : %s' % self.balcony)

    def prompt_init():
        """
        Creates Property.prompt_init dictionary and adds laundry
        and balcony keys with info
        :return: dict
        """
        parent_init = Property.prompt_init()
        laundry = get_valid_input("What laundry facilitirs does"
                                  "the property have? ",
                                  Apartment.valid_laundries)
        balcony = get_valid_input("Does the property have a balcony?",
                                  Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    """
    Is a sub-class of Property
    """
    valid_garage = ('attached', 'detached', 'none')
    valid_fenced = ('yes', 'no')

    def __init__(self, num_stories='',
                 garage='', fenced='', **kwargs):
        """
        :param num_stories:(int) number of stories
        :param garage:(str) info about garage
        :param fenced: (str) info about fenced yard
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        Prints info about apartment as property + info
        about num of stories, garage and fenced yard
        :return: None
        """
        super().display()
        print('HOUSE DETAILS')
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """
        Creates Property.prompt_init dictionary and adds fenced,
        garage and num_stories keys with info
        :return: dict
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)
        num_stories = input("How mwny stories? ")

        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    """
    Class represents info about possibility of purchasing property
    """
    def __init__(self, price='', taxes='', **kwargs):
        """
        Initializes Purchase object
        :param price:(float) price of purchase
        :param taxes: (float) amount of taxes
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        Prints info about super class and prints purchase details
        :return: None
        """
        super().display()
        print(" PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """
        Creates dict where values are input functions
        :return: dict
        """
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are estimated taxes? "))

    prompt_init = staticmethod(prompt_init)


class Rental:
    """
    Class represents info about possibility of renting property
    """
    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        """
        Initializes Rental object
        :param furnished:(str) info about furniture
        :param utilities: (str) info about utilities
        :param rent: (float) sum of rent
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        Prints info about super class and prints rent details
        :return: None
        """
        super().display()
        print("RENTAL DETAILS")
        print('rent: {}'.format(self.rent))
        print("estimated utilities: {}".format(
            self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        Creates dict where values are input functions
        :return: dict
        """
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input(
                "What are the estimated utilities? "),
            furnished=get_valid_input("Is the property furnished? ",
                                      ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    """"""
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class Agent:
    def __init__(self):
        """
        Initializes agent object
        """
        self.property_list = []

    def display_properties(self):
        """
        Displays all properties in list
        :return: None
        """
        for property in self.property_list:
            property.display()

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def add_property(self):
        """
        Adds property to list of properties
        :return: None
        """
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()

        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

    def __repr__(self):
        """
        Returns list of property areas
        :return:list
        """
        return " ".join([property1.square_feet for property1 in self.property_list])

    def display_item(self, property1):
        """
        Displays given property
        :param property1:(Property) property you are looking for
        :return:None
        """
        if property1 in self.property_list:
            property1.display()
