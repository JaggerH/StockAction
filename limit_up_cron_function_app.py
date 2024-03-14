import datetime
import logging
import azure.functions as func

# 添加 TimeTrigger 装饰器，指定触发器的时间间隔或 CRON 表达式
@func.timer_trigger(schedule="0 */1 * * * *")  # 每分钟触发一次
def timed_function(my_timer: func.TimerRequest):
    utc_timestamp = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
    logging.info('Python Timer trigger function ran at %s' % utc_timestamp)

    # 在这里执行你的操作，比如调用其他函数、发送通知等
    # 如果你有其他操作，请在此添加代码

    # 注意：确保你的函数执行时间短，以免超出 Azure Function 的执行限制