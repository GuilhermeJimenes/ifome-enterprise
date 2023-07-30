if __name__ == '__main__':
    from src.application.sales_app import SalesApp
    print('Waiting for a message...')

    while True:
        result = SalesApp().sales()
        if result == 'error':
            break
        elif result:
            print("Result:", result)
