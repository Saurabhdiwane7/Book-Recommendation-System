# Book-Recommendation-System

From the given dataset we are about to build the popularity based, and collaborative filtering based model using the cosine similarity ,CSR matrix algorithms so as  top n number of recommendations. 
Developed a user-friendly interface that is easy to use and navigate, making it simple for users to discover and select books they would like to read.

From the dataset, we have

Books.csv 
  Columns = ('ISBN', 'Title', 'Author', 'Year', 'Publisher', 'Image-URL-S’, Image-URL-M', 'Image-URL-L’)
Shape =(271360, 8) 

Rating.csv 
Columns = (  'User_ID ’ , 'ISBN', 'rating’ )
Shape =(1048575,3)

Users.csv 
Columns = ('User_ID', 'Location', 'Age’ )
Shape = (278858,3)

https://pm1.narvii.com/6769/cda6e56600ccbaf2a8e3338e40b0b97b0782f5dfv2_hq.jpg

we have preprocessed the data, perform EDA and visualizations,imputed the null values and perform all necessary correactions.
used Cosine similarity and CSR algorithms to build and evaluate the model 
we've deployed the model by using flask web framwork.
model gives Top n number of recommendations as per the search result.





