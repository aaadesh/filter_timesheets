
# save excel in windows first

import pandas as pd

df = pd.read_excel(r"path")

print(df['Working Hours'])

new = df['Working Hours'].str.split(":", expand = True)

df['hours'] = new[0]
df['mins'] = new[1]

df['hours'] = pd.to_numeric(df['hours'])
df['mins'] = pd.to_numeric(df['mins'])

print(df.head)

total = df['hours'].sum()
print(total)


def phours(project):
	project_hours = df.loc[df['Project Name'] == project, 'hours'].sum()
	project_mins = df.loc[df['Project Name'] == project, 'mins'].sum()
	project_total = project_hours + project_mins/60
	return project_total

def uhours(user):
	user_hours = df.loc[df['User'] == user, 'hours'].sum()
	user_mins = df.loc[df['User'] == user, 'mins'].sum()
	user_total = user_hours + user_mins/60
	return user_total

projects = df['Project Name'].unique()
#print(projects)

df1 = pd.DataFrame(projects, columns = ['Project'])
	
for i in range(len(df1)):
	df1.loc[i, 'Hours'] = phours(df1.loc[i, 'Project'])


users = df['User'].unique()

df2 = pd.DataFrame(users, columns = ['User'])
	
for j in range(len(df2)):
	df2.loc[j, 'Hours'] = uhours(df2.loc[j, 'User'])

#print(df1)
df1.to_excel(r"H:\Codes\Timesheets\project_hours.xlsx")
df2.to_excel(r"H:\Codes\Timesheets\user_hours.xlsx")