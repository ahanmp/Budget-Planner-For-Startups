from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder='../frontend')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/styles.css')
def styles():
    return send_from_directory(app.static_folder, 'styles.css')

@app.route('/api/recommendation', methods=['POST'])
def recommendation():
    data = request.json
    expenses = data.get('expenses', 0)

    try:
        expenses = float(expenses)
    except ValueError:
        return jsonify({"error": "Invalid expense value"}), 400

    if expenses <= 0:
        return jsonify({"error": "Expense must be greater than zero"}), 400

    # Strategic budget calculation: add savings margin
    recommended_budget = expenses   # 10% savings buffer

    allocations = {
        "Operations": 0.30,
        "Marketing": 0.20,
        "Salaries": 0.25,
        "Research & Development": 0.10,
        "Miscellaneous": 0.05,
        "Savings": 0.10
    }

    breakdown = {k: round(recommended_budget * v, 2) for k, v in allocations.items()}

    if expenses > recommended_budget:
        message = f"Expenses are high. Try reducing them to stay under ₹{recommended_budget:.2f} to allow for savings and better financial stability."
    else:
        message = "Your current expenses are healthy. Keep maintaining this balance for consistent growth."

    return jsonify({
        "total_budget": round(recommended_budget, 2),
        "breakdown": breakdown,
        "recommendation": message
    })

if __name__ == '__main__':
    app.run(debug=True)

