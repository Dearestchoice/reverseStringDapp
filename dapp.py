import json
import sys

def reverse_string(input_string):
    return input_string[::-1]

def handle_advance(data):
    input_data = json.loads(data)
    
    if 'payload' not in input_data:
        return {"status": "error", "message": "No input provided"}

    input_string = input_data['payload']

    # Reverse the string
    reversed_string = reverse_string(input_string)

    # Create a notice
    notice = {
        "type": "notice",
        "payload": f"Original: {input_string}, Reversed: {reversed_string}"
    }

    # Create a voucher with the correct Ethereum address
    voucher = {
        "type": "voucher",
        "destination": "0xaF6983217cd9cC8a25c0866bca72A82DD8a392a6",  # Correct Ethereum address
        "payload": reversed_string
    }

    # Create a report (summary of the operation)
    report = {
        "type": "report",
        "payload": f"Processed reverse operation. Original: '{input_string}', Reversed: '{reversed_string}'"
    }

    # Return the results as JSON
    return json.dumps({
        "status": "success",
        "notices": [notice],
        "vouchers": [voucher],
        "reports": [report]
    })

def main():
    for line in sys.stdin:
        response = handle_advance(line)
        print(response)
        sys.stdout.flush()

if __name__ == "__main__":
    main()
