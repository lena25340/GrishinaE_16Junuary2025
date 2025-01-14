import allure
import requests



@allure.id('1')
@allure.feature("API тесты для функционала корзины")
@allure.title("Тест на добавление товара в корзину")
@allure.description("Тест проверят возврат кода 200 при добавления товара в корзину")
@allure.severity('Normal')
def test_search_by_origin():
    response = requests.post(f'https://pizzaroni.ru/cart/recalc3')
    assert response.status_code == 200



@allure.id('2')
@allure.feature("API тесты для функционала корзины.")
@allure.title("Тест на удаление товара из корзины.")
@allure.description('Тест проверят возврат кода 200 при отправке запроса удаление товара из корзины')
@allure.severity('Normal')
def test_search_by_popularcities():
    response = requests.delete('https://pizzaroni.ru/cart/recalc3')
    assert response.status_code == 200

