from flask import Flask, jsonify, request, json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text, 200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    print(decoded_object, todos, "@@@@@")
    print(jsonify(todos), type(jsonify(todos)), "@@@@@")
    return jsonify(todos), 200

@app.route('/todos', methods=['DELETE'])
def delete_todo(position):
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.remove(decoded_object)
    return jsonify(todos), 200

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

  