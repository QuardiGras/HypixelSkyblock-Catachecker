
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
  print('Invalid inputs, try again.')
else:
  print(api0['dungeons']['catacombs']['level']['level'])


# ['dungeons']['catacombs']['level']['level']