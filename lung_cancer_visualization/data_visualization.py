#!/usr/bin/env python
# coding: utf-8

# In[19]:


#Imports
import pandas as pd
import pandas_profiling as pp
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px
import numpy as np

# In[20]:

color = sns.color_palette()
get_ipython().run_line_magic('matplotlib', 'inline')
py.init_notebook_mode(connected=True)
df = pd.read_csv('lung_cancer.csv')
df.head()

# In[3]:

pp.ProfileReport(df)

# In[23]:

#Pie chart displaying percentage of dataset with lung cancer
dist = df['LUNG_CANCER'].value_counts()
trace = go.Pie(values=(np.array(dist)),labels=dist.index)
data = [trace]
pie_chart = go.Figure(trace, go.Layout(title='Lung Cancer Outcome'))
pie_chart.update_traces(marker=dict(colors=['beige', 'navy'], line=dict(color='#000000', width=2)))
pie_chart.show()


# In[25]:


#Heat map correlation matrix of all the factors
def df_to_plotly(df):
    return {'z': df.values.tolist(),
            'x': df.columns.tolist(),
            'y': df.index.tolist() }
import plotly.graph_objects as go
dfNew = df.corr()
correlation_matrix = go.Figure(data=go.Heatmap(df_to_plotly(dfNew)))
correlation_matrix.show()


# In[45]:


#scatterplot
scatter_plot = px.scatter(df, x='AGE', y='LUNG_CANCER')
scatter_plot.update_traces(marker_color="navy",marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
scatter_plot.update_layout(title_text='Age and Y')
scatter_plot.show()


# In[49]:


#boxplot
box_plot = px.box(df, x='LUNG_CANCER', y='AGE')
box_plot.update_traces(marker_color="green",marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
box_plot.update_layout(title_text='Age and Lung Cancer')
box_plot.show()

