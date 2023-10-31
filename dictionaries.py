#store changeable and unordered data with keys and values
capitals = {'Eth': 'AA',
            'USA': 'DC',
            'England': 'London'}
print(capitals['Eth'])
print(capitals.update({'Eth': 'Adama'}))
print(capitals.update({'kenya': 'nairobi'}))
print(capitals.keys())
print(capitals.values())
print(capitals.pop('kenya'))

for keys, values in capitals.items():
    print(keys, values)
