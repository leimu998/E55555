import threading
import time
import matplotlib.pyplot as plt

class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork, print_lock, max_meals, timeline, timeline_lock):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.print_lock = print_lock
        self.max_meals = max_meals
        self.meals_eaten = 0
        self.timeline = timeline
        self.timeline_lock = timeline_lock

        # Initialize timeline with the philosopher's name
        with self.timeline_lock:
            self.timeline[self.name] = []

    def run(self):
        wait_start_time = time.time()
        while self.meals_eaten < self.max_meals:
            # Thinking
            with self.print_lock:
                print(f"Philosopher {self.name} is thinking")
            time.sleep(1)

            wait_end_time = time.time()
            with self.timeline_lock:
                self.timeline[self.name].append((wait_start_time, wait_end_time, 'wait'))

            # Pick up left fork
            with self.print_lock:
                print(f"Philosopher {self.name} got left fork")
            self.left_fork.acquire()

            # Pick up right fork
            with self.print_lock:
                print(f"Philosopher {self.name} is picking up right fork")
            if self.right_fork.acquire(timeout=5):
                # Eat
                eat_start_time = time.time()
                with self.print_lock:
                    print(f"Philosopher {self.name} is eating")
                    self.meals_eaten += 1
                time.sleep(1)
                eat_end_time = time.time()
                with self.timeline_lock:
                    self.timeline[self.name].append((eat_start_time, eat_end_time, 'eat'))

                # Put down right fork
                with self.print_lock:
                    print(f"Philosopher {self.name} put down right fork")
                self.right_fork.release()

                # Put down left fork
                with self.print_lock:
                    print(f"Philosopher {self.name} put down left fork")
                self.left_fork.release()
            else:
                # Release left fork
                with self.print_lock:
                    print(f"Philosopher {self.name} timed out and released left fork")
                self.left_fork.release()

            wait_start_time = time.time()


if __name__ == "__main__":
    # Create 5 forks and 5 philosophers
    forks = [threading.Lock() for n in range(5)]
    print_lock = threading.Lock()
    timeline = {}
    timeline_lock = threading.Lock()
    philosophers = [Philosopher(f"Philosopher {i}", forks[i], forks[(i + 1) % 5], print_lock, 1, timeline, timeline_lock) for i in range(5)]
    # Start all the philosophers
    for philosopher in philosophers:
        philosopher.start()

    for philosopher in philosophers:
        philosopher.join()

    # Draw timeline
    plt.figure(figsize=(10, 5))
    colors = ['red', 'green']
    labels = ['wait', 'eat']
    for philosopher in philosophers:
        timeline_philosopher = timeline.get(philosopher.name, [])
        for j in range(len(timeline_philosopher)):
            start_time, end_time, label = timeline_philosopher[j]
            color_index = labels.index(label)
            plt.plot([start_time, end_time], [philosophers.index(philosopher), philosophers.index(philosopher)],
                     color=colors[color_index], label=label)
    plt.yticks(list(range(5)), ['Philosopher ' + str(i) for i in range(5)])
    plt.legend()
    plt.title('Philosopher Dining Timeline')
    plt.show()

