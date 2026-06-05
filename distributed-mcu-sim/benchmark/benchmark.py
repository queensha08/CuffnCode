import time
from core.pipeline import run

def run_benchmark(iterations=100):

    latencies = []

    print("🚀 Starting Benchmark...")

    start_all = time.time()

    for i in range(iterations):

        t0 = time.time()

        run()   # 1 full MCU pipeline cycle

        t1 = time.time()

        latencies.append(t1 - t0)

    end_all = time.time()

    total_time = end_all - start_all
    avg_latency = sum(latencies) / len(latencies)
    throughput = iterations / total_time

    print("\n📊 BENCHMARK RESULT")
    print("----------------------")
    print(f"Total iterations : {iterations}")
    print(f"Total time       : {total_time:.4f} s")
    print(f"Avg latency      : {avg_latency:.4f} s / cycle")
    print(f"Throughput       : {throughput:.2f} cycles/sec")

    return {
        "total_time": total_time,
        "avg_latency": avg_latency,
        "throughput": throughput
    }


if __name__ == "__main__":
    run_benchmark(100)