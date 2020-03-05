# Write a Python program that reads a number of seconds and prints it in the format - hrs:min:secs

# Python Program to Convert seconds
# into hours, minutes and seconds

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)


# Driver program
n=int(input("Enter the time in seconds:"))
print(convert(n))


