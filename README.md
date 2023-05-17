# Book-Recommendation-System
![Book recommendation system](https://tse4.mm.bing.net/th?id=OIP._eIMvrY0TdUV_3IipOsJXAHaDq&pid=Api&P=0&h=180)



From the given dataset we are about to build the popularity based, and collaborative filtering based model using the cosine similarity ,CSR matrix algorithms so as  top n number of recommendations. 
Developed a user-friendly interface that is easy to use and navigate, making it simple for users to discover and select books they would like to read.

♦ ## Data Preprocessing

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


♦ ## EDA and Visualizations 

From all the dataset we have dealt with all the null values and perform all the necessary correction as required 

In the Age column which contain 39% null values which we have  imputed with mean values

we have preprocessed the data, perform EDA and visualizations,imputed the null values and perform all necessary correactions.

used Cosine similarity and CSR algorithms to build and evaluate the model 

♦ ## Model Building and Model Evaluation

♦ Popularity based Model
	In this model we have filtered top 50 books as per the num_rating more than 50 
	and avg_rating from descending sequence

♦ Collaborative filtering based model 
We have build the model using cosine similarity, we have created the pivot table to 
Calculate the distance between the similar users.

♦ ##Model Deployment

We've deployed the model by using flask web framework.

Model gives Top 50 book recommendation as per the popularity and current trends and also give top n number of recommendations as per the search result.





