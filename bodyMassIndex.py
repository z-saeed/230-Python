#Zaid Saeed
#Nov. 12 2014
#bodyMassIndex.py

from tkinter import *

class App(Tk):
	def __init__(self):
		Tk.__init__(self)
		
		self.title("BMI Calculator")
		
		self.headerFont = ("Helvetica", "21", "bold")

		Label(self, text = "BMI Calculator",
        	font = self.headerFont).grid(columnspan = 2)

		#Weight input
		Label(self, text = "Weight (lbs)").grid(row = 1, column = 0)
		self.txtLab1 = Entry(self)
		self.txtLab1.grid(row = 1, column = 1)
		self.txtLab1.insert(0, 180)

		#Height Feet input
		Label(self, text = "Height (feet)").grid(row = 2, column = 0)
		self.txtLab2 = Entry(self)
		self.txtLab2.grid(row = 2, column = 1)
		self.txtLab2.insert(0, 5)
    	
    	#Height Inches input
		Label(self, text = "Height (inches)").grid(row = 3, column = 0)
		self.txtLab3 = Entry(self)
		self.txtLab3.grid(row = 3, column = 1)
		self.txtLab3.insert(0, 11)

		#Calculate Button
		self.btnCalc = Button(self, text = "Calculate BMI")
		self.btnCalc.grid(row = 4, columnspan = 2)
		self.btnCalc["command"] = self.calculate

		#BMI Level Output
		Label(self, text = "BMI").grid(row = 5, column = 0)
		self.BMILabel = Label(self, bg = "#fff", anchor = "w", relief = "groove")
		self.BMILabel.grid(row = 5, column = 1, sticky = "we")

		#Status Output
		Label(self, text = "Status").grid(row = 6, column = 0)
		self.statusLabel = Label(self, bg = "#fff", anchor = "w", relief = "groove")
		self.statusLabel.grid(row = 6, column = 1, sticky = "we")

	def calculate(self):
		#Get Values from Labels
		weight = int(self.txtLab1.get())
		feet = int(self.txtLab2.get())
		inches = int(self.txtLab3.get())

		#Convert Feet to inches and find total inches
		totalInches = (feet * 12) + inches

		#Calculate BMI using BMI formula
		BMI = (weight / (totalInches ** 2)) * 703
		self.BMILabel["text"] = "%.2f" % BMI

		#Calculate Status based of BMI
		status = "Normal"
		if BMI <= 18.5:
			status = "Underweight"
		elif BMI <= 24.9:
			status = "Normal"
		elif BMI <= 29.9:
			status = "Overwight"
		elif BMI > 29.9:
			status = "Obese"

		self.statusLabel["text"] = "{}".format(status)

def main():
	a = App()
	a.mainloop()

if __name__ == "__main__":
	main()