print("Hello World!")
print(type(3))
print(type(2019))
ballots = 1341
print(type(ballots))
print(type(73.81))
print(type('Hello World'))
print(type(True))

print("------------")
print(5 + 2 * 3)
print(8 // 5 - 3)
print(8 + 22 * 2 - 4)
print(16- 3 / 2 + 7 - 1)
print(3 ** 3 % 5)
print(5 + 9 * 3 / 2 - 4)
print("------------")
print((5 + 2) * 3)
print((8 // 5) - 3)
print(8 + (22 * (2 - 4)))
print(16 - 3 / (2 + 7) - 1)
print(3 ** (3 % 5))
print(5 + (9 * 3 / (2 - 4)))






counties = ["Arapahoe","Denver","Jefferson"]
print(counties)
print(counties[0])
print(counties[1])
print(counties[2])
print(counties[-1])
print(counties[-2])
print(counties[-3])

print("--------------")
print(len(counties))
print("--------------")
print(counties[0:2])
print(counties[0:1])
print(counties[:2])
print(counties[1:])
print(counties[1:3])
print("--------------")

counties.append("El Paso")
counties.insert(2, "El Paso")
print(len(counties))
print(counties)

counties.remove("El Paso")
print(len(counties))
print(counties)

counties.pop(3)
#counties.pop(-1)
print(counties)

print("-------Update-------")
counties[2] = "El Paso"
print(counties)
print("----------------------")



counties = ["Arapahoe","Denver","Jefferson"]
counties.insert(1,"El Paso")
counties.remove("Arapahoe")
print(counties)
counties.remove("Denver")
counties.insert(2,"Denver")
counties.append("Arapahoe")
print(counties)
print("----------------")


counties_tuple = ("Arapahoe","Denver","Jefferson")
print(len(counties_tuple))
print(counties_tuple[1])
print(counties_tuple[:2])
print(counties_tuple[:-1])
print("------------------")

counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

print(counties_dict["Arapahoe"])
print(counties_dict["Denver"])
print(counties_dict["Jefferson"])
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get("Denver"))
print("---------------")

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data[0]["county"])
print(voting_data[0].get("county"))
print(voting_data[0]["registered_voters"])
print(voting_data[0].get("registered_voters"))

voting_data.append({"county": "El Paso", "registered_voters":461149})
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.pop(0)
voting_data.pop(0)
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)
print("------------------")

# # How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")
# print("-"* 100)
# counties = ["Arapahoe", "Denver", "Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])
# print("--------------")

# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")

x = 0
while x <= 5:
    print(x)
    x = x +1
print("---------------")

counties = ["Arapahoe","Denver","Jefferson"]
for county in counties:
    print(county)
print("---------------")

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
print("---------------")

for num in range(5):
    print(num)
print("---------------")

for i in range(len(counties)):
    print(counties[i])
print("---------------")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)
print("------Keys------")

for county in counties_dict.keys():
    print(county)
print("---------------")

print("Values")
for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

print("Items")
# for key, value in dictionary_name.items():
    # print(key, value)
for county, voters in counties_dict.items():
    print(county, voters)

for county, voters in counties_dict.items():
    print(county, " county has ", voters, " registered voters ")

    voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

# tedious; try not to use this method very much. more efficient ways to do the process
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

