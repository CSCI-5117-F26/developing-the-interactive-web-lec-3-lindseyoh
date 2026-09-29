from flask import Flask, render_template, request, redirect

app = Flask(__name__)

names = []

@app.route("/")
def index():
    return render_template("index.html", names=names)

@app.route("/catch", methods=["POST"])
def catch():
    name = request.form.get("name")
    if name:
        names.append(name)
    return redirect("/")



# def twice(some_funk):
#     def temp(*args, **argv):
#         some_funk(*args, **argv)
#         some_funk(*args, **argv)

# @twice
# def say_moo():
#     print("moo")

# say_moo()

if __name__ == "__main__":
    app.run(debug=True, port=5001)