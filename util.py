#too lazy to merge utils.py and util.py
import floodfill
def outofboard(coord, w, h):
  x = coord['x']
  y = coord['y']
  if not x>w and not x<0 and not y > h and not y<0:
    return False
  else:
    return True
def neighboors(coord, w, h):
  #format: up, down, left, right
  x = coord['x']
  y = coord['y']
  returnthis = []
  if not outofboard({'x':x, 'y':y+1}, w, h):
    returnthis.append({'x':x, 'y':y+1})
  if not outofboard({'x':x, 'y':y-1}, w, h):
    returnthis.append({'x':x, 'y':y-1})
  if not outofboard({'x':x-1, 'y':y}, w, h):
    returnthis.append({'x':x-1, 'y':y})
  if not outofboard({'x':x+1, 'y':y}, w, h):
    returnthis.append({'x':x+1, 'y':y})
  return returnthis
def checkindex(coord, list):
  counter = 0
  for set in list:
    if coord in list[set]:
      return counter+1
    counter +=1
def get_area_control(testdata, snakenumber):
  f = floodfill.floodfill(testdata, testdata['you']['head'], [])
  #print(testdata['you']['head'])
  #print(f"My space: {f}")
  FF = floodfill.floodfill(testdata, testdata['board']['snakes'][snakenumber]['head'], [])
  #print(f"Other space: {FF}")
  myspace = []
  otherspace = []
  nomanszone = []
  for i in range(len(f)):
    for b in f[str(i+1)]:
      opp_access = checkindex(b, FF)
      if i+1<opp_access:
        myspace.append(b)
      if i+1 == opp_access:
        if testdata['board']['snakes'][snakenumber]['length']>=data['you']['length']:
          otherspace.append(b)
        else:
          nomanszone.append(b)
      if i+1>opp_access:
        otherspace.append(b)
  return myspace, nomanszone, otherspace
def newline(num=1):
  for i in range(num):
    print("\n")
def checkfortrapping(testdata, head=None):
  if head==None:
    head = testdata['you']['head']
  my, no, op = get_area_control(testdata, 1)
  aff = floodfill.floodfill(testdata, head, op)
  return aff
