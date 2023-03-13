import json


def test_export_json_to_file():
    from utils import export_json_to_file
    from constants import TV_REQUEST_TYPE

    json_content = json.dumps({'a': 'b'})

    export_json_to_file(json_content, TV_REQUEST_TYPE)

    assert True
