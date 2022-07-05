temp1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
intToC = []
thresHold = 40
# printer(elements)
# - Accepts a list
# - Prints every element of the list


def printer(elements):
    for element in elements:
        print(element)
    return elements
    ...


# to_celsius(temperatures)
# - Accepts a list of temperatures
#   in degrees Fahrenheit
# - Returns a list of temperatures
#   in degrees Celsius
# The conversion is:
#   C = (F - 32) * (5/9)
def to_celsius(temperatures):
    for temp in (temperatures):
        intToC.append(temp - 32 * (5/9))

    return intToC


print(to_celsius(temp1))


# hottest_days(temperatures, threshold)
# - Accepts a list of temperatures
# - Accepts a threshold temperature
# - Returns a list of temperatures
#   that exceed the threshold


def hottest_days(temperatures, threshold):
    hotlist = []
    for temp in (temperatures):
        if temp > threshold:
            hotlist.append(temp)
        else:
            pass
    return hotlist


# log_hottest_days(temperatures, threshhold)
# - Accepts a list of temperatures
#   IN DEGREES FAHRENHEIT
# - Accepts a threshold temperature
#   IN DEGREES FAHRENHEIT
# - Prints temperatures that exceed the
#   threshold IN DEGREES CELSIUS
# hint: you can combine
#       all previous functions
def print_hottest_days(temperatures, threshhold):

    to_celsius(temperatures)
    hottest_days(temperatures, threshhold)
    print(hottest_days(temperatures, threshhold))


print_hottest_days(temp1, thresHold)
