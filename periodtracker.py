#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 10:26:53 2024

@author: gurleensandhu
"""
import matplotlib.pyplot as plt
import datetime

class PeriodTracker:

    def __init__(self):
        self.cycle_data= []
        
    def recordtemp(self, date, cycleday, temp):
        self.cycle_data.append((date, cycleday, temp))
        
    def temphistory (self):
        if self.cycle_data:
            for date, cycleday, temp in self.cycle_data:
                print("\nTemperature History:")
                print(f"Date: {date.strftime('%Y-%m-%d')}\nCycle day: {cycleday}:\nTemperature: {temp:.2f}°C\n")
        else:
            print("\nNo temperature history available")
            

    def get_fertileday(self, temp):
        fertile_temp= 36.3
        return temp>= fertile_temp
        
    def avg_temp(self):
        if not self.cycle_data:
            print("\nNo temperature data available.")
            return None
        
        temps= [temp for _, _, temp in self.cycle_data]
        return sum(temps)/ len(temps)
    
    def analyzedata(self):
        if not self.cycle_data:
            print("\nNo temperature data available for analysis.")
            return
        
        fertile_days = [date.strftime('%Y-%m-%d') for date, _, temp in self.cycle_data if self.get_fertileday(temp)]
        infertile_days = [date.strftime('%Y-%m-%d') for date, _, temp in self.cycle_data if not self.get_fertileday(temp)]
        avg_bbt = self.avg_temp()
        print("\nFertile Days:", fertile_days if fertile_days else "None")
        print("Infertile Days:", infertile_days if infertile_days else "None")
        print(f"Average Basal Body Temperature: {avg_bbt:.2f}°C")
        
    def plot_data(self):
        fertile_temp = 36.3
        if not self.cycle_data:
            print("No temperature data available.")
            return
        
        cycle_days = [cycleday for _, cycleday, _ in self.cycle_data]
        temp_values = [temp for _, _, temp in self.cycle_data]
        
        plt.plot(cycle_days, temp_values, marker='o', label = "Body Temperature")
        plt.axhline(y=fertile_temp, color='r', linestyle='--', label='Fertile Threshold')
        plt.xlabel('Cycle Day')
        plt.ylabel("Body Temperature")
        plt.title('Body Temperature History')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    def next_period_date(self):
        if len(self.cycle_data) < 2:
            print("\nInsufficient data to predict the next period date.")
            return None
    
        cycle_lengths = []
        for i in range(1, len(self.cycle_data)):
           cycle_lengths.append((self.cycle_data[i][0]-self.cycle_data[i-1][0]).days)
           average_cycle_length = sum(cycle_lengths) / len(cycle_lengths)
    
    
        last_period_date = self.cycle_data[-1][0] 
        next_period_date = last_period_date + datetime.timedelta(days=int(average_cycle_length))
        return next_period_date


       
def main():
    tracker = PeriodTracker()
    
    while True:
        print("\nMenu")
        print("1. Log Morning Temperature")
        print("2. Display Temperature History")
        print("3. Show Graph")
        print("4. Analyze Data")
        print("5. Predict Date of Next Period")
        print("6. Help")
        print("7. Exit Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            today = datetime.date.today()
            print(f"\nToday's Date: {today.strftime('%Y-%m-%d')}")
            while True:
                cycleday = input("Enter cycle day: ")
                if cycleday.isdigit():
                    cycleday = int(cycleday)  
                    break
                else:
                    print("\nPlease enter a valid integer for cycle day.")
            
            while True:
                temp = input("Enter morning temperature (°C): ")
                try:
                    temp = float(temp)
                    break
                except ValueError:
                    print("\nPlease enter a valid decimal number for temperature.")
            
            tracker.recordtemp(today, cycleday, temp)
            
        elif choice == "2":
            tracker.temphistory()
            
        elif choice == "3": 
            tracker.plot_data()
            
        elif choice == "5":
            next_period_date = tracker.next_period_date()
            if next_period_date:
                print("\nNext predicted period date:", next_period_date.strftime('%Y-%m-%d'))
                
        elif choice == "4":
            tracker.analyzedata()
            
        elif choice == "6":
            print("\nIf in need of assistance using LUNALOOP:")
            print("\tCall (647) 289-1469 to receive one-on-one guidance.") 
            print("\tEmail our LUNALOOP team at lunaloop@gmail.com.")
            print("\tCome to our resource centre at 452 Crew Road, Cambridge, ON, M3J1P3")
            
        elif choice == "7":
            print("\nYou have exited the menu.")
            print("Have a nice day!")
            break
        
        else:
            print("\nInvalid choice. The number entered must be either 1, 2, 3, 4, 5, or 6.")

if __name__ == "__main__":
    main()