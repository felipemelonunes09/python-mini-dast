from abc import ABC, abstractmethod
from shared.Singleton import SingletonMeta 

class Database(ABC, metaclass=SingletonMeta):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def get_session(self):
        pass
    
    @abstractmethod
    def get_engine(self):
        pass