print('This code is case sensitive, please write answers exactly as they are.')
name = input('What is your name?')
print('Hello, ' + name + '!')
print (name + ', ' + 'This is a demo program designed for people looking to increase their productivity.')
hours_daily = input('How many hours a day do you spend working? Please respond with a whole number.')
satisfied = input('How satisfied are you with that amount of time? Please answer:' + ' Not at all' + ',' + ' Somewhat' + ',' + ' or' +  ' Very.')
if satisfied == ' Not at all':
  print('It seems you are seriously unsatisfied with your current amount of productivity. Please continue with this program to discover your path to improvement.')
elif satisfied == ' Somewhat':
  print('You are moderately satisfied with your life, but there is room for improvement. Please continue with this program to learn more.')
elif satisfied == ' Very':
  print('Congratulations on being so productive and satisfied with that level of performance. There are still always techniques we can use to maximize our potential, and I urge you to still continue with this program.')
else:
  print('Invalid answer, please try again. Case sensitive.')
print('Lets try to balance out your week. The following program will tell you how many hours a day you should be working on a high priority project, especially one that requires a lot of time. Think about the biggest and highest priority project you have to complete over the next week. Let us call this important_project.')
project_hours = input('How many hours on average per week can you dedicate to important_project? Please write one of these, and make sure to write the word "hours":' + ' 40 hours' + ',' + ' 30 hours' + ',' + ' 20 hours' + ',' + ' or' + ' 10 hours' + ' per week.')
if project_hours ==' 40 hours':
  project_hours = 40
elif project_hours == ' 30 hours':
  project_hours = 30
elif project_hours == ' 20 hours':
  project_hours = 20
elif project_hours == ' 10 hours':
  project_hours = 10
print('Thanks for your input. Now that we have established how many hours a week you can dedicate to important_project, this program will calculate how much time per day should be alloted to important_project in order to finish it in one work week, assuming you work 5 days per week. If you start work on Monday, this is the amount of hours you need to work per day to finish by Friday:')
important_project = project_hours / 5
print(important_project)
print('Hours per day needed to complete this task within a Monday to Friday schedule. Please refresh and reuse this program for all of your important projects and total them in order to determine your weekly workload.')
