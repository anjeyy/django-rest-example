import pytest

from rest_api.models import Document


# testsuite creates own test-database
@pytest.mark.django_db(databases=['default'])
def test_get_all_docs(client):
    documents = Document.objects.all()
    assert documents.count() == 0
