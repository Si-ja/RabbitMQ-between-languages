from Brainiac.Brainiac import Brainiac


def ask_a_question(issue, parameters):
    """
                        DESCRIPTION:
    Call calculations that can be performed by the
    Brainiac, depending on what has been requested
    by the user.

                        PARAMETERS:
    > issue (str) - type of an issue that the Brainiac needs
    to solve.
    > parameters (list<type>) - parameters that can be passed to
    the Brainiac.

                           OUTPUT:
    > answer (type) an answer that the Brainiac would deliver
    on a specific question.
    """
    try:
        if issue == "Square area":
            return Brainiac.calculate_area_of_square(parameters[0])

        elif issue == "Rectangle area":
            return Brainiac.calculate_area_of_rectangle(parameters[0], parameters[1])

        elif issue == "Prime values":
            return Brainiac.find_prime_sequence(parameters[0])

        else:
            return "No Answer for this problem"
    except:
        return "No Answer for this problem"

