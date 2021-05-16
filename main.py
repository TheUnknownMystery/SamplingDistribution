# __________Imported Libaries____________

import csv
import statistics as st

import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

# _______________________________________

#------------------------------------------------------------------------#
# Opening the file using the open function and stoaring it in a variable #
#------------------------------------------------------------------------#
File_Object = pd.read_csv('archive (1)\StudentsPerformance.csv')

#------------------------------------------------------------------------#
# Creating a list stoaring all the scores of reading marks in a var      #
#------------------------------------------------------------------------#
Reading_Marks = File_Object["writing score"].tolist()

#mean,median,mode and standardDeviation
mean   = st.mean(Reading_Marks)
median = st.median(Reading_Marks)
mode   = st.mode(Reading_Marks)

sd = st.stdev(Reading_Marks)

# Printing the mean median mode and std

# _____________________Print Statements_________________

print("mean   -> " + str(mean))
print("median -> " + str(median))
print("mode   -> " + str(mode))
print("Std    -> " + str(sd))

# ______________________________________________________

first_std_start, first_std_end = mean - sd, mean + sd
second_std_start, second_std_end = mean - (2*sd), mean + (2*sd)
third_std_start, third_std_end = mean - (3*sd), mean + (3*sd)

thin_1_std = [result for result in Reading_Marks if result >
              first_std_start and result < first_std_end]
thin_2_std = [result for result in Reading_Marks if result >
              second_std_start and result < second_std_end]
thin_3_std = [result for result in Reading_Marks if result >
              third_std_start and result < third_std_end]

print('thin_1_std: ' + str(thin_1_std))
print('thin_2_std: ' + str(thin_2_std))
print('thin_3_std: ' + str(thin_3_std))

# ____________________________Percentage_______________________________

first_counter = 0

for i in range(0, len(Reading_Marks)):
    if(Reading_Marks[i] >= first_std_start and Reading_Marks[i] <= first_std_end):
        first_counter += 1

First_Standard_Deviation_Percentage = (
    first_counter * 100) / len(Reading_Marks)

print(str("First Std Deviation: ") +
      str(First_Standard_Deviation_Percentage) + str("%"))

# _____________________________________Percentage 2 ___________________________________
second_counter = 0

for j in range(0, len(Reading_Marks)):
    if(Reading_Marks[j] >= second_std_start and Reading_Marks[j] <= second_std_end):
        second_counter += 1

Second_Standard_Deviation_Percentage = (
    second_counter * 100) / len(Reading_Marks)

print(str("Second Std Deviation: ") +
      str(Second_Standard_Deviation_Percentage) + str("%"))

# ______________________________________Percentage 3_____________________________________
third_counter = 0

for g in range(0, len(Reading_Marks)):
    if(Reading_Marks[g] >= third_std_start and Reading_Marks[g] <= third_std_end):
        third_counter += 1

Third_Standard_Deviation_Percentage = (
    third_counter * 100) / len(Reading_Marks)

print(str("Third Std Deviation: ") +
      str(Third_Standard_Deviation_Percentage) + str("%"))
# ____________________________________________________________________________________



#_____________________________Figure_________________________________________________
fig = ff.create_distplot([Reading_Marks], ['marks'], show_hist=False)

fig.add_trace(go.Scatter(x=[mean, mean], y=[
              0, 0.025], mode='lines', name='Mean'))



fig.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[
              0, 0.025], mode='lines', name='First Standard Deviation Start'))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[
              0, 0.025], mode='lines', name='First Standard Deviation End'))

fig.add_trace(go.Scatter(x=[second_std_start, second_std_start], y=[
              0, 0.025], mode='lines', name='Second Standard Deviation Start'))
fig.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[
              0, 0.025], mode='lines', name='Second Standard Deviation End'))

fig.add_trace(go.Scatter(x=[third_std_start, third_std_start], y=[
    0, 0.025], mode='lines', name='Third Standard Deviation Start'))
fig.add_trace(go.Scatter(x=[third_std_end, third_std_end], y=[
              0, 0.025], mode='lines', name='Third Standard Deviation End'))



fig.add_trace(go.Scatter(x=[First_Standard_Deviation_Percentage, First_Standard_Deviation_Percentage], y=[
    0, 0.025], mode='lines', name='First Standard Deviation Percentage'))

fig.add_trace(go.Scatter(x=[Second_Standard_Deviation_Percentage, Second_Standard_Deviation_Percentage], y=[
              0, 0.025], mode='lines', name='Second Standard Deviation Percentage'))

fig.add_trace(go.Scatter(x=[Third_Standard_Deviation_Percentage, Third_Standard_Deviation_Percentage], y=[
              0, 0.025], mode='lines', name='Third Standard Deviation Percentage'))

fig.show()

#______________________________________________________________________________________