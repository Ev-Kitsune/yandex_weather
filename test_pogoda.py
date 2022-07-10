import pytest
import meta
import lib

settings = meta.Setting()
driver = settings.initDriver('C:\\v-code\\chromedriver.exe')
weather = lib.Weather(driver)
header = lib.Header(driver)
standart = lib.Standart(driver)


def setup_module(module): ## Перед тестовым прогоном
    settings.mainPth = 'https://yandex.ru/pogoda'

def teardown_module(module): ## После тестового прогона
    driver.quit()

def setup_function(function): ## Перед каждым тестом
    driver.get(settings.mainPth)
    
def teardown_function(function): ## После каждого теста
    driver.refresh()

# Сами тесты

# @pytest.mark.parametrize("request",
# [
# ("Test"),
# ("TEST"),
# ("test"),
# ("123"),
# ('Москва'),
# ('Самара'),
# ('Санкт'),
# ('Белг'),
# ])
# def test_searchPositive(request):
#     assert header.search_play(request, meta.Keys) is True




# Положительные тесты
def test_next10Day():
    """
    Тестирование на переход в раздел "прогноз на 10 дней"

    1. Открыть yandex.ru/pogoda
    2. Нажать на кнопку "прогноз на 10 дней"
    3. Дождаться загрузки

    ОР: 
    1. Загрузилась страница с прогнозами
    2. На странице 10 блоков с информацией о прогнозе погоды на следующие 10 дней
    """
    # Загрузилась страница с прогнозами клик удачный
    assert weather.open_page_10_days() is True

    # На странице 10 блоков с информацией о прогнозе погоды на следующие 10 дней
    assert weather.check_prognoz(10, 'div.forecast-details__day') is True



# def test_market():
#     assert weather.open_page_10_days() is True
#     assert weather.check_prognoz(2, 'article.card_without-card-decoration') is True

# def test_next_mounth():
#     res = header.select_items(1)
#     if res == True:
#         assert res is True
#     else:
#         standart.make_scr('test')
#         assert res is True

#     res = weather.next_30_days()
#     if res == True:
#         assert res is True
#     else:
#         standart.make_scr('test')
#         assert res is True





