import pytest
import api.search as search


@pytest.mark.flaky(max_runs=3, min_passes=1)
class TestUserSearch(object):

    @pytest.mark.loadtest
    def test_unique_username(self):
        response = search.get_search_users_request('patrickromo1')
        assert response['status_code'] == 200
        assert response['body']['total_count'] == 1

    @pytest.mark.loadtest
    def test_correct_login_name(self):
        response = search.get_search_users_request('patrickromo1')
        assert response['status_code'] == 200
        assert response['body']['items'][0]['login'] == 'patrickromo1'

    @pytest.mark.loadtest
    def test_no_username_parameter(self):
        response = search.get_search_users_request('')
        assert response['status_code'] == 422
        assert response['body']['errors'][0]['code'] == 'missing'
        assert response['body']['errors'][0]['field'] == 'q'
        assert response['body']['errors'][0]['resource'] == 'Search'

    @pytest.mark.loadtest
    def test_improbable_username_parameter(self):
        response = search.get_search_users_request('no_user_exists-')
        assert response['status_code'] == 200
        assert response['body']['total_count'] == 0


@pytest.mark.flaky(max_runs=3, min_passes=1)
class TestIssueSearch(object):

    @pytest.mark.loadtest
    def test_search_issue_by_title(self):
        search_query = 'Support for static typing \
            in:title is:issue repo:pytest-dev/pytest'
        response = search.get_search_issues_request(search_query)
        assert response['status_code'] == 200
        assert response['body']['total_count'] == 1
        assert response['body']['items'][0]['title'] == 'Support for static typing'

    @pytest.mark.loadtest
    def test_search_issue_by_body(self):
        search_query = 'naive static analyzer \
            in:body is:issue repo:pytest-dev/pytest'
        response = search.get_search_issues_request(search_query)
        assert response['status_code'] == 200
        assert response['body']['total_count'] == 1
        assert response['body']['items'][0]['title'] == 'Fixture naming convention'

    @pytest.mark.loadtest
    def test_search_issue_by_comment(self):
        search_query = 'We cannot that easily pin stuff in Fedora. \
            in:comment is:issue repo:pytest-dev/pytest'
        response = search.get_search_issues_request(search_query)
        assert response['status_code'] == 200
        assert response['body']['total_count'] == 1
        assert response['body']['items'][0]['title'] == 'Sphinx 2.0.0 compatibility'

    @pytest.mark.loadtest
    def test_search_open_issue_not_found_with_closed_search_query(self):
        search_query = 'Support for static typing \
            in:title is:issue state:closed repo:pytest-dev/pytest'
        response = search.get_search_issues_request(search_query)
        assert response['status_code'] == 200
        assert len(response['body']['items']) == 0
        assert response['body']['total_count'] == 0

    @pytest.mark.loadtest
    def test_search_closed_issue_not_found_with_open_search_query(self):
        search_query = 'Sphinx 2.0.0 compatibility \
            in:title is:issue state:open repo:pytest-dev/pytest'
        response = search.get_search_issues_request(search_query)
        assert response['status_code'] == 200
        assert len(response['body']['items']) == 0
        assert response['body']['total_count'] == 0


@pytest.mark.flaky(max_runs=3, min_passes=1)
class TestPullRequestSearch(object):

    @pytest.mark.loadtest
    def test_search_pr_by_title(self):
        search_query = 'Add example for k flag \
            in:title is:pr repo:pytest-dev/pytest'
        response = search.get_search_issues_request(search_query)
        assert response['status_code'] == 200
        assert response['body']['total_count'] == 1
        assert response['body']['items'][0]['title'] == 'Add example for k flag'

    @pytest.mark.loadtest
    def test_search_pr_by_body(self):
        search_query = 'All this patch does is throwing \
            in:body is:pr repo:pytest-dev/pytest'
        response = search.get_search_issues_request(search_query)
        assert response['status_code'] == 200
        assert response['body']['total_count'] == 1
        assert response['body']['items'][0]['title'] == 'Make pytest.skip work in doctest'

    @pytest.mark.loadtest
    def test_search_pr_by_comment(self):
        search_query = 'im +1 on having match as kwarg and encouraging its usage \
            in:comment is:pr repo:pytest-dev/pytest'
        response = search.get_search_issues_request(search_query)
        assert response['status_code'] == 200
        assert response['body']['total_count'] == 1
        assert response['body']['items'][0]['title'] == 'add matching the error message to pytest.raises'
