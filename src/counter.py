from flask import Flask
from . import status

app = Flask(__name__)

COUNTERS = {}


# We will use the app decorator and create a route called slash counters.
# specify the variable in route <name>
# let Flask know that the only methods that is allowed to called
# on this function is "POST".


@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    """Create a counter"""
    app.logger.info(f"Request to create counter: {name}")
    global COUNTERS

    if name in COUNTERS:
        return {"Message": f"Counter {name} already exists"}, status.HTTP_409_CONFLICT

    COUNTERS[name] = 0
    return {name: COUNTERS[name]}, status.HTTP_201_CREATED


@app.route('/counters/<name>', methods=['PUT'])
def update_counter(name):
    """Update a counter by incrementing its value by 1"""
    app.logger.info(f"Request to update counter: {name}")
    global COUNTERS

    if name not in COUNTERS:
        return {"message": f"Counter {name} not found"}, status.HTTP_404_NOT_FOUND

    COUNTERS[name] += 1
    return {name: COUNTERS[name]}, status.HTTP_200_OK


@app.route('/counters/<name>', methods=['GET'])
def get_counter(name):
    """Retrieve the value of a counter"""
    app.logger.info(f"Request to retrieve counter: {name}")
    global COUNTERS

    if name not in COUNTERS:
        return {"message": f"Counter {name} not found"}, status.HTTP_404_NOT_FOUND

    return {name: COUNTERS[name]}, status.HTTP_200_OK


@app.route('/counters/<name>', methods=['DELETE'])
def delete_counter(name):
    """Delete a counter"""
    app.logger.info(f"Request to delete counter: {name}")
    global COUNTERS

    if name not in COUNTERS:
        return {"message": f"Counter {name} not found"}, status.HTTP_404_NOT_FOUND

    del COUNTERS[name]
    return "", status.HTTP_204_NO_CONTENT
