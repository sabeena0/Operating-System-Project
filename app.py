from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

processes = []
resources = []
edges = []

@app.route('/api/check-deadlock', methods=['GET'])
def check_deadlock():
    try:
        # Build wait-for graph
        graph = {}
        
        # Create entries for all processes
        for process in processes:
            graph[process] = []
        
        # Process the edges to build wait-for relationships
        for edge in edges:
            if edge['type'] == 'assignment':
                # Process -> Resource assignment
                # Find if any process is waiting for this resource
                resource = edge['to']
                for req_edge in edges:
                    if req_edge['type'] == 'request' and req_edge['from'] == resource:
                        # Process holds resource that another process wants
                        graph[edge['from']].append(req_edge['to'])
        
        # Check for cycles (deadlock detection)
        has_deadlock = detect_deadlock(graph)
        return jsonify({"deadlock": has_deadlock})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/graph', methods=['POST'])
def update_graph():
    global processes, resources, edges
    data = request.json
    processes = data.get('processes', [])
    resources = data.get('resources', [])
    edges = data.get('edges', [])
    return jsonify({"message": "Graph updated successfully"})

def detect_deadlock(graph):
    visited = set()
    recursion_stack = set()

    def is_cyclic(node):
        if node not in visited:
            visited.add(node)
            recursion_stack.add(node)
            
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    if is_cyclic(neighbor):
                        return True
                elif neighbor in recursion_stack:
                    return True
            
            recursion_stack.remove(node)
        return False

    for node in list(graph.keys()):
        if is_cyclic(node):
            return True
    return False

if __name__ == '__main__':
    app.run(debug=True, port=5000)
