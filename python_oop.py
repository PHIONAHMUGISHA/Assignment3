       #assignment
#1. Add a constructor for the cohort class

#2. Add a method to the class that prints the cohort name
# and the total number of students

#3. Create a new instance of the cohort class    

 
class Cohort:
    def __init__(self, name, description, start_date, end_date, student_total_num):
        self.name = name
        self.description = description
        self.start_start = start_date
        self.end_date = end_date
        self.student_total_num= student_total_num
    def print_cohort_info(self):
        print(f"Cohort Name: {self.name}")
        print(f"Total Number of students: {self.student_total_num}")

Cohort4 = Cohort(name="python programming",
                description="Course on python programming",
                start_date="20th/08/2024",
                end_date= "20th/08/2026",
                student_total_num=65)
Cohort4.print_cohort_info()                




        

    