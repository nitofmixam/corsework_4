import pytest
from unittest.mock import patch

from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy


@pytest.fixture
def hh_api():
    """Создание экземпляра HHApi"""
    return HeadHunterAPI()


@patch('requests.get')
def test_get_vacancies_success(mock_get, hh_api):
    """Получение вакансий"""
    mock_response = {
        'items': [
            {
                'name': 'Работа',
                'area': {'name': 'Москва'},
                'salary': {'from': 50000, 'to': 100000},
                'employment': {'name': 'Полная занятость'},
                'alternate_url': 'https://hh.ru/vacancy/12345678'
            }
        ]
    }
    mock_get.return_value.json.return_value = mock_response

    vacancies = hh_api.get_vacancies('python', 1)

    assert len(vacancies) == 1
    assert isinstance(vacancies[0], Vacancy)
    assert vacancies[0].vacancy_title == "Работа"
    assert vacancies[0].town == "Москва"
    assert vacancies[0].salary_from == 50000
    assert vacancies[0].salary_to == 100000
    assert vacancies[0].employment == 'Полная занятость'
    assert vacancies[0].url == 'https://hh.ru/vacancy/12345678'


@patch('requests.get')
def test_get_vacancies_empty(mock_get, hh_api):
    mock_response = {'items': []}
    mock_get.return_value.json.return_value = mock_response

    vacancies = hh_api.get_vacancies('python', 1)

    assert len(vacancies) == 0


@patch('requests.get')
def test_get_vacancies_no_salary(mock_get, hh_api):
    mock_response = {
        'items': [
            {
                'name': 'Работа',
                'area': {'name': 'Москва'},
                'salary': None,
                'employment': {'name': 'Полная занятость'},
                'alternate_url': 'https://hh.ru/vacancy/12345678'
            }
        ]
    }
    mock_get.return_value.json.return_value = mock_response

    vacancies = hh_api.get_vacancies('python', 1)

    assert vacancies[0].salary_from == 0
    assert vacancies[0].salary_to == 0
