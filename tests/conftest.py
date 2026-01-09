import pytest
from faker import Generator
from faker_ru_pii import (
    PassportProvider,
    RuResidencePermitProvider,
    RuForeignPassportProvider
)


@pytest.fixture
def passport_provider() -> PassportProvider:
    return PassportProvider(generator=Generator())


@pytest.fixture
def residence_permit_provider() -> RuResidencePermitProvider:
    return RuResidencePermitProvider(generator=Generator())


@pytest.fixture
def foreign_passport_provider() -> RuForeignPassportProvider:
    return RuForeignPassportProvider(generator=Generator())


@pytest.fixture(autouse=True)
def num_samples(request):
    try:
        num = int(request.cls.num_samples)
    except AttributeError:
        num = 100
    return num
