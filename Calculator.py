"""
TODO
"""
import math
import tkinter as tk
from typing import Any, Callable, Iterator, List, Tuple, Union


class CalculatorV2(tk.Frame):
    """
    TODO
    """

    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.grid()

        self.operation: str = ""
        self.reset_screen: bool = False
        self.result: float = 0
        self.number_stored: float = 0

        self._substract_counter: int = 0
        self._multiply_counter: int = 0
        self._division_counter: int = 0
        self._modulo_counter: int = 0

        self.buttons: List[tk.Button] = []

        master.title("Calculator")
        master.resizable(width=False, height=False)

        self.number_screen = tk.StringVar()
        self._screen = tk.Entry(
            self,
            textvariable=self.number_screen,
            state="readonly",
            readonlybackground="black",
            bd=20,
            relief="flat",
            fg="#9FEAF4",
        )
        self._screen.grid(row=1, column=1, columnspan=10, sticky="we")
        self._screen.config(justify="right")
        self.number_screen.set("0")
        self.config_first_button()
        self.config_buttons()

    def press_number(self, num: str) -> None:
        if (
            self.number_screen.get() == "0"
            and num not in "0."
            and not self.number_screen.get().count(".")
        ):
            self.number_screen.set("")

        if self.reset_screen:
            self.number_screen.set(num)
            self.reset_screen = False

        else:
            if (
                num not in "0."
                or (num == "0" and self.number_screen.get() != "0")
                or (num == "." and not self.number_screen.get().count("."))
            ):
                self.number_screen.set(self.number_screen.get() + num)

    def add_func(self) -> None:
        num: str = self.number_screen.get()
        if "." in num:
            self.result += float(num)

        else:
            self.result += int(num)
        self.operation = "+"
        self.reset_screen = True
        self.number_screen.set(self.result)

    def substract_func(self) -> None:
        num: str = self.number_screen.get()
        if num != "-":
            number: float = float(num)
            if not self._substract_counter:
                if self.number_screen.get() == "0":
                    self.number_screen.set("-")
                    return
                else:
                    self.number_stored = number

            else:
                if self._substract_counter == 1:
                    self.result = self.number_stored - number

                else:
                    self.result -= number

                self.number_screen.set(self.result)

            self._substract_counter += 1
            self.operation = "-"
            self.reset_screen = True

    def factorial_func(self) -> None:
        num: str = self.number_screen.get()
        try:
            number: float = float(num) if num.endswith(".0") else int(num)

        except ValueError:
            self.number_screen.set("USE ONLY INTEGRAL VALUES")

        else:
            if number >= 0:
                self.number_screen.set(math.factorial(number))

            else:
                self.number_screen.set("YOU BROKE IT, IDIOT")

        self.reset_screen = True

    def multiply_func(self) -> None:
        number: float = float(self.number_screen.get())
        if not self._multiply_counter:
            self.number_stored = number

        else:
            self.result = self.number_stored * number
            self.number_screen.set(self.result)

        self._multiply_counter += 1
        self.operation = "*"
        self.reset_screen = True

    def division_func(self) -> None:
        number: float = float(self.number_screen.get())
        if not self._division_counter:
            self.number_stored = number

        else:
            if self._division_counter == 1:
                self.result = self.number_stored / number

            else:
                self.result /= number

            self.number_screen.set(self.result)

        self._division_counter += 1
        self.operation = "/"
        self.reset_screen = True

    def modulo_func(self) -> None:
        number: float = float(self.number_screen.get())
        if not self._modulo_counter:
            self.number_stored = number

        else:
            if self._modulo_counter == 1:
                self.result = self.number_stored % number

            else:
                self.result %= number

            self.number_screen.set(self.result)

        self._modulo_counter += 1
        self.operation = "%"
        self.reset_screen = True

    def sqrt_func(self) -> None:
        number: float = float(self.number_screen.get())
        if number >= 0:
            self.number_screen.set(math.sqrt(number))

        else:
            number = math.sqrt(abs(number))
            self.number_screen.set(f"{number}j")

        self.reset_screen = True

    def square_func(self) -> None:
        number: float = float(self.number_screen.get())
        self.number_screen.set(number ** 2)
        self.reset_screen = True

    def trigonometric_func(self, function: Callable[[float], float]) -> None:
        number: float = float(self.number_screen.get())
        self.number_screen.set(function(number))
        self.reset_screen = True

    ##############################################

    def results(self) -> None:
        number: float = float(self.number_screen.get())
        operation_done: str = self.operation
        if operation_done == "+":
            self.number_screen.set(self.result + number)
            self.result = 0

        elif operation_done == "-":
            self.number_screen.set(self.number_stored - number)
            self._substract_counter = 0

        elif operation_done == "*":
            self.number_screen.set(self.number_stored * number)
            self._multiply_counter = 0

        elif operation_done == "/":
            self.number_screen.set(self.number_stored / number)
            self._division_counter = 0

        elif operation_done == "%":
            self.number_screen.set(self.number_stored % number)
            self._modulo_counter = 0

        self.number_stored = 0
        self.operation = ""

    def reset(self) -> None:
        self.result = 0
        self.number_stored = 0

        self._substract_counter = 0
        self._multiply_counter = 0
        self._division_counter = 0
        self._modulo_counter = 0

        self.number_screen.set("0")

    def config_first_button(self) -> None:
        self.buttons.append(
            tk.Button(self, text="AC", command=self.reset, bg="#252440", fg="white")
        )
        self.buttons[0].config(height=4, width=8)
        self.buttons[0].grid(row=2, column=0, columnspan=3, ipadx=33)

    def config_buttons(self) -> None:
        symbols: List[str] = [
            "√n",
            "n!",
            "%",
            "7",
            "8",
            "9",
            "➗",
            "cos(x)",
            "4",
            "5",
            "6",
            "✖",
            "sin(x)",
            "1",
            "2",
            "3",
            "➖",
            "tan(x)",
            "0",
            ".",
            "=",
            "➕",
            "x^2",
        ]

        functions: List[Callable[..., None]] = [
            self.sqrt_func,
            self.factorial_func,
            self.modulo_func,
            self.press_number,
            self.press_number,
            self.press_number,
            self.division_func,
            self.trigonometric_func,
            self.press_number,
            self.press_number,
            self.press_number,
            self.multiply_func,
            self.trigonometric_func,
            self.press_number,
            self.press_number,
            self.press_number,
            self.substract_func,
            self.trigonometric_func,
            self.press_number,
            self.press_number,
            self.results,
            self.add_func,
            self.square_func,
        ]
        parameters: Iterator[Callable[[float], float]] = iter(
            [math.cos, math.sin, math.tan]
        )

        columns: Iterator[int] = iter(
            [3, 4, 5] + [number for _ in range(7) for number in range(1, 6)]
        )

        button_indexes: Iterator[int] = iter(range(1, 24))

        rows: Iterator[int] = iter(
            [2, 2, 2] + [number for number in range(3, 7) for _ in range(5)]
        )

        for symbol, function in zip(symbols, functions):
            if function == self.press_number:
                self.buttons.append(
                    tk.Button(
                        self,
                        text=symbol,
                        bg="#81BEF7",
                        command=lambda parameter=symbol: self.press_number(parameter),
                    )
                )

            elif function == self.trigonometric_func:
                self.buttons.append(
                    tk.Button(
                        self,
                        text=symbol,
                        bg="grey",
                        fg="white",
                        command=lambda function=function, parameter=next(
                            parameters
                        ): function(parameter),
                    )
                )
            else:
                self.buttons.append(
                    tk.Button(
                        self,
                        text=symbol,
                        bg="grey",
                        fg="white",
                        command=lambda function=function: function(),
                    )
                )
            index_of_button: int = next(button_indexes)
            self.buttons[index_of_button].config(height=4, width=8)
            self.buttons[index_of_button].grid(row=next(rows), column=next(columns))


CALCULATOR = tk.Tk()

APP = CalculatorV2(CALCULATOR)

CALCULATOR.mainloop()
