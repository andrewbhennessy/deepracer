# Copyright 2019 Andrew Boughan Hennessy ©
def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    import math
    
    # Read input parameters
    #//track_width = params['track_width']
    #distance_from_center = params['distance_from_center']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    all_wheels_on_track = params['all_wheels_on_track']
    is_left_of_center = params['is_left_of_center']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    
    turn5turn6 = [25,26,27,28,29,30]
    turn6turn1 = [1,2,3,4,5,6]
    turn1turn2 = [7,8,9]
    turn2turn3 = [10,11,12,13,14,15]
    turn4turn5 = [16,17,18,19,20,21,22,23,24]
    
    
    # Initialize the reward with typical value 
    reward = 1.0
	
    locOnTrack = 0
    if is_left_of_center:
        locOnTrack = track_width/2 - distance_from_center
    else:
	    locOnTrack = track_width/2 + distance_from_center
	
	# Calculate 3 markers that are at varying distances away from the center line
    inside = 0.33 * track_width
    middle = 0.66 * track_width
    outside = 1 * track_width

	
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
	
	# Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0]) 
	# Convert to degree
    track_direction = math.degrees(track_direction)
    # Cacluate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)

	# Penalize the reward if the difference is too large
    DIRECTION_THRESHOLD = 10.0
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5
    if not all_wheels_on_track:
        reward *= 0.5
	    
    if next_point in turn5turn6:
        if locOnTrack <= inside:
            reward *= .5
        elif locOnTrack <= middle:
            reward *= 1.1
        elif locOnTrack <= outside:
            reward * 1.5
        else:
            reward *= .25  # likely crashed/ close to off track
    elif next_point in turn6turn1:
        if locOnTrack <= inside:
            reward *= .5
        elif locOnTrack <= middle:
            reward *= 1.3
        elif locOnTrack <= outside:
            reward * 1.5
        else:
            reward *= .25  # likely crashed/ close to off track
    elif next_point in turn1turn2:
        if locOnTrack <= inside:
            reward *= .5
        elif locOnTrack <= middle:
            reward *= 1.5
        elif locOnTrack <= outside:
            reward * .75
        else:
            reward *= .25  # likely crashed/ close to off track
    elif next_point in turn2turn3:
        if locOnTrack <= inside:
            reward *= 1.5
        elif locOnTrack <= middle:
            reward *= 1.1
        elif locOnTrack <= outside:
            reward * .5
        else:
            reward *= .25  # likely crashed/ close to off track
    elif next_point in turn4turn5:
        if locOnTrack <= inside:
            reward *= 1.5
        elif locOnTrack <= middle:
            reward *= 1.01
        elif locOnTrack <= outside:
            reward * .5
        else:
            reward *= .25  # likely crashed/ close to off track
    else:
	    pass
    
    return float(reward)
