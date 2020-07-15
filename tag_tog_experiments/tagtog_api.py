import requests

user_name = 'charantej'
password = 'Password*01'
project_name = 'sample'
tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"


def get_auth():
    auth = requests.auth.HTTPBasicAuth(username=user_name, password=password)
    return auth


def send_plain_text():
    """
    The example below imports plain text and retrieve the automatic annotations in ann.json format
    """
    params = {'project': project_name, 'owner': user_name, 'output': 'ann.json'}
    payload = {
        'text': 'Antibody-dependent cellular cytotoxicity (ADCC), a key effector function for the clinical effectiveness of monoclonal antibodies, is triggered by the engagement of the antibody Fc domain with the Fcγ receptors expressed by innate immune cells such as natural killer (NK) cells and macrophages.'}
    response = requests.post(tagtogAPIUrl, params=params, auth=get_auth(), data=payload)
    print(response.text)


def send_plan_text_return_no_annotation():
    """
    Sending plain text without asking annotation in return.
    """
    params = {"project": project_name, "owner": user_name, "format": "verbatim", "output": "null"}
    payload = {
        "text": "The film stars Leonardo DiCaprio, Brad Pitt and Margot Robbie"
    }
    response = requests.post(tagtogAPIUrl, params=params, auth=get_auth(), data=payload)
    print(response.text)


def send_web_link_tag_tog():
    """
    sending web link and creating the html and tagging it there.
    """
    params = {'project': project_name, 'owner': user_name, 'output': 'weburl',
              'url': 'https://en.wikipedia.org/wiki/Autonomous_cruise_control_system'}
    response = requests.post(tagtogAPIUrl, params=params, auth=get_auth())
    print(response.text)


def send_ann_text_content():
    """
    sending both annotation and the text file which can be pre-tagged
    """
    params = {'project': project_name, 'owner': user_name, 'output': 'null', 'format': 'default-plus-annjson'}
    with open('ann.json', 'r') as f:
        annotations = f.read()
    files = {
        'ann': ('text.ann.json', annotations),
        'plain': ('text.txt', open('./text.txt'))
    }
    response = requests.post(tagtogAPIUrl, params=params, auth=get_auth(), files=files)
    print(response.text)


if __name__ == '__main__':
    send_ann_text_content()
# send_web_link_tag_tog()
# send_plain_text()
# send_plan_text_return_no_annotation()
