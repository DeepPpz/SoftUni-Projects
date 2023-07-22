def show_success_message(operation, message):
    operation_message = f"Successfully executed {operation}."
    
    print(operation_message)
    print("=" * len(operation_message))
    print(f"{message}.")


def show_warning_message(message):
    operation_message = f"Warning: {message}."
    
    print(operation_message)
    print("=" * len(operation_message))


def show_error_message(operation, message, error_code):
    operation_message = f"Error: Failed to execute {operation}."
    
    print(operation_message)
    print("=" * len(operation_message))
    print(f"Reason: {message}.")
    print(f"Error code: {error_code}.")


def read_and_process_message(message_type):
    if message_type == "success":
        operation = input()
        message = input()
        show_success_message(operation, message)

    elif message_type == "warning":
        message = input()
        show_warning_message(message)

    elif message_type == "error":
        operation = input()
        message = input()
        error_code = input()
        show_error_message(operation, message, error_code)
    
    print()


for i in range(int(input())):
    message_type = input()
    read_and_process_message(message_type)
