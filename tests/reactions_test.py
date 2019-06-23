import pytest
import api.reactions as reactions


@pytest.mark.flaky(max_runs=3, min_passes=1)
class TestReactions(object):

    @pytest.mark.loadtest
    def test_get_issue_reactions(self):
        response = reactions.get_issue_comment_reaction('476103467')
        assert response['status_code'] == 200
        assert response['body'][0]['content'] == '+1'

    def test_post_issue_reaction(self):
        response = reactions.post_issue_comment_reaction('476103467', 'heart')
        assert response['status_code'] == 201
        assert response['body']['content'] == 'heart'
        response2 = reactions.delete_issue_comment_reaction(response['body']['id'])
        assert response2['status_code'] == 204
