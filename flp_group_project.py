# -*- coding: utf-8 -*-
"""FLP Group Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KawovsFY_oUoIIfYPu5e6_Tj0_umOTat
"""

import calendar
from datetime import datetime

days = {num: str(num) + "th" if num not in [1, 2, 3] else str(num) + ["st", "nd", "rd"][num - 1] for num in range(1, 31)}

def split (text):
  return text.split()

def extractDate(date):
  year, month, day = map(int, date.split("-"))
  print("This log was created on",days[day],"of",calendar.month_name[month],"in the year",year)
  return

def extractTime(time):
  time_obj = datetime.strptime(time, "%H:%M:%S")
  formatted_time = time_obj.strftime("%I:%M %p")
  print(formatted_time)
  return

def extractLevel(level):
  print("Log level is",level)
  return

def extractMessage(text):
  msg = "The message is: " + " ".join(filter(lambda x: x != "-", text))
  print(msg)

def extractInfo(text):
  date = text.pop(0)
  extractDate(date)
  time = text.pop(0)
  extractTime(time)
  level = text.pop(1)
  extractLevel(level)
  extractMessage(text)
  return

text = "2024-02-29 13:55:23 - INFO - Starting server"
textArray = split(text)
extractInfo(textArray)