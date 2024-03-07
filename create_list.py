# Create a list
NFL_teams = ["Titans", "Colts", "Bears", "Steelers", "Seahawks"]

# Create the loop to print the list
for teams in NFL_teams:
    # Print the list
    print(teams)

# Add Ravens to the list
NFL_teams.append("Ravens")

# Verify that Ravens was added
print(NFL_teams)

# Print the length of the list
print(len(NFL_teams))

# Add Ravens to the list
NFL_teams.remove("Ravens")
# Verify that Ravens was removed from the list
print(NFL_teams)

# Print the length of the list
print(len(NFL_teams))