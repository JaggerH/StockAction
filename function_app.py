import logging
import azure.functions as func

from app.main import app as fastapi_app

from utilities.tushare_limit_up import sendLimitUpEmail

app = func.AsgiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.ANONYMOUS)

# 时间对应中国时间下午16-19点
@app.schedule(schedule="0 */5 8-11 * * 1-5", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def LimitUpNotification(myTimer: func.TimerRequest) -> None:
    sendLimitUpEmail()