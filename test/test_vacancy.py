import pytest

from src.vacancy import Vacancy, Vacancies


@pytest.fixture
def vacancy():
    """Образец вакансии"""
    return Vacancy(
        vacancy_title="Python Developer",
        town="Москва",
        salary_from=100000,
        salary_to=150000,
        employment="Полная занятость",
        url="https://example.com/job/123"
    )


@pytest.fixture
def vacancies_list():
    """Образец списка вакансии"""
    vacancy1 = Vacancy("Работа A", "Город A", 50000,
                       70000, "Полная занятость", "url_a")
    vacancy2 = Vacancy("Работа B", "Город B", 80000,
                       100000, "Частичная занятость", "url_b")
    vacancy3 = Vacancy("Работа C", "Город C", 60000,
                       90000, "Remote", "url_c")
    return [vacancy1, vacancy2, vacancy3]


# Tests for Vacancy class

def test_vacancy_str(vacancy):
    expected_str = (
        "название вакансии: Python Developer\n"
        "город: Москва\n"
        "зарплата от: 100000\n"
        "зарплата до: 150000\n"
        "тип занятости: Полная занятость\n"
        "ссылка на вакансию: https://example.com/job/123\n"
    )
    assert str(vacancy) == expected_str


def test_vacancy_equality(vacancy):
    same_vacancy = Vacancy(
        "Python Developer", "Москва", 100000, 150000,
        "Полная занятость", "https://example.com/job/123"
    )
    different_vacancy = Vacancy(
        "Java Developer", "Москва", 80000, 120000,
        "Полная занятость", "https://example.com/job/456"
    )
    assert vacancy == same_vacancy
    assert vacancy != different_vacancy


def test_vacancy_comparison(vacancy):
    lower_salary_vacancy = Vacancy(
        "Java Developer", "Москва", 80000, 120000, "Полная занятость",
        "https://example.com/job/456"
    )
    higher_salary_vacancy = Vacancy(
        "Data Scientist", "Москва", 120000, 180000, "Полная занятость",
        "https://example.com/job/789"
    )
    assert vacancy > lower_salary_vacancy
    assert vacancy < higher_salary_vacancy
    assert vacancy >= lower_salary_vacancy
    assert vacancy <= higher_salary_vacancy


def test_vacancy_to_dict(vacancy):
    expected_dict = {
        'vacancy_title': "Python Developer",
        'town': "Москва",
        'salary_from': 100000,
        'salary_to': 150000,
        'employment': "Полная занятость",
        'url': "https://example.com/job/123"
    }
    assert vacancy.to_dict() == expected_dict


def test_vacancy_from_dict(vacancy):
    vacancy_dict = vacancy.to_dict()
    new_vacancy = Vacancy.from_dict(vacancy_dict)
    assert vacancy == new_vacancy


def test_vacancies_add_and_delete(vacancies_list):
    vacancies = Vacancies()
    vacancies.add_vacancies(vacancies_list)
    assert len(vacancies.all_vacancies) == 3
    vacancies.delete_vacancies([vacancies_list[0]])
    assert len(vacancies.all_vacancies) == 2
    assert vacancies_list[0] not in vacancies.all_vacancies


def test_vacancies_sort(vacancies_list):
    vacancies = Vacancies()
    vacancies.add_vacancies(vacancies_list)
    vacancies.sort_vacancies_by_salary()
    assert vacancies.all_vacancies[0].salary_from == 80000
    assert vacancies.all_vacancies[-1].salary_from == 50000


def test_vacancies_to_list_dict(vacancies_list, vacancy):
    vacancies = Vacancies()
    vacancies.add_vacancies(vacancies_list)
    vacancy_dicts = vacancies.to_list_dict()
    assert len(vacancy_dicts) == 3
    assert all(isinstance(vacancy, dict) for vacancy in vacancy_dicts)
