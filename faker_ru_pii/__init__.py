from faker import Faker
from faker_ru_pii.ru_passport_provider import PassportProvider
from faker_ru_pii.ru_residence_permit_provider import RuResidencePermitProvider


providers = [
    PassportProvider,
    RuResidencePermitProvider
]

faker = Faker("ru_RU")

for provider in providers:
    faker.add_provider(provider)
