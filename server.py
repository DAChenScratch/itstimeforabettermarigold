import bottle
import os
from best_move import best
    # TODO: Do things with data

@bottle.post('/snake/ping')
def ping():
  return 'pong'

@bottle.get('/snake')
def metadata():
    return {
        'color': '#888888',
        'author': 'DAChenScratch',
        'apiversion':"1",
        'version':'1.00 Beta',
        "head":"default",
        "tail":"default",
    }

@bottle.post('/snake/move')
def move():
    data = bottle.request.json
    scores = [
      350, 1.5, 70, 1.3, 60, 60, 60, 70, 55, 2.5, 60
    ]
    print(f"TURN NUMBER: {data['turn']}")
    move = best(data, scores)
    print('Sending move response as:', {"move": move})
    return {"move": move}

@bottle.post('/snake/end')
def end():
  data = bottle.request.json
  names = 'Snake names are: '
  for snake in data['board']['snakes']:
    if data['board']['snakes'].index(snake) != len(data['board']['snakes']) - 1:
      names =  names + snake['name'] + ', '
    else:
      if not len(data['board']['snakes']) == 1:
        names = names + 'and ' + snake['name'] + '.'
      else:
        names = names  + snake['name'] + '.'
  #os.system('clear')
  print('SNAKES REMAINING:', len(data['board']['snakes']))
  print(names)
  if len(data['board']['snakes']) == 1 and names == 'Snake names are: ' + data['you']['name']+'.':
    print('YEAH!!! VICTORY!!!')
  else:
    print('\n\n\n\nF in the terminal I lost.')
  return "hi"
# Expose WSGI app (so gunicorn can find it)

application = bottle.default_app()
bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))

