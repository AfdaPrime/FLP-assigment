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
  print(msg+"\n")

def extractInfo(text,count):
  print("Log no: ",count)
  date = text.pop(0)
  extractDate(date)
  time = text.pop(0)
  extractTime(time)
  level = text.pop(1)
  extractLevel(level)
  extractMessage(text)
  return

count = 0  # Initialize row counter
rows_to_display = 10  # Number of rows to display per action

with open('system_file.txt', 'r') as file:
  lines = file.readlines()  # Read all lines into a list

  total_lines = len(lines)  # Total number of lines in the file
  start_index = 0  # Starting index for the next set of rows

  while start_index < total_lines:
    print(start_index)
    end_index = min(start_index + rows_to_display, total_lines)
    for line in lines[start_index:end_index]:
        count += 1
        textArray = split(line)
        extractInfo(textArray, count)
    # Ask user for input to determine next action
    action = input("Press 'a' to display the next 10 rows, 'b' for the next 100 rows, 'c' to display all, or any other key to exit: ")

    if action == 'a':
        rows_to_display = 10
    elif action == 'b':
        rows_to_display = 100
    elif action == 'c':
        rows_to_display = total_lines
    else:
        break  # Exit loop if any other key is pressed

    start_index = end_index