### PII labels
That labels implemented in lib:

- [X] full name of the employee in one field
- [X] lastname of the employee
- [X] client full name in one field
- [X] client lastname
- [X] client name
- [X] client middle name
- [X] date of birth
- [?] place of birth
- [X] nationality (текст)
- [X] passport department code (PassportProvider.department_code)
- [X] the authority that issued the passport (PassportProvider.passport_issuing_authority)
- [X] passport series (PassportProvider.passport_series)
- [X] passport number (PassportProvider.passport_number)
- [X] passport details in one field (PassportProvider.passport_full)
- [X] passport series + number in one field (PassportProvider.passport_series_number)
- [X] номер вида на жительство (RuResidencePermitProvider.residence_permit_number) ?
- [X] Серия + номер вида на жительство (RuResidencePermitProvider.residence_permit_full) ?
- [X] Серия вида на жительство (RuResidencePermitProvider.residence_permit_serial) ?

#### Загранпаспорт РФ
- [X] номер загранпаспорта (Старый формат загранпаспорта)
- [X] серия загранпаспорта (Старый формат)
- [X] Номер загранпаспорта (Старый / новый формат)
- [X] Серия + номер загранпаспорта (Старый / новый формат)

#### Свидетельство о рождении
- [X] серия свидетельства о рождении
- [X] номер свидетельства о рождении
- [X] Серия + номер свидетельства о родении


#### Водительское удостоверение
- [ ] номер водительского удостоверения
- [ ] Серия + номер водительского удостоверения

- [ ] разрешение на работу / визу
- [x] СНИЛС
- [ ] Номер миграционной карты
- [ ] Серия + номер миграционной карты
- [ ] Универсальная маска для ДУЛ
- [x] Teкст адреса регистрации по паспорту
- [x] Текст адреса места жительства фактический
- [ ] квартира/офис
- [x] строение
- [x] дом
- [x] Улица и т.п.
- [ ] Различные элементы адреса ФЛ в одном поле
- [x] email
- [x] номер телефона
- [ ] Номера телефонов и электронной почты в не нормализованном виде
- [ ] Наименование учебного заведения
- [ ] серия диплома/сертификата после 2014 года
- [ ] серия диплома/сертификата до 2014 года
- [ ] номер диплома/сертификата
- [x] название организации
- [ ] Сведения о номере серии и дате выдачи трудовой книжки
- [ ] военный билет
- [ ] свидетельство о браке
- [ ] Кадастровый номер объекта залога
- [ ] Идентификатор земельного участка
- [x] номер машины
- [x] Полный номер платежной карты
- [ ] Имя держателя карты
- [ ] реквизиты организации ЮЛ
- [ ] ОКПО
- [X] ИНН
- [X] ОГРН
- [ ] ОКОГУ
- [X] Структура данных (xml json и т.д) **Пока только JSON. Нужно добавить XML**
- [ ] Поля с комментариями (пользовательские)
- [ ] Поля с описанием платежа
- [ ] Поля с произвольным содержанием