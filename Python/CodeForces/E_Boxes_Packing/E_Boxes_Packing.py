box_number= int(input())
boxes_lenghts = list(map(int, input().split()))


boxes_frequency = {i: boxes_lenghts.count(i) for i in boxes_lenghts}

min_visible_boxes = max(boxes_frequency.values())

print(min_visible_boxes)