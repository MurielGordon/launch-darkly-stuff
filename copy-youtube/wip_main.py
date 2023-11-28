from flask.templating import render_template
from flask import Flask
import ldclient
from ldclient.config import Config 

app = Flask(__name__)


context = {
    "kind": "user",
    "key": "example-user-key",
    "name": "Sandy"
}


@app.route("/")
def get_feature():
    # REMOVE BEFORE POSTING
    ldclient.set_config(Config("*****"))
    show_feature = ldclient.get().variation("launchTheme", context, False)
    if show_feature == True:
    #    show_ripley = ldclient.get().variation("launchRipley", user, "alien.jpg")
    #    print(show_ripley)
    #    ldclient.get().close()
        return render_template("home.html")#, ripley=show_ripley)
    #else:
    #    ldclient.get().close()
    #    return """
    #    <h1>Welcome to Python and LaunchDarkly</h1>
    #    <h2>This is highly boring and not on brand</h2>
    #    <h2>:(</h2>
    #    """

if __name__ == '__main__':
    app.run(debug=True)