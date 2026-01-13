from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Experiments data
experiments = [
    {
        'number': 7,
        'title': 'Fusion Compiler Physical Design',
        'file': 'exp7_fusion_compiler_physical_design.html',
        'description': 'Introduction to Fusion Compiler and physical design flow',
        'color': '#667eea'
    },
    {
        'number': 8,
        'title': 'Physical Synthesis with Fusion Compiler',
        'file': 'exp8_physical_synthesis_fusion_compiler.html',
        'description': 'Physical synthesis techniques and optimization',
        'color': '#764ba2'
    },
    {
        'number': 9,
        'title': 'Clock Tree Synthesis (CTS)',
        'file': 'exp9_clock_tree_synthesis_cts.html',
        'description': 'Clock tree design, skew optimization, and timing closure',
        'color': '#2a5298'
    },
    {
        'number': 10,
        'title': 'Routing',
        'file': 'exp10_routing.html',
        'description': 'Global and detailed routing, DRC checking, and optimization',
        'color': '#1e3c72'
    }
]

@app.route('/')
def index():
    return render_template('index.html', experiments=experiments)

@app.route('/experiment/<filename>')
def experiment(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
