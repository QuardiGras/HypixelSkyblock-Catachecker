
# importing dependencies
import requests

# defining functions

# deciding 
ign = input('What is your ign? \n')
profile = input('What profile? \n')

# main
api0 = requests.get('https://sky.shiiyu.moe/api/v2/dungeons/' + ign + '/' + profile).json()

invalid = 'error' in api0

if invalid == True:
  print(' ')
else: 
  print('Catacombs level for user "' + ign + '" on the profile "' + profile + '": ', api0['dungeons']['catacombs']['level']['level'])


# ['dungeons']['catacombs']['level']['level']

try:
  progress = api0['dungeons']['catacombs']['level']['progress']

  progress_roundable = progress * 100

  progress_printable = round(progress_roundable, 2)

  print('Estimated percent of the way there to the next catacombs level:', progress_printable)

except:
  print('Invalid inputs, try again.')