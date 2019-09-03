# instagram
File *load_inst.py* contains every function or class written by me and used in this project.  
File *inst_analysis_likes.ipynb* is notebook with code which was used to obtain results below.  
File *inst_analysis_likes_no_output.ipynb* is the same as *inst_analysis_likes.ipynb*, but without any output, so you may look at the code via github.
## Introduction
	
Project is based on data about instagram photos of user [mkaciubapl](https://www.instagram.com/mkaciubapl/). You can find oryginal data [here](https://www.dropbox.com/sh/hobhqg7rvreweml/AADIfllpRt6cDwXFM5gGeh1Qa?dl=0).  
The initial  goal is to find the best time to upload photos (i.e. time so that the photos get the most likes).  

## About data
The data consists of 8 columns:
* time of record
* photo ID
* number of likes
* number of comments
* number of followers
* number of characters in description
* number of tags
* time of upload  

Each row represents one photo (in whole data set there are 60 of them) at a given time. Subsequent measurements were made every five minutes.  
Here are first 5 rows:  
<img src="https://user-images.githubusercontent.com/53919928/62839932-8c80a900-bc92-11e9-806b-a0dc342fbb72.png" width="80%"></img>  
and whole data plotted:  
<img src="https://user-images.githubusercontent.com/53919928/62839967-2ba5a080-bc93-11e9-820c-64696efeeca0.png" width="90%"></img> 

## Initial analysis  
### Data transforms  
First I transformed the data so that only the rows containing information about the next hours and days since the upload remain. For example here is head of dataframe containing information about first hour since upload  
<img src="https://user-images.githubusercontent.com/53919928/62840111-98219f00-bc95-11e9-950e-aebb88df3733.png" width="80%"></img>  
Next I divided upload time into 3 intervals:  
* 4 a.m-7 a.m   
* 7 a.m-10 a.m 
* 10 a.m-4 p.m  

For simplicity I used the 24 hour format.  
<img src="https://user-images.githubusercontent.com/53919928/62840179-74128d80-bc96-11e9-9c6f-ad1ea957015d.png" width="80%"></img>  
### Plots  
<img src="https://user-images.githubusercontent.com/53919928/62840225-49750480-bc97-11e9-9987-ce04be1a188f.png" width="30%"></img> <img src="https://user-images.githubusercontent.com/53919928/62840226-4c6ff500-bc97-11e9-94f3-731dd1561a18.png" width="30%"></img> <img src="https://user-images.githubusercontent.com/53919928/62840229-4f6ae580-bc97-11e9-80e2-7fe1db0373a9.png" width="30%"></img>   
Above figures show the number of likes after 1, 6, 12 hours in relation to the upload time. 
It seems that there is no much difference between 4 a.m-7 a.m and 7 a.m-10 a.m. It also looks like interval 10 a.m-4 p.m  is the worst, but this result may be skewed because lack of data.  
Let's look at some numbers:  
<img src="https://user-images.githubusercontent.com/53919928/62840374-f6508100-bc99-11e9-9daa-71547bf04d36.png" width="50%"></img> <img src="https://user-images.githubusercontent.com/53919928/62840376-fea8bc00-bc99-11e9-9c01-7970fb70b01a.png" width="50%"></img> <img src="https://user-images.githubusercontent.com/53919928/62840381-0e280500-bc9a-11e9-9622-30556184f6ca.png" width="50%"></img>  
We see that numbers of likes in each interval after 1st hour are almost the same, but after 6 and 12 hours interval  
10 a.m-4 p.m looks worse than other two.  
Let's summarize the observations on one chart:  
<img src="https://user-images.githubusercontent.com/53919928/62840460-74f9ee00-bc9b-11e9-903e-52c4591453fc.png" width="90%"></img>  
Regression line for 1h is almost parallel to x-axis, but lines for 6 and 12 hours clearly decrease. This may indicate negative relation between number of likes and time (hours treated as integers) of upload.  
Let's do the same for days.    
<img src="https://user-images.githubusercontent.com/53919928/62840510-5811ea80-bc9c-11e9-8015-c0e04ebfe986.png" width="30%"></img> <img src="https://user-images.githubusercontent.com/53919928/62840511-5b0cdb00-bc9c-11e9-88bb-157427335080.png" width="30%"></img> <img src="https://user-images.githubusercontent.com/53919928/62840512-5ea06200-bc9c-11e9-85cc-34c77a250091.png" width="30%"></img>   
It seems that the longer the period of time, the smaller the relative differences.  
<img src="https://user-images.githubusercontent.com/53919928/62840570-159cdd80-bc9d-11e9-9246-02dfc7b611e6.png" width="50%"></img> <img src="https://user-images.githubusercontent.com/53919928/62840571-1cc3eb80-bc9d-11e9-8f36-edd9c9b97988.png" width="50%"></img> <img src="https://user-images.githubusercontent.com/53919928/62840589-39f8ba00-bc9d-11e9-9014-d6e73fdc3495.png" width="50%"></img>  
Statistics show that boxplots for 10 a.m-4 p.m are skewed because of some poorly rated photos, also between 4 a.m and 10 a.m where uploaded photos that found many fans after 6 or 12 days.   
Let's sum up observations for days  
<img src="https://user-images.githubusercontent.com/53919928/62840650-81337a80-bc9e-11e9-8252-39e47696748b.png" width="90%"></img>  
Each regression line is almost parallel to x-axis.  
The first conclusion may be that after a few days the time of photo upload doesn't matter. This proposal may be premature, so some tests are needed.  
Before moving to test let's look at [correlation](https://en.wikipedia.org/wiki/Correlation_and_dependence) between number of likes and upload time

|     	| Correlation                             	|
|-----	|----------------------------------	|
| 1h  	| 0.006522701649949623             	|
| 6h  	| -0.25816888239888214             	|
| 12h 	| -0.31037895946598903             	|
| 1d  	| -0.12875793666188126             	|
| 6d  	| 0.06196442375367117              	|
| 12d 	| -0.01825883695090743		 	|  

We can see that it is mostly close to 0, but when we look at correlation after 6 and 12 hours since upload we can see moderate influence.  
[Kruskal-Wallis test](https://en.wikipedia.org/wiki/Kruskal%E2%80%93Wallis_one-way_analysis_of_variance) proved that number of likes doesn't depends on time of upload ([p-value](https://en.wikipedia.org/wiki/P-value) was greater than 0.05, you may find exact numbers in *inst_analysis_likes.ipynb*). One exception was result of test after 12h since upload - p-value=0.0404, so groups should significantly differ, but [post hoc_analysis](https://en.wikipedia.org/wiki/Post_hoc_analysis) showed that no group is much different from another. 

### Conclusion  
It looks that time of uploading photo doesn't affect number of likes which photo gets. 

## Numbers of likes in different time intervals  
Let now look at numbers of likes in different time intervals, more precisely, changes in those numbers.  
I desided to split day into 8 intervals, each three hours long.  
I considered two cases:
* each photo as single observation
* each day as single observation  
### Each photo as single observation  
#### Plots
First look at boxplot of data with every observation  
<img src="https://user-images.githubusercontent.com/53919928/64136430-c9534200-cdf1-11e9-8866-bf0a8ddbf779.png" width="60%"></img> 
It doesn't seem very helpful. Let's discard observations with no change. We get  
<img src="https://user-images.githubusercontent.com/53919928/64136431-c9534200-cdf1-11e9-8966-825d2f480547.png" width="60%"></img>  
It looks that number of likes increases as evening approaches. There are many observations in each interval, so it is reasonable to plot histograms.  
<img src="https://user-images.githubusercontent.com/53919928/64136402-a032b180-cdf1-11e9-8132-c96b150b0acf.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/64136403-a032b180-cdf1-11e9-9f47-3d309a5f9ba5.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/64136404-a032b180-cdf1-11e9-9ccf-fc83518d6aee.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/64136405-a0cb4800-cdf1-11e9-84d6-d6db36b7d463.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/64136406-a0cb4800-cdf1-11e9-90f5-4682e1e50557.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/64136407-a0cb4800-cdf1-11e9-93be-9b1d34ced342.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/64136408-a0cb4800-cdf1-11e9-8863-69664b8a70a7.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/64136409-a163de80-cdf1-11e9-8642-9c9c4e544f9f.png" width="45%"></img>  
We can see that distributions of changes in numbers of likes clearly aren't normal, most likely for changes is beeing close to zero, but not negative.  
#### Statistics
Now we will look at some basic statistics. We will start with basic data (including observations without any changes).  
<img src="https://user-images.githubusercontent.com/53919928/64136929-446a2780-cdf5-11e9-866e-99967a6f3989.png" width="50%">  
Mean for every time interval is close to zero and every quartile equals zero. There nothing interesting here.  
Now we remove 'zero' observations  
<img src="https://user-images.githubusercontent.com/53919928/64136935-4af89f00-cdf5-11e9-8bbe-433f072ac3a4.png" width="50%"></img>  
It reduced number of observations by thousands, but now it's clear that most of stagnation was in night and early morning (before 6), and most changes happened just before midday and at evening. It also seems that photos get most likes between 18 and 21, but to prove it we need statistical tests.  
### Each day as single observation  
From now on, single observation will be the sum of the change in the number of likes of all photos in a given time interval on a given day. Transforming data in this case was slightly harder than in previous one. Let start as before with boxplots.  
#### Plots  
<img src="https://user-images.githubusercontent.com/53919928/64136315-17b41100-cdf1-11e9-84d7-caf53e4ad260.png" width="60%"></img>  
We can see, that there are many observations with zero change so medians are exact zero or very close to it. I removed them, it resulted in the plot below  
<img src="https://user-images.githubusercontent.com/53919928/64136316-17b41100-cdf1-11e9-8eca-c6218a9ad12e.png" width="60%"></img>  
It seems that the greatest positive changes in numbers of likes occur between 18 and 21.  
Let's take a look at histograms  
<img src="https://user-images.githubusercontent.com/53919928/64136257-c60b8680-cdf0-11e9-8772-c2748a6e4ce8.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/64136258-c6a41d00-cdf0-11e9-9616-177e1d6e0edb.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/64136264-c73cb380-cdf0-11e9-8a6c-5fb46b21575b.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/64136259-c6a41d00-cdf0-11e9-9e57-990cc7eaa148.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/64136260-c6a41d00-cdf0-11e9-9814-9556df0e3a4a.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/64136261-c6a41d00-cdf0-11e9-8267-e164c4b56e26.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/64136262-c73cb380-cdf0-11e9-8143-c0daa30ba216.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/64136263-c73cb380-cdf0-11e9-8d07-70780ffbb2a3.png" width="45%"></img>  
It seems that probability of changes in numbers of likes is more uniformly distributed than before (but it doesn't look like [uniform distribution](https://en.wikipedia.org/wiki/Uniform_distribution_(continuous))).  
### Statistics  
First statistics of all observations  
</img> <img src="https://user-images.githubusercontent.com/53919928/64136940-52b84380-cdf5-11e9-96cc-187defdd3811.png" width="50%"></img>  
Intervals 9-12 and 18-21 clearly have the highest mean. Median for almost every interval is the same, it equals zero.  
<img src="https://user-images.githubusercontent.com/53919928/64136945-58158e00-cdf5-11e9-8c1e-23586f9e4f97.png" width="50%"></img>  
After removing 'zero' observations (about half of the total of observations). It is clear that interval 18-21 has the greates mean and median. Interval 9-12 is winner if it comes to the highest number of nonzero observations.  
Just like before some tests are needed to prove if differences between time intervals are statistically significant.
