names = ['jos', 'jef', 'jeffrey', 'jamal', 'josselyn', 'jablaze', 'karl', 'marx']

new_list= []

for name in names:
    if name.startswith('j'):
        name = name.capitalize()
        new_list = new_list + [name]
print(new_list)

# dit bovenste gedeelte kan hieronder in één lijn code 

with_capital = [value.capitalize() for value in names if value.startswith('j') ]
print(with_capital)


