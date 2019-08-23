# instagram
File *load_inst.py* (name will be probably changed) contains every function or class written by me and used in this project.  
File *inst_analysis_likes.ipynb* is notebook with code which was used to obtain results below.
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
First I transformed the data so that only the rows containing information about the next hours and days from the upload remain. For example here is head of dataframe containing information about first hour since upload  
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
Before moving to test let's look at [correlation](https://en.wikipedia.org/wiki/Correlation_and_dependence)  

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



