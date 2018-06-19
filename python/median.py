def median(l):
    is_even = (len(l)%2 == 0)
    sorted_list = sorted(l)
    if is_even:
        one_index = len(l)/2
        second_index = one_index-1
        med = (sorted_list[one_index]+sorted_list[second_index])/2.0
        return med
    else:
        median_index =(len(l)-1)/2
        return sorted_list[median_index]
        

print median([1,3,6,7,12])
print median([7,3,1,4])