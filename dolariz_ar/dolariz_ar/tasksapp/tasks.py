from dolariz_ar.tasksapp.celery import app


@app.task(name="This is a example task")
def divide(x, y):
    import time

    time.sleep(5)
    return x / y
