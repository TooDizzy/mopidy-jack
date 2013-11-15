from __future__ import unicode_literals

import os

# TODO: Comment in if you need to register GStreamer elements below, else
# remove entirely
#import pygst
#pygst.require('0.10')
import gst
import gobject

from mopidy import config, ext

__version__ = '0.1.0'


class Extension(ext.Extension):

    dist_name = 'Mopidy-Jack'
    ext_name = 'jack'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        # TODO: Comment in and edit, or remove entirely
        #schema['username'] = config.String()
        #schema['password'] = config.Secret()
        return schema


    def register_gstreamer_elements(self):
        from .patchbay import JackPatchBay
        gobject.type_register(JackPatchBay)
        gst.element_register(JackPatchBay, 'jackmixer', gst.RANK_MARGINAL)