from maths import distance_between
def assign(target):
  u = {
    "x":target['x'],
    "y":target['y'] + 1,
  }
  d = {
    "x":target['x'],
    "y":target['y'] - 1,
  }
  r = {
    "x":target['x'] + 1,
    "y":target['y'],
  }
  l = {
    "x":target['x'] - 1,
    "y":target['y'],
  }
  return u, d, l, r

def getPossibleMoves(bodies, startCoord, data, mybody, trapped = False, shouldprint = False):
  food = data['board']['food']
  ate_num = 0
  open_squares = [startCoord]
  if startCoord in bodies:
    return 0
  try:
    tail = mybody[len(mybody) - 1]
  except:
    return len(mybody) + 10
  width = data['board']['width']
  height = data['board']['height']
  DANGER = 0
  added = 1
  while not added == 0 and not len(open_squares) >=len(mybody) and not tail in open_squares:
    added = 0
    for coord in open_squares:
      temp_coords = assign(coord)
      for minicoord in temp_coords:
        if len(open_squares) > len(mybody):
          break
        if shouldprint:
          print(temp_coords)
        if not minicoord in bodies and not minicoord in open_squares and -1<coord['x']<width and -1<coord['y']<height:
          added +=1
          open_squares.append(minicoord)
          if minicoord in food:
            ate_num+=1
          if minicoord in get_dangerous_heads(data):
            DANGER +=1
  if trapped:
    #print('DANGERS:', DANGER)
    if tail in open_squares:
      return len(mybody) + 10
  return (len(open_squares) - ate_num - DANGER * 10) * 2


def getHeads(data):
  heads = []
  for i in range(len(data['board']['snakes'])):
    heads.append(data['board']['snakes'][i]['head'])
  return heads

def smaller_snakes_get_heads(data):
  heads = []
  for i in range(len(data['board']['snakes'])):
    if len(data['you']['body']) > len(data['board']['snakes'][i]['body']):
      heads.append(data['board']['snakes'][i]['head'])
  return heads

def get_dangerous_heads(data):
  heads = []
  for i in range(len(data['board']['snakes'])):
    if len(data['you']['body']) <= len(data['board']['snakes'][i]['body']) and data['board']['snakes'][i]['body'] != data['you']['body']:
      heads.append(data['board']['snakes'][i]['head'])
  return heads

def getBodies(data):
  bodies = []
  for j in range(len(data['board']['snakes'])):
    for k in range(len(data['board']['snakes'][j]['body']) - 1):
      #wow so many brackets
      bodies.append(data['board']['snakes'][j]['body'][k])
  return bodies

def indvBodies(data):
  bodies = []
  for j in range(len(data['board']['snakes'])):
    thisBody= []
    for k in range(len(data['board']['snakes'][j]['body']) - 1):
      #wow so many brackets
      thisBody.append(data['board']['snakes'][j]['body'][k])
    bodies.append(thisBody)
  return bodies

def safe(target, oh, ob, myh, mb):
  #oh for other's heads

  #ob for other's bodies
  close_units = []
  for i in range(3):
    y = target['y'] + i - 1
    for j in range(3):
      x = target['x'] + j - 1
      dct = {
        "x":x,
        "y":y,
      }
      #print(dct)
      if dct in oh:
        for body in ob:
          if body[0] == dct:
            length = len(body)
        #print(length)
        if length >= len(mb):
          close_units.append(dct)
  return close_units
def onlyOneWayToGo(data, target, shouldPrint):
  body = getBodies(data)
  movedUp, movedDown, movedRight, movedLeft = assign(target)
  moveList = [movedUp, movedDown, movedRight, movedLeft]
  moveScore = [None, None, None, None]
  for m in range(4):
    if not moveList[m] in body and -1<moveList[m]['x'] < data['board']['width'] and -1<moveList[m]['y']<data['board']['height']:
      moveScore[m] = 1
  if shouldPrint:
    print(f"MOVESCORE: {moveScore}")
    pass
  if 1 in moveScore:
    moveScore.pop(moveScore.index(1))
  if 1 in moveScore:
    return False
  else:
    return True

def areas_near_heads(heads, bodies, mybody, myhead):
  ret = []
  can_go = True
  for head in heads:
    for body in bodies:
      if body[0] == head and len(body) >= len(mybody) or head == myhead:
        can_go = False
    if can_go:
      areas = assign(head)
      for coord in areas:
        if coord in bodies:
          bodies.pop(bodies.index(coord))
        else:
          ret.append(coord)
  return ret


def i_am_closest(heads, myhead, target, actual_head):
  try:
    heads.pop(heads.index(actual_head))
  except:
    pass
  for h in heads:
    if distance_between(h, target) <= distance_between(myhead, target):
      return False
  return True




def trapped(bodies, target, data, shouldPrint):
  movedUp, movedDown, movedRight, movedLeft = assign(target)
  moveList = [movedUp, movedDown, movedRight, movedLeft]
  moveScore = [None, None, None, None]
  for m in range(4):
    if not moveList[m] in bodies and -1<moveList[m]['x'] < data['board']['width'] and -1<moveList[m]['y']<data['board']['height']:
      moveScore[m] = 1
  if shouldPrint:
    print(f"MOVESCORE: {moveScore}")
    pass
  if 1 in moveScore:
    moveScore.pop(moveScore.index(1))
  if not 1 in moveScore:
    return True
  else:
    return False


def onedge(myhead, width, height):
  if myhead['x'] == 0 or myhead['x'] == width - 1 or myhead['y'] == 0 or myhead['y'] == height - 1:
    return True
  return False
