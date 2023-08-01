#!/usr/bin/python3

def canUnlockAll(boxes):
    # Initialize a set to keep track of the keys we have
    keys = set([0])

    # Initialize a set to keep track of the boxes we can visit
    visited_boxes = set()

    # Perform a depth-first search to find all reachable boxes
    def dfs(box_num):
        visited_boxes.add(box_num)
        for key in boxes[box_num]:
            if key not in visited_boxes:
                keys.add(key)
                dfs(key)

    # Start the DFS from the first box (box 0)
    dfs(0)

    # Check if we have visited all boxes
    return len(visited_boxes) == len(boxes)
