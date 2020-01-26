#!/usr/bin/env python
# coding: utf-8

# # Using Wikipedia API to get Artificial Intelligence articles

# In[1]:


import sqlite3
import wptools
import re
from bs4 import BeautifulSoup


# In[2]:


category = 'Category:Artificial_intelligence'
depth = 2
DATABASE = '../data/content.db'


# In[17]:


class crawl_wikipedia:
    def __init__(self, db_file):
        self.categories=[]
        #self.pageids=[]
        self.count=0
        # Create db
        self.conn = sqlite3.connect(db_file)
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS content
            (pageid text, url text, content text)''')
        self.conn.commit()
        self.cursor = self.conn.cursor()
     
    def save_page_content(self, pageid, url, content):
        self.cursor.execute("INSERT INTO content VALUES (?,?,?)",
            (pageid, url, content))
        self.conn.commit()
        
    def get_page_content(self, columns='*'):
        # TODO - Add in ability to select single columns
        output = []
        for row in self.cursor.execute("SELECT url FROM content"):
            output.append(row)
            print(row)
        return output
            
    def get_categories_and_members(self, category, depth):
        print('Checking for subcategories of {} at depth {}'.format(category, depth))
        if depth:
            cat = wptools.category(category)
            cat_members = cat.get_members()
            # First let's save any members (pages) for this category
            if 'members' in cat_members.data.keys():
                for cat_member in cat_members.data['members']:
                    # print('Appending {} to pageids'.format(cat_member['pageid']))                   
                    #self.pageids.append(cat_member['pageid'])
                    page = wptools.page(pageid=cat_member['pageid']).get_parse()
                    # Remove <ref> and other HTML syntax
                    text = BeautifulSoup(page.data['wikitext'], 'html.parser').get_text()
                    # Remove other markup such as [[...]] and {{...}}
                    clean_content = re.sub(r"\s*{.*}\s*|\s*\[.*\]\s*", " ", text)
                    # Get URL in wikipedia
                    url = page.get_query().data['url']
                    # Now store
                    print('Saving pageid {} / url {}'.format(cat_member['pageid'], url))
                    self.save_page_content(cat_member['pageid'], url, clean_content)
            # Now iterate through any subcategories
            if 'subcategories' in cat_members.data.keys():
                subcats = cat_members.data['subcategories']               
                for subcat in subcats: 
                    self.categories.append(subcat)
                    self.count += 1
                    #print('Appending {} / count = {}'.format(subcat['title'], self.count))
                    self.get_categories_and_members(subcat['title'], depth - 1)
            


# In[18]:


crawler = crawl_wikipedia(DATABASE)


# In[ ]:


crawler.get_categories_and_members(category, depth)


# In[13]:


len(crawler.categories)


# In[19]:


x=crawler.get_page_content()


# In[21]:


len(x)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[288]:


page = wptools.page(pageid=1648132).get_parse()


# In[289]:


page.get_parse()


# In[290]:


text = page.data['wikitext']


# In[291]:


page.get_query().data['url']


# In[ ]:





# In[ ]:





# In[ ]:





# In[292]:


from bs4 import BeautifulSoup


# In[293]:


soup = BeautifulSoup(text, 'html.parser')


# In[294]:


txt2 = soup.get_text()


# In[295]:


import re
re.sub(r"\s*{.*}\s*|\s*\[.*\]\s*", " ", txt2)


# In[ ]:





# In[ ]:




