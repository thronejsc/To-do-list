from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = {
    'todo': ['Task 1', 'Task 2', 'Task 3'],
    'in_progress': ['Task 4', 'Task 5'],
    'done': ['Task 6']
}

# Routes
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    column = request.form['column']
    task_name = request.form['task_name']
    tasks[column].append(task_name)
    return jsonify({'success': True})

@app.route('/move_task', methods=['POST'])
def move_task():
    from_column = request.form['from_column']
    to_column = request.form['to_column']
    task_name = request.form['task_name']
    tasks[from_column].remove(task_name)
    tasks[to_column].append(task_name)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)