import json


# def test_export_json_to_file():
#     from utils import export_json_to_file
#     from constants import TV_REQUEST_TYPE
#
#     json_content = json.dumps({'a': 'b'})
#
#     export_json_to_file(json_content, TV_REQUEST_TYPE)
#
#     assert True

def test_choose_random_position():
    from utils import choose_random_position

    test_tv_list = [{'position': '1', 'title': 'Nasza planeta'}, {'position': '2', 'title': 'Breaking Bad'}, {'position': '3', 'title': 'Biuro'}, {'position': '4', 'title': 'Ostatni taniec'}, {'position': '5', 'title': 'Arcane'}, {'position': '6', 'title': 'Peaky Blinders'}, {'position': '7', 'title': 'BoJack Horseman'}, {'position': '8', 'title': 'Narcos'}, {'position': '9', 'title': 'Latający Cyrk Monty Pythona'}, {'position': '10', 'title': 'Chłopaki z baraków'}, {'position': '11', 'title': 'House of Cards'}, {'position': '12', 'title': 'Wikingowie'}, {'position': '13', 'title': 'Oderwij wzdłuż linii'}, {'position': '14', 'title': 'Uwięzione'}, {'position': '15', 'title': 'Stranger Things'}, {'position': '16', 'title': 'Awatar: Legenda Aanga'}, {'position': '17', 'title': 'Czarne lustro'}, {'position': '18', 'title': 'Hunter x Hunter'}, {'position': '19', 'title': 'Line of Duty - Wydział wewnętrzny'}, {'position': '20', 'title': 'Alchemia dusz'}, {'position': '21', 'title': 'Cowboy Bebop'}, {'position': '22', 'title': 'Zadzwoń do Saula'}, {'position': '23', 'title': 'Crash Landing on You'}, {'position': '24', 'title': 'Miecz zabójcy demonów - Kimetsu no Yaiba'}, {'position': '25', 'title': 'The Crown'}]
    test_movie_list = []
    print(choose_random_position(test_tv_list))
    print(choose_random_position(test_movie_list))

test_choose_random_position()