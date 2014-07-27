# Creating Data Objects

## Construct Vectors
vector_one = c(1:6)
vector_one
vector_one[1]
vector_one[1:3] #This grabs the first three values
vector_one[0]
vector_one[10]
bigger_vector = vector_one * 5
bigger_vector
bigger_vector == vector_one #remember that '=' assigns values, whereas '==' compares.
bigger_vector == (vector_one * 5)
bigger_vector - vector_one #vector to vector math!
class(bigger_vector)

## Construct Matrices
row_wise = matrix(data=c(3, 4, 5, 6, 7, 8), nrow=2, ncol=3, byrow = TRUE)
col_wise = matrix(data=c(3, 4, 5, 6, 7, 8), nrow=2, ncol=3, byrow = FALSE)
row_wise
col_wise
class(col_wise)
weird_matrix = matrix(data=c(3:8), nrow = 10, ncol = 10, byrow = TRUE)
weird_matrix
#help(matrix)

## Construct Data Frames
my_numbers = c(6, 7, 8)
my_strings = c("I", "Love", "Potatoes")
my_logicals = c(FALSE, FALSE, TRUE)
my_dataframe = data.frame(my_numbers, my_strings, my_logicals)
my_dataframe
class(my_dataframe)
names(my_dataframe)
my_dataframe$my_logicals
my_dataframe$my_strings
my_dataframe$my_numbers
class(my_dataframe$my_logicals)
my_dataframe[1]
my_dataframe[3] #note that this is slightly different from "my_dataframe$my_logicals". More on this later.


# Acessing Data

## Accessing Matrix
test_matrix = matrix(c(1, 2, 3, 4, 5, 6), nrow=3, ncol=2) #let's first create the matrix
test_matrix[1,1]
# test_matrix[1,10]
# test_matrix[1,100]
# test_matrix[1,1000]
# test_matrix
# test_matrix[2]
# test_matrix[2,]
# test_matrix[,2]

x = matrix(c(1, 2, 3, 4, 5, 7:9), nrow=1, ncol=8)
x[1,1:4]
x[1:4]
x[8]
x[1,8]

## Accessing dataframe
my_dataframe
my_dataframe$my_numbers
my_dataframe$my_numbers[1]
my_dataframe$my_numbers[1:3]
my_dataframe$my_numbers[1:10]
#my_dataframe$my_numbers[1,]  # Error!
#my_dataframe$my_numbers[1,] # for reference :  [1,] tries to access a row.
my_dataframe[1,]
my_dataframe[,1]


# Functions()
class(1)
summary(1)
# help(class)
# help(summary)
summary(my_dataframe$my_numbers) #we created my_dataframe earlier!
# if this is assigned to x, then we could access individuals 
# results of summary through methods like x[1:6]

## Plotting via plot()
#help(plot)
plot(c(1:5),c(6:10))
x_to_plot = c(1,2,3)
y_to_plot = c(1,2,3)
plot(x_to_plot, y_to_plot, main="first plot woot!")
plot(y_to_plot ~ x_to_plot, main="second plot yea!")
# Examples from help
plot(sin, -pi, 2*pi)
plot(tan, -pi, 2*pi)
plot(x <- sort(rnorm(47)), type = "s", main = "plot(x, type = \"s\")")
points(x, cex = .5, col = "dark red")
plot(cars)
lines(lowess(cars))
