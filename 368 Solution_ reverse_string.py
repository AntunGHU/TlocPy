def reverse_string(str):
  s = ''
  for i, char in enumerate(str[::-1]):
    s += char
  return s

reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'
