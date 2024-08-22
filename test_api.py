import requests
import allure 


@allure.title("Поиск фильма по названию на кириллице") 
@allure.description("Тест проверяет поиск фильма по названию на кириллице")  
@allure.severity("критический")
def test_search_by_id(): 
    with allure.step("Создание хедеров"):    
        json = { 
      "X-API-KEY": "EZV01TV-TCFMMH7-HJEW9P1-4QJB16P" 
    }
    with allure.step("отправка запроса "):     
        response = requests.get("https://api.kinopoisk.dev/v1.4/movie/535341", headers=json)    
    with allure.step("Проверка результата"):   
        assert response.status_code == 200


def test_search_by_name(): 
    with allure.step("Создание хедеров"):  
        json = { 
      "X-API-KEY": "EZV01TV-TCFMMH7-HJEW9P1-4QJB16P" 
    }
    with allure.step("отправка запроса "):
        response = requests.get("https://api.kinopoisk.dev/v1.4/movie/search?limit=10&query=1%2B1", headers=json)    
    with allure.step("Проверка результата"):   
        assert response.status_code == 200


def test_search_by_ganre(): 
    with allure.step("Создание хедеров"): 
        json = { 
      "X-API-KEY": "EZV01TV-TCFMMH7-HJEW9P1-4QJB16P" 
    }
    with allure.step("отправка запроса "):
        response = requests.get("https://api.kinopoisk.dev/v1/movie/possible-values-by-field?field=type", headers=json)    
    with allure.step("Проверка результата"):
        assert response.status_code == 200


def test_search_by_ganre_negative(): 
    with allure.step("Создание хедеров"): 
        json = { 
      "X-API-KEY": "EZV01TV-TCFMMH7-HJEW9P1-4QJB16P" 
    }
    with allure.step("отправка запроса "):
        response = requests.get("https://api.kinopoisk.dev/v1/movie/possible-values-by-field", headers=json)    
    with allure.step("Проверка результата"):
        assert response.status_code == 400


def test_search_by_id_negative(): 
    with allure.step("Создание хедеров"):
        json = { 
      "X-API-KEY": "EZV01TV-TCFMMH7-HJEW9P1-4QJB16P" 
    }
    with allure.step("отправка запроса "):
       response = requests.get("https://api.kinopoisk.dev/v1.4/movie/5353414", headers=json)    
    with allure.step("Проверка результата"):   
       assert response.status_code == 404