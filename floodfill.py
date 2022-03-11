import util
def floodfill(data, start, nocheck=[]):
  #assign variables
  #format: up down left right
  access_space = {}
  already_checked = []
  #nocheck = []
  counter = 1
  squares_added = None
  newcoords = []
  oldcoords = []
  #conveinience
  board = data['board']
  food = board['food']
  snakes = board['snakes']
  you = data['you']
  h = board['height']
  w = board['width']
  for snake in data['board']['snakes']:
    for bodypart in snake['body']:
      nocheck.append(bodypart)
  nocheck.append(start)
  #print("NOCHECK:", nocheck)
  oldcoords.append(start)
  while squares_added !=0:
    #print("starting")
    added_nodes = []
    # add new coords
    for rootcoord in oldcoords:
      new_nodes = util.neighboors(rootcoord, w, h)
      for newcoord in new_nodes:
        if newcoord not in nocheck:
          added_nodes.append(newcoord)
          nocheck.append(newcoord)
    squares_added = len(added_nodes)
    if squares_added == 0:
      break
    oldcoords = None
    oldcoords = added_nodes.copy()
    access_space[str(counter)] = added_nodes.copy()
    counter +=1
  return access_space
