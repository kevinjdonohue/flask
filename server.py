from flask import Flask, request

from root_controller import RootController
from tokens_controller import TokensController

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def root():
    r = RootController()
    return r.hello_world()

@app.route('/tokens', methods=['GET'])
def tokens():
    query_parameters = request.args

    tokens_request_validator = TokensRequestValidator()
    is_valid = tokens_request_validator.Validate(query_parameters)

    tokens_controller = TokensController()
    return tokens_controller.get_all_tokens()
