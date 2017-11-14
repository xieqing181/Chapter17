#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import random

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url, timeout = 150)
r.encoding ='utf-8'
print("Status code: ", r.status_code)

response_dict = r.json()

#print(response_dict.keys())

print("Total repositories: ", response_dict['total_count'])

repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    #if repo_dict['id'] == 1362490:	
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)
    
print(plot_dicts)
print('\n')
#print(isinstance(plot_dicts,unicode))    
my_style = LS("#333366", base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_size = 24
my_config.label_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos_1.svg')

'''
#research the first Repository
repo_dict = repo_dicts[0]

this is just to print out the keys to let me select useful info

print("\nKeys: ", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

#print("html_url: ", repo_dict['html_url'])
#print("\nfollowers_url: ", repo_dict['owner']['followers_url'])

for repo_dict in repo_dicts:
    #print("\nSelected information about first repository: ")
    print("\nName: ", repo_dict['name'])
    print("Owner: ", repo_dict['owner']['login'])
    print("Stars: ", repo_dict['stargazers_count'])
    print("Repository: ", repo_dict['html_url'])
    print("Created: ", repo_dict['created_at'])
    #print("Updated: ", repo_dict['updated_at'])
    print("Description: ", repo_dict['description'])
'''
