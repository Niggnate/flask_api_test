from flask import Flask, make_response, jsonify

from api.statement_generator import StatementGenerator

app = Flask(__name__)


@app.route('/cms_source_email', methods=['POST'])
def cms_email():
    statement = StatementGenerator()
    return make_response(jsonify(statement.generate_statement_payload()), 200)


if __name__ == "__main__":
    app.run(debug=True)
