## Take home technical assignment for LaunchDarkly job application
Prompt:
* Create a feature flag in SDK coding language of your choice
* Use an LaunchDarkly SDK to implement the feature flag 

## Requirements:
1. Python3
2. pip
3. [A virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
4. Flask
5. [LaunchDarkly Python server SDK v9.0.1](https://docs.launchdarkly.com/sdk/server-side/python)

After requirements 1-4 have been met you are ready to start working with the LaunchDarkly UI and LaunchDarkly SDK. 

If you are not working with an existing [LaunchDarkly Project](https://docs.launchdarkly.com/home/organize/projects), a new one can be created by going to **Account Settings > Projects > Create Project.** From there the SDK setup wizard will walk you through the process of connecting an SDK to your Project, as well as a short program to help you verify that the connection was successful. 

If you're working with an existing Project, instructions for where to find your SDK key will come later in this tutorial.

Once you've got a live Project to work with, navigate to **Feature flags** in the LaunchDarkly UI and click **Create flag > Custom flag**. Give it a descriptive name and add a description if desired. Keep the configuration for this flag set to Boolean, and keep the default rules: when targeting is on serve Enabled, when targeting is off serve Disabled. Make note of the flag-key and save your flag.

Next let's get the LDClient set up on your local machine. Use pip install to [install the Python server SDK.](https://docs.launchdarkly.com/sdk/server-side/python#getting-started)

After installing the SDK, you will need to import the LaunchDarkly client into your application code:
```
import ldclient
from ldclient.config import Config
```

Next you will need to instantiate the LDClient in your code:
```
ldclient.set_config(Config("sdk-key-123abc"))
client = ldclient.get()
```

The SDK key (sdk-key-123abc) will need to come from the SDK that is connected to your LaunchDarkly Project. Navigate to Account Settings > Projects > select your project > copy the SDK key for the Project environment you intend to use.

The rest of the code you'll need to run this program is the following:
```
from ldclient import Context

context = Context.builder("context-key-123abc").name("Sandy").build()
flag_value = client.variation("flag-key-123abc", context, False)

if flag_value:
    # application code to show the feature
else:
    # the code to run if the feature is off

```
The flag-key can be found on the Feature flags page for your project. 

