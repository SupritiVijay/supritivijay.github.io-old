import pandas as pd
import numpy as np
import calendar
import datetime

def read_publications(path="./configs/publications.csv"):
	df = pd.read_csv(path)
	df = df.values
	unique_years = np.sort(list(set([int(i) for i in df.T[0]])))[::-1]
	shorts = '<div>\n						<h4>'+' | '.join(['<a href="#'+str(y)+'" class="active">'+str(y)+'</a>' for y in unique_years])+'</h4>\n					</div>'
	c = 0
	output = shorts+'\n'
	for year in unique_years:
		curr_count = len(df)-c
		top = '					<div id="'+str(year)+'">\n					<hr class="thin">\n						<h4>'+str(year)+'</h4>\n						<ol reversed start = "'+str(curr_count)+'" class="fa-ol text-left">\n'
		bottom = '						</ol>\n					</div>'
		output+=top
		for row in df:
			if int(row[0])==year:
				a = '						<li><b>'
				a += str(row[1])+'</b>&nbsp;&nbsp;&nbsp;&nbsp;<a href="'
				a += str(row[3])+'" target="_blank">Link</a>&nbsp;&nbsp;\n							<h6>'
				a += str(row[2])+'<br>\n							<i>'
				a += str(row[4])+'</i></h6>\n						</li>\n'
				output += a
				c+=1
		output += bottom+'\n'
	return output


def read_projects(path="./configs/projects.csv"):
	df = pd.read_csv(path)
	df = df.values
	outs = []
	for row in df:
		if not pd.isna(row[3]):
			out = '<li><h5><b>'+str(row[0])+":</b> "+'<a href="'+row[3]+'" target="_blank">'+row[1]+'</a><br>'+row[2]+'</li>'
		else:
			out = '<li><h5><b>'+str(row[0])+":</b> "+''+row[1]+'<br>'+row[2]+'</li>'
		outs.append(out)
	return '\n						'.join(outs)


def read_main_experience(path="./configs/main_experience.csv"):
	df = pd.read_csv(path)
	df = df.values
	outs = []
	for row in df:
		a = '<li><h5><b>'+str(row[0])+'</b>, '+str(row[1])+', <i><a href="'+str(row[3])+'" target="_blank">'+str(row[2])+'</a></i></h5></li>'
		outs.append(a)
	outs = '\n						'.join(outs)
	return outs

def read_main_education(path="./configs/main_education.csv"):
	df = pd.read_csv(path)
	df = df.values
	outs = []
	for row in df:
		a = '<li><h5>'+str(row[0])+'</h5><h5>'+str(row[1])+'</h5><h5> <a href="'+str(row[3])+'" target="_blank">'+str(row[2])+'</a></h5></li>'
		outs.append(a)
	outs = '\n						'.join(outs)
	return outs


def read_achievements(path="./configs/achievements.csv"):
	df = pd.read_csv(path)
	df = df.values
	outs = []
	for row in df:
		if not pd.isna(row[4]):
			a = '<li><h5><b>'+str(row[0])+' '+str(row[1])+':</b> <a href="'+str(row[4])+'" target="_blank">'+str(row[2])+'</a><br>'+str(row[3])+'</li>'
		else:
			a = '<li><h5><b>'+str(row[0])+' '+str(row[1])+':</b> '+str(row[2])+'<br>'+str(row[3])+'</li>'
		outs.append(a)
	outs = '\n						'.join(outs)
	return outs

def read_news(path="./configs/news.csv"):
	df = pd.read_csv(path)
	df = df.values
	outs = []
	for row in df:
		a = '<li><h5><b>'+str(row[0])+'</b> '+str(row[1])+' <a href="'+str(row[2])+'" target="_blank">(Link)</a></li>'
		outs.append(a)
	outs = '\n						'.join(outs)
	return outs

def read_config(path="./configs/config.txt"):
	with open(path, "r") as f:
		raw_data = f.readlines()
	raw_data = [i.strip() for i in raw_data]
	data = {}
	for item in raw_data:
		key, value = item[:item.index('=')], item[item.index('=')+1:]
		data[key] = value
	return data

def read_index_html(path="./configs/index.html"):
	with open(path, "r") as f:
		raw_data = f.readlines()
	return raw_data

def write_site(data, path="index.html"):
	with open(path, "w") as f:
		f.write("".join(data))

def main():
	projects = read_projects()
	pub = read_publications()
	exp = read_main_experience()
	edu = read_main_education()
	ach = read_achievements()
	news = read_news()
	config = read_config()
	site = read_index_html()
	currentDate = datetime.date.today()
	currentMonthName = calendar.month_name[currentDate.month]
	currentYear = currentDate.year
	config['currentYear'] = str(currentYear)
	config['month'] = currentMonthName
	for row_index in range(0, len(site)):
		site[row_index] = site[row_index].replace('$#RESEARCH#$', config['research'].replace('$#SPLIT#$', config['about_me_split']))
		site[row_index] = site[row_index].replace('$#NAME#$', config['name']).replace('$#DESCRIPTION#$', config['description']).replace('$#ABOUT_ME#$', config['about_me'].replace('$#SPLIT#$', config['about_me_split']))
		site[row_index] = site[row_index].replace('$#profile_img#$', config['profile_img']).replace('$#EMAIL#$', config['email']).replace('$#TWIITER_ID#$', config['twitter_id']).replace('$#LINKEDIN_ID#$', config['linkedin_id']).replace('$#SCHOLAR_LINK#$', config['scholar_link'])
		site[row_index] = site[row_index].replace('$#CV_FILENAME#$', config['cv_filename']).replace('$#EMAIL_COOL#$', config['email_cool'])
		site[row_index] = site[row_index].replace('$#NEWS_LISTS#$', news)
		site[row_index] = site[row_index].replace('$#ACHIEVEMENTS_LISTS#$', ach)
		site[row_index] = site[row_index].replace('$#EDUCATION_LISTS#$', edu)
		site[row_index] = site[row_index].replace('$#EXPERIENCE_LISTS#$', exp)
		site[row_index] = site[row_index].replace('$#PROJECT_LISTS#$', projects)
		site[row_index] = site[row_index].replace('$#PUBLICATION_LISTS#$', pub).replace('$#EDIT_MONTH#$', config['month']).replace('$#EDIT_YEAR#$', config['currentYear'])
	write_site(site)

if __name__ == '__main__':
	main()