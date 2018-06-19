import math
def clockangle(hrs,mins):
    
    # the hrs are between 0 and 11, and minutes from 0 to 59
    if (hrs in range(0,12) and mins in range(0,60)):
    #angle between minute hand and 12 'o' clock:
    #Now imagine the hands at 12, its 0 degrees, the minute hand moves 60 minutes to cover 360 degrees
    #So minute hand moves 360/60 degrees each minute. O for x minutes, the angle is 6x
        angle_min_12 = 6 * mins
    
    #angle between hour hand and 12 'o' clock:
    #So it takes 12 hours to make 360 degrees, so it makes 360/12=30 degrees for each hour angle.
    #But we need additional position as well.
    #The hour hand of a normal 12-hour analogue 
    #clock turns 360 d egreein 12 hours (720 minutes) or 0.5 degree per minute.
    #The minute hand rotates through 360 degree in 60 minutes or 6 degree per minute.
        angle_hr_12 = (30 * hrs) + (0.5 * mins)    
        clock_angle = math.fabs(angle_hr_12 - angle_min_12)        
        return clock_angle
    
    else:
        return -1
    
    
print clockangle(0,30);
    
    
    
    
        