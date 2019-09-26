# instagram
File *load_inst.py* contains every function or class written by me and used in this project.  
File *inst_analysis_likes.ipynb* is notebook with code which was used to obtain results below.  
File *inst_analysis_likes_no_output.ipynb* is the same as *inst_analysis_likes.ipynb*, but without any output, so you may look at the code via github.
## Introduction
	
Project is based on data about instagram photos of user [mkaciubapl](https://www.instagram.com/mkaciubapl/). You can find original data [here](https://www.dropbox.com/sh/hobhqg7rvreweml/AADIfllpRt6cDwXFM5gGeh1Qa?dl=0).  
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
Statistics show that boxplots for 10 a.m-4 p.m are skewed because of some poorly rated photos, also between 4 a.m and 10 a.m were uploaded photos that found many fans after 6 or 12 days.   
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
<img src="https://user-images.githubusercontent.com/53919928/65555938-41fb7900-df2e-11e9-9dc4-ea9121a6881c.png" width="60%"></img>  
It doesn't seem very helpful. Let's discard observations with no change. We get  
<img src="https://user-images.githubusercontent.com/53919928/65555941-41fb7900-df2e-11e9-9b91-01e6d4b36fbb.png" width="60%"></img>  
It looks that number of likes increases as evening approaches. It also seems that photo gets most of its likes in time interval of its upload. There are many observations in each interval, so it is reasonable to plot histograms.  
<img src="https://user-images.githubusercontent.com/53919928/65556370-a539db00-df2f-11e9-94e4-13343f252bf3.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65556371-a539db00-df2f-11e9-853c-22d1191ddaa2.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65556372-a4a14480-df2f-11e9-9771-cefdefb29e23.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65556373-a539db00-df2f-11e9-9590-b9433813fa96.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65556374-a539db00-df2f-11e9-8731-81f34c27620d.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65556375-a5d27180-df2f-11e9-94d1-883c6834ec52.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65556376-a5d27180-df2f-11e9-94fd-56c180468f97.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65556377-a5d27180-df2f-11e9-8eca-148bde646fef.png" width="45%"></img>    
We can see that distributions of changes in numbers of likes clearly aren't normal, most likely for changes is beeing close to zero, but not negative.  
#### Statistics
Now we will look at some basic statistics. We will start with basic data (including observations without any changes).  
<img src="https://user-images.githubusercontent.com/53919928/65556561-3dd05b00-df30-11e9-9298-8283b0d33e1a.png" width="50%">  
Mean for every time interval is close to zero and every quartile equals zero. There nothing interesting here.  
Now we remove 'zero' observations  
<img src="https://user-images.githubusercontent.com/53919928/65556571-4759c300-df30-11e9-8508-b381989263b6.png" width="50%"></img>  
It reduced number of observations by thousands, but now it's clear that most of stagnation was in night and early morning (before 6), and most changes happened just before midday and at evening. It also seems that photos get most likes between 18 and 21, but to prove it we need statistical tests.  

#### Tests
First I used Kruskal-Wallis test on data with 'zero' observations. It showed that there are statistically significant differences between groups (p-value was very close to 0). Let's look at the results of post-hoc test
<img src="https://user-images.githubusercontent.com/53919928/65556903-a8ce6180-df31-11e9-9a74-d336f43450bd.png" width="70%"></img>  
Red color means that p-value is small and differences are significant. It's clearly visible that intervals 0-3 and 3-6 differ the most from other intervals.  
Now observations without zeros.  
Kruskal-Wallis test also resulted in very small p-value. Table of post-hoc test is below  
<img src="https://user-images.githubusercontent.com/53919928/65556917-b5eb5080-df31-11e9-8823-a24171b645ab.png" width="70%"></img>  
Without zeros interval 3-6 doesn't differ so much and 0-3 differs from every other interval.

### Each day as single observation  
From now on, single observation will be the sum of the change in the number of likes of all photos in a given time interval on a given day. Transforming data in this case was slightly harder than in previous one. Let start as before with boxplots.  
#### Plots  
<img src="https://user-images.githubusercontent.com/53919928/65557028-1b3f4180-df32-11e9-92b0-52c0e1efade0.png" width="60%"></img>  
We can see, that there are many observations with zero change so medians are exact zero or very close to it. I removed them, it resulted in the plot below  
<img src="https://user-images.githubusercontent.com/53919928/65557029-1b3f4180-df32-11e9-8e15-4f0a91646119.png" width="60%"></img>  
It seems that the greatest positive changes in numbers of likes occur in intervals 6-9 and 18-21.  
Let's take a look on histograms  
<img src="https://user-images.githubusercontent.com/53919928/65557289-1a5adf80-df33-11e9-8063-5481f44b7b6a.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65557290-1a5adf80-df33-11e9-9323-70e8e04b5182.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65557291-1a5adf80-df33-11e9-9b37-d29d7cfae6cb.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65557292-1a5adf80-df33-11e9-85fa-7124f256c96c.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65557294-1a5adf80-df33-11e9-9402-7ae3cf1e0a51.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65557295-1af37600-df33-11e9-9761-a084301fdfe1.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65557296-1af37600-df33-11e9-83ba-2bfe061c9b4f.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65557297-1af37600-df33-11e9-8bc3-8f0b8f2b09f4.png" width="45%"></img>   
It seems that probability of changes in numbers of likes is more uniformly distributed than before (but it doesn't look like [uniform distribution](https://en.wikipedia.org/wiki/Uniform_distribution_(continuous))).  
#### Statistics  
First statistics of all observations  
</img> <img src="https://user-images.githubusercontent.com/53919928/64136940-52b84380-cdf5-11e9-96cc-187defdd3811.png" width="50%"></img>  
Intervals 9-12 and 18-21 clearly have the highest mean. Median for almost every interval is the same, it equals zero.  
<img src="https://user-images.githubusercontent.com/53919928/64136945-58158e00-cdf5-11e9-8c1e-23586f9e4f97.png" width="50%"></img>  
After removing 'zero' observations (about half of the total of observations). It is clear that interval 18-21 has the greates mean and median. Interval 9-12 is winner if it comes to the highest number of nonzero observations.  
Just like before some tests are needed to prove if differences between time intervals are statistically significant.  
#### Tests  
First test for every observation (with 'zeros'). Kruskal-Wallis test resulted in very small p-value. Let's do post-hoc test.   
<img src="https://user-images.githubusercontent.com/53919928/65557980-77f02b80-df35-11e9-9f7a-d2824abb2444.png" width="70%"></img>  
Table looks very simmilar to table of test for every photo as single observation - intervals 0-3 and 3-6 differ the most from other intervals. Instresting thing is that in every differing pair is 0-3 or 3-6.  
Kruskal-Wallis test for data without 'zeros' resulted also in very small p-value.  
<img src="https://user-images.githubusercontent.com/53919928/65558018-8b02fb80-df35-11e9-9924-0090555392bb.png" width="70%"></img>  
Results of post-hoc test are very simmilar to those above, but now there are more pairs of differing intervals.  
## Days of week  
Let now look at numbers of likes in different days of week.  
I considered two cases:
* each photo as single observation
* each day as single observation  
### Each photo as single observation  
#### Plots
First look on boxplot of data with every observation  
<img src="https://user-images.githubusercontent.com/53919928/65642769-50aa6480-dff0-11e9-8184-7f9a3f5a129a.png" width="60%"></img>  
Let's discard observations with no change. We get  
<img src="https://user-images.githubusercontent.com/53919928/65645925-9ae41380-dff9-11e9-8a94-eac11f263905.png" width="60%"></img>  
In above figures we can see that most of likes photos get in the day they were uploaded. It shouldn't be surprising - photos get most of their likes in short time after upload.  
Let's take a look on histograms of changes in likes (only non-zero changes)   
<img src="https://user-images.githubusercontent.com/53919928/65645985-d54db080-dff9-11e9-9255-83c299cc5e55.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65645986-d54db080-dff9-11e9-9026-cca62b3acac6.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65645987-d54db080-dff9-11e9-9ca8-cd9b521e5c55.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65645988-d54db080-dff9-11e9-958a-fb9c8bbadb44.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65645989-d54db080-dff9-11e9-9e1f-ab4523a59e75.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65645991-d5e64700-dff9-11e9-8a7f-9ac452d51784.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65645992-d5e64700-dff9-11e9-95f3-7ea171e12e03.png" width="45%"></img>  
Histograms show that most of changes in numbers of likes are close to zero.  
#### Statistics  
First statistics of all observations  
</img> <img src="https://user-images.githubusercontent.com/53919928/65646331-0bd7fb00-dffb-11e9-8295-d3b8213770d5.png" width="50%"></img>  
This table doesn't look much instresting. Let's see what will change after removing 'zero' observations.  
</img> <img src="https://user-images.githubusercontent.com/53919928/65646344-172b2680-dffb-11e9-84ae-93350c855028.png" width="50%"></img>  
There are many observations without changes - most of them from weekend.  
#### Tests  
I conducted the Kruskal-Wallis test for all observations. P-value was very small, so there are significant differences between some pairs.  
</img> <img src="https://user-images.githubusercontent.com/53919928/65646827-ac7aea80-dffc-11e9-8f08-d1dffa8fa572.png" width="70%"></img>  
Red color means that two days differ in significant way.  
Result of test for data without 'zero' observations was also very small.  
</img> <img src="https://user-images.githubusercontent.com/53919928/65647003-640ffc80-dffd-11e9-9d06-9c91890ac101.png" width="70%"></img>  
Results of post-hoc test show that sunday differs the most.  
### Each day as single observation  
#### Plots  
First boxplot for every observation.   
<img src="https://user-images.githubusercontent.com/53919928/65647537-552a4980-dfff-11e9-8d32-99e120eb653c.png" width="60%"></img>   
Now boxplot without observation with zero change of number of likes.  
<img src="https://user-images.githubusercontent.com/53919928/65647540-552a4980-dfff-11e9-8799-353ee86c34de.png" width="60%"></img>  
It looks like discarding 'zeros' changes the most in saturday.  
Let's take a look on histograms for every day (with 'zeros').  
<img src="https://user-images.githubusercontent.com/53919928/65691437-1df48080-e071-11e9-9b53-0d133904deec.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65691438-1df48080-e071-11e9-9b4a-01f1bc01a15f.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65691439-1df48080-e071-11e9-8c05-18f2107c449e.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65691441-1e8d1700-e071-11e9-869f-ce6f88eacfd7.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65691442-1e8d1700-e071-11e9-974f-451c03707ccd.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65691444-1e8d1700-e071-11e9-840a-a101f046003b.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/53919928/65691446-1f25ad80-e071-11e9-9413-afe1c008d460.png" width="45%"></img>  
It looks like changes are smallest for saturday and sunday.  
#### Statistics  
First, we'll look at summaries for all data.  
</img> <img src="https://user-images.githubusercontent.com/53919928/65689267-f56a8780-e06c-11e9-8873-382f1f800fb4.png" width="50%"></img>  
We can see that the greatest increase in number of likes occured on tuesday and wednesday  
</img> <img src="https://user-images.githubusercontent.com/53919928/65689278-fd2a2c00-e06c-11e9-97e8-94588b018b18.png" width="50%"></img>  
Above table shows that most of days without change in number of likes were sundays.  
#### Tests  
Results of Kruskall-Wallis test tell that there are some significant differences between days.  
<img src="https://user-images.githubusercontent.com/53919928/65693649-eee00e00-e074-11e9-8677-1ecbd71ecd03.png" width="70%"></img>  
Post-hoc test shows that only sunday and wednesday differ in significant way.


