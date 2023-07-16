import time, random, threading, queue

my_videos = ["video1.mp4", "video2.mp4", "video3.mp4", "video4.mp4", "video5.mp4"]

# create the job queue
job_queue = queue.Queue()

# fill up job_queue
for i in my_videos:
    job_queue.put(i)


def video_converter():
    while not job_queue.empty():
        next_job = job_queue.get()
        print(f"Working on {next_job}...")
        time.sleep(random.randint(3, 10))
        print(f"Convert finished: {next_job}")
        job_queue.task_done()


for _ in range(3):
    t = threading.Thread(target=video_converter)
    t.start()