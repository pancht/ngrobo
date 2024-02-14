"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com

Development is still in progress...
"""
chrome_switches = [
    # Commonly unwanted browser features
    '--disable-client-side-phishing-detection',
    '--disable-component-extensions-with-background-pages',
    '--disable-default-apps',
    '--disable-extensions',
    '--hide-scrollbars',
    '--mute-audio',
    '--no-default-browser-check',
    '--no-first-run',
    '--ash-no-nudges',
    '--disable-search-engine-choice-screen',
    '--disable-features=InterestFeedContentSuggestions',
    '--disable-features=Translate',
    '--disable-background-timer-throttling',
    '--disable-backgrounding-occluded-windows',
    '--disable-features=CalculateNativeWinOcclusion',
    '--disable-hang-monitor',
    '--disable-ipc-flooding-protection',
    '--disable-renderer-backgrounding',
    '--disable-hang-monitor',
    '--disable-ipc-flooding-protection',
    '--disable-renderer-backgrounding',
    # web platform behavior
    '--aggressive-cache-discard',
    '--allow-running-insecure-content',
    '--disable-back-forward-cache',
    '--disable-features=AcceptCHFrame',
    '--disable-features=AutoExpandDetailsElement',
    '--disable-features=AvoidUnnecessaryBeforeUnloadCheckSync',
    '--disable-features=BackForwardCache',
    '--disable-features=HeavyAdPrivacyMitigations',
    '--disable-features=IsolateOrigins',
    '--disable-features=LazyFrameLoading',
    '--disable-features=ScriptStreaming',
    '--no-process-per-site',
    '--enable-precise-memory-info',
    '--js-flags=--random-seed=1157259157',
    '--use-fake-device-for-media-stream',
    '--use-fake-ui-for-media-stream',
    '--use-file-for-fake-video-capture=<path-to-file>',
    # Interactivity suppression
    # In-progess
]

task_throttling_feature = [


]