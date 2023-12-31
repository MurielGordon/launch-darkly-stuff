from flask.templating import render_template
from flask import Flask
import ldclient
from ldclient import Context
from ldclient.config import Config 

app = Flask(__name__)

# swap out context key and name
context = Context.builder("*****").name("Sandy").build()


@app.route("/")
def get_feature():
    # swap out SDK key 
    ldclient.set_config(Config("*****"))
    # input your feature flag key name below
    show_feature = ldclient.get().variation("tutorialFlag", context, False)
    # set if-statement for True when feature flag targeting is set to "serve Enabled when on" 
    if show_feature == True:
        ldclient.get().close()
        return """
        <h1>Well done!</h1>
        <h3>Your feature flag is working as expected.</h3>
        <h3>You now have a foundational understanding of how the LaunchDarkly Python server SDK works with your code.</h3>
        """
    else: 
        ldclient.get().close()
        return """
        <h1>I'm sorry to report that something went wrong with your implementation.</h1>
        <img src="data:image/png;base64,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" alt="Oh No">
        <h2>Are you sure you toggled your feature flag to 'on'?</h2>
        """
        # yes that URL is hilariously long but trust me it's worth it

if __name__ == '__main__':
    app.run(debug=True)