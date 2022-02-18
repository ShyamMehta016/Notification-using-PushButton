from typing import Text
from pushbullet import Pushbullet
API_KEY="o.tOorw3GMHQ5LtlMgL3T0kuJeeHfUoSeY"
file=r"D:/F DRIVE/WORKSPACE/ZESTECH/Push Notification/notification.txt.txt"

with open(file,mode='r') as f:
    Text=f.read()

pb=Pushbullet(API_KEY)
push=pb.push_note('Please remember', Text)