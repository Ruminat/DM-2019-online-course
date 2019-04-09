for l in range(1, 1000):
  print(' --- --- l = ' + str(l) + ' --- ---')
  elems = []
  for n in range(1, l + 1):
    if (l % n == 0): elems.append(n)
  print(2**(len(elems)), elems)