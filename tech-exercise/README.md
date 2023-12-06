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

If you are not working with an existing [LaunchDarkly Project](https://docs.launchdarkly.com/home/organize/projects), a new one can be created by going to **Account Settings > Projects > Create Project.** From there the SDK setup wizard will walk you through the process of connecting an SDK to your project, as well as a short program to help you verify that the connection was successful. 

If you're working with an existing Project, instructions for where to find your SDK key will come later in this tutorial.

Next let's get the LDClient set up on your local machine. Use pip install to [install the Python server SDK.](https://docs.launchdarkly.com/sdk/server-side/python#getting-started)

After installing the SDK, you will need to import the LaunchDarkly client into your application code:
- import ldclient
- from ldclient.config import Config

Next you will need to instantiate the LDClient in your code:
- ldclient.set_config(Config("sdk-key-123abc"))
- client = ldclient.get()

The SDK key (sdk-key-123abc) will need to come from the SDK that is connected to your LaunchDarkly Project. Navigate to Account Settings > Projects > select your project > copy the SDK key for the Project environment you intend to use.

