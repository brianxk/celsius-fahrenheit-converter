"""
Program: temperatureConversionGUIWithoutButtons.py
Author: Brian Kim

This module will provide a GUI for converting Celsius temperatures to Fahrenheit
and vice versa

1. Import tkinter and computation function modules
2. Initialize interface (GUI)
3. Design and implement MVC pattern w/ input validation
"""
from tkinter import *
from temperatureConversion import *

class temperatureGUI(Frame):
    """Class definition for temperature conversion GUI"""

    def __init__(self):
        """Constructor for GUI window and widgets"""

        # Construct window and reset title
        Frame.__init__(self)
        self.master.title("Temperature Converter")
        self.grid()

        # Label and Entry for Fahrenheit
        fahrenheitLabel = Label(text = "°F")
        fahrenheitLabel.grid(row = 0, column = 0)
        self.fahrenheitVar = DoubleVar(value = 32.0)
        fahrenheitEntry = Entry(textvariable = self.fahrenheitVar)
        fahrenheitEntry.bind("<KeyRelease>", self.convertToCelsius)
        fahrenheitEntry.grid(row = 1, column = 0)
        
        # Label and Entry for Celcius
        celsiusLabel = Label(text = "°C")
        celsiusLabel.grid(row = 0, column = 1)
        self.celsiusVar = DoubleVar()
        celsiusEntry = Entry(textvariable = self.celsiusVar)
        celsiusEntry.bind("<KeyRelease>", self.convertToFahrenheit)
        celsiusEntry.grid(row = 1, column = 1)

        # Error Label
        self.errorLabel = Label(text = "Must enter a number")

    def convertToCelsius(self, event):
        """Event-handler triggered by <KeyRelease> in the Fahrenheit entry field
            - determines Celsius temp and adjusts corresponding entry field accordingly"""

        # Remove error label and convert
        try:
            if self.fahrenheitVar.get() <= -459.67:
                messagebox.showerror(message = "Temperatures cannot reach or exceed absolute zero (-459.67 °F)")
                self.fahrenheitVar.set(32)
                self.celsiusVar.set(0)
            else:
                self.errorLabel.grid_remove()
                self.celsiusVar.set(fahrenheitToCelsius(self.fahrenheitVar.get()))

        # Show error label and clear field
        except ValueError:
            self.errorLabel.grid(row = 2, column = 0)
            self.celsiusVar.set("")
        
    def convertToFahrenheit(self, event):
        """Event-handler triggered by <KeyRelease> in the Celsius entry field
            - determines Fahrenheit temp and adjusts corresponding entry field accordingly"""

        # Remove error label and convert
        try:
            if self.celsiusVar.get() <= -273.15:
                messagebox.showerror(message = "Temperatures cannot reach or exceed absolute zero (-273.15 °C)")
                self.fahrenheitVar.set(32)
                self.celsiusVar.set(0)
            else:
                self.errorLabel.grid_remove()
                self.fahrenheitVar.set(celsiusToFahrenheit(self.celsiusVar.get()))

        # Show error label and clear field
        except ValueError:
            self.errorLabel.grid(row = 2, column = 0)
            self.fahrenheitVar.set("")

def main():
    """Instantiates GUI window object for temperature conversion"""

    temperatureGUI().mainloop()

main()

