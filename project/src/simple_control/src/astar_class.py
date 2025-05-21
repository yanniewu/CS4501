from Queue import PriorityQueue
import copy
import math


class AStarPlanner:

  def __init__(self, safe_distance=1):
    self.safe_distance = safe_distance

  def plan(self, map_data, drone_position, goal_position):

    frontier = PriorityQueue()
    frontier.put((0, drone_position))
    came_from = {}
    cost_so_far = {}
    came_from[str(drone_position)] = None
    cost_so_far[str(drone_position)] = 0
    final_path = []
    while not frontier.empty():
      current = frontier.get()
      current = list(current[1])
      if current[0] == goal_position[0] and current[1] == goal_position[1]:
          while came_from[str(current)] != None:
              final_path.append(current)
              current = came_from[str(current)]
          final_path.append(current)
          return list(reversed(final_path))
      for next in self.get_neighbors(current, map_data):
        edge_cost = math.sqrt(((current[0] - next[0])**2) + ((current[1] - next[1]) ** 2))
        goal_cost = math.sqrt(((goal_position[0] - next[0])**2) + ((goal_position[1] - next[1]) ** 2))
        new_cost = cost_so_far[str(current)] + edge_cost
        if str(next) not in cost_so_far or new_cost < cost_so_far[str(next)]:
            cost_so_far[str(next)] = new_cost
            priority = new_cost + goal_cost
            frontier.put((priority, next))
            came_from[str(next)] = current
    return [drone_position]

  # Get the children nodes for the current node
  def get_neighbors(self, node_in, map_in):
    # A list of neighbors
    neighbors = []
    # Get the current position
    pos = node_in
    # For all adjacent values
    for x_dim in range(-1, 2):
      for y_dim in range(-1, 2):
        # If the values are not 0, 0 (which is itself)
        if not (x_dim == 0 and y_dim == 0):
          # If the values are inside the map
          if (0 <= pos[0] + x_dim < map_in.shape[0]) and(0 <= pos[1] + y_dim < map_in.shape[1]):
            # If that value is an open square on the map
            if map_in[pos[0] + x_dim][pos[1] + y_dim] == 0:
              # Create a neighbor with the new position
              n = [pos[0] + x_dim, pos[1] + y_dim]
              # Save the neighbors
              neighbors.append(n)
    return neighbors
