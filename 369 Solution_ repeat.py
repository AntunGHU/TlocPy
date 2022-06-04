def repeat(string, num):
  if(num == 0): 
      return ''
  i = 0
  newStr = ''
  while(i < num):
      newStr += string
      i += 1
  return newStr
  
repeat('*', 3) # '***' 
repeat('abc', 2) # 'abcabc' 
repeat('abc', 0) # ''
