from flask import Flask, request, jsonify, send_from_directory
import os
import logging

# Define absolute paths
static_folder = os.path.abspath('../frontend/static')
template_folder = os.path.abspath('../frontend/templates')

app = Flask(__name__, static_folder=static_folder, template_folder=template_folder)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Enable debug mode
app.config['DEBUG'] = True

@app.route('/')
def serve_index():
    try:
        logging.info(f"Serving index.html from {template_folder}")
        return send_from_directory(template_folder, 'index.html')
    except Exception as e:
        logging.error(f"Error serving index.html: {e}")
        return str(e), 500

@app.route('/static/<path:path>')
def send_static(path):
    try:
        logging.info(f"Serving static file from {static_folder}/{path}")
        return send_from_directory(static_folder, path)
    except Exception as e:
        logging.error(f"Error serving static file: {e}")
        return str(e), 500

@app.route('/query', methods=['GET'])
def query():
    user_query = request.args.get('text')
    logging.info(f"Received query: {user_query}")
    # Placeholder response
    response = {"response": f"You asked: {user_query}"}
    return jsonify(response)

if __name__ == '__main__':
    # Enable debug mode by setting debug=True
    app.run(host='0.0.0.0', port=5000, debug=True)
