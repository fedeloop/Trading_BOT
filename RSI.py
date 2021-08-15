import time


# Global variables
N_for_RSI = 14


def RS(ticks: list) -> float:
    """Function to get the RS.

    Args:
        ticks (list): List with prices.

    Returns:
        float: Value of the RS.
    """
    up = 0
    down = 0
    i = 0
    
    while i < len(ticks)-2:
        print(ticks[i])
        if ticks[i] < ticks[i+1]:
            up += ticks[i+1]-ticks[i]
        elif ticks[i] > ticks[i+1]:
            down += ticks[i]-ticks[i+1]
        i+=1
    
    print(len(ticks), up, down)
    up /= len(ticks)
    down /= len(ticks)
    print(len(ticks), up, down, up/down)
    
    return up/down


def RSI(ticks: list) -> float:
    """Function to compute the value of the RSI.

    Args:
        ticks (list): List with prices.

    Returns:
        float: Value of the RSI.
    """
    return 100 - ( 100/( 1+RS(ticks) ) )


def thread_RSI(pill2kill, ticks: list, indicators: dict):
    """Function executed by a thread. Calculates the RSI and 
    stores it in the dictionary.

    Args:
        pill2kill (Threading.event): Event for stopping the threads executuion.
        ticks (list): List with prices.
        indicators (dict): Dictionary where the values are stored.
    """
    # If the list hasn't enough values we wait.
    while len(ticks) < N_for_RSI:
        print("[THREAD - RSI] - Waiting for ticks")
        time.sleep(1.5)
    
    print("[THREAD - RSI] - Computing values")
    
    while not pill2kill.wait(1):
        indicators['RSI'] = RSI(ticks[-N_for_RSI:])