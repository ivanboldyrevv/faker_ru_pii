import pytest
from faker import Generator
from faker_ru_pii import PassportProvider


@pytest.fixture
def passport_provider() -> PassportProvider:
    return PassportProvider(generator=Generator())


@pytest.fixture(autouse=True)
def num_samples(request):
    try:
        num = int(request.cls.num_samples)
    except AttributeError:
        num = 100
    return num
