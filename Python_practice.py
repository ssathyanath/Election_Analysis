# print("Hello World")

# ## If Statement
# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# temperature = int(input("What is the temperature outside? "))

# ## If Else
# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")

# ## Nested If
# score = int(input("What is your test score? "))

# # Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# else:
#     if score >= 80:
#         print('Your grade is a B.')
#     else:
#         if score >= 70:
#             print('Your grade is a C.')
#         else:
#             if score >= 60:
#                 print('Your grade is a D.')
#             else:
#                 print('Your grade is an F.')


# ## Membership Operators
# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties

# for county in counties:
#     print(county)


# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# # for county in counties_dict:
# #     print(county)

# # for county in counties_dict.keys():
# #     print(county)

# for county, voters in counties_dict.items():
#     print(f"{county} has {voters} registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(f"{county_dict['county']} has {county_dict['registered_voters']} registered voters")