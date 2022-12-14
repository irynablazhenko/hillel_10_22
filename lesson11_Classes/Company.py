class Company:
    contact_person = 'Head of Company'  # Принято правиласи компании, что контактное лицо должно быть всегда Head of Company
    count = 0  # счетчик компаний
    amount = []

    def __init__(self, name, year, rate, phone, price):
        """Инициализация эллементов класа"""
        self.name = name
        self.year = year
        self.rate = rate
        self.phone = phone
        self.price = price
        Company.count += 1
        Company.amount.append(price)

    def change_data(self, new_data: dict):
        """Изменение данных компании"""
        print(new_data)
        if new_data.get('name'):
            self.name = new_data.get('name')
        if new_data.get('year'):
            self.year = new_data.get('year')
        if new_data.get('rate'):
            self.rate = new_data.get('rate')
        if new_data.get('phone'):
            self.phone = new_data.get('phone')
        if new_data.get('price'):
            self.price = new_data.get('price')


    def print_conpany_info(self):
        """Вывод информации о компании"""
        print(f'Название компании: {self.name},\nгод основания: {self.year},\nрейтинг: {self.rate},\nномер телефона: '
              f'{self.phone},\nконтактное лицо: {Company.contact_person},\nдоход от компании: {self.price}\n')

    @staticmethod
    def get_rate_avg(*rate: list):
        """Расчет среднего рейта компаний"""
        summ = sum(rate[0])
        avg = round(summ / Company.count, 2)
        print(f'Средний рейт компаний: {avg}')
        return avg

    @staticmethod
    def get_price_avg(*price: list):
        """Расчет среднего дохода компаний компаний"""
        summ = sum(price[0])
        avg = round(summ / Company.count)
        print(f'Средний доход компаний: {avg}')
        return avg

    @classmethod
    def predict_amount(cls, increase, *price: list):
        """Расчет ожидаемого дохода при приросте компаний в указанном %"""
        avg_amount = sum(price[0]) / Company.count
        predict_amount = round(Company.count * (increase + 1) * avg_amount)
        print(f'Ожидаемый доход при приросте компаний на {increase} раз составит: {predict_amount}$\n')
        return predict_amount
