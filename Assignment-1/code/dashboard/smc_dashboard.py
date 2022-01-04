import pandas as pd    
import numpy as np
import matplotlib.pyplot as plt
import csv
import streamlit as st

#%matplotlib inline  

def draw_daily_tweets():
    Date = []
    Samsung_Y = []
    Huawei_Y = []
    
    with open('Samsung_status.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(csvfile)
        for row in lines:
            Samsung_Y.append(row[0])
            Date.append((row[-1]))
            
    with open('Huawei_status.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(csvfile)
        for row in lines:
            Huawei_Y.append(row[0])
            
    
    #code to get the daily increase       
    Samsung_Y = [int(i) for i in Samsung_Y]
    Samsung_Y = [y-x for x,y in zip(Samsung_Y,Samsung_Y[1:])]
    Samsung_Y.insert(0, 0)

    
    
    Huawei_Y = [int(i) for i in Huawei_Y]
    Huawei_Y = [y-x for x,y in zip(Huawei_Y,Huawei_Y[1:])]
    Huawei_Y.insert(0, 0)
    
    
    #creating dataframe
    Samsung_df = pd.read_csv("Samsung_status.csv")
    Samsung_df = Samsung_df.drop(Samsung_df.columns[[1,2,3,4,5,6]],axis=1)
    Samsung_df['Daily Increase'] = Samsung_Y
    
    Huawei_df = pd.read_csv("Huawei_status.csv")
    Huawei_df = Huawei_df.drop(Huawei_df.columns[[1,2,3,4,5,6]],axis=1)
    Huawei_df['Daily Increase'] = Huawei_Y
    

     #plotting the graph  
    figure = plt.figure(figsize=(20,10))   
      
    plt.plot(Date, Samsung_Y, color = 'b', linestyle = 'dashed',
             marker = 'o',label = "Samsung Daily Tweets Counts")
    
    
    plt.plot(Date, Huawei_Y, color = 'r', linestyle = 'dashed',
             marker = 'o',label = "Huawei Daily Tweets Counts")
    
      
    
    plt.ylim([0,30])
    plt.xticks(rotation = 25, fontsize = 30)
    plt.yticks(fontsize = 30)
    plt.xlabel('Dates', fontsize = 40)
    plt.ylabel('Tweets', fontsize = 40)
    plt.title('Daily Tweets Posted ', fontsize = 60)
    plt.legend(bbox_to_anchor=(1.04,1), loc="upper left", prop={"size":25}) 
    plt.show()
    
    return figure,Samsung_df,Huawei_df

def draw_daily_followers():
    
    Date = []
    Samsung_Y = []
    Huawei_Y = []
    
    with open('Samsung_status.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(csvfile)
        for row in lines:
            Samsung_Y.append(row[1])
            Date.append((row[-1]))
            
    with open('Huawei_status.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(csvfile)
        for row in lines:
            Huawei_Y.append(row[1])
    
          
    #code to get the daily increase 
    Samsung_Y = [int(i) for i in Samsung_Y]
    Samsung_Y = [y-x for x,y in zip(Samsung_Y,Samsung_Y[1:])]
    Samsung_Y.insert(0, 0)
    
    
    Huawei_Y = [int(i) for i in Huawei_Y]
    Huawei_Y = [y-x for x,y in zip(Huawei_Y,Huawei_Y[1:])]
    Huawei_Y.insert(0, 0)
    
    #creating dataframe
    Samsung_df = pd.read_csv("Samsung_status.csv")
    Samsung_df = Samsung_df.drop(Samsung_df.columns[[0,2,3,4,5,6]],axis=1)
    Samsung_df['Daily Increase'] = Samsung_Y
    
    Huawei_df = pd.read_csv("Huawei_status.csv")
    Huawei_df = Huawei_df.drop(Huawei_df.columns[[0,2,3,4,5,6]],axis=1)
    Huawei_df['Daily Increase'] = Huawei_Y
       
    
    #plotting the graph
    figure = plt.figure(figsize=(20,10))     
        
    plt.plot(Date, Samsung_Y, color = 'b', linestyle = 'dashdot',
             marker = 'o',label = "Samsung Daily New Followers")
    
    plt.plot(Date, Huawei_Y, color = 'r', linestyle = 'dashdot',
             marker = 'o',label = "Huawei Daily New Followers")
    
    
    plt.ylim([-200,1000])
    plt.xticks(rotation = 25, fontsize = 30)
    plt.yticks(fontsize = 30)
    plt.xlabel('Dates', fontsize = 40)
    plt.ylabel('Followers', fontsize = 40)
    plt.title('Daily Increased Followers Count ', fontsize = 60)
    plt.legend(bbox_to_anchor=(1.04,1), loc="upper left", prop={"size":25}) 
    plt.show()
    
    return figure, Samsung_df, Huawei_df

def draw_daily_retweets():
    
    Date = []
    Samsung_Y = []
    Huawei_Y = []
    
    with open('Samsung_status.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(csvfile)
        for row in lines:
            Samsung_Y.append(row[3])
            Date.append((row[-1]))
            
    with open('Huawei_status.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(csvfile)
        for row in lines:
            Huawei_Y.append(row[3])
    
        
    #code to get the daily increase     
    Samsung_Y = [int(i) for i in Samsung_Y]
    Samsung_Y = [y-x for x,y in zip(Samsung_Y,Samsung_Y[1:])]
    Samsung_Y.insert(0, 0)

    
    Huawei_Y = [int(i) for i in Huawei_Y]
    Huawei_Y = [y-x for x,y in zip(Huawei_Y,Huawei_Y[1:])]
    Huawei_Y.insert(0, 0)

    
    #replace the outliers with mean 
    # Samsung_Y_mean = Samsung_Y.copy()
    # Samsung_Y_mean.pop(0)
    # Samsung_Y_mean.pop(0)
    
    # mean = np.mean(Samsung_Y_mean)
    
    # Samsung_Y_mean = Samsung_Y.copy()
    # Samsung_Y_mean[1] = mean
    
    #creating dataframe
    Samsung_df = pd.read_csv("Samsung_status.csv")
    Samsung_df = Samsung_df.drop(Samsung_df.columns[[1,2,0,4,5,6]],axis=1)
    Samsung_df['Daily Increase'] = Samsung_Y
    
    Huawei_df = pd.read_csv("Huawei_status.csv")
    Huawei_df = Huawei_df.drop(Huawei_df.columns[[1,2,0,4,5,6]],axis=1)
    Huawei_df['Daily Increase'] = Huawei_Y

     
    #plotting the figure  
    figure = plt.figure(figsize=(20,10))     
         
    plt.plot(Date, Samsung_Y, color = 'b', linestyle = '-',
             marker = 'o',label = "Samsung Daily New Retweets")
    
    plt.plot(Date, Huawei_Y, color = 'r', linestyle = '-',
             marker = 'o',label = "Huawei Daily New Retweets")
    
    
    
    plt.ylim([-2000,6000])
    plt.xticks(rotation = 25, fontsize = 30)
    plt.yticks(fontsize = 30)
    plt.xlabel('Dates', fontsize = 40)
    plt.ylabel('Retweets', fontsize = 40)
    plt.title('Daily Increased Retweets Count ', fontsize = 60)
    plt.legend(bbox_to_anchor=(1.04,1), loc="upper left", prop={"size":25}) 
    plt.show()
    
    
    
    return figure, Samsung_df, Huawei_df

def draw_daily_favorites():
    
    Date = []
    Samsung_Y = []
    Huawei_Y = []
    
    with open('Samsung_status.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(csvfile)
        for row in lines:
            Samsung_Y.append(row[4])
            Date.append((row[-1]))
            
    with open('Huawei_status.csv','r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(csvfile)
        for row in lines:
            Huawei_Y.append(row[4])
    
         
    #code to get the daily increase 
    Samsung_Y = [int(i) for i in Samsung_Y]
    Samsung_Y = [y-x for x,y in zip(Samsung_Y,Samsung_Y[1:])]
    Samsung_Y.insert(0, 0)

    
    Huawei_Y = [int(i) for i in Huawei_Y]
    Huawei_Y = [y-x for x,y in zip(Huawei_Y,Huawei_Y[1:])]
    Huawei_Y.insert(0, 0)


    #creating dataframe
    Samsung_df = pd.read_csv("Samsung_status.csv")
    Samsung_df = Samsung_df.drop(Samsung_df.columns[[1,2,3,0,5,6]],axis=1)
    Samsung_df['Daily Increase'] = Samsung_Y
    
    Huawei_df = pd.read_csv("Huawei_status.csv")
    Huawei_df = Huawei_df.drop(Huawei_df.columns[[1,2,3,0,5,6]],axis=1)
    Huawei_df['Daily Increase'] = Huawei_Y

       
    #plotting the figure
    figure = plt.figure(figsize=(20,10))     
        
      
    plt.plot(Date, Samsung_Y, color = 'b', linestyle = '-',
             marker = 'o',label = "Samsung Daily New Favorites")
    
    plt.plot(Date, Huawei_Y, color = 'r', linestyle = '-',
             marker = 'o',label = "Huawei Daily New Favorites")
    
    
    plt.ylim([-3000,30000])
    plt.xticks(rotation = 25, fontsize = 30)
    plt.yticks(fontsize = 30)
    plt.xlabel('Dates', fontsize = 40)
    plt.ylabel('Favorites', fontsize = 40)
    plt.title('Daily Increased Favorites Count ', fontsize = 60)
    plt.legend(bbox_to_anchor=(1.04,1), loc="upper left", prop={"size":25}) 
    plt.show()

    
    return figure, Samsung_df, Huawei_df



#### paste the story here into the respective story string
followers_story_str = "Even thought Samsung has a lot more followers than Huawei, Huawei has more daily follower increase compare to Samsung. This is because Samsung might already have reach all their pontential consumers while Huawei still starting to approach more variety consumer."
tweets_story_str ="Huawei tweet more than Samsung as most Huawei tweet are more related to their product usecase which need more than 1 tweets to showcase the product usecase on different scenario while Samsung tweets are more focus on the product features which different from what Huawei does. Another interesting fact is that both pages doesnt tweet at Saturday."
retweets_story_str = "The cause of sudden spike of Samsung daily retweet counts on 22/September is because on 21/September samsung retweets about BTS stuff and get alot of retweets while the sudden drop is because Samsung might have use bot to boost their retweet of certain post and caught by twitter anti-bot algorithm and had their retweet count to be remove. Another cause of droping that the new post doesnt generate enough retweet to cover back the bot detection algorithm. From here we at least can conclude that, Huawei doesnt use bot to help them boot their own tweets because their decline tweets might due to dissatisfied from consumer"
favorites_story_str = "The cause of sudden spike of Samsung daily favourite counts is the same reason as retweets which Samsung retweets about BTS stuff. As for the declide also the same as retweets reason which samsung use bot to boost their tweets."




#config on basic settings of stramlit
st.set_page_config(layout="wide")
st.title("Social media analysis for Samsung and Huawei on Twitter")
st.markdown("***")


option = st.sidebar.selectbox('Which visualization to show?', ('Daily increase of followers', 'Daily increase of tweets','Daily increase of retweets','Daily increase of favorites'))

### using columns to make the visualization looks better
col = st.columns(2)

#using if else to show the choice of user on the dashboard
if(option == 'Daily increase of followers'):
    figure,Samsung_df, Huawei_df  = draw_daily_followers()
    with col[0]:
        st.write(figure)
        st.write(followers_story_str)
    with col[1]:
        st.write("Samsung data")
        st.write(Samsung_df)
        st.write("Huawei data")
        st.write(Huawei_df)
    
elif(option == 'Daily increase of tweets'):
    figure,Samsung_df, Huawei_df = draw_daily_tweets()
    with col[0]:
        st.write(figure)
        st.write(tweets_story_str)
    with col[1]:
        st.write("Samsung data")
        st.write(Samsung_df)
        st.write("Huawei data")
        st.write(Huawei_df)
    
    
elif(option == 'Daily increase of retweets'):
    figure ,Samsung_df, Huawei_df = draw_daily_retweets()
    with col[0]:
        st.write(figure)
        st.write(retweets_story_str)
    with col[1]:
        st.write("Samsung data")
        st.write(Samsung_df)
        st.write("Huawei data")
        st.write(Huawei_df)

elif(option == 'Daily increase of favorites'):
    figure,Samsung_df, Huawei_df  = draw_daily_favorites()
    with col[0]:
        st.write(figure)
        st.write(favorites_story_str)
    with col[1]:
        st.write("Samsung data")
        st.write(Samsung_df)
        st.write("Huawei data")
        st.write(Huawei_df)







