
import randfacts as rf

print('Random facts')
x = ''

while x == '':
    print('Press enter for a fact')
    x = input()
    facts = rf.get_fact()
    print(facts)

