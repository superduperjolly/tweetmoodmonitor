"""Main module for running the application"""
from tweetmoodmonitor.main import app

if __name__ == "__main__":
    app.run_server(debug=True)
