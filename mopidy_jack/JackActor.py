'''
Created on 12/11/2013

@author: tue
'''

import pykka
import jack
import mopidy.core


class JackActor(pykka.ThreadingActor, mopidy.core.CoreListener):
    """
    Independent thread which does the communication with the Arcam amplifier.
    
    """
    
    _jack_connection = None
    
    def __init__(self):
        super(JackActor, self).__init__()
        
    #def on_start(self):
        #print "Attaching to jack."
        #jack.attach("default")
        #print "Attached."
        #print "Jack ports: %s", jack.get_ports()

    def on_stop(self):
        print "Detaching from JACK"
        jack.detach()
        
    def track_playback_started(self, tl_track):
        print "Attaching to jack."
        jack.attach("default")
        print "Attached."
        print "Jack ports: %s", jack.get_ports()
        
        print "Track playback started. Time for some JACK magic."
        
        # Connect the specified JACK ports together.
        jack.connect("mopidy:out_jackaudiosink0_1","python:in_openob_tx_test-link_1")
        jack.connect("mopidy:out_jackaudiosink0_2","python:in_openob_tx_test-link_2")