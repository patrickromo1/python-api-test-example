import api.authentication as authenticated_request


def get_issue_comment_reaction(comment_id):
    return authenticated_request.get_with_custom_headers('/repos/rcorreia/pytest-template/issues/comments/' + comment_id + '/reactions',
                                                         {'Accept': 'application/vnd.github.squirrel-girl-preview+json'})


def post_issue_comment_reaction(comment_id, content):
    return authenticated_request.post_with_custom_headers('/repos/rcorreia/pytest-template/issues/comments/' + comment_id + '/reactions',
                                                          {'Accept': 'application/vnd.github.squirrel-girl-preview+json'}, {'content': content})


def delete_issue_comment_reaction(reaction_id):
    reactions_uri = '/reactions/' + str(reaction_id)
    return authenticated_request.delete_with_custom_header(reactions_uri,
                                                           {'Accept': 'application/vnd.github.squirrel-girl-preview+json'})
