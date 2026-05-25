from abc import ABC, abstractmethod

class BaseAdapter(ABC):
    @abstractmethod
    def chat(self, messages, tools=None):
        pass