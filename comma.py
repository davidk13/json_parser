with open('new_partners.txt') as f:
  result = ','.join(f) + ','
  close('new_partners.txt')
print f