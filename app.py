from flask import Flask, jsonify
import json

app = Flask(__name__)

# --- Load Data From Cleaned JSON Files ---
def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

divisions = load_data('divisions_data.json')
districts = load_data('districts_data.json')
upazilas = load_data('upazilas_data.json')
unions = load_data('unions_data.json')
# --- End of Data Loading ---


# --- API Endpoints ---

# Endpoint to get all divisions
@app.route('/division', methods=['GET'])
def get_divisions():
    return jsonify(divisions)

# Endpoint to get districts for a specific division
@app.route('/division/<int:division_id>', methods=['GET'])
def get_districts(division_id):
    # Note: division_id is an integer, but in JSON it's a string.
    filtered_districts = [d for d in districts if d.get('division_id') == str(division_id)]
    if not filtered_districts:
        return jsonify({"error": "Division not found or no districts available"}), 404
    return jsonify(filtered_districts)

# Endpoint to get upazilas for a specific district
@app.route('/division/<int:division_id>/district/<int:district_id>', methods=['GET'])
def get_upazilas(division_id, district_id):
    filtered_upazilas = [u for u in upazilas if u.get('district_id') == str(district_id)]
    if not filtered_upazilas:
        return jsonify({"error": "District not found or no upazilas available"}), 404
    return jsonify(filtered_upazilas)
    
# Endpoint to get unions for a specific upazila
@app.route('/division/<int:division_id>/district/<int:district_id>/upazila/<int:upazila_id>', methods=['GET'])
def get_unions(division_id, district_id, upazila_id):
    # Note the spelling: the key in your JSON is "upazilla_id"
    filtered_unions = [u for u in unions if u.get('upazilla_id') == str(upazila_id)]
    if not filtered_unions:
        return jsonify({"error": "Upazila not found or no unions available"}), 404
    return jsonify(filtered_unions)


if __name__ == '__main__':
    app.run(debug=True)

