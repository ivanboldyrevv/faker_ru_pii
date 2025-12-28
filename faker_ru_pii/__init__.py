from faker import Faker
from faker_ru_pii.ru_passport_provider import PassportProvider

faker = Faker("ru_RU")
faker.add_provider(PassportProvider)
