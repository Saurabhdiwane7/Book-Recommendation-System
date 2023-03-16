from flask import Flask, render_template,request
import pickle
import numpy as np

popular = pickle.load(open('popular_df.pkl', 'rb'))
books_pivot = pickle.load(open('book_pivot.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
sim_score = pickle.load(open('sim_score.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular['Title'].values),
                           author=list(popular['Author'].values),
                           image=list(popular['Image-URL-M'].values),
                           votes=list(popular['num_rating'].values),
                           rating=list(popular['avg_rating'].values)

                           )


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(books_pivot.index == user_input)[0][0]
    distances = sorted(list(enumerate(sim_score[index])), key=lambda x: x[1], reverse=True)[1:11]

    data = []
    for f in distances:
        item = []
        temp_df = books[books['Title'] == books_pivot.index[f[0]]]
        item.extend(list(temp_df.drop_duplicates('Title')['Title']))
        item.extend(list(temp_df.drop_duplicates('Title')['Author']))
        item.extend(list(temp_df.drop_duplicates('Title')['Image-URL-M']))

        data.append(item)
        print(data)
    return render_template('recommend.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)
