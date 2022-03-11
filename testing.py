from best_move import best
data = {"game":{"id":"804205","ruleset":{"name":"standard","version":"v.1.2.3"},"timeout":500},"turn":200,"you":{"health":100,"id":"you","name":"#22aa34","body":[{"x":5,"y":3},{"x":4,"y":3},{"x":4,"y":2},{"x":3,"y":2},{"x":2,"y":2},{"x":2,"y":3},{"x":2,"y":4},{"x":2,"y":5}],"head":{"x":5,"y":3},"length":8},"board":{"food":[{"x":1,"y":7}],"height":11,"width":11,"snakes":[{"health":100,"id":"you","name":"#22aa34","body":[{"x":5,"y":3},{"x":4,"y":3},{"x":4,"y":2},{"x":3,"y":2},{"x":2,"y":2},{"x":2,"y":3},{"x":2,"y":4},{"x":2,"y":5}],"head":{"x":5,"y":3},"length":8},{"health":100,"id":"#FFd54f","name":"#FFd54f","body":[{"x":6,"y":2},{"x":6,"y":1},{"x":7,"y":1}],"head":{"x":6,"y":2},"length":3}]}}
scores = [
  350, 1.5, 70, 1.3, 60, 60, 60, 70, 55, 2.5, 60
]
print(best(data, scores))
