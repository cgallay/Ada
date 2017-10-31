# ISP Analysis For Switzerland

# Abstract
The goal of our project is to compare the network operator in Switzerland to help people truly select the best operator for their needs. To answer this question we would use an external dataset provided by [Ookla](http://www.ookla.com/). As we write this, we still haven't received a feedback from Ookla on whether we are allowed to use their dataset. That's the reason why we are proposing another [backup project](../Project/README.md).

Given that we get the dataset, we would like to build an interactive map of Switzerland where the user would be able to zoom on regions in order to see a heat map of the network speed per operator.

Depending on the richness of the dataset, we would like to add the possibility for the user to travel in time to see how the network speed changed over the years. This is interesting in order to see which [ISP](https://en.wikipedia.org/wiki/Internet_service_provider) is really investing for a better network and where.

Finally, this project could have a social approach in a sense that a lot of people pay for a service that does not always fulfil its obligations.


# Research questions
Here is a list of the answer we would try to answer if time and data allow us to do so: 
- Which is the best ISP in Switzerland for a specific user needs?
- Where/When is the network mostly saturated (time of the day and place)?
- Which ISP is mostly investing itself into building a better network?

# Dataset
The full dataset is not open source but a [sample one](http://go.ookla.com/nmdata) can be downloaded. 

Based on the sample we can already extract some interesting information for us such as test_date, client_country, network_operator_name, is_ISP, device, client_latitude, client_longitude, latency, download_kbps, upload_kbps. The fact that this information is present makes us more confident to use this dataset as our main source of information. We might later need to use some other dataset to help us define if the speed measured by a device is limited by the network capacity, the device, the subscription or other reason.  

The format of the dataset being csv we should not have too much difficulty to use it.

# A list of internal milestones up until project milestone 2
If we get the dataset quickly enough, here is what we plan to do for the next deadline:
- Exploring the dataset
- Find a good library to represent our data on a map.
- Basis analysis to gain global answer to our answer.

# Questions for TAa
- If the dataset appears not to be free, are we still allow to use it? 