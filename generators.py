from random import choices


def unordered_sequence(max_len=100):
    """
    Generates a list of random integers in arbitrary order.

    Args:
        max_len (int): Desired length of the sequence.

    Returns:
        list[int]: List of randomly selected integers from range -1000 to 999.
    """
    return choices(range(-1000, 1000), k=max_len)


def ordered_sequence(max_len=100):
    """
    Generates a sorted list of random integers.

    Args:
        max_len (int): Desired length of the sequence.

    Returns:
        list[int]: Sorted list of randomly selected integers
        from range -1000 to 999.
    """
    return sorted(choices(range(-1000, 1000), k=max_len))


def dna_sequence(max_len=100):
    """
    Generates a random DNA sequence.

    Args:
        max_len (int): Desired length of the sequence.

    Returns:
        str: String composed of characters "A", "C", "G", "T".
    """
    return "".join(choices("ACGT", k=max_len))


def main():
    """
    Runs basic tests for sequence generation functions.
    """
    print(unordered_sequence(max_len=500))
    print(ordered_sequence(max_len=500))
    print(dna_sequence(max_len=500))


if __name__ == "__main__":
    main()

    sizes = [100, 500, 1000, 5000, 10000]
    linear_times = []
    binary_times = []
    import time

    numbers = [4, 8, 15, 16, 23, 42, 55, 78, 91, 120]
    target = 78

    start = time.perf_counter()

    for number in numbers:
        if number == target:
            break

    end = time.perf_counter()

    duration = end - start
    print(f"Měření trvalo {duration:.8f} s")

    import matplotlib.pyplot as plt

    sizes = [100, 500, 1000, 5000, 10000]
    times = [0.00001, 0.00003, 0.00006, 0.00031, 0.00067]

    plt.plot(sizes, times)

    plt.xlabel("Velikost vstupu je")
    plt.ylabel("Čas [s]")
    plt.title("Ukázkový graf měření")
    plt.show()

