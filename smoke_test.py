import sys
from src.features import get_hash_bucket

def run_smoke_test():
    print("--- Starting MLOps Smoke Test ---")
    try:
        # 1. Simulate a request to our 'feature service'
        test_input = "health_check_user"
        result = get_hash_bucket(test_input)
        
        # 2. Check if the result is valid
        if isinstance(result, int):
            print("Status: 200 OK - Service is Healthy")
            return True
        else:
            print("Status: 500 - Invalid Response")
            sys.exit(1)
            
    except Exception as e:
        print(f"Smoke Test Failed with error: {e}")
        sys.exit(1)

# This part ensures the code runs when you call the file
if __name__ == "__main__":
    run_smoke_test()