# Music-Recommender

An app that uses [Spotify's Web API](https://developer.spotify.com/documentation/web-api) to recommend songs based on the input that the user provides. 

Built with Python, Flask and JavaScript. Styled with TailwindCSS.


## Getting Started


### Local Install

Installation of this project requires Node.js and Python installed.


1. To close the project run:
 `git clone https://github.com/BrettAdamson/Music-Recommender.git`

2.
    `cd` into the Music Recommender folder and run `npm install`

3.
    Sign up for developer access to [Spotify's Web API](https://developer.spotify.com/documentation/web-api). You will need both the **Client ID** and **Client Secret**.

4. Setup a .env file in the base directory that has the following lines:
        `CLIENT_SECRET=your_secret`
        `CLIENT_ID=your_id`
        Replace the values with the id and secret you got from the Spotify Web API.

5. Setup a Python Virtual Environment as seen here [Flask Install](https://flask.palletsprojects.com/en/3.0.x/installation/).
   1. For Windows run `py -3 -m venv .venv` and then activate the environment with `.venv\Scripts\activate`
6. Then run `pip install -r requirements. txt` to install all python dependencies.
7. Lastly, run `flask run` to run the Flask application.



