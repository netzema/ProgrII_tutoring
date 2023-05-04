import json

class Address:
    def __init__(self, street, city, state, postal_code, country):
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.residents = []
    
    def validate(self):
        # code to validate the address
        pass
    
    def outputAsLabel(self):
        # code to output the address as a label
        pass
    
class Person:
    def __init__(self, name, phone_number, email_address, address):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address
        self.address = address
        address.residents.append(self)
    
    def purchaseParkingPass(self):
        # code to purchase a parking pass
        pass
    
    def to_dict(self, addresses):
        return {
            "name": self.name,
            "phone_number": self.phone_number,
            "email_address": self.email_address,
            "address_index": addresses.index(self.address)
        }

class Student(Person):
    def __init__(self, name, phone_number, email_address, address, student_number, average_mark):
        super().__init__(name, phone_number, email_address, address)
        self.student_number = student_number
        self.average_mark = average_mark
    
    def isEligibleToEnroll(self):
        # code to check eligibility for enrollment
        pass
    
    def getSeminarsTaken(self):
        # code to get seminars taken
        pass
    
    def to_dict(self, addresses):
        data = super().to_dict(addresses)
        data.update({
            "student_number": self.student_number,
            "average_mark": self.average_mark
        })
        return data

class Professor(Person):
    def __init__(self, name, phone_number, email_address, address, salary, staff_number, years_of_service, number_of_classes):
        super().__init__(name, phone_number, email_address, address)
        self.salary = salary
        self.staff_number = staff_number
        self.years_of_service = years_of_service
        self.number_of_classes = number_of_classes
    
    def to_dict(self, addresses):
        data = super().to_dict(addresses)
        data.update({
            "salary": self.salary,
            "staff_number": self.staff_number,
            "years_of_service": self.years_of_service,
            "number_of_classes": self.number_of_classes
        })
        return data

# custom JSON encoder and decoder
class PersonEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.obj_index = {}
        self.addresses = set()
    
    def default(self, obj):
        obj_id = id(obj)
        if obj_id in self.obj_index:
            return self.obj_index[obj_id]
        if isinstance(obj, Person):
            address = obj.address
            if address not in self.addresses:
                self.addresses.add(address)
                self.obj_index[id(address)] = address.__dict__
            data = obj.to_dict(address)
            self.obj_index[obj_id] = data
            return data
        return super().default(obj)
    
    def encode(self, obj):
        self.obj_index.clear()
        self.addresses = set(a for p in obj.values() for a in p.address.residents)
        data = {
            "addresses": [a.__dict__ for a in self.addresses],
            "persons": [self.default(p) for p in obj.values()]
        }
        return super().encode(data)


def person_decoder(dct):
    if "name" in dct:
        address_index = dct["address_index"]
        address = addresses[address_index]
        if "average_mark" in dct:
            return Student(**{**dct, "address": address})
        elif "salary" in dct:
            return Professor(**{**dct, "address": address})
        else:
            return Person(**{**dct, "address": address})
    return dct

address = Address("123 Main St", "Anytown", "CA", "12345", "USA")
professor = Professor("John Smith", "555-1234", "jsmith@example.com", address, 80000, "1234", 5, 3)
student1 = Student("Jane Doe", "555-5678", "jdoe@example.com", address, "5678", 3.5)
student2 = Student("Bob Johnson", "555-9012", "bjohnson@example.com", address, "9012", 2.7)

addresses = [address]
data = {
    "professor": professor,
    "students": [student1, student2]
}

# encode data as JSON string
json_string = json.dumps(data, cls=PersonEncoder)

# decode JSON string as data
decoded_data = json.loads(json_string, object_hook=person_decoder)

# verify decoded data
print(decoded_data["professor"].__class__.__name__)  # Professor
print(decoded_data["students"][0].__class__.__name__)  # Student
print(decoded_data["students"][1].__class__.__name__)  # Student
print([r.name for r in decoded_data["professor"].address.residents])  # ['John Smith', 'Jane Doe', 'Bob Johnson']
print([r.name for r in decoded_data["students"][0].address.residents])  # ['John Smith', 'Jane Doe', 'Bob Johnson']
print([r.name for r in decoded_data["students"][1].address.residents])  # ['John Smith', 'Jane Doe', 'Bob Johnson']

