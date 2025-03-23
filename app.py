from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Data structures to store processes, resources, and allocations
processes = []
resources = []
allocations = []

@app.route('/api/check-deadlock', methods=['GET'])
def check_deadlock():
    # Build the graph for deadlock detection
    graph = build_graph()
    
    # Check for cycles in the graph (deadlock detection)
    has_deadlock = detect_deadlock(graph)
    
    return jsonify({"deadlock": has_deadlock})

@app.route('/api/graph', methods=['POST'])
def update_graph():
    global processes, resources, allocations
    data = request.json
    processes = data.get('processes', [])
    resources = data.get('resources', [])
    allocations = data.get('edges', [])
    return jsonify({"message": "Graph updated successfully"})

def build_graph():
    """
    Builds a graph representation of the resource allocation graph (RAG).
    """
    graph = {}
    
    # Add processes and resources as nodes
    for process in processes:
        graph[process] = []
    for resource in resources:
        graph[resource] = []
    
    # Add edges based on allocations
    for edge in allocations:
        from_node = edge['from']
        to_node = edge['to']
        if from_node in graph:
            graph[from_node].append(to_node)
    
    return graph

def detect_deadlock(graph):
    """
    Detects deadlock by checking for cycles in the graph.
    Uses Depth-First Search (DFS) to detect cycles.
    """
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

    for node in graph:
        if is_cyclic(node):
            return True
    return False

if __name__ == '__main__':
    app.run(debug=True)