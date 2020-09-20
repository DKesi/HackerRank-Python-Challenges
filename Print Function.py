# The included code stub will read an integer, , from STDIN.
#
# Without using any string methods, try to print the following:
# 123.....n
#
# Note that "" represents the consecutive values in between.
#
# Example
#
# Print the string 12345.

print("enter an integer")
n = int(input())
for i in range(1,n+1):
    print(i, end="")
