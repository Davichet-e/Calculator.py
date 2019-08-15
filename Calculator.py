"""
A basic calculator made with tkinter library,
inspired by @pildorasinformaticas and made by @Davichet-e
"""
import math
import cmath
import tkinter as tk
from typing import Callable, Iterator, List, Tuple, Union


class Calculator:
    """
    Basic tkinter calculator
    """

    def __init__(self, master=None) -> None:
        self._frame: tk.Frame = tk.Frame(master=master)
        self._frame.grid()

        self._operation: str = ""
        self._reset_screen: bool = False
        self._result: Union[float, complex] = 0
        self._number_stored: Union[float, complex] = 0

        self._substract_counter: int = 0
        self._multiply_counter: int = 0
        self._division_counter: int = 0
        self._modulo_counter: int = 0

        self._buttons: List[tk.Button] = []

        master.title("Calculator")
        master.resizable(width=False, height=False)

        self._number_screen = tk.StringVar()
        self._operation_str_var = tk.StringVar()
        self._screen = tk.Entry(
            self._frame,
            textvariable=self._number_screen,
            state="readonly",
            readonlybackground="black",
            bd=20,
            relief="flat",
            fg="#9FEAF4",
        )
        self._screen2 = tk.Entry(
            self._frame,
            textvariable=self._operation_str_var,
            state="readonly",
            width=4,
            readonlybackground="black",
            bd=20,
            relief="flat",
            fg="#9FEAF4",
        )

        self._screen2.grid(row=0, column=0, sticky="e")
        self._screen2.config(justify="left")

        self._screen.grid(row=0, column=1, columnspan=5, sticky="we")
        self._screen.config(justify="right")

        self._number_screen.set("0")
        self._config_buttons()

    @property
    def _number_on_screen(self) -> Union[float, complex]:
        number: str = self._number_screen.get()
        # I considered to use ast.literal_eval for safety reasons,
        # but since I manage the input, for performance reasons,
        # I prefer using the built-in eval function
        return eval(number)

    def _press_number(self, num: str) -> None:
        number_on_screen: str = self._number_screen.get()

        if (
            number_on_screen == "0"
            and num not in "0."
            and not number_on_screen.count(".")
        ):
            self._number_screen.set("")
            self._operation_str_var.set("")

            # Update the changes on the screen
            number_on_screen = self._number_screen.get()

        if self._reset_screen:
            self._number_screen.set(num)
            self._operation_str_var.set("")
            self._reset_screen = False

        else:
            if (
                num not in "0."
                or (num == "0" and number_on_screen != "0")
                or (num == "." and not number_on_screen.count("."))
            ):
                self._number_screen.set(number_on_screen + num)

    def _add_func(self) -> None:
        number: Union[float, complex] = self._number_on_screen

        self._result = number + self._number_stored

        self._operation_str_var.set("+")

        self._operation = "+"
        self._reset_screen = True
        self._number_screen.set(self._result)

    def _sign_func(self):
        num: str = self._number_screen.get()
        if "-" in num:
            self._number_screen.set(num.strip("-"))

        else:
            self._number_screen.set("-" + num)

    def _substract_func(self) -> None:
        screen_display: str = self._number_screen.get()
        if screen_display == "-":
            return

        number: Union[float, complex] = self._number_on_screen

        self._operation_str_var.set("-")

        if self._substract_counter == 0:
            self._number_stored = number

        else:
            self._result -= number
            self._number_screen.set(self._result)

        self._substract_counter += 1
        self._operation = "-"
        self._reset_screen = True

    def _factorial_func(self) -> None:
        number: Union[float, complex] = self._number_on_screen

        self._operation_str_var.set("n!")

        if isinstance(number, float):
            # See https://es.wikipedia.org/wiki/Funci%C3%B3n_gamma
            self._number_screen.set(math.gamma(number + 1))

        elif isinstance(number, int):
            self._number_screen.set(math.factorial(number))

        else:
            self._number_screen.set("USE ONLY REAL NUMBERS")

        self._reset_screen = True

    def _multiply_func(self) -> None:
        number: Union[float, complex] = self._number_on_screen

        self._operation_str_var.set("x")
        if not self._multiply_counter:
            self._number_stored = number

        else:
            self._result = self._number_stored * number
            self._number_screen.set(self._result)

        self._multiply_counter += 1
        self._operation = "*"
        self._reset_screen = True

    def _division_func(self) -> None:
        number: Union[float, complex] = self._number_on_screen

        self._operation_str_var.set("➗")
        if not self._division_counter:
            self._number_stored = number

        else:
            if self._division_counter == 1:
                self._result = self._number_stored / number

            else:
                self._result /= number

            self._number_screen.set(self._result)

        self._division_counter += 1
        self._operation = "/"
        self._reset_screen = True

    def _modulo_func(self) -> None:
        number: Union[float, complex] = self._number_on_screen

        if isinstance(number, complex):
            self._number_screen.set("MOD OPERATOR NOT DEFINED FOR COMPLEX NUMBERS")
            return

        self._operation_str_var.set("%")
        if not self._modulo_counter:
            self._number_stored = number

        else:

            if self._modulo_counter == 1:
                self._result = self._number_stored % number

            else:
                self._result %= number

            self._number_screen.set(self._result)

        self._modulo_counter += 1
        self._operation = "%"
        self._reset_screen = True

    def _sqrt_func(self) -> None:
        number: Union[float, complex] = self._number_on_screen
        self._operation_str_var.set("√n")

        if isinstance(number, complex) or number < 0:
            self._number_screen.set(cmath.sqrt(number))

        else:
            self._number_screen.set(math.sqrt(number))

        self._reset_screen = True

    def _inverse_func(self) -> None:
        number: Union[float, complex] = self._number_on_screen
        self._operation_str_var.set("1/x")
        self._number_screen.set(1 / number)

        self._reset_screen = True

    def _square_func(self) -> None:
        number: Union[float, complex] = self._number_on_screen

        self._operation_str_var.set("x^2")

        self._number_screen.set(number ** 2)
        self._reset_screen = True

    def _logarithmic_func(self) -> None:
        number: Union[float, complex] = self._number_on_screen

        self._operation_str_var.set("ln(x)")

        if isinstance(number, complex):
            self._number_screen.set(cmath.log(number))
        else:
            if number > 0:
                self._number_screen.set(math.log(number))
            else:
                self._number_screen.set("USE ONLY POSITIVE NUMBERS")

        self._reset_screen = True

    def _trigonometric_func(self, function: str) -> None:
        self._operation_str_var.set("trig func")
        number: Union[float, complex] = self._number_on_screen

        # Depending on if it's a complex number, use the appropriate library
        if isinstance(number, complex):
            self._number_screen.set(getattr(cmath, function)(number))
        else:
            self._number_screen.set(getattr(math, function)(number))

        self._reset_screen = True

    ##############################################
    def _constants(self, constant: float) -> None:
        self._number_screen.set(constant)
        self._reset_screen = True

    ##############################################

    def _results(self) -> None:
        number: Union[float, complex] = self._number_on_screen

        operation_done: str = self._operation

        res: Union[float, complex] = number

        if operation_done == "+":
            res = self._result + number
            self._result = 0

        elif operation_done == "-":
            res = self._number_stored - number
            self._substract_counter = 0

        elif operation_done == "*":
            res = self._number_stored * number
            self._multiply_counter = 0

        elif operation_done == "/":
            res = self._number_stored / number
            self._division_counter = 0

        elif operation_done == "%":
            res = self._number_stored % number
            self._modulo_counter = 0

        self._number_screen.set(res)

        self._number_stored = 0
        self._operation = ""

    def _reset(self) -> None:
        self._result = 0
        self._number_stored = 0

        self._substract_counter = 0
        self._multiply_counter = 0
        self._division_counter = 0
        self._modulo_counter = 0

        self._number_screen.set("0")
        self._operation_str_var.set("")

    def _config_buttons(self) -> None:

        functions_with_it_symbol: List[Tuple[Callable[..., None], str]] = [
            (self._constants, "π"),
            (self._reset, "AC"),
            (self._sqrt_func, "√n"),
            (self._factorial_func, "n!"),
            (self._modulo_func, "%"),
            (self._constants, "e"),
            (self._press_number, "7"),
            (self._press_number, "8"),
            (self._press_number, "9"),
            (self._division_func, "➗"),
            (lambda: self._trigonometric_func("cos"), "cos(x)"),
            (self._inverse_func, "1/x"),
            (self._press_number, "4"),
            (self._press_number, "5"),
            (self._press_number, "6"),
            (self._multiply_func, "✖"),
            (lambda: self._trigonometric_func("sin"), "sin(x)"),
            (self._sign_func, "±"),
            (self._press_number, "1"),
            (self._press_number, "2"),
            (self._press_number, "3"),
            (self._substract_func, "➖"),
            (lambda: self._trigonometric_func("tan"), "tan(x)"),
            (self._logarithmic_func, "ln(x)"),
            (self._press_number, "0"),
            (self._press_number, "."),
            (self._results, "="),
            (self._add_func, "➕"),
            (self._square_func, "x^2"),
        ]
        constants: Iterator[float] = iter((math.pi, math.e))

        columns: Iterator[int] = iter(
            [0, 1, 3, 4, 5] + [number for _ in range(4) for number in range(6)]
        )

        rows: Iterator[int] = iter(
            [1, 1, 1, 1, 1] + [number for number in range(2, 6) for _ in range(6)]
        )

        button_indexes: Iterator[int] = iter(range(29))

        for function, symbol in functions_with_it_symbol:
            if function == self._press_number:
                self._buttons.append(
                    tk.Button(
                        self._frame,
                        text=symbol,
                        bg="#81BEF7",
                        command=lambda symbol=symbol: self._press_number(symbol),
                    )
                )

            elif function == self._constants:
                self._buttons.append(
                    tk.Button(
                        self._frame,
                        text=symbol,
                        command=lambda constant=next(constants): self._constants(
                            constant
                        ),
                        bg="#8A0808",
                        fg="white",
                    )
                )

            elif function == self._reset:
                self._buttons.append(
                    tk.Button(
                        self._frame,
                        text=symbol,
                        command=self._reset,
                        bg="#252440",
                        fg="white",
                    )
                )
                self._buttons[-1].grid(row=1, column=1, columnspan=2, ipadx=53)
                self._buttons[-1].config(height=4)

            else:
                self._buttons.append(
                    tk.Button(
                        self._frame,
                        text=symbol,
                        bg="#585858",
                        fg="white",
                        command=function,
                    )
                )

            index_of_button: int = next(button_indexes)
            row: int = next(rows)
            column: int = next(columns)

            if function != self._reset:
                self._buttons[index_of_button].config(height=4, width=8)
                self._buttons[index_of_button].grid(row=row, column=column)


if __name__ == "__main__":
    WINDOW = tk.Tk()

    CALCULATOR = Calculator(WINDOW)

    WINDOW.mainloop()
