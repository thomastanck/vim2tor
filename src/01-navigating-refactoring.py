""" 01 Navigating and refactoring """

"""
Do the following refactors to the following code:

1) Extract out the Business Logic from the methods `Business.add_data` and `Business.__init__` to a new method `Business._parse_data` because duplicate code ain't good for nobody
2) Move the __init__ method to the top of the class so people can find it
3) Rename "Business" to "Deliverable" because it's more posh (and "Businesses" should become "Deliverables"!)
4) Move all the create_.*_business factory methods to the bottom of the class
"""

class Business:
    some_global = Logic(55)

    @classmethod
    def create_linguine_business(cls):
        return cls(Logic('linguine'), False)

    @classmethod
    def create_cheddar_cheese_business(cls):
        return cls(Logic('cheddar_cheese'), False)

    @classmethod
    def create_table_business(cls):
        return cls(Logic('table'), False)

    @classmethod
    def create_office_appliances_business(cls):
        return cls(Logic('office_appliances'), False)

    @classmethod
    def create_soul_crushing_despair_business(cls):
        return cls(Logic('soul_crushing_despair'), False)

    @classmethod
    def create_strange_UFO_business(cls):
        return cls(Logic('strange_UFO'), False)

    def add_data(self, new_business):
        if self.update_business:
            new_business.x = new_business.y
            new_business.z = new_business.x
            new_business.create_new_data()
            new_business.reticulate_splines()
            new_business.forge_timestamps()

        self.business_data.append(new_business)

    def new_business_context(self, business_context):
        assert(business_context is not None)
        self.business_contexts.append(business_context)

    @classmethod
    def create_spaghetti_business(cls):
        return cls(Logic('spaghetti'), False)

    @classmethod
    def create_macaroni_business(cls):
        return cls(Logic('macaroni'), False)

    @classmethod
    def create_chair_business(cls):
        return cls(Logic('chair'), False)

    def __init__(self, business_data, update_business):
        if update_business:
            for business in business_data:
                business.x = business.y
                business.z = business.x
                business.create_new_data()
                business.reticulate_splines()
                business.forge_timestamps()

        self.business_data = business_data
        self.update_business = update_business
        self.business_contexts = []

    @classmethod
    def create_office_appliances_business(cls):
        return cls(Logic('office_appliances'), False)

    @classmethod
    def create_soul_crushing_despair_business(cls):
        return cls(Logic('soul_crushing_despair'), False)

    @classmethod
    def create_strange_UFO_business(cls):
        return cls(Logic('strange_UFO'), False)

    @classmethod
    def create_free_and_open_source_software_business(cls):
        return cls(Logic('free_and_open_source_software'), False)

    @classmethod
    def create_shady_business(cls):
        return cls(Logic('shady'), False)
