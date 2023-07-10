from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task",
      "done": False },

    { "label": "My second task",
      "done": False }
]

@app.route('/todos', methods=['GET'])
def getTodos():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    #if position < len(todos):
        #popped_item = todos.pop(0)
        del todos[0]
        print("This is the position to delete: ", position)
        return jsonify(todos)
    #else:
     #   return jsonify({"error": "Invalid position"}), 404

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)