import time
import tracemalloc

def measure_performance(algorithm_func, text, pattern):
    tracemalloc.start()
    start_time = time.perf_counter()
    
    matches = algorithm_func(text, pattern)
    
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return {
        'matches': matches,
        'time': round((end_time - start_time) * 1000, 2),  # ms
        'memory': round(peak / 1024, 2)  # KB
    }
