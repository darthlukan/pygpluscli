## PyGplusCli

### Description:
A simple CLI client for reading the most recent G+
posts from those in your circles.

**Author:** Brian Tomlinson

**Contact:** darthlukan at gmail dot com

**License:** [GPLv2](http://www.gnu.org/licenses/gpl-2.0.txt)

_**Note:**_ This software uses the google-api-python-client library.
please see [Google Developers Site](https://developers.google.com) for
information on Google's licensing of their software.

Requires Python-2.7.x, google-api-python-client, 
Developer API Key from Google APIs console.

**TODO:**

1. Tests
2. Reconfigure config setup for one-shot.
4. More features!


### Setup Instructions:

**Abstract:** Because there are only 10,000 API calls available per day
for free from Google, usage of this program requiers the user to setup
an API project in [Google's API Console](https://developers.google.com/console). If Google ever extends the amount
of calls to a level where a lot of users could run this app at the same time,
then I'll update it.  Until then, read on.


**Steps:**

1. Navigate to [Google's API Console](https://developers.google.com/console)
2. Select "Create" from the dropdown menu on the left and enter a project name.
3. In the services page, enable the Google+ API.
4. In the API Access pane, click "Create an OAuth 2.0 Client ID.
5. in the Product name field, enter an application name and click "Next".
6. In the "Client ID" Settings section, select "Installed Application".
7. In the API Access pane, click "Download JSON" to the right of the client ID you just created.
8. Open your terminal and cd to where you want this program to be installed (ex: ~/apps)
9. Execute:

    $ git clone git@github.com:darthlukan/pygpluscli.git

10. cd into pygpluscli
11. mv the client_secrets.json file into your current working directory, ex:
    
    $ mv ~/Downloads/client_secrets.json .      (Note the period!)

12. Create a keys.dat file in your current working directory, ex:

    $ touch keys.dat

13. In your favorite text editor, add the following:
    a. [CONFIG]  (Must be line 1 of the file)
    b. devkey: "" (Must be line 2 of the file!)
14. In the API Access pane, Find the section labeled "Simple API Access"
15. Copy the API key there and place it inside of the quotes in the keys.dat file that you just created.
16. Save that file and close it.
17. Switch user to root (su) or use sudo so that you can execute the following command:
    
    pip install google-api-python-client

18. Run the main.py file with your Python2 executable (no support for Python3 yet [blame Google]), ex:
    
    $ python2 main.py

19. Enjoy!
