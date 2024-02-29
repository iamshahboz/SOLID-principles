# you should not do

from abc import ABC, abstractmethod 

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass 

    @abstractmethod
    def fax(self, document):
        pass 

    @abstractmethod
    def scan(self, document):
        pass 

class OldPrinter(Printer):
    def print(self, document):
        print(f'Printing {document} in color...')

    def fax(self, document):
        print(f'Faxing {document} ...')
    
    def scan(self, document):
        print(f'Scanning {document} ...')

# In this example, the base class Printer provides the interface that its subclasses must
# implement. OldPrinter inherits from Printer  and must implement the same interface.
# However, OldPrinter does not use .fax() and .scan() methods because this type of 
# printer does not support these functionalities. This implementation violates. 

