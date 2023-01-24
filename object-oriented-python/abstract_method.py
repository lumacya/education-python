from abc import ABC, abstractmethod

class ChessPiece(ABC):

    # обший метод, который будут использовать все наследники этого класса
    def draw(self):
        print("Drew a chess piece")

    # абстрактный метод, который будет необходимо переопределить для каждого подкласса
    @abstractmethod
    def passmove(self):
        pass
