import pytest

from rest_api.serializers import DocumentSerializer


@pytest.mark.unit
def test_valid_model():
    document_serializer = DocumentSerializer(data={"title": "pytest",
                                                   "person": "python3",
                                                   "file_size": -2048})
    assert document_serializer.is_valid() == True


@pytest.mark.unit
def test_invalid_model():
    document_serializer = DocumentSerializer(data={"title": "pytest",
                                                   "person": 204,
                                                   "file_size": "fake number"})
    assert document_serializer.is_valid() == False
