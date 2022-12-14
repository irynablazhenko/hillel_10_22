class Company:
    contact_person = 'Head of Company'
    count = 0  # счетчик компаний
    amount = []
    """Инициализация эллементов класа"""

    def __init__(self, name, year, rate, phone, price):
        self.name = name
        self.year = year
        self.rate = rate
        self.phone = phone
        self.price = price
        Company.count += 1
        Company.amount.append(price)

    """Изменение всех данных компании"""

    def change_data(self, new_name, new_year, new_rate, new_phone, new_price):
        self.name = new_name
        self.name = new_name
        self.year = new_year
        self.rate = new_rate
        self.phone = new_phone
        self.price = new_price

    """Вывод информации о компании"""

    def print_conpany_info(self):
        print(f'Название компании: {self.name},\nгод основания: {self.year},\nрейтинг: {self.rate},\nномер телефона: '
              f'{self.phone},\nконтактное лицо: {Company.contact_person}\n')

    """Расчет среднего рейта компаний"""
    @staticmethod
    def get_rate_avg(*rate: list):
        summ = sum(rate[0])
        avg = round(summ / Company.count,2)
        print(f'Средний рейт компаний: {avg}')
        return avg

    """Расчет среднего дохода компаний компаний"""
    @staticmethod
    def get_price_avg(*price: list):
        summ = sum(price[0])
        avg = round(summ / Company.count)
        print(f'Средний доход компаний: {avg}')
        return avg

    """Опциональное поле - описание компании"""

    @classmethod
    def set_description(cls, description):
        cls.description = description

    """Расчет ожидаемого дохода при приросте компаний в указанном %"""

    @classmethod
    def predict_amount(cls, increase, *price: list):
        avg_amount = sum(price[0]) / Company.count
        predict_amount = round(Company.count * (increase + 1) * avg_amount)
        print(f'Ожидаемый доход при приросте компаний на {increase} раз составит: {predict_amount}$')
        return predict_amount
