from flask import Flask, render_template, request
import numpy as np
import pickle
import pandas as pd


popular_df = pickle.load(open('popular.pkl', 'rb'))
pop_df = pd.DataFrame(popular_df)
book = pickle.load(open('books.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
pt = pd.DataFrame(pt)
similarity_score = pickle.load(open('similarity_scores.pkl', 'rb'))

app = Flask(__name__)

### When entering book names make sure to add exact book name or it'll throw error
### all the pkl is genereated from "collaborative recommendation" tutroial repo check that out

@app.route('/')
def index():
    return render_template('index1.html',
                           book_name=list(pop_df['Book-Title'].values),
                           author=list(pop_df['Book-Author'].values),
                           image=list(pop_df['Image-URL-M'].values),
                           votes=list(pop_df['num_ratings'].values),
                           rating=list(pop_df['avg_rating'].values)
                           )


@app.route('/recommend')
def recommend_ui():
    return render_template("recommend.html")


@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')

    index = np.where(pt.index == user_input)[0][0]
    similars = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similars:
        item = []
        # print(pt.index[i[0]])
        # extend used bc we don't want 2D list
        # we don't want array so list is used
        temp_df = book[book['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    print(data)

    return render_template('recommend.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
