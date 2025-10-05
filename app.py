from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        # You can save this to a database or send an email
        print(f"New message from {name} ({email}): {message}")
        flash("Your message has been sent successfully!", "success")
        return redirect("/")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
