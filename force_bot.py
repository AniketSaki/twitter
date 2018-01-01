import twitter
import datetime as dt
from bot_config import *

suffix = {1: 'st', 2: 'nd', 3: 'rd', 21: 'st', 22: 'nd', 23: 'rd', 31: 'st'}
month = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 
         9: 'September', 10: 'October', 11: 'November', 12: 'December'}
         
api = twitter.Api(consumerKey, consumerSecret, accessToken, accessTokenSecret)
today = dt.date.today()
day = today.day
msg = month[today.month] + ' the ' + str(day)
if day in suffix:
    msg = msg + suffix[day]
else:
    msg = msg + 'th'
msg = msg + ' be with you!'
status = api.PostUpdate(msg)
print(status.text)
del api
