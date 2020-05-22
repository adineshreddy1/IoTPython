from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
import random
import time
SHADOW_CLIENT = "myshadowClient"
HOSTNAME = "a2p32d836jrk2t-ats.iot.us-east-1.amazonaws.com"
ROOT_CA = "AmazonRootCA1.pem"
PRIVATE_KEY = "2b00dfcd6d-private.pem.key"
CERT_FILE = "2b00dfcd6d-certificate.pem.crt"
SHADOW_HANDLER = "Dineshsensor"
def myshadowCallback(payload, responseStatus, token):
  print()
print('UPDATE:$aws/things/' + SHADOW_HANDLER +
  '/shadow/update/#')
print("payload = " + payload)
print("responseStatus = " + responseStatus)
print("token = " + token)
myShadowClient = AWSIoTMQTTShadowClient(SHADOW_CLIENT)
myShadowClient.configureEndpoint(HOST_NAME, 8883)
myShadowClient.configureCredentials(ROOT_CA, PRIVATE_KEY,
  CERT_FILE)
myShadowClient.configureConnectDisconnectTimeout(10)
myShadowClient.connect()
myDeviceShadow = myShadowClient.createShadowHandlerWithName(
  SHADOW_HANDLER, True)
while True:
  moisture = random.choice([True, False])
if moisture:
  myDeviceShadow.shadowUpdate(
    '{"state":{"reported":{"moisture":"okay"}}}',
    myShadowUpdateCallback, 5)
else :
  myDeviceShadow.shadowUpdate(
    '{"state":{"reported":{"moisture":"low"}}}',
    myShadowUpdateCallback, 5)
  time.sleep(60)
