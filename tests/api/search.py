import api.authentication as authenticated_request


def get_search_users_request(user_query):
    return authenticated_request.get('/search/users?q=' + user_query)


def get_search_issues_request(issue_query):
    return authenticated_request.get('/search/issues?q=' + issue_query)
