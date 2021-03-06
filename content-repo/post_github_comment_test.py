from post_github_comment import get_post_url, get_link_for_doc_file, ROOT_DIR, get_link_for_ref_file
from pytest_mock import MockerFixture
import os


def test_get_post_url_env(mocker: MockerFixture):
    mocker.patch.dict(os.environ, {'CIRCLE_PULL_REQUEST': 'https://github.com/demisto/content-docs/pull/9'})
    assert get_post_url() == 'https://api.github.com/repos/demisto/content-docs/issues/9/comments'


def test_get_post_url_comment(mocker: MockerFixture):
    mocker.patch('subprocess.check_output', return_value='Update docs (#1111)')
    assert get_post_url() == 'https://api.github.com/repos/demisto/content-docs/issues/1111/comments'


def test_get_link_for_doc_file():
    (name, url) = get_link_for_doc_file("http://localhost", f"{ROOT_DIR}/docs/integrations/code-conventions.md")
    assert name == "Python Code Conventions"
    assert url == "http://localhost/docs/integrations/code-conventions"


def test_get_link_for_ref_file():
    (name, url) = get_link_for_ref_file("http://localhost", f"{ROOT_DIR}/content-repo/extra-docs/releases/20.12.0.md")
    assert name == "Content Release 20.12.0"
    assert url == "http://localhost/docs/reference/releases/20.12.0"
    (name, url) = get_link_for_ref_file("http://localhost", f"{ROOT_DIR}/content-repo/extra-docs/integrations/syslog.md")
    assert name == "Syslog"
    assert url == "http://localhost/docs/reference/integrations/syslog"
