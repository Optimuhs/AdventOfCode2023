# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen

# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?
word_digits = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight":8, "nine": 9}
starts_with = ["z", "o", "t", "f", "s", "e", "n"]

def calibrate():
  filePath = 'trebuchetData.txt'
  parsedData = parseFile(filePath)
  return parsedData

# Check sliding window to see if it matches any of the numbers spelled
def windowChecker(window):
    for i in word_digits.keys():
        if window in i:
            return True
    return False
    

def parseDataUtil(line):
  nums = []
  slow = 0
  fast = 1
  # While the fast pointer is still within bounds of the string
  while fast <= len(line):
    str_slice = line[slow: fast + 1]
    # Check if our starting character is a number
    if line[slow].isdigit():
      nums.append(line[slow])
      fast += 1
      slow += 1
    # Check if our fast pointer has moved out of bounds
    elif fast >= len(line):
        break
    # Check if fast pointer is a numbers 
    elif line[fast].isdigit():
      nums.append(int(line[fast]))
      slow = fast + 1
      fast = slow + 1
    # If our window matches a number spelling
    elif str_slice in word_digits.keys():
      nums.append(word_digits[str_slice])
      slow = fast 
      fast += 1
    # Check our window to ensure our string is on course to match
    elif not windowChecker(str_slice):
      slow += 1
      fast = slow + 1
    else:
      fast += 1
  return nums

def parseFile(dataFilePath):
  valueArray = []
  total = 0 
  with open(dataFilePath, "r") as file:
    for line in file:
      line = line.strip("\n")
      parsedValue = parseDataUtil(line)
      # Make 2 digit value
      str_val = str(parsedValue[0]) + str(parsedValue[-1])
      total += int(str_val)
  return total


if __name__ == "__main__":
  result = calibrate()
  print(f"calibrated value {result}")