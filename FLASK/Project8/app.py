from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Dummy user data
user_data = {
    "1": {"name": "John Doe", "email": "john@example.com"},
    "2": {"name": "Jane Smith", "email": "jane@example.com"},
    "3": {"name": "Emily Johnson", "email": "emily@example.com"}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/userDetails', methods=['POST'])
def user_details():
    userid = request.form.get('userid')
    if userid in user_data:
        return jsonify(user_data[userid])
    else:
        return jsonify({"error": "User not found"})

if __name__ == '__main__':
    app.run(debug=True)