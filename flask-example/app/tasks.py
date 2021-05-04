import time


def example_task(seconds):
    print('Starting the task')
    for i in range(seconds):
        print(i)
        time.sleep(1)
    print('Task has completed')

if __name__ == '__main__':
    example_task(23)