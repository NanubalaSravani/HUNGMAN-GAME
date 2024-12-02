from collections import defaultdict

class Lane:
    def _init_(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
    
    def is_vertical(self):
        return self.x1 == self.x2
    
    def is_horizontal(self):
        return self.y1 == self.y2

def check_overlap(lane1, lane2):
    # Check if two lanes overlap
    if lane1.is_horizontal() and lane2.is_horizontal() and lane1.y1 == lane2.y1:
        return not (max(lane1.x1, lane1.x2) < min(lane2.x1, lane2.x2) or min(lane1.x1, lane1.x2) > max(lane2.x1, lane2.x2))
    if lane1.is_vertical() and lane2.is_vertical() and lane1.x1 == lane2.x1:
        return not (max(lane1.y1, lane1.y2) < min(lane2.y1, lane2.y2) or min(lane1.y1, lane1.y2) > max(lane2.y1, lane2.y2))
    return False

def check_intersection(lane1, lane2):
    # Check if two lanes intersect at a right angle
    if lane1.is_horizontal() and lane2.is_vertical():
        if min(lane1.x1, lane1.x2) <= lane2.x1 <= max(lane1.x1, lane1.x2) and min(lane2.y1, lane2.y2) <= lane1.y1 <= max(lane2.y1, lane2.y2):
            return (lane2.x1, lane1.y1)
    elif lane1.is_vertical() and lane2.is_horizontal():
        if min(lane2.x1, lane2.x2) <= lane1.x1 <= max(lane2.x1, lane2.x2) and min(lane1.y1, lane1.y2) <= lane2.y1 <= max(lane1.y1, lane1.y2):
            return (lane1.x1, lane2.y1)
    return None

def find_cross_junctions(lanes):
    junctions = defaultdict(int)
    
    # Iterate over each pair of lanes to check for cross-junctions
    for i in range(len(lanes)):
        for j in range(i + 1, len(lanes)):
            lane1, lane2 = lanes[i], lanes[j]
            
            # Check for overlap
            if check_overlap(lane1, lane2):
                continue
            
            # Check for intersection
            intersection = check_intersection(lane1, lane2)
            if intersection:
                junctions[intersection] += 1
    
    # Filter for cross-junctions that are actual cross-roads
    cross_junctions = [coord for coord, count in junctions.items() if count >= 1]
    return cross_junctions

# Sample input
lanes = [
    Lane(0, 0, 6, 0),   # Horizontal lane
    Lane(0, 0, 0, 6),   # Vertical lane, forming cross-junction with the horizontal one
    Lane(3, 0, 6, 0),   # Overlapping part of the horizontal lane
    Lane(2, 0, 6, 0)    # Overlapping part of the horizontal lane
]

# Finding cross-junctions where flyovers should be constructed
cross_junctions = find_cross_junctions(lanes)
print("Cross-junctions for flyovers:", cross_junctions)