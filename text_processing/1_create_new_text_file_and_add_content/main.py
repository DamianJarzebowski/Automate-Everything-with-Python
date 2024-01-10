file = open('file.txt', 'w')
file.write('First text\n')
file.write('Second text')
file.close()




# Recomended, because file is automatic close
content = """
First text

Second text"""

with open('file1.txt', 'w') as file:
  file.write(content)
  file.close


