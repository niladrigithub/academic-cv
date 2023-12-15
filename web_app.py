from flask import Flask, render_template
from tkinter import *

app = Flask(__name__)

# Function to open the portfolio link in a web browser
def open_portfolio():
    import webbrowser
    webbrowser.open("https://unityclubx.wixsite.com/academic-cv")

# GUI window
root = Tk()
root.title("Personal Web Page")

# Label to display your name
name_label = Label(root, text="Niladri Das", font=("Helvetica", 20))
name_label.pack(pady=10)

# Button to open the portfolio link
portfolio_button = Button(root, text="Portfolio", command=open_portfolio)
portfolio_button.pack(pady=10)

# Label to display a motivational quote
quote_label = Label(root, text="\"Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.\" - Christian D. Larson", font=("Helvetica", 12), wraplength=300)
quote_label.pack(pady=20)

# Start Flask web application
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
