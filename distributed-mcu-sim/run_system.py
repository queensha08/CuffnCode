import os

def run_dashboard():
    os.system("streamlit run app.py")

def run_benchmark():
    os.system("python benchmark/benchmark.py")

def main():
    print("===================================")
    print(" EVALUASI3 - MCU SIMULATION SYSTEM ")
    print("===================================")
    print("1. Run Dashboard (Streamlit)")
    print("2. Run Benchmark")
    print("3. Exit")
    print("===================================")

    choice = input("Pilih mode: ")

    if choice == "1":
        run_dashboard()
    elif choice == "2":
        run_benchmark()
    else:
        print("Exit")

if __name__ == "__main__":
    main()