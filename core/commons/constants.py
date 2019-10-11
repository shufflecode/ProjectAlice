VERSION = 0.13
DEFAULT_SITE_ID = 'default'
UNKNOWN_WORD = 'unknownword'
UNKNOWN_USER = 'unknownUser'
UNKNOWN_MANAGER = 'unknownManager'
UNKNOWN = 'unknown'
ALL = 'all'
DUMMY = 'dummy'

TOPIC_AUDIO_FRAME = 'hermes/audioServer/default/audioFrame'
TOPIC_HOTWORD_DETECTED = 'hermes/hotword/default/detected'
TOPIC_WAKEWORD_DETECTED = 'hermes/hotword/{user}/detected'
TOPIC_ASR_START_LISTENING = 'hermes/asr/startListening'
TOPIC_SESSION_STARTED = 'hermes/dialogueManager/sessionStarted'
TOPIC_SESSION_QUEUED = 'hermes/dialogueManager/sessionQueued'
TOPIC_SESSION_ENDED = 'hermes/dialogueManager/sessionEnded'
TOPIC_TEXT_CAPTURED = 'hermes/asr/textCaptured'
TOPIC_INTENT_NOT_RECOGNIZED = 'hermes/dialogueManager/intentNotRecognized'
TOPIC_INTENT_PARSED = 'hermes/nlu/intentParsed'
TOPIC_TTS_SAY = 'hermes/tts/say'
TOPIC_TTS_FINISHED = 'hermes/tts/sayFinished'
TOPIC_HOTWORD_TOGGLE_ON = 'hermes/hotword/toggleOn'
TOPIC_PLAY_BYTES = 'hermes/audioServer/{}/playBytes/{}'
TOPIC_START_SESSION = 'hermes/dialogueManager/startSession'
TOPIC_CONTINUE_SESSION = 'hermes/dialogueManager/continueSession'
TOPIC_END_SESSION = 'hermes/dialogueManager/endSession'
TOPIC_DIALOGUE_MANAGER_CONFIGURE = 'hermes/dialogueManager/configure'
TOPIC_TOGGLE_FEEDBACK_ON = 'hermes/feedback/sound/toggleOn'
TOPIC_TOGGLE_FEEDBACK_OFF = 'hermes/feedback/sound/toggleOff'
TOPIC_TOGGLE_FEEDBACK = 'hermes/feedback/sound/toggle{}'
TOPIC_STOP_LISTENING = 'hermes/asr/stopListening'
TOPIC_NLU_QUERY = 'hermes/nlu/query'