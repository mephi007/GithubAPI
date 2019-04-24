from flask import Flask, request, render_template
from searchOperation import searchOperation
from reposOperation import reposOperation

app = Flask(__name__)


class globalData():
    username = None

data = globalData()


@app.route("/", methods = ['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route("/searchResult", methods= ['GET', 'POST'])
def searchResult():
    username = request.form['username']
    data.username = username
    print(username)
    dataSend = searchOperation(username=username)
    dataSend.show()
    img_url = dataSend.ProfilePic()
    name = dataSend.userName()
    company = dataSend.company()
    location = dataSend.location()
    bio = dataSend.bio()
    repos = dataSend.repos()
    return render_template('SearchResult.html', username=username, img_url=img_url, name=name, company=company, location=location, bio=bio, repos=repos)

@app.route("/searchResult/repos", methods= ['GET', 'POST'])
def repos_detail():
    username = data.username
    dataRepo = reposOperation(username=username)
    show = dataRepo.list_repo()
    print(type(dataRepo.list_repo()))
    print("in a route")
    print(show)
    return render_template('repos.html', username=username, show=show)


if(__name__)==("__main__"):
    app.run(debug = True)
