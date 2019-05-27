#!/usr/bin/env python
# coding: utf-8

# # HACKER NEWS COMMENTS
# 
# In the project, we will analyze the following hacker news comments. 
# 1. Which post gets more comments? Ask vs Show?
# 2. What time the post get most comments
# 

# In[2]:


from csv import reader

opened_file = open('hacker_news.csv')
read_file = reader(opened_file)
hn = list(read_file)
headers = hn[:1]
hn = hn[1:]

for row in hn[:5]:
    print(row)
    print('\n')


# In[3]:


ask_posts = []
show_posts = []
other_posts = []

for row in hn:
    title = row[1]
    title_lower = title.lower()
    if title_lower.startswith('ask hn') == True:
        ask_posts.append(row)
    elif title_lower.startswith('show hn') == True:
        show_posts.append(row)
    else:
        other_posts.append(row)
        
print('Ask Posts : ', len(ask_posts))
print('Show Posts : ', len(show_posts))
print('Other Posts : ', len(other_posts))
    
print(ask_posts[:5])
print(show_posts[:5])


# In[4]:


total_ask_comments = 0

for row in ask_posts:
    num_comments = row[4]
    total_ask_comments = total_ask_comments + int(num_comments)
    
avg_ask_comments = total_ask_comments/len(ask_posts)
print('avg_ask_comments: ', avg_ask_comments)

total_show_comments = 0

for row in show_posts:
    num_comments = row[4]
    total_show_comments = total_show_comments + int(num_comments)
    
avg_show_comments = total_show_comments/len(show_posts)
print('avg_show_comments: ', avg_show_comments)


# In[15]:


import datetime as dt

result_list = []

for row in ask_posts:
    temp = []
    created_at = row[6]
    num_comments = row[4]
    temp.append(created_at)
    temp.append(num_comments)
    result_list.append(temp)
    
counts_by_hour = {}
comments_by_hour = {}

for row in result_list:
    temp_date = row[0]
    num_comments = int(row[1])
    comment_date = dt.datetime.strptime(temp_date, "%m/%d/%Y %H:%M")
    comment_hour = dt.datetime.strftime(comment_date, "%H")
    if comment_hour not in counts_by_hour:
        counts_by_hour[comment_hour] = 1
        comments_by_hour[comment_hour] = num_comments
    else:
        counts_by_hour[comment_hour] += 1
        comments_by_hour[comment_hour] += num_comments
        
print(counts_by_hour)
print(comments_by_hour)


# In[18]:


avg_by_hour = []

for hour_count in counts_by_hour:
    for hour_comments in comments_by_hour:
        if hour_count == hour_comments:
            avg_by_hour.append([hour_count, comments_by_hour[hour_count]/counts_by_hour[hour_count]])
print(avg_by_hour)


# In[22]:


swap_avg_by_hour = []

for row in avg_by_hour:
    swap_avg_by_hour.append([row[1],row[0]])
    
print(swap_avg_by_hour)

sorted_swap = sorted(swap_avg_by_hour, reverse = True)

print("Top 5 Hours for Ask Posts Comments")

for row in sorted_swap[:5]:
    hour = dt.datetime.strptime(row[1], "%H")
    hour_fmt = dt.datetime.strftime(hour, "%H:%M")
    avg_fmt = '{:.2f}'.format(row[0])
    
    print("{0}: {1} average comments per post".format(hour_fmt,avg_fmt))
    
    
    


# From the analysis, we can observe that the best time to receive comment for a post between 3pm EST and 5pm EST followed by 8pm EST and 10pm EST. You also have better change of comment at 2am in the morning.
