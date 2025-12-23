class Enrollment:
    def initialization(self,emp_name,empDob):
        self.emp_name=emp_name
        self.empDob=empDob
    def display(self):
        print(f'Employee name :{self.emp_name}\n Date of birth:{self.empDob} ')
ob=Enrollment()
print(ob.initialization('Arjun','21st jan'))
ob.display()

ob2=Enrollment()
print(ob2.initialization('Shreyas Y','1st February'))
ob2.display()