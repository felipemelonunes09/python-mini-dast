from abc import ABC, abstractmethod

class Scanner(ABC):

    @abstractmethod
    def start_scan(self, urls):
        pass

    @abstractmethod
    def get_results():
        pass