import math


class Brainiac:

    @staticmethod
    def calculate_area_of_square(a: float) -> float:
        """
                            DESCRIPTION:
        Calculate the surface area of a square shape.

                            PARAMETERS:
        > a (float) - size of the square's side

                               OUTPUT:
        > area (float) - an area of the square
        """
        if type(a) not in [float, int]:
            raise ValueError(f"The sides of an area must be a value. You entered: {a}")
        if a <= 0:
            raise ValueError(f"The sides of an area must be positive values. You entered: {a}")

        return math.pow(a, 2)


    @staticmethod
    def calculate_area_of_rectangle(a: float, b: float) -> float:
        """
                            DESCRIPTION:
        Calculate the surface area of a rectangle shape.

                            PARAMETERS:
        > a (float) - size of the first rectangle side
        > b (float) - size of the second rectangle side

                               OUTPUT:
        > area (float) - an area of the rectangle
        """
        if type(a) not in [float, int] or type(b) not in [float, int]:
            raise ValueError(f"The sides of the area must be made of values. You entered: {a} & {b}")
        if a <= 0 or b <= 0:
            raise ValueError(f"The sides of the area must be made of positive values. You entered: {a} & {b}")

        return a * b

    @staticmethod
    def find_prime_sequence(value: int) -> list:
        """
                            DESCRIPTION:
        Find the sequence of prime numbers up to a certain value.
        But this only applies for positive values.

                            PARAMETERS:
        > value (int) - up to which instance we want to know
                        the sequence.

                               OUTPUT:
        > primes (list) - a list of prime values
        """
        if type(value) != int:
            try:
                value = int(value)
            except:
                raise ValueError(f"Passed value to the function needs to be an integer or be convertable to a number. You entered: {value}")
        if value < 2:
            raise ValueError(f"Passed value to the function needs to be at least equal to 2 or be higher. You entered: {value}")

        primes = []

        for i in range(2, value):
            prime = True
            for y in range(2, int(i / 2) + 1):
                if i % y == 0:
                    prime = False
                    break
            if prime:
                primes.append(i)

        return primes
