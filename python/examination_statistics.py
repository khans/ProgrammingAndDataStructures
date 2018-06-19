grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

#Printing the grades
print_grades(grades)

#Summing up
def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
#Printing the sum
print grades_sum(grades)

#Average
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / len(grades)
    return average
#Print average
print grades_average(grades)

#Variance
def grades_variance(grades,average):
    variance = 0
    var_list = []
    for each in grades:
        #subtract the grade from the average and square it
        temp = (average - each)**2
        #append the squared number to var_list
        var_list.append(temp)
    #Summing the squares    
    for var in var_list:
        variance += var
    
    #returning correct variance:
    variance = variance/len(grades)
    return variance
#Printing Variance
print grades_variance(grades, grades_average(grades))

#Standard deviation
def grades_std_deviation(variance):
    #standard deviation is the square root of variance
    standard_deviation = variance**0.5
    return standard_deviation

#Printing standard deviation
print grades_std_deviation(grades_variance(grades, grades_average(grades)))