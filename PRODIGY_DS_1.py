#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\tittu\Downloads\2010-2024 Movies Box Ofice Collection.csv")


# In[4]:


df.head()


# In[5]:


df['Worldwide'] = df['Worldwide'].replace({',': ''}, regex=True).astype(float)


# In[6]:


top_movies = df.sort_values(by='Worldwide', ascending=False).head(10)



# In[13]:


plt.figure(figsize=(12, 8))
plt.barh(top_movies['Release Group'], top_movies['Worldwide'], color='skyblue')
plt.xlabel('Worldwide Box Office Collection (in billions)')
plt.ylabel('Movies')
plt.title('Top 10 Movies by Worldwide Box Office Collection')
plt.gca().invert_yaxis() 
# Invert y-axis to show the highest-grossing movie at the top
plt.show()


# In[14]:


pip install plotly


# In[15]:


import plotly.express as px
import pandas as pd


fig = px.bar(
    top_movies,
    x='Release Group',
    y='Worldwide',
    title='Top 10 Movies by Worldwide Box Office Collection',
    color='Worldwide', 
    labels={'Worldwide': 'Worldwide Box Office Collection (in billions)', 'Release Group': 'Movies'}
)

fig.update_traces(
    hovertemplate='<b>%{x}</b><br>Worldwide: %{y:.2f} billion<br>',
    text=top_movies['Worldwide'],
    textposition='auto'
)

fig.show()


# In[ ]:




