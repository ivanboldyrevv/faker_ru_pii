from faker import Faker
from faker_ru_pii.ru_passport_provider import PassportProvider
from faker_ru_pii.ru_residence_permit_provider import RuResidencePermitProvider
from faker_ru_pii.ru_foreign_passport_provider import RuForeignPassportProvider
from faker_ru_pii.ru_birth_certificate_provider import RuBirthCertificateProvider
from faker_ru_pii.ru_driver_license import RuDriverLicenseProvider

providers = [
    PassportProvider,
    RuResidencePermitProvider,
    RuForeignPassportProvider,
    RuBirthCertificateProvider,
    RuDriverLicenseProvider
]

__all__ = providers

faker = Faker("ru_RU")

for provider in providers:
    faker.add_provider(provider)
