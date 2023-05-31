import pandas as pd


class person:
    __Name = str()
    __familyName = str()
    __fathersName = str()
    __nationalCode = int()
    __birthDate = int()
    __tellNum = int()
    __address = str()
    __postalCode = str()
    # Methods
    def insert(self, name, familyName, fathersName, nationalCode, birthDate, tellNum, address, postalCode):
        self.__Name = name
        self.__familyName = familyName
        self.__fathersName = fathersName
        self.__nationalCode = nationalCode
        self.__birthDate = birthDate
        self.__tellNum = tellNum
        self.__address = address
        self.__postalCode = postalCode

    def display(self):
        print ("\033[1m{:<20} {:<20} {:<20} {:<20}\033[0m".format('Name','Family Name','Father\'s Name','National Code'))
        print ("{:<20} {:<20} {:<20} {:<20}".format(self.__Name, self.__familyName, self.__fathersName, self.__nationalCode))
        print()
        print ("\033[1m{:<20} {:<20} {:<20} {:<20}\033[0m".format('Birth Date','Tell Number','Address','Postal Code'))
        print ("{:<20} {:<20} {:<20} {:<20}".format(self.__birthDate, self.__tellNum, self.__address, self.__postalCode))
        print()
        
    def edit(self, dictEdit: dict):

        for key, value in dictEdit.items():
            if key == 'Name':
                self.__Name = value    
            if key == 'Family Name':
                self.__familyName = value
            if key == 'Fathers Name':
                self.__fathersName = value
            if key == 'National Code':
                self.__nationalCode = value
            if key == 'Birth Date':
                self.__birthDate = value
            if key == 'Tell Number':
                self.__tellNum = value
            if key == 'Address':
                self.__address = value
            if key == 'Postal Code':
                self.__postalCode = value

    def __del__(self):
        print('User {} is deleted.'.format(self.__nationalCode))


class employee:
    __empDate = int()
    __position = int()
    __wage = float()
    __nationalCode = int()
    # Methods
    def insert(self, empDate, position, wage, nationalCode):
        self.__empDate = empDate
        self.__position = position
        self.__wage = wage
        self.__nationalCode = nationalCode

    def display(self):
        print ("\033[1m{:<20} {:<20} {:<20} {:<20}\033[0m".format('Employment Date','Position','Wage','National Code'))
        print ("{:<20} {:<20} {:<20} {:<20}".format(self.__empDate, self.__position, self.__wage, self.__nationalCode))
        print()

    def edit(self, dictEdit):

        for key, value in dictEdit.items():
            if key == 'Employment Date':
                self.__empDate = value    
            if key == 'Position':
                self.__position = value
            if key == 'Wage':
                self.__wage = value
            if key == 'National Code':
                self.__nationalCode = value

    def __del__(self):
        print('Employee {} is deleted.'.format(self.__nationalCode))



class enrollment:
    __enrlDate = int()
    __enrlCode = int()
    __stdCode = int()
    # Methods
    def insert(self, enrlDate, enrlCode, stdCode):
        self.__enrlDate = enrlDate
        self.__enrlCode = enrlCode
        self.__stdCode = stdCode

    def display(self):
        print ("\033[1m{:<20} {:<20} {:<20}\033[0m".format('Enrollment Date','Enrollment Code','Student Code'))
        print ("{:<20} {:<20} {:<20}".format(self.__enrlDate, self.__enrlCode, self.__stdCode))
        print()

    def edit(self, dictEdit):

        for key, value in dictEdit.items():
            if key == 'Enrollment Date':
                self.__enrlDate = value    
            if key == 'Enrollment Code':
                self.__enrlCode = value
            if key == 'Student Code':
                self.__stdCode = value

    def __del__(self):
        print('Member {} is deleted.'.format(self.__stdCode))



class member(enrollment):
    __memCode = int()
    __stdCode = int()
    __issueDate = int()
    __exprDate = int()
    # Methods
    def insert(self, memCode, stdCode, issueDate, exprDate, enrlDate, enrlCode):
        enrollment.insert(self, enrlDate, enrlCode, stdCode)
        self.__memCode = memCode
        self.__stdCode = stdCode
        self.__issueDate = issueDate
        self.__exprDate = exprDate

    def display(self):
        enrollment.display(self)
        print ("\033[1m{:<20} {:<20} {:<20} {:<20}\033[0m".format('Member Code','Student Code','Issue Date','Expire Date'))
        print ("{:<20} {:<20} {:<20} {:<20}".format(self.__memCode, self.__stdCode, self.__issueDate, self.__exprDate))
        print()

    def edit(self, dictEdit):
        enrollment.edit(self, dictEdit)
        for key, value in dictEdit.items():
            if key == 'Member Code':
                self.__memCode = value    
            if key == 'Student Code':
                self.__stdCode = value
            if key == 'Issue Date':
                print('Issue Date cannot be edited!')
            if key == 'Expire Date':
                self.__exprDate = value
    
    def __del__(self):
        enrollment.__del__(self)



class student(person, member):
    __stdCode = int()
    __major = str()
    __gradlvl = str()
    __department = str()
    # Methods
    def insert(self, stdCode, major, gradlvl, department, name, familyName, fathersName, nationalCode, birthDate, tellNum, address, postalCode = ''):
        person.insert(self, name, familyName, fathersName, nationalCode, birthDate, tellNum, address, postalCode='')
        self.__stdCode = stdCode
        self.__major = major
        self.__gradlvl = gradlvl
        self.__department = department

    def display(self):
        person.display(self)
        print ("\033[1m{:<20} {:<20} {:<20} {:<20}\033[0m".format('Student Code','Major','Graduation Level','Department'))
        print ("{:<20} {:<20} {:<20} {:<20}".format(self.__stdCode, self.__major, self.__gradlvl, self.__department))
        print()
    
    def edit(self, dictEdit):
        person.edit(self,dictEdit)
        for key, value in dictEdit.items():
            if key == 'Student Code':
                self.__stdCode = value    
            if key == 'Major':
                self.__major = value
            if key == 'Graduation Level':
                self.__gradlvl = value
            if key == 'Department':
                self.__gradlvl = value

    def __del__(self):
        person.__del__(self)
    


class librarian(person, employee):
    __username = str()
    __password = str()
    __department = str()
    __empCode = int()
    # Methods
    def insert(self, username, password, department, empCode ,name, familyName, fathersName, nationalCode, birthDate, tellNum, address, postalCode, empDate, position, wage, notionalCode):
        employee.insert(self, empDate, position, wage, notionalCode)
        person.insert(self, name, familyName, fathersName, nationalCode, birthDate, tellNum, address, postalCode='')
        self.__username = username
        self.__password = password
        self.__department = department
        self.__empCode = empCode

    def display(self):
        employee.display()
        person.display(self)
        print ("\033[1m{:<20} {:<20} {:<20} {:<20}\033[0m".format('Username','Password','Department', 'Employee Code'))
        print ("{:<20} {:<20} {:<20} {:<20}".format(self.__username, self.__password, self.__department, self.__empCode))
        print()

    def edit(self, dictEdit: dict):
        employee.edit(self, dictEdit)
        person.edit(self, dictEdit)
        for key, value in dictEdit.items():
            if key == 'Username':
                self.__username = value    
            if key == 'Password':
                self.__password = value
            if key == 'Department':
                self.__department = value
            if key == 'Employee Code':
                self.__empCode = value

    def __del__(self):
        employee.__del__(self)
        person.__del__(self)




class manager(person, employee):
    __univCode = int()
    __empNames = list()
    # Methods
    def insert(self, univCode, empNames: list, name, familyName, fathersName, nationalCode, birthDate, tellNum, address, postalCode, empDate, position, wage):
        person.insert(self, name, familyName, fathersName, nationalCode, birthDate, tellNum, address, postalCode='')
        employee.insert(self, empDate, position, wage, nationalCode)
        self.__univCode = univCode
        self.__empNames = empNames

    def display(self):
        employee.display(self)
        person.display(self)
        print ("\033[1m{:<20} {:<20}\033[0m".format('Univercity Code','Employees Names'))
        print ("{:<20} {:<20}".format(self.__univCode, self.__empNames))
        print()

    def edit(self, dictEdit):
        employee.edit(self, dictEdit)
        person.edit(self, dictEdit)
        for key, value in dictEdit.items():
            if key == 'Univercity Code':
                self.__univCode = value    
            if key == 'Employees Names':
                self.__empNames = value

    def __del__(self):
        employee.__del__()
        person.__del__()




class report:
    __reportID = int()
    __reportDate = int()
    __period = str()
    __startDate = int()
    __endDate = int()
    __report = pd.DataFrame()
    # Methods
    def insert(self, reportID, reportDate, period, startDate, endDate, report: pd.DataFrame):
        self.__reportID = reportID
        self.__reportDate = reportDate
        self.__period = period
        self.__startDate = startDate
        self.__endDate = endDate
        self.__report = report

    def display(self):
        # TODO: how to display a report?
        return




class addBook:
    __bookName =str()
    __authorName = list()
    __bookID = int()
    __publisher = str()
    __pubYear = int()
    __donation = bool()
    __category = str()
    __department = str()
    __shelfNum = int()
    # Methods
    def insert(self, bookName, authorName: list, bookID, publisher, pubYear, donation, category, department, shelfNum):
        self.__bookName = bookName
        self.__authorName = authorName
        self.__bookID = bookID
        self.__publisher = publisher
        self.__pubYear = pubYear
        self.__donation = donation
        self.__category = category
        self.__department = department
        self.__shelfNum = shelfNum

    def display(self):
        print ("\033[1m{:<20} {:<20} {:<20} {:<20}\033[0m".format('Book Name','Authors Names','Book ID', 'Publisher'))
        print ("{:<20} {:<20} {:<20} {:<20}".format(self.__bookName, self.__authorName, self.__bookID, self.__publisher))
        print()
        print ("\033[1m{:<20} {:<20} {:<20} {:<20}\033[0m".format('Publish Year','Donation','Category', 'Shelf Number'))
        print ("{:<20} {:<20} {:<20} {:<20}".format(self.__pubYear, self.__donation, self.__category, self.__shelfNum))
        print()
        print ("\033[1m{:<20}\033[0m".format('Department'))
        print ("{:<20}".format(self.__department))
        print()

    def edit(self, dictEdit):

        for key, value in dictEdit.items():
            if key == 'Book Name':
                self.__bookName = value    
            if key == 'Authors Name':
                self.__authorName = value
            if key == 'Book ID':
                self.__bookID = value
            if key == 'Publisher':
                self.__publisher = value
            if key == 'Publish Year':
                self.__pubYear = value    
            if key == 'Donation':
                self.__donation = value
            if key == 'Category':
                self.__category = value
            if key == 'Shelf Number':
                self.__shelfNum = value
            if key == 'Department':
                self.__department = value




class search(addBook):
    __searchID = int()
    __searchDate = int()
    # Methods
    def insert(self, searchID, searchDate, bookName, authorName, bookID, publisher, pubYear, donation, category, department, shelfNum):
        addBook.insert(self, bookName, authorName, bookID, publisher, pubYear, donation, category, department, shelfNum)
        self.__searchID = searchID
        self.__searchDate = searchDate

    def display(self):
        addBook.display(self)
        print ("\033[1m{:<20} {:<20}\033[0m".format('Search ID', 'Search Date'))
        print ("{:<20}".format(self.__searchID, self.__searchDate))
        print()

    def print(self):
        # TODO: how print on paper?
        return
    



class membershipExtn:
    __extnCode = int()
    __memCode = int()
    __duration = int()
    __extnDate = int()
    # Methods
    def insert(self, extnCode, memCode, duration, extnDate):
        self.__extnCode = extnCode
        self.__memCode = memCode
        self.__duration = duration
        self.__extnDate = extnDate

    def display(self):
        print ("\033[1m{:<20} {:<20} {:<20} {:<20}\033[0m".format('Extension Code','Membership Code','Duration', 'Extension Date'))
        print ("{:<20} {:<20} {:<20} {:<20}".format(self.__extnCode, self.__memCode, self.__duration, self.__extnDate))
        print()

    def edit(self, dictEdit):

        for key, value in dictEdit.items():
            if key == 'Extension Code':
                self.__extnCode = value    
            if key == 'Membership Code':
                self.__memCode = value
            if key == 'Duration':
                self.__duration = value
            if key == 'Extension Date':
                self.__extnDate = value




class loanBook:
    __loanID = int()
    __loanDate =int()
    __stdCode = int()
    __bookID = int()
    # Methods
    def insert(self, loanID, loanDate, stdCode, bookID):
        self.__loanID = loanID
        self.__loanDate = loanDate
        self. __stdCode = stdCode
        self.__bookID = bookID

    def display(self):
        print ("\033[1m{:<20} {:<20} {:<20} {:<20}\033[0m".format('Loan ID','Loan Date','Student Code', 'Book ID'))
        print ("{:<20} {:<20} {:<20} {:<20}".format(self.__loanID, self.__loanDate, self.__stdCode, self.__bookID))
        print()




class loanBookExtn:
    __loExtnID = int()
    __loExtnDate = int()
    __loanID = int()
    __times = int()
    # Methods
    def insert(self, loExtnID, loExtnDate, loanID, times):
        self.__loExtnID = loExtnID
        self.__loExtnDate = loExtnDate
        self.__loanID = loanID
        self.__times = times

    def display(self):
        print ("\033[1m{:<20} {:<20} {:<20} {:<20}\033[0m".format('Loan Extension ID','Loan Extension Date','Loan ID', 'Times'))
        print ("{:<20} {:<20} {:<20} {:<20}".format(self.__extnCode, self.__memCode, self.__duration, self.__extnDate))
        print()