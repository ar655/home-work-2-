class Company:
    def __init__(self,company_bank,company_name,money):
        self.company_bank = company_bank
        self.company_name = company_name
        self.money = money






class Person(Company):

    def __init__(self,company_bank,company_name,money,first_name,last_name,salary):
        super().__init__(company_bank,company_name,money)
        self.first_name = first_name
        self.last_name  = last_name
        self.salary = salary


    def get_salary(self):

        if self.money <=0:
            print(f'У компаний не достаточно средств!')
            self.salary += self.company_bank
            print(f'{self.salary} зарплата выделенная из капитала')

    def person_info(self):
        print(f'personal information\n'
              f'name:{self.first_name}\n'
              f'lastname:{self.last_name}\n'
              f'salary:{self.salary}')



person = Person(company_bank=50000,company_name='some-bank',money=0,first_name='john',last_name='freeman',salary=3000)
print(person.salary)
person.get_salary()
person.person_info()
