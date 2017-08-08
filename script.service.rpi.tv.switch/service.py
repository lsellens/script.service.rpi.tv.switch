import xbmc
import xbmcaddon
try:
    import RPi.GPIO as GPIO
except RuntimeError, e:
    xbmc.log("rpi.tv.switch: RPi.GPIO import error", level=xbmc.LOGERROR)
    xbmc.log(str(e), level=xbmc.LOGERROR)

# addon
__addon__ = xbmcaddon.Addon(id='script.service.rpi.tv.switch')
__scriptname__   = "rpi.tv.switch"
__author__       = "lsellens"
__url__          = "https://github.com/lsellens/xbmc.addons"
txToSwitch = __addon__.getSetting('txToSwitch')
rxFromSwitch = __addon__.getSetting('rxFromSwitch')


if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(rxFromSwitch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(txToSwitch, GPIO.OUT, initial=GPIO.HIGH)
    monitor = xbmc.Monitor()
 
    while not monitor.abortRequested():
        if not GPIO.input(rxFromSwitch):
            xbmc.log("rpi.tv.switch: TV is off. Shutting down RPi", level=xbmc.LOGDEBUG)
            xbmc.shutdown()
        if monitor.waitForAbort(10):
            break

