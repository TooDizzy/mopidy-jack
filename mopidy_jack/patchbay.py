"""Mixer that controls volume using a NAD amplifier."""

from __future__ import unicode_literals

import logging

import pygst
from mopidy_jack.JackActor import JackActor
pygst.require('0.10')
import gobject
import gst

try:
    import serial
except ImportError:
    serial = None  # noqa


logger = logging.getLogger('mopidy_jack')


class JackPatchBay(gst.Element, gst.ImplementsInterface, gst.interfaces.Mixer):
    __gstdetails__ = (
        'JackPatchBay',
        'Mixer',
        'Mixer to control Arcam amplifiers using a serial link',
        'Mopidy')

    _volume_cache = 0

    def list_tracks(self):
        track = create_track(
            label='Master',
            initial_volume=0,
            min_volume=0,
            max_volume=100,
            num_channels=1,
            flags=(
                gst.interfaces.MIXER_TRACK_MASTER |
                gst.interfaces.MIXER_TRACK_OUTPUT))
        return [track]

    def get_volume(self, track):
        return [self._volume_cache]

    def set_volume(self, track, volumes):
        if len(volumes):
            volume = volumes[0]
            self._volume_cache = volume
            self._arcam_talker.set_volume(volume)

    def set_mute(self, track, mute):
        self._arcam_talker.mute(mute)

    def do_change_state(self, transition):
        if transition == gst.STATE_CHANGE_NULL_TO_READY:
            if serial is None:
                logger.warning('arcammixer dependency pyserial not found')
                return gst.STATE_CHANGE_FAILURE
            
            self._jack = JackActor.start().proxy()
            
#            self._start_arcam_talker()
#            self._start_arcam_reader()
        return gst.STATE_CHANGE_SUCCESS

 
def create_track(label, initial_volume, min_volume, max_volume,
                 num_channels, flags):

    class Track(gst.interfaces.MixerTrack):
        def __init__(self):
            super(Track, self).__init__()
            self.volumes = (initial_volume,) * self.num_channels

#        @gobject.property
#        def label(self):
#            return label

#        @gobject.property
#        def min_volume(self):
#            return min_volume

#        @gobject.property
#        def max_volume(self):
#            return max_volume

#        @gobject.property
#        def num_channels(self):
#            return num_channels

#        @gobject.property
#        def flags(self):
#            return flags

    return Track()
