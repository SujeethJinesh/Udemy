# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Data.csv')

#Now we need to avg the values of the features in order to
#put them into the null/NaN values.
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm=TRUE)),
                     dataset$Age)
dataset$Salary = ifelse(is.na(dataset$Salary),
                     ave(dataset$Salary, FUN = function(x) mean(x, na.rm=TRUE)),
                     dataset$Salary)
