# def is_leap_year(year):
#     # every year divisible by 4
#     if year % 4 == 0:
#         # EXCEPT every year divisible by 100
#         if year % 100 == 0:
#             # UNLESS year also divisible by 400
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True

##### refactor #####
def is_leap_year(year):
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))
