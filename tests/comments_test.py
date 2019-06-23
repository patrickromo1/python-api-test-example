import pytest
import api.comments as comments


@pytest.mark.flaky(max_runs=3, min_passes=1)
class TestComments(object):

    @pytest.mark.loadtest
    def test_get_issue_comment(self):
        response = comments.get_issue_comments('17')
        assert response['status_code'] == 200
        assert response['body'][0]['body'] == 'Hi I am a comment for reaction\'s api POST requests. '
