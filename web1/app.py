#1. Create a flask app
from flask import Flask,render_template

app = Flask(__name__)
#2. Create router
ps = [
        "Before you can begin to determine what the composition of a particular paragraph will be, you must first decide on an argument and a working thesis statement for your paper. What is the most important idea that you are trying to convey to your reader? The information in each paragraph must be related to that idea. In other words, your paragraphs should remind your reader that there is a recurrent relationship between your thesis and the information in each paragraph. A working thesis functions like a seed from which your paper, and your ideas, will grow. The whole process is an organic one—a natural progression from a seed to a full-blown paper where there are direct, familial relationships between all of the ideas in the paper",
        "The decision about what to put into your paragraphs begins with the germination of a seed of ideas; this “germination process” is better known as brainstorming. There are many techniques for brainstorming; whichever one you choose, this stage of paragraph development cannot be skipped. Building paragraphs can be like building a skyscraper: there must be a well-planned foundation that supports what you are building. Any cracks, inconsistencies, or other corruptions of the foundation can cause your whole paper to crumble",
        "ddafahjkfdjkfdsajhfasdjkhsadfjkgdska;jfhsf",
    ]
@app.route("/")
def homepage():
    
    return render_template('homepage.html',
    title = "Yesterday",
    posts = ps


@app.route('/post/<int:position>')
def post_detail(position):
    if position < 0 or position >= len(ps):
        return 'Not found', 404
    post = ps[position - 1]
    return render_template('post_detail.html', post = post)
    

@app.route('/posts')
def posts():
    shortened_ps = []
    for post in ps:
        shortened_ps.append(post[0:20])
    return render_template('post_detail.html', posts = shortened_ps)


@app.route('/cuong')
def cuong():
    return 'Hello Cuong'


@app.route('/hello/<name>')
def hello(name):
    return 'Hello ' + name


@app.route('/add/<int:a>/<int:b>')
def sum(a, b):
    c = a + b
    return str(c)


@app.route('/h1tag')
def h1tag():
    return '<h1>Heading 1 - Bigg</h1><p>Awesome</p>'

#3. Run app
print('Running app')
if __name__ == "__main__":
    app.run(debug = True) #listening
