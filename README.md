# 🌤️ Weather Report System using JSON (Python)

A simple Python application that reads weather data from a JSON file and displays the weather report for a user-entered city.

## Description
This project demonstrates how to store structured data in a JSON file and read it using Python.  
Based on the city entered by the user, the program displays temperature and weather condition.

## Project Files
- weather.json → Stores weather data
- winter.py → Python program to read and display weather information

## Input File (weather.json)
{
    "chennai": {
        "temp": 32,
        "condition": "sunny"
    },
    "bangalore": {
        "temp": 25,
        "condition": "cloudy"
    },
    "delhi": {
        "temp": 30,
        "condition": "hot"
    },
    "mumbai": {
        "temp": 29,
        "condition": "humid"
    }
}

## Requirements
- Python 3.x

## How to Run
1. Keep `weather.json` and `winter.py` in the same folder
2. Run the program:
python winter.py

## Sample Output
Enter the city: chennai

Weather Report  
City: Chennai  
Temperature: 32 °C  
Condition: sunny  

## Concepts Used
- JSON file handling
- json module
- Dictionary access
- User input handling
- Conditional statements

## Learning Outcome
- Learned how to read JSON files in Python
- Understood structured data storage
- Practiced real-world data retrieval logic

## Author
Keerthisai
