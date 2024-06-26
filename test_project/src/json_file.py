import json

# Read JSON data
with open('euro_cap_matches.json', 'r') as file:
    matches = json.load(file)

# Calculating Total goals scored
total_goals = sum(match['Score A'] + match['Score B'] for match in matches)
print(f"Total goals scored in all matches: {total_goals}")

# Filtering high scoring matches
high_scoring_matches = [matches for match in matches if match ['Score A'] + match ['Score B'] > 3]

# high_scoring_matches = []
# for match in matches:
#     if match['Score A'] + match['Score B'] > 3:
#         high_scoring_matches += match
# In this example, you need to initialise high_scoring_matches to empty list first


# Writing the filtered data to a new JSON file
with open('high_scoring_matches.json', 'w') as file:
    json.dump(high_scoring_matches, file, indent=4)
    