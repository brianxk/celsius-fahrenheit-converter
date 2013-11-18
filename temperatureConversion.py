"""
Program: temperatureConversion.py
Author: Brian Kim

This module contains computation functions that perform Fahrenheit to
Celsius conversions and vice versa

1. Define two separate functions for each aforementioned duty
2. Computation functions will be independent of a main function
"""

def fahrenheitToCelsius(fahrenheit):
    """Receives Fahrenheit, computes and returns Celsius"""

    return (round(((fahrenheit - 32) * (5/9)), 2))

def celsiusToFahrenheit(celsius):
    """Receives Celsius, computes and returns Celsius"""

    return (round(((celsius * (9/5)) + 32), 2))

