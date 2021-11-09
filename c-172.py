class Doctor:
    def __init__(self):
        print("This is class Doctor")
    def BMI(weight, height):
        bmi = weight/(height*height)
        print("Your BMI is " + str(bmi))
    def heart_rate(heart_rates):
        if(heart_rates>60 & heart_rates<100):
            print("Your Heart rate is normal")
        else:
            print("Your Heart rate not seems normal, please visit the clinic")
            
class Patient(Doctor):
    def __init__(self):
        self.patient_name = name
        self.patient_weight = weight
        self.patient_height = height
        self.patient_heart_rates = heart_rates
    def healthCheck(self):
        print("\n Patient name: " + self.patient_name)
        Doctor.BMI(self.patient_weight, self.patient_height)
        Doctor.heart_rate(self.patient_heart_rates)
        
patient_1 = Patient("Michael", 30, 0.9144, 80)
patient_1.healthCheck()

patient_2 = Patient("Jessica",40 , 1, 120)
patient_2.healthCheck()