from flask.templating import render_template
from flask import Flask
import ldclient
from ldclient.config import Config 

app = Flask(__name__)

#is this still relevant? I think v9 has something about not needing users
user = {
    "key": "aa0ceb",
    "firstName": "Mara",
    "lastName": "Jade",
    "email": "email@fake.com",
    "custom": {
        "groups": ["Jedi"]
    }
}


@app.route("/")
def get_feature():
    ldclient.set_config(Config("*****"))
    show_feature = ldclient.get().variation("launchTheme", user, False)
    if show_feature == True:
        show_ripley = ldclient.get().variation("launchRipley", user, "alien.jpg")
        print(show_ripley)
        ldclient.get().close()
        return render_template("home.html", ripley=show_ripley)
    else:
        ldclient.get().close()
        return """
        <h1>Welcome to Python and LaunchDarkly</h1>
        <h2>This is highly boring and not on brand</h2>
        <h2>:(</h2>
        """

if __name__ == '__main__':
    app.run(debug=True)