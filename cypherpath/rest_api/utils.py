from cypherpath.rest_api import user


def get_vnc_url(sdi_id, machine_id, user_id):
    response = user.create_user_single_use_login_token(user_id=user_id).json()
    response_url = response['url']
    sdi_url = f'{response_url}?next=/sdi/{sdi_id}/topology/machine/{machine_id}/vnc/'
    return sdi_url
