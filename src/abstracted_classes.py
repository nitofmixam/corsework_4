from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс для метода получения вакансий"""

    @abstractmethod
    def get_vacancies(self, name_job: str, pages: int):
        pass


class JSONABCSaver(ABC):
    """
    Запись полученных вакансий в файл json и чтение
    """

    @abstractmethod
    def file_writer(self):
        pass

    @abstractmethod
    def file_reader(self):
        pass
