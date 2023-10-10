from website import create_app

app = create_app()

if __name__ == '__main__':  #This line means, app will only run if we run this file and not just import app on it.
    app.run(debug=True)