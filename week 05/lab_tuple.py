# tuple.py
# this program stores the months of the year
# tuple in tuple that contains summer months only
# and prints out the summer months one at a time
# Author: Rachel King

months = ("January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
)
summer = months[4:7]
for month in summer:
    print(month)