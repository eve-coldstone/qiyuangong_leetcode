import timeit

def measure_time(func, *args, repeats=1000, **kwargs):
    """
    Measures the average execution time of a function in microseconds.
    
    Args:
        func: function to measure
        *args, **kwargs: arguments to pass to func
        repeats: number of times to repeat (default 1000)
        
    Returns:
        Average running time per call in microseconds (float)
    """
    # Wrapper to call the function with arguments
    def wrapper():
        return func(*args, **kwargs)
    
    total_time = timeit.timeit(wrapper, number=repeats)
    avg_time_us = (total_time / repeats) * 1_000_000  # convert to μs
    return avg_time_us