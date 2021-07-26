url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/27282dea-d2b7-4c36-9f97-27804e58f0ed'
apikey = 'dOs2TEaBsKeWgxTGorFs5v4YroTiTBOGkXpLGIgcjxvh'

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator = authenticator)
tts.set_service_url(url)


with open ('C:/Users/iYaza/Desktop/TextToSpeech/speech.mp3' , 'wb') as audio_file:
    res = tts.synthesize('Hello my name is Yazan, nice to meet you', accept ='audio/mp3' , voice= 'en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)
