import api.authentication as authenticated_request


def get_issue_comments(issue_id):
    return authenticated_request.get('/repos/rcorreia/pytest-template/issues/' + issue_id + '/comments')
