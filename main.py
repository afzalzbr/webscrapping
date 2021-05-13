import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

# Getting the title tag
print(soup.title)

# Getting the name of the tag
print(soup.title.name)

# Getting the name of parent tag
print(soup.title.parent.name)

# use the child attribue to get 
# the name of the child tag

s = soup.find('div', class_='entry-content')

# Finding Elements by Class 
print('Find element by class = \'entry-content\'')
print(s)

lines = s.find_all('p')
print(lines)

# finding element by id
m = soup.find('div', id= 'main')

print('Finding element with id = \'main\'')
# print(m)


print('Extract text from the tags')
for line in lines:
    print(line.text)

# Getting the leftbar
leftbar = m.find('ul', class_='leftBarList')

print('Printing the text from leftbar')
# All the li under the above ul
lines_left = leftbar.find_all('li')

for line in lines_left:
    print(line.text)