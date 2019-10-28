# Copyright (C) 2017  DESY, Christoph Rosemann, Notkestr. 85, D-22607 Hamburg
#
# lavue is an image viewing program for photon science imaging detectors.
# Its usual application is as a live viewer using hidra as data source.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation in  version 2
# of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA  02110-1301, USA.
#
# Authors:
#     Christoph Rosemann <christoph.rosemann@desy.de>
#     Jan Kotanski <jan.kotanski@desy.de>
#


""" live viewer settings """

from __future__ import print_function
from __future__ import unicode_literals


import time
import socket
import json
from .qtuic import uic
import numpy as np
import pyqtgraph as _pg
from pyqtgraph import QtCore, QtGui
import os
import zmq
import sys
import argparse


from . import imageSource as isr
from . import messageBox

from . import sourceGroupBox
from . import toolWidget
from . import sourceWidget
from . import preparationGroupBox
from . import scalingGroupBox
from . import levelsGroupBox
from . import statisticsGroupBox
from . import imageWidget
from . import imageField
from . import configDialog
from . import release
from . import edDictDialog
from . import filters

try:
    from . import controllerClient
    TANGOCLIENT = True
except Exception:
    TANGOCLIENT = False

from . import imageFileHandler
from . import sardanaUtils
from . import dataFetchThread
from . import settings

from .hidraServerList import HIDRASERVERLIST


if sys.version_info > (3,):
    basestring = str
    unicode = str


#: ( (:obj:`str`,:obj:`str`,:obj:`str`) )
#:         pg major version, pg minor verion, pg patch version
_VMAJOR, _VMINOR, _VPATCH = _pg.__version__.split(".")[:3] \
    if _pg.__version__ else ("0", "9", "0")

_formclass, _baseclass = uic.loadUiType(
    os.path.join(os.path.dirname(os.path.abspath(__file__)),
                 "ui", "MainDialog.ui"))


class MainWindow(QtGui.QMainWindow):

    def __init__(self, options, parent=None):
        """ constructor

        :param options: commandline options
        :type options: :class:`argparse.Namespace`
        :param parent: parent object
        :type parent: :class:`pyqtgraph.QtCore.QObject`
        """
        QtGui.QMainWindow.__init__(self, parent)
        self.__lavue = LiveViewer(options, self)
        self.centralwidget = QtGui.QWidget(self)
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.addWidget(self.__lavue, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        if hasattr(options, "instance") and options.instance:
            self.setWindowTitle(
                "laVue: Live Image Viewer (v%s) [%s]" %
                (str(release.__version__), options.instance))
        else:
            self.setWindowTitle(
                "laVue: Live Image Viewer (v%s)" %
                str(release.__version__))

    def closeEvent(self, event):
        """ stores the setting before finishing the application

        :param event: close event
        :type event:  :class:`pyqtgraph.QtCore.QEvent`:
        """
        self.__lavue.closeEvent(event)
        QtGui.QMainWindow.closeEvent(self, event)


class LiveViewer(QtGui.QDialog):

    '''The master class for the dialog, contains all other
    widget and handles communication.'''

    #: (:class:`pyqtgraph.QtCore.pyqtSignal`) state updated signal
    _stateUpdated = QtCore.pyqtSignal(bool)

    def __init__(self, options, parent=None):
        """ constructor

        :param options: commandline options
        :type options: :class:`argparse.Namespace`
        :param parent: parent object
        :type parent: :class:`pyqtgraph.QtCore.QObject`
        """
        QtGui.QDialog.__init__(self, parent)
        # self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        if options.mode and options.mode.lower() in ["expert"]:
            #: (:obj:`str`) execution mode: expert or user
            self.__umode = "expert"
        else:
            #: (:obj:`str`) execution mode: expert or user
            self.__umode = "user"
        #: (:obj:`bool`) histogram should be updated
        self.__updatehisto = False
        #: (:obj:`int`) program pid
        self.__apppid = os.getpid()
        #: (:obj:`str`) host name
        self.__targetname = socket.getfqdn()

        #: (:obj:`list` < :obj:`str` > ) allowed source metadata
        self.__allowedmdata = ["datasources"]
        #: (:obj:`list` < :obj:`str` > ) allowed widget metadata
        self.__allowedwgdata = ["axisscales", "axislabels"]

        # (:class:`lavuelib.imageSource.BaseSource`) data source object
        self.__datasource = isr.BaseSource()

        #: (:class:`lavuelib.sardanaUtils.SardanaUtils`)
        #:  sardana utils
        self.__sardana = None

        #: (:class:`lavuelib.settings.Settings`) settings
        self.__settings = settings.Settings()
        self.__settings.load(QtCore.QSettings())

        #: (:obj:`list` < :obj:`str` > ) source class names
        self.__sourcetypes = []

        #: (:obj:`list` < :obj:`str` > ) all source aliases
        self.__allsourcealiases = []
        #: (:obj:`dict` < :obj:`str`, :obj:`str` > ) source alias names
        self.__srcaliasnames = {}

        #: (:obj:`list` < :obj:`str` > ) tool class names
        self.__tooltypes = []

        #: (:obj:`list` < :obj:`str` > ) all tool aliases
        self.__alltoolaliases = []
        #: (:obj:`dict` < :obj:`str`, :obj:`str` > ) tool alias names
        self.__tlaliasnames = {}

        self.__updateTypeList(
            sourceWidget.swproperties, self.__sourcetypes,
            self.__allsourcealiases, self.__srcaliasnames
        )
        self.__updateTypeList(
            toolWidget.twproperties, self.__tooltypes,
            self.__alltoolaliases, self.__tlaliasnames
        )

        #: (:obj:`list` < :obj:`str` > ) rgb tool class names
        self.__rgbtooltypes = []
        self.__rgbtooltypes.append("RGBIntensityToolWidget")

        #: (:class:`lavuelib.controllerClient.ControllerClient`)
        #:   tango controller client
        self.__tangoclient = None

        #: (:obj:`int`) stacking dimension
        self.__growing = None
        #: (:obj:`int`) current frame id
        self.__frame = None
        #: (:obj:`str`) nexus field path
        self.__fieldpath = None

        #: (:class:`filters.FilterList` ) user filters
        self.__filters = filters.FilterList()

        #: (:obj:`int`) filter state
        self.__filterstate = 0

        #: (:obj:`float`) last time read
        self.__lasttime = 0
        #: (:obj:`float`) current time
        self.__currentime = 0

        # WIDGET DEFINITIONS
        #: (:class:`lavuelib.sourceGroupBox.SourceGroupBox`) source groupbox
        self.__sourcewg = sourceGroupBox.SourceGroupBox(
            parent=self, sourcetypes=self.__sourcetypes,
            expertmode=(self.__umode == 'expert'))
        self.__sourcewg.updateSourceComboBox(
            [self.__srcaliasnames[twn]
             for twn in json.loads(self.__settings.imagesources)])

        #: (:class:`lavuelib.preparationGroupBox.PreparationGroupBox`)
        #: preparation groupbox
        self.__prepwg = preparationGroupBox.PreparationGroupBox(
            parent=self, settings=self.__settings)
        #: (:class:`lavuelib.scalingGroupBox.ScalingGroupBox`) scaling groupbox
        self.__scalingwg = scalingGroupBox.ScalingGroupBox(parent=self)
        #: (:class:`lavuelib.levelsGroupBox.LevelsGroupBox`) level groupbox
        self.__levelswg = levelsGroupBox.LevelsGroupBox(
            parent=self, settings=self.__settings,
            expertmode=(self.__umode == 'expert'))
        #: (:class:`lavuelib.statisticsGroupBox.StatisticsGroupBox`)
        #:     statistic groupbox
        self.__statswg = statisticsGroupBox.StatisticsGroupBox(parent=self)
        #: (:class:`lavuelib.imageWidget.ImageWidget`) image widget
        self.__imagewg = imageWidget.ImageWidget(
            parent=self, tooltypes=self.__tooltypes,
            settings=self.__settings,
            rgbtooltypes=self.__rgbtooltypes)
        self.__imagewg.updateToolComboBox(
            [self.__tlaliasnames[twn]
             for twn in json.loads(self.__settings.toolwidgets)])

        self.__levelswg.setImageItem(self.__imagewg.image())
        self.__levelswg.showGradient(True)
        self.__levelswg.updateHistoImage(autoLevel=True)

        #: (:class:`lavuelib.maskWidget.MaskWidget`) mask widget
        self.__maskwg = self.__prepwg.maskWidget
        #: (:class:`lavuelib.highValueMaskWidget.HighValueMaskWidget`)
        #               high value mask widget
        self.__highvaluemaskwg = self.__prepwg.highValueMaskWidget
        #: (:class:`lavuelib.bkgSubtractionWidget.BkgSubtractionWidget`)
        #:    background subtraction widget
        self.__bkgsubwg = self.__prepwg.bkgSubWidget
        #: (:class:`lavuelib.transformationsWidget.TransformationsWidget`)
        #:    transformations widget
        self.__trafowg = self.__prepwg.trafoWidget
        #: (:class:`lavuelib.filtersWidget.FiltersWidget`)
        #:    filters widget
        self.__filterswg = self.__prepwg.filtersWidget

        # keep a reference to the "raw" image and the current filename
        #: (:class:`numpy.ndarray`) raw image
        self.__rawimage = None
        #: (:class:`numpy.ndarray`) raw image
        self.__filteredimage = None
        #: (:class:`numpy.ndarray`) raw gray image
        self.__rawgreyimage = None
        #: (:obj:`str`) image name
        self.__imagename = None
        #: (:obj:`str`) last image name
        self.__lastimagename = None
        #: (:obj:`str`) metadata JSON dictionary
        self.__metadata = ""
        #: (:obj:`str`) metadata dictionary
        self.__mdata = {}
        #: (:class:`numpy.ndarray`) displayed image after preparation
        self.__displayimage = None
        #: (:class:`numpy.ndarray`) scaled displayed image
        self.__scaledimage = None

        #: (:class:`numpy.ndarray`) background image
        self.__backgroundimage = None
        #: (:obj:`bool`) apply background image subtraction
        self.__dobkgsubtraction = False

        #: (:class:`numpy.ndarray`) mask image
        self.__maskimage = None
        #: (:obj:`float`) file name
        self.__maskvalue = None
        #: (:class:`numpy.ndarray`) mask image indices
        self.__maskindices = None
        #: (:obj:`bool`) apply mask
        self.__applymask = False

        #: (:obj:`str`) source configuration string
        self.__sourceconfiguration = None

        #: (:obj:`str`) source label
        self.__sourcelabel = None

        #: (:obj:`str`) reload flag
        self.__reloadflag = False

        #: (:obj:`str`) transformation name
        self.__trafoname = "None"

        #: (:obj:`bool`) lazy image slider
        self.__lazyimageslider = False

        #: (:obj: dict < :obj:`str` , :obj:`str` >) unsigned/signed int map
        self.__unsignedmap = {
            "uint8": "int16",
            "uint16": "int32",
            "uint32": "int64",
            "uint64": "int64"
            # "uint64": "float64"
        }
        #: (:class:`Ui_LevelsGroupBox') ui_groupbox object from qtdesigner
        self.__ui = _formclass()
        self.__ui.setupUi(self)

        # # LAYOUT DEFINITIONS
        self.__ui.confVerticalLayout.addWidget(self.__sourcewg)
        self.__ui.confVerticalLayout.addWidget(self.__prepwg)
        self.__ui.confVerticalLayout.addWidget(self.__scalingwg)
        self.__ui.confVerticalLayout.addWidget(self.__levelswg)
        self.__ui.confVerticalLayout.addWidget(self.__statswg)
        self.__ui.imageVerticalLayout.addWidget(self.__imagewg)
        spacer = QtGui.QSpacerItem(
            0, 0,
            QtGui.QSizePolicy.Minimum,
            QtGui.QSizePolicy.Expanding
        )
        self.__ui.confVerticalLayout.addItem(spacer)
        self.__ui.splitter.setStretchFactor(0, 1)
        self.__ui.splitter.setStretchFactor(1, 10)

        # SIGNAL LOGIC::

        # signal from intensity scaling widget:
        # self.__scalingwg.scalingChanged.connect(self.scale)
        self.__scalingwg.simpleScalingChanged.connect(self._plot)
        self.__scalingwg.scalingChanged.connect(
            self.__levelswg.setScalingLabel)

        # signal from limit setting widget
        self.__levelswg.minLevelChanged.connect(self.__imagewg.setMinLevel)
        self.__levelswg.maxLevelChanged.connect(self.__imagewg.setMaxLevel)
        self.__levelswg.autoLevelsChanged.connect(self.__imagewg.setAutoLevels)
        self.__levelswg.levelsChanged.connect(self._plot)
        self.__ui.cnfPushButton.clicked.connect(self._configuration)
        self.__ui.quitPushButton.clicked.connect(self.close)
        self.__ui.loadPushButton.clicked.connect(self._loadfile)
        if self.__umode in ["user"]:
            self.__ui.cnfPushButton.hide()
        self.__imagewg.roiCoordsChanged.connect(self._calcUpdateStatsSec)
        # connecting signals from source widget:
        self.__sourcewg.sourceConnected.connect(self._connectSource)
#        self.__sourcewg.sourceConnected.connect(self._startPlotting)

#        self.__sourcewg.sourceDisconnected.connect(self._stopPlotting)
        self.__sourcewg.sourceDisconnected.connect(self._disconnectSource)

        # gradient selector
        self.__levelswg.rgbChanged.connect(self.setrgb)
        self.__levelswg.channelChanged.connect(self._plot)
        self.__imagewg.aspectLockedToggled.connect(self._setAspectLocked)
        self.__levelswg.storeSettingsRequested.connect(
            self._storeSettings)

        self.__imagewg.replotImage.connect(self._replot)
        # simple mutable caching object for data exchange with thread
        #: (:class:`lavuelib.dataFetchTread.ExchangeList`)
        #:    exchange list
        self.__exchangelist = dataFetchThread.ExchangeList()

        #: (:class:`lavuelib.dataFetchTread.DataFetchThread`)
        #:    data fetch thread
        self.__dataFetcher = dataFetchThread.DataFetchThread(
            self.__datasource, self.__exchangelist)
        self.__dataFetcher.newDataNameFetched.connect(self._getNewData)
        # ugly !!! sent current state to the data fetcher...
        self._stateUpdated.connect(self.__dataFetcher.changeStatus)
        self.__sourcewg.sourceStateChanged.connect(self._updateSource)
        self.__sourcewg.sourceChanged.connect(self._onSourceChanged)

        self.__bkgsubwg.bkgFileSelected.connect(self._prepareBkgSubtraction)
        self.__bkgsubwg.useCurrentImageAsBkg.connect(
            self._setCurrentImageAsBkg)
        self.__bkgsubwg.applyStateChanged.connect(self._checkBkgSubtraction)

        self.__maskwg.maskFileSelected.connect(self._prepareMasking)
        self.__maskwg.applyStateChanged.connect(self._checkMasking)

        self.__highvaluemaskwg.maskHighValueChanged.connect(
            self._checkHighMasking)

        # signals from transformation widget
        self.__trafowg.transformationChanged.connect(
            self._assessTransformation)

        # signals from transformation widget
        self.__filterswg.filtersChanged.connect(
            self._assessFilters)

        # set the right target name for the source display at initialization

        self.__sourcewg.configurationChanged.connect(
            self._setSourceConfiguration)
        self.__sourcewg.sourceLabelChanged.connect(
            self._switchSourceDisplay)
        self.__sourcewg.addIconClicked.connect(
            self._addLabel)
        self.__sourcewg.removeIconClicked.connect(
            self._removeLabel)

        self.__ui.frameLineEdit.textChanged.connect(self._spinreloadfile)
        self.__ui.lowerframePushButton.clicked.connect(
            self._lowerframepushed)
        self.__ui.higherframePushButton.clicked.connect(
            self._higherframepushed)
        self.__ui.frameHorizontalSlider.valueChanged.connect(
            self._sliderreloadfilelazy)
        self.__connectslider()

        self.__sourcewg.updateLayout()
        self.__sourcewg.emitSourceChanged()
        self.__imagewg.showCurrentTool()

        self.__loadSettings()

        self.__resetFilters(self.__settings.filters)

        self.__updateframeview()

        self.__updateframeratetip(self.__settings.refreshrate)

        start = self.__applyoptions(options)
        self._plot()
        if start:
            self.__sourcewg.start()

        if options.tool:
            QtCore.QTimer.singleShot(10, self.__imagewg.showCurrentTool)

    def __updateTypeList(self, properties, typelist,
                         allaliases, snametoname):
        typelist[:] = []
        allaliases[:] = []
        for wp in properties:
            avail = True
            for req in wp["requires"]:
                if not getattr(isr, req):
                    avail = False
                    break
            if avail:
                if wp["alias"] not in typelist:
                    typelist.append(wp["widget"])
            allaliases.append(wp["alias"])
            snametoname[wp["alias"]] = wp["name"]

    def __switchlazysignals(self, lazy=False):
        """switch lazy signals

        :param lazy: lazy image slider flag
        :type lazy: :obj:`bool`
        """
        if lazy:
            self.__ui.frameHorizontalSlider.sliderReleased.connect(
                self._sliderreloadfile)
            self.__lazyimageslider = True
        else:
            self.__ui.frameHorizontalSlider.sliderReleased.disconnect(
                self._sliderreloadfile)
            self.__lazyimageslider = False

    def __disconnectslider(self):
        """switch lazy signals

        :param lazy: lazy image slider flag
        :type lazy: :obj:`bool`
        """
        if self.__lazyimageslider:
            self.__ui.frameHorizontalSlider.sliderReleased.disconnect(
                self._sliderreloadfile)

    def __connectslider(self):
        """switch lazy signals

        :param lazy: lazy image slider flag
        :type lazy: :obj:`bool`
        """
        if self.__lazyimageslider:
            self.__ui.frameHorizontalSlider.sliderReleased.connect(
                self._sliderreloadfile)

    def __resetFilters(self, filters):
        """ resets filters

        :param filters: filters settings
        :type filters: :obj:`str`
        """
        try:
            fsettings = json.loads(filters)
            self.__filters.reset(fsettings)
            label = " | ".join([flt[0].split(".")[-1]
                                for flt in fsettings if flt[0]])
            if len(label) > 32:
                label = label[:32] + " ..."
            self.__filterswg.setLabel(label)
            self.__filterswg.setToolTip(
                "\n".join(
                    ["%s(%s)" %
                     (flt[0],
                      ("'%s'" % flt[1]) if flt[1] else "")
                     for flt in fsettings if flt[0]])
            )
            if self.__settings.filters != filters:
                self.__settings.filters = filters
        except Exception as e:
            self.__filterswg.setState(0)
            import traceback
            value = traceback.format_exc()
            messageBox.MessageBox.warning(
                self, "lavue: problems in setting filters",
                "%s" % str(e),
                "%s" % value)
            # print(str(e))

    @QtCore.pyqtSlot(str, str)
    def _addLabel(self, name, value):
        """ emits addIconClicked signal

        :param name: object name
        :type name: :obj:`str`
        :param value: text value
        :type value: :obj:`str`
        """
        name = str(name)
        value = str(value)
        labelvalues = json.loads(getattr(self.__settings, name) or '{}')
        dform = edDictDialog.EdDictDialog(self)
        dform.record = labelvalues
        dform.newvalues = [value]
        # dform.title = self.__objtitles[repr(obj)]
        dform.createGUI()
        dform.exec_()
        if dform.dirty:
            labelvalues = dform.record
            for key in list(labelvalues.keys()):
                if not str(key).strip():
                    labelvalues.pop(key)
            setattr(self.__settings, name, json.dumps(labelvalues))
            self.__updateSource()
            self._storeSettings()

    @QtCore.pyqtSlot(str, str)
    def _removeLabel(self, name, label):
        """ emits addIconClicked signal

        :param name: object name
        :type name: :obj:`str`
        :param value: text value label to remove
        :type value: :obj:`str`
        """
        name = str(name)
        label = str(label)
        labelvalues = json.loads(getattr(self.__settings, name) or '{}')
        if label in labelvalues.keys():
            labelvalues.pop(label)
            setattr(self.__settings, name, json.dumps(labelvalues))
            self.__updateSource()
            self._storeSettings()

    def __updateSource(self):
        detservers = json.loads(self.__settings.detservers)
        if detservers:
            if self.__settings.defdetservers:
                serverdict = dict(HIDRASERVERLIST)
                defpool = set(serverdict["pool"])
                defpool.update(detservers)
                serverdict["pool"] = list(defpool)
            else:
                serverdict = {"pool": list(detservers)}
        elif self.__settings.defdetservers:
            serverdict = HIDRASERVERLIST
        else:
            serverdict = {"pool": []}
        self.__sourcewg.updateMetaData(
            zmqtopics=self.__settings.zmqtopics,
            dirtrans=self.__settings.dirtrans,
            tangoattrs=self.__settings.tangoattrs,
            tangoevattrs=self.__settings.tangoevattrs,
            tangofileattrs=self.__settings.tangofileattrs,
            tangodirattrs=self.__settings.tangodirattrs,
            zmqservers=self.__settings.zmqservers,
            httpurls=self.__settings.httpurls,
            autozmqtopics=self.__settings.autozmqtopics,
            nxslast=self.__settings.nxslast,
            nxsopen=self.__settings.nxsopen,
            serverdict=serverdict,
            hidraport=self.__settings.hidraport,
            doocsprops=self.__settings.doocsprops
        )

    @QtCore.pyqtSlot(str)
    def _updateLavueState(self, state):
        """ updates lavue state configuration

        :param state: json dictionary with configuration
        :type state: :obj:`str`
        """
        if state:
            dctcnf = json.loads(str(state))
            if dctcnf:
                srccnf = "source" in dctcnf.keys() or \
                    "configuration" in dctcnf.keys()
                stop = dctcnf["stop"] if "stop" in dctcnf.keys() else None
                start = dctcnf["start"] if "start" in dctcnf.keys() else None
                tool = dctcnf["tool"] if "tool" in dctcnf.keys() else None
                running = self.__sourcewg.isConnected()
                if srccnf or stop is True or start is True:
                    if self.__sourcewg.isConnected():
                        self.__sourcewg.toggleServerConnection()
                self.__applyoptionsfromdict(dctcnf)
                if not self.__sourcewg.isConnected():
                    if start is True:
                        self.__sourcewg.toggleServerConnection()
                    elif running and srccnf and stop is not True:
                        self.__sourcewg.toggleServerConnection()
                if tool:
                    QtCore.QTimer.singleShot(
                        10, self.__imagewg.showCurrentTool)

    def __applyoptionsfromdict(self, dctcnf):
        """ apply options

        :param dctcnf: commandline options
        :type dctcnf: :obj:`dict` <:obj:`str`, any >
        """
        if dctcnf:
            options = argparse.Namespace()
            for key, vl in dctcnf.items():
                setattr(options, key, vl)
            self.__applyoptions(options)
            if 'levels' not in dctcnf.keys():
                self.__levelswg.setAutoLevels(2)
            if 'bkgfile' not in dctcnf.keys():
                self.__bkgsubwg.checkBkgSubtraction(False)
                self.__dobkgsubtraction = None
            if 'maskfile' not in dctcnf.keys():
                self.__maskwg.noImage()
                self.__applymask = False

    def __applyoptions(self, options):
        """ apply options

        :param options: commandline options
        :type options: :class:`argparse.Namespace`
        :returns: start flag
        :rtype: :obj:`bool`
        """
        if hasattr(options, "doordevice") and options.doordevice is not None:
            self.__settings.doorname = str(options.doordevice)

        if hasattr(options, "analysisdevice") and \
           options.analysisdevice is not None:
            self.__settings.analysisdevice = str(options.analysisdevice)

        # load image file
        if hasattr(options, "imagefile") and options.imagefile is not None:
            oldname = self.__settings.imagename
            oldpath = self.__fieldpath
            oldgrowing = self.__growing
            try:
                self.__settings.imagename = str(options.imagefile)
                if ":/" in self.__settings.imagename:
                    self.__settings.imagename, self.__fieldpath =  \
                        self.__settings.imagename.split(":/", 1)
                else:
                    self.__fieldpath = None
                self.__growing = 0
                self._loadfile(fid=0)
            except Exception:
                self.__settings.imagename = oldname
                self.__fieldpath = oldpath
                self.__growing = oldgrowing

        # set image source
        if hasattr(options, "source") and options.source is not None:
            srcname = str(options.source)
            if srcname in self.__srcaliasnames.keys():
                self.__sourcewg.setSourceComboBoxByName(
                    self.__srcaliasnames[srcname])

        if hasattr(options, "configuration") and \
           options.configuration is not None:
            self.__sourcewg.configure(str(options.configuration))

        if hasattr(options, "bkgfile") and options.bkgfile is not None:
            self.__bkgsubwg.setBackground(str(options.bkgfile))

        if hasattr(options, "maskfile") and options.maskfile is not None:
            self.__maskwg.setMask(str(options.maskfile))

        if hasattr(options, "maskhighvalue") and \
           options.maskhighvalue is not None:
            self.__highvaluemaskwg.setMask(str(options.maskhighvalue))

        if hasattr(options, "transformation") and \
           options.transformation is not None:
            self.__trafowg.setTransformation(str(options.transformation))

        if hasattr(options, "filters"):
            if options.filters is True:
                self.__filterswg.setState(2)
            elif options.filters is False:
                self.__filterswg.setState(0)

        if hasattr(options, "scaling") and options.scaling is not None:
            self.__scalingwg.setScaling(str(options.scaling))

        if hasattr(options, "levels") and options.levels is not None:
            self.__levelswg.setLevels(str(options.levels))

        if hasattr(options, "autofactor") and options.autofactor is not None:
            self.__levelswg.setAutoFactor(str(options.autofactor))

        if hasattr(options, "gradient") and options.gradient is not None:
            self.__levelswg.setGradient(str(options.gradient))

        if hasattr(options, "tool") and options.tool is not None:
            tlname = str(options.tool)
            if tlname in self.__tlaliasnames.keys():
                self.__imagewg.setTool(self.__tlaliasnames[tlname])

        if hasattr(options, "tangodevice") and \
           TANGOCLIENT and options.tangodevice is not None:
            self.__tangoclient = controllerClient.ControllerClient(
                str(options.tangodevice))
            self.__tangoclient.energyChanged.connect(
                self.__imagewg.updateEnergy)
            self.__tangoclient.detectorDistanceChanged.connect(
                self.__imagewg.updateDetectorDistance)
            self.__tangoclient.beamCenterXChanged.connect(
                self.__imagewg.updateBeamCenterX)
            self.__tangoclient.beamCenterYChanged.connect(
                self.__imagewg.updateBeamCenterY)
            self.__tangoclient.detectorROIsChanged.connect(
                self.__imagewg.updateDetectorROIs)
            self.__imagewg.setTangoClient(self.__tangoclient)
            self.__tangoclient.subscribe()
            self.__tangoclient.lavueStateChanged.connect(
                self._updateLavueState)
        else:
            self.__tangoclient = None

        if hasattr(options, "viewrange") and options.viewrange is not None:
            self.__imagewg.setViewRange(str(options.viewrange))
        self.__sourcewg.updateLayout()
        if hasattr(options, "start"):
            return options.start is True
        else:
            return False

    def __loadSettings(self):
        """ loads settings from QSettings object
        """
        settings = QtCore.QSettings()
        if self.parent() is not None:
            self.parent().restoreGeometry(settings.value(
                "Layout/Geometry", type=QtCore.QByteArray))
        self.restoreGeometry(settings.value(
            "Layout/DialogGeometry", type=QtCore.QByteArray))
        status = self.__settings.load(settings)
        self.__levelswg.updateCustomGradients(
            self.__settings.customGradients())
        for topic, value in status:
            text = messageBox.MessageBox.getText(topic)
            messageBox.MessageBox.warning(self, topic, text, str(value))

        self.__setSardana(self.__settings.sardana)
        self.__imagewg.setAspectLocked(self.__settings.aspectlocked)
        self.__imagewg.setAutoDownSample(self.__settings.autodownsample)
        self._assessTransformation(self.__trafoname)
        self.__datasource.setTimeOut(self.__settings.timeout)
        dataFetchThread.GLOBALREFRESHRATE = self.__settings.refreshrate
        self.__imagewg.setStatsWOScaling(self.__settings.statswoscaling)
        self.__imagewg.setROIsColors(self.__settings.roiscolors)

        self.__updateSource()

        self.__statswg.changeView(self.__settings.showstats)
        self.__viewFrameRate(self.__settings.showframerate)
        self.__levelswg.changeView(
            self.__settings.showhisto,
            self.__settings.showlevels,
            self.__settings.showaddhisto
        )
        self.__prepwg.changeView(
            self.__settings.showmask,
            self.__settings.showsub,
            self.__settings.showtrans,
            self.__settings.showhighvaluemask,
            self.__settings.showfilters
        )
        self.__scalingwg.changeView(self.__settings.showscale)
        self.__levelswg.changeView()
        if self.__lazyimageslider != self.__settings.lazyimageslider:
            self.__switchlazysignals(self.__settings.lazyimageslider)

    def __viewFrameRate(self, status):
        """ show/hide frame rate
        :param status: True for show and False for hide
        :type status: :obj:`bool`
        """
        if status:
            self.__ui.framerateLineEdit.show()
        else:
            self.__ui.framerateLineEdit.hide()

    @QtCore.pyqtSlot()
    def _storeSettings(self):
        """ stores settings in QSettings object
        """
        settings = QtCore.QSettings()
        if self.parent() is not None and self.parent().parent() is not None:
            settings.setValue(
                "Layout/Geometry",
                QtCore.QByteArray(self.parent().parent().saveGeometry()))
        settings.setValue(
            "Layout/DialogGeometry",
            QtCore.QByteArray(self.saveGeometry()))

        self.__settings.refreshrate = dataFetchThread.GLOBALREFRESHRATE
        self.__settings.sardana = True if self.__sardana is not None else False
        self.__settings.store(settings)

    @QtCore.pyqtSlot(bool)
    def _setAspectLocked(self, status):
        self.__settings.aspectlocked = status
        self.__imagewg.setAspectLocked(self.__settings.aspectlocked)

    def closeEvent(self, event):
        """ stores the setting before finishing the application

        :param event: close event
        :type event:  :class:`pyqtgraph.QtCore.QEvent`:
        """
        if self.__tangoclient:
            self.__tangoclient.unsubscribe()
        self._storeSettings()
        self.__settings.secstream = False
        try:
            self.__dataFetcher.newDataNameFetched.disconnect(self._getNewData)
        except Exception:
            pass
        # except Exception as e:
        #     print (str(e))

        if self.__sourcewg.isConnected():
            self.__sourcewg.toggleServerConnection()
        self._disconnectSource()
        self.__dataFetcher.stop()
        self.__dataFetcher.wait()
        self.__settings.seccontext.destroy()
        QtGui.QApplication.closeAllWindows()
        if event is not None:
            event.accept()

    @QtCore.pyqtSlot(int)
    @QtCore.pyqtSlot()
    def _loadfile(self, fid=None):
        """ reloads the image file

        :param fid: frame id
        :type fid: :obj:`int`
         """
        self._reloadfile(fid, showmessage=True)

    @QtCore.pyqtSlot(str)
    @QtCore.pyqtSlot()
    def _spinreloadfile(self, fid=None, showmessage=False):
        """ reloads the image file

        :param fid: frame id
        :type fid: :obj:`int`
        :param showmessage: no image message
        :type showmessage: :obj:`bool`
         """
        try:
            if not self.__reloadflag:
                self.__reloadflag = True
                if fid is None:
                    fid = self.__ui.frameLineEdit.text()
                try:
                    fid = int(fid)
                    self._reloadfile(fid, showmessage)
                except Exception:
                    pass
                time.sleep(0.1)
        finally:
            self.__reloadflag = False

    @QtCore.pyqtSlot()
    def _lowerframepushed(self):
        step = self.__ui.framestepSpinBox.value()
        try:
            frame = int(self.__ui.frameLineEdit.text())
        except Exception:
            frame = self.__frame or 0
        nframe = frame - step
        if frame >= 0:
            nframe = max(nframe, 0)
        self.__ui.frameLineEdit.setText(str(nframe))

    @QtCore.pyqtSlot()
    def _higherframepushed(self):
        step = self.__ui.framestepSpinBox.value()
        try:
            frame = int(self.__ui.frameLineEdit.text())
        except Exception:
            frame = self.__frame or 0
        nframe = frame + step
        if frame < 0:
            nframe = min(nframe, -1)
        self.__ui.frameLineEdit.setText(str(nframe))

    @QtCore.pyqtSlot()
    def _sliderreloadfilelazy(self):
        """ reloads the image file or
        if lazy flag it displays only splider value
        """
        if self.__lazyimageslider:

            fid = self.__ui.frameHorizontalSlider.value()
            self.__ui.frameLineEdit.textChanged.disconnect(
                self._spinreloadfile)
            self.__ui.frameLineEdit.setText(str(fid))
            self.__ui.frameLineEdit.textChanged.connect(
                self._spinreloadfile)
        else:
            self._sliderreloadfile()

    @QtCore.pyqtSlot(int)
    @QtCore.pyqtSlot()
    def _sliderreloadfile(self, fid=None, showmessage=False):
        """ reloads the image file

        :param fid: frame id
        :type fid: :obj:`int`
        :param showmessage: no image message
        :type showmessage: :obj:`bool`
         """
        try:
            if not self.__reloadflag:
                self.__reloadflag = True
                if fid is None:
                    fid = self.__ui.frameHorizontalSlider.value()
                self._reloadfile(fid, showmessage)
        finally:
            self.__reloadflag = False

    @QtCore.pyqtSlot(int)
    @QtCore.pyqtSlot()
    def _reloadfile(self, fid=None, showmessage=False):
        """ reloads the image file

        :param fid: frame id
        :type fid: :obj:`int`
        :param showmessage: no image message
        :type showmessage: :obj:`bool`
         """
        newimage = None
        metadata = None
        if fid is None:
            fileDialog = QtGui.QFileDialog()
            fileout = fileDialog.getOpenFileName(
                    self, 'Load file', self.__settings.imagename or '.')
            if isinstance(fileout, tuple):
                imagename = str(fileout[0])
            else:
                imagename = str(fileout)
        else:
            self.__frame = int(fid)
            imagename = self.__settings.imagename
        if imagename:
            if imagename.endswith(".nxs") or imagename.endswith(".h5") \
               or imagename.endswith(".nx") or imagename.endswith(".ndf"):
                try:
                    self.__settings.imagename = imagename
                    handler = imageFileHandler.NexusFieldHandler(
                        str(self.__settings.imagename))
                    fields = handler.findImageFields()
                except Exception as e:
                    print(str(e))
                    fields = None
                if fields:
                    if fid is None or self.__fieldpath is None:
                        imgfield = imageField.ImageField(self)
                        imgfield.fields = fields
                        imgfield.createGUI()
                        if imgfield.exec_():
                            self.__fieldpath = imgfield.field
                            self.__growing = imgfield.growing
                            self.__frame = imgfield.frame
                        else:
                            return
                    currentfield = fields[self.__fieldpath]
                    try:
                        newimage = handler.getImage(
                            currentfield["node"],
                            self.__frame, self.__growing, refresh=False)
                    except Exception as e:
                        print(str(e))

                    metadata = handler.getMetaData(currentfield["node"])
                    # if metadata:
                    #     print("Metadata = %s" % str(metadata))
                    self.__ui.frameLineEdit.textChanged.disconnect(
                        self._spinreloadfile)
                    self.__disconnectslider()
                    self.__ui.frameHorizontalSlider.valueChanged.disconnect(
                        self._sliderreloadfilelazy)
                    try:
                        if len(currentfield["shape"]) < 3:
                            gsize = 0
                        else:
                            gsize = currentfield["shape"][self.__growing] - 1
                        if gsize >= 0:
                            self.__ui.frameLineEdit.setToolTip(
                                "current frame (max: %s)" % gsize)
                            self.__ui.frameHorizontalSlider.setMaximum(gsize)
                            self.__ui.frameHorizontalSlider.setToolTip(
                                "current frame (max: %s)" % gsize)
                        else:
                            self.__ui.frameLineEdit.setToolTip("current frame")
                            self.__ui.frameHorizontalSlider.setMaximum(0)
                            self.__ui.frameHorizontalSlider.setToolTip(
                                "current frame")
                    except Exception:
                        self.__ui.frameLineEdit.setToolTip("current frame")
                    while newimage is None and self.__frame > 0:
                        self.__frame -= 1
                        self.__updateframeview(True)
                        newimage = handler.getImage(
                            currentfield["node"],
                            self.__frame, self.__growing, refresh=False)
                    self.__ui.frameLineEdit.textChanged.connect(
                        self._spinreloadfile)
                    self.__ui.frameHorizontalSlider.valueChanged.connect(
                        self._sliderreloadfilelazy)
                    self.__connectslider()
                else:
                    if showmessage:
                        text = messageBox.MessageBox.getText(
                            "lavue: Image %s cannot be loaded"
                            % self.__settings.imagename)
                        messageBox.MessageBox.warning(
                            self,
                            "lavue: File %s cannot be loaded"
                            % self.__settings.imagename,
                            "File %s without images"
                            % self.__settings.imagename)
                    return
                if imagename:
                    imagename = "%s:/%s" % (
                        self.__settings.imagename,
                        currentfield["nexus_path"])
                    self.__updateframeview(True)
            else:
                self.__fieldpath = None
                self.__settings.imagename = imagename
                try:
                    fh = imageFileHandler.ImageFileHandler(
                        str(self.__settings.imagename))
                    newimage = fh.getImage()
                    metadata = fh.getMetaData()
                    self.__updateframeview()
                except Exception as e:
                    print(str(e))
            if newimage is not None:
                self.__metadata = metadata
                if metadata:
                    self.__mdata = json.loads(str(metadata))
                    if self.__settings.geometryfromsource:
                        self.__settings.updateMetaData(**self.__mdata)
                        self.__imagewg.updateCenter(
                            self.__settings.centerx, self.__settings.centery)
                        self.__imagewg.mouseImagePositionChanged.emit()
                        self.__imagewg.geometryChanged.emit()
                else:
                    self.__mdata = {}
                self.__imagename = imagename
                self.__rawimage = np.transpose(newimage)
                self._plot()
                if fid is None:
                    self.__imagewg.autoRange()
            else:
                text = messageBox.MessageBox.getText(
                    "lavue: File %s cannot be loaded"
                    % self.__settings.imagename)
                messageBox.MessageBox.warning(
                    self,
                    "lavue: File %s cannot be loaded"
                    % self.__settings.imagename,
                    text,
                    str("lavue: File %s cannot be loaded"
                        % self.__settings.imagename))

    @QtCore.pyqtSlot()
    def _configuration(self):
        """ launches the configuration dialog
        """
        cnfdlg = configDialog.ConfigDialog(self)
        if not self.__settings.doorname and self.__sardana is not None:
            self.__settings.doorname = self.__sardana.getDeviceName("Door")
        cnfdlg.sardana = True if self.__sardana is not None else False
        cnfdlg.door = self.__settings.doorname
        cnfdlg.addrois = self.__settings.addrois
        cnfdlg.orderrois = self.__settings.orderrois
        cnfdlg.showsub = self.__settings.showsub
        cnfdlg.showtrans = self.__settings.showtrans
        cnfdlg.showscale = self.__settings.showscale
        cnfdlg.showlevels = self.__settings.showlevels
        cnfdlg.showframerate = self.__settings.showframerate
        cnfdlg.showhisto = self.__settings.showhisto
        cnfdlg.showaddhisto = self.__settings.showaddhisto
        cnfdlg.showmask = self.__settings.showmask
        cnfdlg.showhighvaluemask = self.__settings.showhighvaluemask
        cnfdlg.showfilters = self.__settings.showfilters
        cnfdlg.showstats = self.__settings.showstats
        cnfdlg.filters = self.__settings.filters
        cnfdlg.secautoport = self.__settings.secautoport
        cnfdlg.secport = self.__settings.secport
        cnfdlg.hidraport = self.__settings.hidraport
        cnfdlg.secstream = self.__settings.secstream
        cnfdlg.zeromask = self.__settings.zeromask
        cnfdlg.refreshrate = dataFetchThread.GLOBALREFRESHRATE
        cnfdlg.timeout = self.__settings.timeout
        cnfdlg.aspectlocked = self.__settings.aspectlocked
        cnfdlg.autodownsample = self.__settings.autodownsample
        cnfdlg.keepcoords = self.__settings.keepcoords
        cnfdlg.lazyimageslider = self.__settings.lazyimageslider
        cnfdlg.statswoscaling = self.__settings.statswoscaling
        cnfdlg.zmqtopics = self.__settings.zmqtopics
        cnfdlg.autozmqtopics = self.__settings.autozmqtopics
        cnfdlg.interruptonerror = self.__settings.interruptonerror
        cnfdlg.dirtrans = self.__settings.dirtrans
        cnfdlg.tangoattrs = self.__settings.tangoattrs
        cnfdlg.doocsprops = self.__settings.doocsprops
        cnfdlg.tangoevattrs = self.__settings.tangoevattrs
        cnfdlg.tangofileattrs = self.__settings.tangofileattrs
        cnfdlg.tangodirattrs = self.__settings.tangodirattrs
        cnfdlg.httpurls = self.__settings.httpurls
        cnfdlg.zmqservers = self.__settings.zmqservers
        cnfdlg.nxslast = self.__settings.nxslast
        cnfdlg.nxsopen = self.__settings.nxsopen
        cnfdlg.sendrois = self.__settings.sendrois
        cnfdlg.showallrois = self.__settings.showallrois
        cnfdlg.storegeometry = self.__settings.storegeometry
        cnfdlg.geometryfromsource = self.__settings.geometryfromsource
        cnfdlg.roiscolors = self.__settings.roiscolors
        cnfdlg.sourcedisplay = self.__settings.sourcedisplay
        cnfdlg.imagesources = self.__settings.imagesources
        cnfdlg.imagesourcenames = self.__srcaliasnames
        cnfdlg.toolwidgets = self.__settings.toolwidgets
        cnfdlg.toolwidgetnames = {}
        cnfdlg.availimagesources = self.__allsourcealiases
        cnfdlg.availtoolwidgets = self.__alltoolaliases
        cnfdlg.defdetservers = self.__settings.defdetservers
        cnfdlg.detservers = json.dumps(self.__mergeDetServers(
            HIDRASERVERLIST if cnfdlg.defdetservers else {"pool": []},
            json.loads(self.__settings.detservers)))
        cnfdlg.createGUI()
        if cnfdlg.exec_():
            self.__updateConfig(cnfdlg)
            self._storeSettings()

    def __updateConfig(self, dialog):
        """ updates the configuration
        """
        self.__settings.doorname = dialog.door
        if dialog.sardana != (True if self.__sardana is not None else False):
            self.__setSardana(dialog.sardana)
            self.__settings.sardana = dialog.sardana
        self.__settings.addrois = dialog.addrois
        self.__settings.orderrois = dialog.orderrois

        if self.__settings.showsub != dialog.showsub:
            self.__prepwg.changeView(showsub=dialog.showsub)
            self.__settings.showsub = dialog.showsub
        if self.__settings.showtrans != dialog.showtrans:
            self.__prepwg.changeView(showtrans=dialog.showtrans)
            self.__settings.showtrans = dialog.showtrans
        if self.__settings.showmask != dialog.showmask:
            self.__settings.showmask = dialog.showmask
            self.__prepwg.changeView(dialog.showmask)
        if self.__settings.showhighvaluemask != dialog.showhighvaluemask:
            self.__settings.showhighvaluemask = dialog.showhighvaluemask
            self.__prepwg.changeView(
                showhighvaluemask=dialog.showhighvaluemask)
        if self.__settings.showfilters != dialog.showfilters:
            self.__settings.showfilters = dialog.showfilters
            self.__prepwg.changeView(
                showfilters=dialog.showfilters)

        if self.__settings.showscale != dialog.showscale:
            self.__scalingwg.changeView(dialog.showscale)
            self.__settings.showscale = dialog.showscale

        if self.__settings.showlevels != dialog.showlevels:
            self.__levelswg.changeView(showlevels=dialog.showlevels)
            self.__settings.showlevels = dialog.showlevels

        if self.__settings.showframerate != dialog.showframerate:
            self.__settings.showframerate = dialog.showframerate
            self.__viewFrameRate(self.__settings.showframerate)
        if self.__settings.showhisto != dialog.showhisto:
            self.__levelswg.changeView(dialog.showhisto)
            self.__settings.showhisto = dialog.showhisto
        if self.__settings.showaddhisto != dialog.showaddhisto:
            self.__levelswg.changeView(showadd=dialog.showaddhisto)
            self.__settings.showaddhisto = dialog.showaddhisto
        if self.__settings.showstats != dialog.showstats:
            self.__statswg.changeView(dialog.showstats)
            self.__settings.showstats = dialog.showstats
        if self.__settings.imagesources != dialog.imagesources:
            self.__settings.imagesources = dialog.imagesources
            self.__sourcewg.updateSourceComboBox(
                [self.__srcaliasnames[twn]
                 for twn in json.loads(self.__settings.imagesources)],
                self.__sourcewg.currentDataSourceName())
        if self.__settings.toolwidgets != dialog.toolwidgets:
            self.__settings.toolwidgets = dialog.toolwidgets
            self.__imagewg.updateToolComboBox(
                [self.__tlaliasnames[twn]
                 for twn in json.loads(self.__settings.toolwidgets)],
                self.__imagewg.currentTool())
        dataFetchThread.GLOBALREFRESHRATE = dialog.refreshrate
        replot = False

        if self.__settings.refreshrate != dialog.refreshrate:
            self.__settings.refreshrate = dialog.refreshrate
            self.__updateframeratetip(self.__settings.refreshrate)
        if self.__settings.filters != dialog.filters:
            self.__resetFilters(dialog.filters)
            replot = True

        if self.__settings.secstream != dialog.secstream or (
                self.__settings.secautoport != dialog.secautoport
                and dialog.secautoport):
            if self.__settings.secstream:
                # workaround for a bug in libzmq
                try:
                    self.__settings.secsocket.unbind(
                        self.__settings.secsockopt)
                except Exception:
                    pass
                if self.__sourcewg.isConnected():
                    self.__sourcewg.connectSuccess(None)
            if dialog.secstream:
                if dialog.secautoport:
                    self.__settings.secsockopt = b"tcp://*:*"
                    self.__settings.secsocket.bind(self.__settings.secsockopt)
                    dialog.secport = unicode(
                        self.__settings.secsocket.getsockopt(
                            zmq.LAST_ENDPOINT)).split(":")[-1]
                else:
                    self.__settings.secsockopt = b"tcp://*:%s" % dialog.secport
                    self.__settings.secsocket.bind(self.__settings.secsockopt)
                if self.__sourcewg.isConnected():
                    self.__sourcewg.connectSuccess(dialog.secport)
        self.__settings.secautoport = dialog.secautoport
        self.__settings.secport = dialog.secport
        self.__settings.timeout = dialog.timeout
        self.__datasource.setTimeOut(self.__settings.timeout)
        self.__settings.aspectlocked = dialog.aspectlocked
        self.__imagewg.setAspectLocked(self.__settings.aspectlocked)
        self.__settings.autodownsample = dialog.autodownsample
        self.__imagewg.setAutoDownSample(self.__settings.autodownsample)
        remasking = False
        if self.__settings.keepcoords != dialog.keepcoords:
            self.__settings.keepcoords = dialog.keepcoords
            self._assessTransformation(self.__trafoname)
            replot = True
        if self.__settings.lazyimageslider != dialog.lazyimageslider:
            self.__settings.lazyimageslider = dialog.lazyimageslider
            self.__switchlazysignals(self.__settings.lazyimageslider)

        self.__settings.secstream = dialog.secstream
        self.__settings.storegeometry = dialog.storegeometry
        self.__settings.geometryfromsource = dialog.geometryfromsource
        self.__settings.interruptonerror = dialog.interruptonerror
        self.__settings.sourcedisplay = dialog.sourcedisplay
        setsrc = False
        if self.__settings.hidraport != dialog.hidraport:
            self.__settings.hidraport = dialog.hidraport
            setsrc = True
        if self.__settings.dirtrans != dialog.dirtrans:
            self.__settings.dirtrans = dialog.dirtrans
            setsrc = True
        if self.__settings.tangoattrs != dialog.tangoattrs:
            self.__settings.tangoattrs = dialog.tangoattrs
            setsrc = True
        if self.__settings.doocsprops != dialog.doocsprops:
            self.__settings.doocsprops = dialog.doocsprops
            setsrc = True
        if self.__settings.tangoevattrs != dialog.tangoevattrs:
            self.__settings.tangoevattrs = dialog.tangoevattrs
            setsrc = True
        if self.__settings.tangofileattrs != dialog.tangofileattrs:
            self.__settings.tangofileattrs = dialog.tangofileattrs
            setsrc = True
        if self.__settings.tangodirattrs != dialog.tangodirattrs:
            self.__settings.tangodirattrs = dialog.tangodirattrs
            setsrc = True
        if self.__settings.httpurls != dialog.httpurls:
            self.__settings.httpurls = dialog.httpurls
            setsrc = True
        if self.__settings.zmqservers != dialog.zmqservers:
            self.__settings.zmqservers = dialog.zmqservers
            setsrc = True
        if self.__settings.zmqtopics != dialog.zmqtopics:
            self.__settings.zmqtopics = dialog.zmqtopics
            setsrc = True
        if self.__settings.defdetservers != dialog.defdetservers:
            self.__settings.defdetservers = dialog.defdetservers
            setsrc = True
        detservers = json.dumps(self.__retrieveUserDetServers(
            HIDRASERVERLIST if dialog.defdetservers else {"pool": []},
            json.loads(dialog.detservers)))
        if self.__settings.detservers != detservers:
            self.__settings.detservers = detservers
            setsrc = True
        if self.__settings.autozmqtopics != dialog.autozmqtopics:
            self.__settings.autozmqtopics = dialog.autozmqtopics
            setsrc = True
        if self.__settings.nxsopen != dialog.nxsopen:
            self.__settings.nxsopen = dialog.nxsopen
            setsrc = True
        if self.__settings.nxslast != dialog.nxslast:
            self.__settings.nxslast = dialog.nxslast
            setsrc = True
        if self.__settings.sendrois != dialog.sendrois:
            self.__settings.sendrois = dialog.sendrois
        if self.__settings.showallrois != dialog.showallrois:
            self.__settings.showallrois = dialog.showallrois
        if setsrc:
            self.__updateSource()

        self.__settings.statswoscaling = dialog.statswoscaling
        replot = replot or \
            self.__imagewg.setStatsWOScaling(
                self.__settings.statswoscaling)

        if self.__settings.zeromask != dialog.zeromask:
            self.__settings.zeromask = dialog.zeromask
            remasking = True
            replot = True

        if self.__settings.roiscolors != dialog.roiscolors:
            self.__settings.roiscolors = dialog.roiscolors
            self.__imagewg.setROIsColors(self.__settings.roiscolors)

        if remasking:
            self.__remasking()

        if replot:
            self._plot()

    def __mergeDetServers(self, detserverdict, detserverlist):
        """ merges detector servers from
        a dictionary and a list

        :param detserverdict: detector server dictionary
        :type detserverdict: :obj:`dict` <:obj:`str`, :obj:`list`<:obj:`str`>>
        :param detserverklist: detector server list
        :type detserverlist: :obj:`list` < :obj:`str`>
        :returns: merged detector server list
        :rtype: :obj:`list` < :obj:`str`>

        """
        servers = set(detserverdict["pool"])
        if self.__targetname in detserverdict.keys():
            servers.update(detserverdict[self.__targetname])
        if detserverlist:
            servers.update(detserverlist)
        return list(servers)

    def __retrieveUserDetServers(self, detserverdict, detserverlist):
        """ retrives user detector servers from a list
             which are not in a dictionary

        :param detserverdict: detector server dictionary
        :type detserverdict: :obj:`dict` <:obj:`str`, :obj:`list`<:obj:`str`>>
        :param detserverklist: detector server list
        :type detserverlist: :obj:`list` < :obj:`str`>
        :returns: user detector server list
        :rtype: :obj:`list` < :obj:`str`>
        """
        servers = []
        if detserverlist:
            defservers = set(detserverdict["pool"])
            if self.__targetname in detserverdict.keys():
                defservers.update(detserverdict[self.__targetname])
            servers = list(set(detserverlist) - defservers)
        return list(servers)

    @QtCore.pyqtSlot(str)
    def _setSourceConfiguration(self, sourceConfiguration):
        """ sets the source configuration

        :param sourceConfiguration: source configuration string
        :type sourceConfiguration: :obj:`str
        """
        self.__sourceconfiguration = sourceConfiguration
        if self.__sourcewg.currentDataSource() == \
           str(type(self.__datasource).__name__):
            self.__datasource.setConfiguration(self.__sourceconfiguration)

    @QtCore.pyqtSlot(str)
    def _switchSourceDisplay(self, label):
        """switches source display parameters

        :param sourceConfiguration: source configuration string
        :type sourceConfiguration: :obj:`str
        """
        if self.__sourcelabel != str(label) and label and \
           self.__settings.sourcedisplay:
            self.__sourcelabel = str(label)
            values = self.__settings.sourceDisplay(
                self.__sourcelabel)
            self.__applyoptionsfromdict(values)

    def __setSourceLabel(self):
        """sets source display parameters
        """
        if self.__sourcelabel and self.__settings.sourcedisplay:
            label = self.__sourcelabel
            values = {}
            values["transformation"] = self.__trafowg.transformation()
            values["tool"] = self.__imagewg.tool()
            values["scaling"] = self.__scalingwg.currentScaling()
            if not self.__levelswg.isAutoLevel():
                values["levels"] = self.__levelswg.levels()
                values["autofactor"] = ""
            else:
                values["autofactor"] = self.__levelswg.autoFactor()
            values["gradient"] = self.__levelswg.gradient()
            if self.__bkgsubwg.isBkgSubApplied():
                values["bkgfile"] = str(self.__settings.bkgimagename)
            if self.__maskwg.isMaskApplied():
                values["maskfile"] = str(self.__settings.maskimagename)
            mvalue = self.__highvaluemaskwg.mask()
            if mvalue is not None:
                values["maskhighvalue"] = str(mvalue)
            else:
                values["maskhighvalue"] = ""
            values["viewrange"] = self.__imagewg.viewRange()
            self.__settings.setSourceDisplay(label, values)

    def __setSardana(self, status):
        """ sets the sardana utils
        """
        if status is False:
            self.__sardana = None
        else:
            self.__sardana = sardanaUtils.SardanaUtils()
        self.__imagewg.setSardanaUtils(self.__sardana)

    @QtCore.pyqtSlot(int)
    def _onSourceChanged(self, status):
        if status:
            self.__datasource = getattr(
                isr, self.__sourcewg.currentDataSource())(
                    self.__settings.timeout)
            self.__sourcewg.updateMetaData(**self.__datasource.getMetaData())

    @QtCore.pyqtSlot(int)
    def _updateSource(self, status):
        """ update the current source

        :param status: current source status id
        :type status: :obj:`int`
        """
        if status:
            self.__datasource.setTimeOut(self.__settings.timeout)
            self.__dataFetcher.setDataSource(self.__datasource)
            if self.__sourceconfiguration:
                self.__datasource.setConfiguration(self.__sourceconfiguration)
            self.__sourcewg.updateMetaData(**self.__datasource.getMetaData())
        self._stateUpdated.emit(bool(status))

    @QtCore.pyqtSlot(bool)
    def _replot(self, autorange):
        """ The main command of the live viewer class:
        draw a numpy array with the given name and autoRange.
        """
        self._plot()
        if autorange:
            self.__imagewg.autoRange()

    @QtCore.pyqtSlot()
    def _plot(self):
        """ The main command of the live viewer class:
        draw a numpy array with the given name.
        """
        # apply user filters
        self.__applyFilters()

        if "channellabels" in self.__mdata:
            self.__levelswg.updateChannelLabels(self.__mdata["channellabels"])

        # prepare or preprocess the raw image if present:
        self.__prepareImage()

        # perform transformation
        # (crdtranspose, crdleftrightflip, crdupdownflip,
        # orgtranspose, orgleftrightflip, orgupdownflip)
        allcrds = self.__transform()
        self.__imagewg.setTransformations(*allcrds)
        # use the internal raw image to create a display image with chosen
        # scaling
        self.__scale(self.__scalingwg.currentScaling())
        # calculate and update the stats for this
        self.__calcUpdateStats()
        # calls internally the plot function of the plot widget
        if self.__imagename is not None and self.__scaledimage is not None:
            self.__ui.fileNameLineEdit.setText(self.__imagename)
        self.__imagewg.plot(
            self.__scaledimage,
            self.__displayimage
            if self.__settings.statswoscaling else self.__scaledimage)
        if self.__settings.showhisto and self.__updatehisto:
            self.__levelswg.updateHistoImage()
            self.__updatehisto = False

    @QtCore.pyqtSlot()
    def _calcUpdateStatsSec(self):
        """ calcuates statistics without  sending security stream
        """
        self.__calcUpdateStats(secstream=False)

    def __calcUpdateStats(self, secstream=True):
        """ calcuates statistics

        :param secstream: send security stream flag
        :type secstream: :obj:`bool`
        """
        # calculate the stats for this

        auto = self.__levelswg.isAutoLevel()
        stream = secstream and self.__settings.secstream and \
            self.__scaledimage is not None
        display = self.__settings.showstats
        maxval, meanval, varval, minval, maxrawval, maxsval = \
            self.__calcStats(
                (stream or display,
                 stream or display,
                 display,
                 stream or auto,
                 stream,
                 auto)
            )
        smaxval = "%.4f" % maxval
        smeanval = "%.4f" % meanval
        svarval = "%.4f" % varval
        sminval = "%.3f" % minval
        smaxrawval = "%.4f" % maxrawval
        calctime = time.time()
        currentscaling = self.__scalingwg.currentScaling()
        # update the statistics display
        if stream:
            messagedata = {
                'command': 'alive', 'calctime': calctime, 'maxval': smaxval,
                'maxrawval': smaxrawval,
                'minval': sminval, 'meanval': smeanval, 'pid': self.__apppid,
                'scaling': (
                    'linear'
                    if self.__settings.statswoscaling
                    else currentscaling)}
            topic = 10001
            message = "%d %s" % (
                topic, str(json.dumps(messagedata)).encode("ascii"))
            self.__settings.secsocket.send_string(str(message))

        self.__statswg.updateStatistics(
            smeanval, smaxval, svarval,
            'linear' if self.__settings.statswoscaling else currentscaling)

        # if needed, update the level display
        if auto:
            self.__levelswg.updateAutoLevels(minval, maxsval)

    @QtCore.pyqtSlot()
    def _startPlotting(self):
        """ mode changer: start plotting mode.
        It starts plotting if the connection is really established.
        """
        #
        if not self.__sourcewg.isConnected():
            return
        self.__dataFetcher.changeStatus(True)
        if not self.__dataFetcher.isRunning():
            self.__dataFetcher.start()

    @QtCore.pyqtSlot()
    def _stopPlotting(self):
        """ mode changer: stop plotting mode
        """

        if self.__dataFetcher is not None:
            self.__dataFetcher.changeStatus(False)
            pass

    @QtCore.pyqtSlot(int)
    def _connectSource(self, status):
        """  calls the connect function of the source interface

        :param status: current source status id
        :type status: :obj:`int`
        """
        self._updateSource(status)
        if self.__datasource is None:
            messageBox.MessageBox.warning(
                self, "lavue: No data source is defined",
                "No data source is defined",
                "Please select the image source")

        if not self.__datasource.connect():
            self.__sourcewg.connectFailure()
            messageBox.MessageBox.warning(
                self, "lavue: The %s connection could not be established"
                % type(self.__datasource).__name__,
                "The %s connection could not be established"
                % type(self.__datasource).__name__,
                str(self.__datasource.errormessage))
        else:
            self.__sourcewg.connectSuccess(
                self.__settings.secport if self.__settings.secstream else None)
        if self.__settings.secstream:
            calctime = time.time()
            messagedata = {
                'command': 'start', 'calctime': calctime, 'pid': self.__apppid}
            topic = 10001
            # print(str(messagedata))
            self.__settings.secsocket.send_string("%d %s" % (
                topic, str(json.dumps(messagedata)).encode("ascii")))
        self.__updatehisto = True
        self.__setSourceLabel()
        self._startPlotting()

    @QtCore.pyqtSlot()
    def _disconnectSource(self):
        """ calls the disconnect function of the source interface
        """
        self._stopPlotting()
        self.__datasource.disconnect()
        self.__imagename = None
        self.__imagename = None
        if self.__settings.secstream:
            calctime = time.time()
            messagedata = {
                'command': 'stop', 'calctime': calctime, 'pid': self.__apppid}
            # print(str(messagedata))
            topic = 10001
            self.__settings.secsocket.send_string("%d %s" % (
                topic, str(json.dumps(messagedata)).encode("ascii")))
        self._updateSource(0)
        self.__setSourceLabel()
        # self.__datasource = None

    @QtCore.pyqtSlot(str, str)
    def _getNewData(self, name, metadata=None):
        """ checks if data is there at all

        :param name: image name
        :type name: :obj:`str`
        :param metadata: JSON dictionary with metadata
        :type metadata: :obj:`str`
        """

        name, rawimage, metadata = self.__exchangelist.readData()

        if str(self.__imagename).strip() == str(name).strip() and not metadata:
            self.__dataFetcher.ready()
            return
        if name == "__ERROR__":
            if self.__settings.interruptonerror:
                if self.__sourcewg.isConnected():
                    self.__sourcewg.toggleServerConnection()
                errortext = rawimage
                messageBox.MessageBox.warning(
                    self, "lavue: Error in reading data",
                    "Viewing will be interrupted", str(errortext))
            else:
                self.__sourcewg.setErrorStatus(name)
            self.__dataFetcher.ready()
            return
        self.__sourcewg.setErrorStatus("")

        if name is None:
            self.__dataFetcher.ready()
            return
        # first time:
        if str(self.__metadata) != str(metadata) and str(metadata).strip():
            imagename, self.__metadata = name, metadata
            if str(imagename).strip() and \
               not isinstance(rawimage, basestring):
                if not hasattr(rawimage, "size") or rawimage.size != 0:
                    self.__imagename = imagename
                    self.__rawimage = rawimage
            try:
                self.__mdata = json.loads(str(metadata))
                if isinstance(self.__mdata, dict):
                    resdata = dict((k, v) for (k, v) in self.__mdata.items()
                                   if k in self.__allowedmdata)
                    wgdata = dict((k, v) for (k, v) in self.__mdata.items()
                                  if k in self.__allowedwgdata)
                    if wgdata:
                        self.__imagewg.updateMetaData(**wgdata)
                    if resdata:
                        self.__sourcewg.updateMetaData(**resdata)
                    if self.__settings.geometryfromsource:
                        self.__settings.updateMetaData(**self.__mdata)
                        self.__imagewg.updateCenter(
                            self.__settings.centerx, self.__settings.centery)
                        self.__imagewg.mouseImagePositionChanged.emit()
                        self.__imagewg.geometryChanged.emit()
            except Exception as e:
                print(str(e))
        elif str(name).strip():
            if self.__imagename is None or str(self.__imagename) != str(name):
                self.__imagename, self.__metadata \
                    = name, metadata
                if not isinstance(rawimage, basestring):
                    if not hasattr(rawimage, "size") or rawimage.size != 0:
                        self.__rawimage = rawimage
        if not str(metadata).strip():
            self.__mdata = {}

        self.__updateframeview()
        self.__currenttime = time.time()
        if self.__settings.showframerate and self.__lasttime:
            self.__updateframerate(self.__currenttime - self.__lasttime)
        self.__lasttime = self.__currenttime

        self._plot()
        QtCore.QCoreApplication.processEvents()
        self.__dataFetcher.ready()

    def __updateframeview(self, status=False):
        if status:
            if self.__frame is not None:
                self.__ui.frameLineEdit.setText(str(self.__frame))
                if self.__frame >= 0:
                    self.__ui.frameHorizontalSlider.setValue(self.__frame)
                else:
                    self.__ui.frameHorizontalSlider.setValue(
                        self.__ui.frameHorizontalSlider.maximum())
                self.__ui.framestepSpinBox.show()
                self.__ui.framestepLabel.show()
                self.__ui.lowerframePushButton.show()
                self.__ui.higherframePushButton.show()
                self.__ui.frameLineEdit.show()
            self.__ui.frameHorizontalSlider.show()
        else:
            self.__fieldpath = None
            self.__ui.lowerframePushButton.hide()
            self.__ui.higherframePushButton.hide()
            self.__ui.framestepSpinBox.hide()
            self.__ui.frameLineEdit.hide()
            self.__ui.framestepLabel.hide()
            self.__ui.frameHorizontalSlider.hide()

    def __updateframerate(self, ratetime):
        if ratetime:
            fr = 1.0/float(ratetime)
            if fr >= 9.9:
                self.__ui.framerateLineEdit.setText("%.0f Hz" % fr)
            else:
                self.__ui.framerateLineEdit.setText("%.1f Hz" % fr)
        else:
            self.__ui.framerateLineEdit.setText("")

    def __updateframeratetip(self, ratetime):
        if ratetime:
            fr = 1.0/float(ratetime)
            if fr >= 9.9:
                self.__ui.framerateLineEdit.setToolTip(
                    "Set frame rate: %.0f Hz" % fr)
            else:
                self.__ui.framerateLineEdit.setToolTip(
                    "Set frame rate: %.1f Hz" % fr)
        else:
            self.__ui.framerateLineEdit.setToolTip("Frame rate in Hz")

    def __prepareImage(self):
        """applies: make image gray, substracke the background image and
           apply the mask
        """
        if self.__filteredimage is None:
            return

        if len(self.__filteredimage.shape) == 3:
            self.__levelswg.setNumberOfChannels(self.__filteredimage.shape[0])
            if not self.__levelswg.colorChannel():
                self.__rawgreyimage = np.sum(self.__filteredimage, 0)
                if self.rgb():
                    self.setrgb(False)
            else:
                try:
                    if len(self.__filteredimage) >= \
                       self.__levelswg.colorChannel():
                        self.__rawgreyimage = self.__filteredimage[
                            self.__levelswg.colorChannel() - 1]
                        if self.rgb():
                            self.setrgb(False)
                            self.__levelswg.showGradient(True)
                    elif (len(self.__filteredimage) + 1 ==
                          self.__levelswg.colorChannel()):
                        if self.rgb():
                            self.setrgb(False)
                            self.__levelswg.showGradient(True)
                        self.__rawgreyimage = np.mean(self.__filteredimage, 0)
                    elif self.__filteredimage.shape[0] > 1:
                        if not self.rgb():
                            self.setrgb(True)
                            self.__levelswg.showGradient(False)
                        self.__rawgreyimage = np.moveaxis(
                            self.__filteredimage, 0, -1)
                        rgbs = self.__levelswg.rgbchannels()
                        if rgbs == (0, 1, 2):
                            if self.__rawgreyimage.shape[-1] > 3:
                                self.__rawgreyimage = \
                                    self.__rawgreyimage[:, :, :3]
                            elif self.__filteredimage.shape[-1] == 2:
                                nshape = list(self.__rawgreyimage.shape)
                                nshape[-1] = 1
                                self.__rawgreyimage = np.concatenate(
                                    (self.__rawgreyimage,
                                     np.zeros(
                                         shape=nshape.
                                         shape[:, :, -1],
                                         dtype=self.__rawgreyimage.dtype)),
                                    axis=2)
                        else:
                            zeros = None
                            nshape = list(self.__rawgreyimage.shape)
                            nshape[-1] = 1
                            if -1 in rgbs:
                                zeros = np.zeros(
                                    shape=nshape,
                                    dtype=self.__rawgreyimage.dtype)

                            self.__rawgreyimage = np.concatenate(
                                (self.__rawgreyimage[:, :, rgbs[0]].
                                 reshape(nshape)
                                 if rgbs[0] != -1 else zeros,
                                 self.__rawgreyimage[:, :, rgbs[1]].
                                 reshape(nshape)
                                 if rgbs[1] != -1 else zeros,
                                 self.__rawgreyimage[:, :, rgbs[2]].
                                 reshape(nshape)
                                 if rgbs[2] != -1 else zeros),
                                axis=2)

                    elif self.__filteredimage.shape[0] == 1:
                        if self.rgb():
                            self.setrgb(False)
                            self.__levelswg.showGradient(True)
                        self.__rawgreyimage = self.__filteredimage[:, :, 0]

                except Exception:
                    import traceback
                    value = traceback.format_exc()
                    text = messageBox.MessageBox.getText(
                        "lavue: color channel %s does not exist."
                        " Reset to grey scale"
                        % self.__levelswg.colorChannel())
                    messageBox.MessageBox.warning(
                        self,
                        "lavue: color channel %s does not exist. "
                        " Reset to grey scale"
                        % self.__levelswg.colorChannel(),
                        text, str(value))
                    self.__levelswg.setChannel(0)
        elif len(self.__filteredimage.shape) == 2:
            if self.rgb():
                self.setrgb(False)
                self.__levelswg.showGradient(True)
            if self.__applymask:
                self.__rawgreyimage = np.array(self.__filteredimage)
            else:
                self.__rawgreyimage = self.__filteredimage
            self.__levelswg.setNumberOfChannels(0)

        elif len(self.__filteredimage.shape) == 1:
            if self.rgb():
                self.setrgb(False)
                self.__levelswg.showGradient(True)
            self.__rawgreyimage = np.array(
                self.__filteredimage).reshape(
                    (self.__filteredimage.shape[0], 1))
            self.__levelswg.setNumberOfChannels(0)

        self.__displayimage = self.__rawgreyimage

        if self.__dobkgsubtraction and self.__backgroundimage is not None:
            # simple subtraction
            try:
                if (hasattr(self.__rawgreyimage, "dtype") and
                   self.__rawgreyimage.dtype.name in
                    self.__unsignedmap.keys()) \
                   and (hasattr(self.__backgroundimage, "dtype") and
                   self.__backgroundimage.dtype.name in
                        self.__unsignedmap.keys()):
                    self.__displayimage = np.subtract(
                        self.__rawgreyimage, self.__backgroundimage,
                        dtype=self.__unsignedmap[
                            self.__rawgreyimage.dtype.name])
                else:
                    self.__displayimage = \
                        self.__rawgreyimage - self.__backgroundimage
            except Exception:
                self._checkBkgSubtraction(False)
                self.__backgroundimage = None
                self.__dobkgsubtraction = False
                import traceback
                value = traceback.format_exc()
                text = messageBox.MessageBox.getText(
                    "lavue: Background image does not match "
                    "to the current image")
                messageBox.MessageBox.warning(
                    self, "lavue: Background image does not match "
                    "to the current image",
                    text, str(value))

        if self.__settings.showmask and self.__applymask and \
           self.__maskindices is not None:
            # set all masked (non-zero values) to zero by index
            try:
                self.__displayimage = np.array(self.__displayimage)
                self.__displayimage[self.__maskindices] = 0
            except IndexError:
                self.__maskwg.noImage()
                self.__applymask = False
                import traceback
                value = traceback.format_exc()
                text = messageBox.MessageBox.getText(
                    "lavue: Mask image does not match "
                    "to the current image")
                messageBox.MessageBox.warning(
                    self, "lavue: Mask image does not match "
                    "to the current image",
                    text, str(value))

        if self.__settings.showhighvaluemask and \
           self.__maskvalue is not None:
            try:
                self.__displayimage = np.array(self.__displayimage)
                self.__displayimage[self.__displayimage > self.__maskvalue] = 0
            except IndexError:
                # self.__highvaluemaskwg.noValue()
                import traceback
                value = traceback.format_exc()
                text = messageBox.MessageBox.getText(
                    "lavue: Cannot apply high value mask to the current image")
                messageBox.MessageBox.warning(
                    self, "lavue: Cannot apply high value mask"
                    " to the current image",
                    text, str(value))

    def __transform(self):
        """ does the image transformation on the given numpy array.

        :returns: crdtranspose, crdleftrightflip, crdupdownflip,
         orgtranspose, orgleftrightflip, orgupdownflip flags
        :rtype: (:obj:`bool`, :obj:`bool`, :obj:`bool`,:obj:`bool`,
                 :obj:`bool`, :obj:`bool`)
        """
        crdupdownflip = False
        crdleftrightflip = False
        crdtranspose = False
        orgupdownflip = False
        orgleftrightflip = False
        orgtranspose = False
        if self.__trafoname == "none":
            pass
        elif self.__trafoname == "flip (up-down)":
            orgupdownflip = True
            if self.__settings.keepcoords:
                crdupdownflip = True
            elif self.__displayimage is not None:
                self.__displayimage = np.fliplr(self.__displayimage)
        elif self.__trafoname == "flip (left-right)":
            orgleftrightflip = True
            if self.__settings.keepcoords:
                crdleftrightflip = True
            elif self.__displayimage is not None:
                self.__displayimage = np.flipud(self.__displayimage)
        elif self.__trafoname == "transpose":
            orgtranspose = True
            if self.__displayimage is not None:
                self.__displayimage = np.swapaxes(
                    self.__displayimage, 0, 1)
                # self.__displayimage = np.transpose(self.__displayimage)
            if self.__settings.keepcoords:
                crdtranspose = True
        elif self.__trafoname == "rot90 (clockwise)":
            orgtranspose = True
            orgupdownflip = True
            if self.__settings.keepcoords:
                crdtranspose = True
                crdupdownflip = True
                if self.__displayimage is not None:
                    self.__displayimage = np.swapaxes(
                        self.__displayimage, 0, 1)
                    # self.__displayimage = np.transpose(self.__displayimage)
            elif self.__displayimage is not None:
                # self.__displayimage = np.transpose(
                #     np.flipud(self.__displayimage))
                self.__displayimage = np.swapaxes(
                    np.flipud(self.__displayimage), 0, 1)
        elif self.__trafoname == "rot180":
            orgupdownflip = True
            orgleftrightflip = True
            if self.__settings.keepcoords:
                crdupdownflip = True
                crdleftrightflip = True
            elif self.__displayimage is not None:
                self.__displayimage = np.flipud(
                    np.fliplr(self.__displayimage))
        elif self.__trafoname == "rot270 (clockwise)":
            orgtranspose = True
            orgleftrightflip = True
            if self.__settings.keepcoords:
                crdtranspose = True
                crdleftrightflip = True
                if self.__displayimage is not None:
                    self.__displayimage = np.swapaxes(
                        self.__displayimage, 0, 1)
                    # self.__displayimage = np.transpose(self.__displayimage)
            elif self.__displayimage is not None:
                self.__displayimage = np.swapaxes(
                    np.fliplr(self.__displayimage), 0, 1)
                # self.__displayimage = np.transpose(
                #     np.fliplr(self.__displayimage))
        elif self.__trafoname == "rot180 + transpose":
            orgtranspose = True
            orgupdownflip = True
            orgleftrightflip = True
            if self.__settings.keepcoords:
                crdtranspose = True
                crdupdownflip = True
                crdleftrightflip = True
                if self.__displayimage is not None:
                    # self.__displayimage = np.transpose(self.__displayimage)
                    self.__displayimage = np.swapaxes(
                        self.__displayimage, 0, 1)
            elif self.__displayimage is not None:
                self.__displayimage = np.swapaxes(
                    np.fliplr(np.flipud(self.__displayimage)), 0, 1)
                # self.__displayimage = np.transpose(
                #     np.fliplr(np.flipud(self.__displayimage)))
        return (crdtranspose, crdleftrightflip, crdupdownflip,
                orgtranspose, orgleftrightflip, orgupdownflip)

    def __applyFilters(self):
        """ applies user filters
        """
        self.__filteredimage = self.__rawimage
        if self.__filterstate:
            for flt in self.__filters:
                try:
                    if self.__filteredimage is not None:
                        image = flt(
                            self.__filteredimage,
                            self.__imagename,
                            self.__metadata,
                            self.__imagewg
                        )
                        fltmdata = None
                        if isinstance(image, tuple):
                            if len(image) >= 2:
                                image, fltmdata = image[:2]
                            if len(image) == 1:
                                image = image
                        if image is not None and (
                                hasattr(image, "size") and image.size > 1):
                            self.__filteredimage = image
                        if isinstance(fltmdata, dict):
                            self.__mdata.update(fltmdata)
                except Exception as e:
                    self.__filterswg.setState(0)
                    import traceback
                    value = traceback.format_exc()
                    messageBox.MessageBox.warning(
                        self, "lavue: problems in applying filters",
                        "%s" % str(e),
                        "%s" % value)
                    # print(str(e))

    def __scale(self, scalingtype):
        """ sets scaletype on the image

        :param scalingtype: scaling type
        :type scalingtype: :obj:`str`
        """
        self.__imagewg.setScalingType(scalingtype)
        if self.__displayimage is None:
            self.__scaledimage = None
        elif scalingtype == "sqrt":
            self.__scaledimage = np.clip(self.__displayimage, 0, np.inf)
            self.__scaledimage = np.sqrt(self.__scaledimage)
        elif scalingtype == "log":
            self.__scaledimage = np.clip(self.__displayimage, 10e-3, np.inf)
            self.__scaledimage = np.log10(self.__scaledimage)
        elif _VMAJOR == '0' and _VMINOR == '9' and int(_VPATCH) > 7:
            # (for 0.9.8 <= version < 0.10.0 i.e. ubuntu 16.04)
            self.__scaledimage = self.__displayimage.astype("float")
        else:
            self.__scaledimage = self.__displayimage

    def __calcStats(self, flag):
        """ calcualtes scaled limits for intesity levels

        :param flag: (max value, mean value, variance value,
                  min scaled value, max raw value, max scaled value)
                  to calculate
        :type flag: [:obj:`bool`, :obj:`bool`, :obj:`bool`,
                       :obj:`bool`, :obj:`bool`, :obj:`bool`]
        :returns: max value, mean value, variance value,
                  min scaled value, max raw value, max scaled value
        :rtype: [:obj:`str`, :obj:`str`, :obj:`str`, :obj:`str`,
                    :obj:`str`, :obj:`str`]
        """
        if self.__settings.statswoscaling and self.__displayimage is not None:
            maxval = np.amax(self.__displayimage) if flag[0] else 0.0
            meanval = np.mean(self.__displayimage) if flag[1] else 0.0
            varval = np.var(self.__displayimage) if flag[2] else 0.0
            maxsval = np.amax(self.__scaledimage) if flag[5] else 0.0
        elif (not self.__settings.statswoscaling
              and self.__scaledimage is not None):
            maxval = np.amax(self.__scaledimage) if flag[0] or flag[5] else 0.0
            meanval = np.mean(self.__scaledimage) if flag[1] else 0.0
            varval = np.var(self.__scaledimage) if flag[2] else 0.0
            maxsval = maxval
        else:
            return 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
        maxrawval = np.amax(self.__rawgreyimage) if flag[4] else 0.0
        minval = np.amin(self.__scaledimage) if flag[3] else 0.0
        return (maxval, meanval, varval, minval, maxrawval,  maxsval)

    @QtCore.pyqtSlot(str)
    def _checkHighMasking(self, value):
        """ reads the mask image, select non-zero elements and store the indices
        """
        try:
            self.__maskvalue = float(value)
        except Exception:
            self.__maskvalue = None
        self._plot()

    @QtCore.pyqtSlot(int)
    def _checkMasking(self, state):
        """ replots the image with mask if mask exists
        """
        self.__applymask = state
        if self.__applymask and self.__maskimage is None:
            self.__maskwg.noImage()
        self._plot()

    @QtCore.pyqtSlot(str)
    def _prepareMasking(self, imagename):
        """ reads the mask image, select non-zero elements and store the indices
        """
        imagename = str(imagename)
        if imagename:
            if imagename.endswith(".nxs") or imagename.endswith(".h5") \
               or imagename.endswith(".nx") or imagename.endswith(".ndf"):
                fieldpath = None
                growing = 0
                frame = 0
                handler = imageFileHandler.NexusFieldHandler(
                    str(imagename))
                fields = handler.findImageFields()
                if fields:
                    imgfield = imageField.ImageField(self)
                    imgfield.fields = fields
                    imgfield.frame = 0
                    imgfield.createGUI()
                    if imgfield.exec_():
                        fieldpath = imgfield.field
                        growing = imgfield.growing
                        frame = imgfield.frame
                    else:
                        return
                    currentfield = fields[fieldpath]
                    self.__maskimage = np.transpose(handler.getImage(
                        currentfield["node"],
                        frame, growing, refresh=False))
                else:
                    return
            else:
                self.__maskimage = np.transpose(
                    imageFileHandler.ImageFileHandler(
                        str(imagename)).getImage())
            if self.__settings.zeromask:
                self.__maskindices = (self.__maskimage == 0)
            else:
                self.__maskindices = (self.__maskimage != 0)
        else:
            self.__maskimage = None
        # self.__maskindices = np.nonzero(self.__maskimage != 0)

    def __remasking(self):
        """ recalculates the mask
        """
        if self.__maskimage is not None:
            if self.__settings.zeromask:
                self.__maskindices = (self.__maskimage == 0)
            else:
                self.__maskindices = (self.__maskimage != 0)

    @QtCore.pyqtSlot(int)
    def _checkBkgSubtraction(self, state):
        """ replots the image with subtranction if background image exists
        """
        self.__dobkgsubtraction = state
        if self.__dobkgsubtraction and self.__backgroundimage is None:
            self.__bkgsubwg.setDisplayedName("")
        else:
            self.__bkgsubwg.checkBkgSubtraction(state)
        self.__imagewg.setDoBkgSubtraction(state)
        self._plot()

    @QtCore.pyqtSlot(str)
    def _prepareBkgSubtraction(self, imagename):
        """ reads the background image
        """
        imagename = str(imagename)
        if imagename:
            if imagename.endswith(".nxs") or imagename.endswith(".h5") \
               or imagename.endswith(".nx") or imagename.endswith(".ndf"):
                fieldpath = None
                growing = 0
                frame = 0
                handler = imageFileHandler.NexusFieldHandler(
                    str(imagename))
                fields = handler.findImageFields()
                if fields:
                    imgfield = imageField.ImageField(self)
                    imgfield.fields = fields
                    imgfield.frame = 0
                    imgfield.createGUI()
                    if imgfield.exec_():
                        fieldpath = imgfield.field
                        growing = imgfield.growing
                        frame = imgfield.frame
                    else:
                        return
                    currentfield = fields[fieldpath]
                    self.__backgroundimage = np.transpose(
                        handler.getImage(
                            currentfield["node"],
                            frame, growing, refresh=False))
                else:
                    return
            else:
                self.__backgroundimage = np.transpose(
                    imageFileHandler.ImageFileHandler(
                        str(imagename)).getImage())
        else:
            self.__backgroundimage = None

    @QtCore.pyqtSlot()
    def _setCurrentImageAsBkg(self):
        """ sets the chrrent image as the background image
        """
        if self.__rawgreyimage is not None:
            self.__backgroundimage = self.__rawgreyimage
            self.__bkgsubwg.setDisplayedName(str(self.__imagename))
        else:
            self.__bkgsubwg.setDisplayedName("")

    @QtCore.pyqtSlot(bool)
    def _assessFilters(self, state):
        """ assesses the filter on/off state
        """
        if self.__filterstate != state:
            self.__filterstate = state
            for flt in self.__filters:
                try:
                    if state:
                        if hasattr(flt, "initialize"):
                            flt.initialize()
                    else:
                        if hasattr(flt, "terminate"):
                            flt.terminate()
                except Exception as e:
                    self.__filterswg.setState(0)
                    import traceback
                    value = traceback.format_exc()
                    messageBox.MessageBox.warning(
                        self, "lavue: problems in starting or stoping filters",
                        "%s" % str(e),
                        "%s" % value)
                    # print(str(e))

            if self.__displayimage is not None:
                self._plot()

    @QtCore.pyqtSlot(str)
    def _assessTransformation(self, trafoname):
        """ assesses the transformation and replot it
        """
        self.__trafoname = trafoname
        if trafoname in [
                "transpose", "rot90 (clockwise)",
                "rot270 (clockwise)", "rot180 + transpose"]:
            self.__trafowg.setKeepCoordsLabel(
                self.__settings.keepcoords, True)
        else:
            self.__trafowg.setKeepCoordsLabel(
                self.__settings.keepcoords, False)
        self._plot()

    def keyPressEvent(self,  event):
        """ skips escape key action

        :param event: close event
        :type event:  :class:`pyqtgraph.QtCore.QEvent`:
        """
        if event.key() != QtCore.Qt.Key_Escape:
            QtGui.QDialog.keyPressEvent(self, event)
        # else:
        #     self.closeEvent(None)

    @QtCore.pyqtSlot(bool)
    def setrgb(self, status=True):
        """ sets RGB on/off

        :param status: True for on and False for off
        :type status: :obj:`bool`
        """
        self.__imagewg.setrgb(status)
        self._plot()

    def rgb(self):
        """ gets RGB on/off

        :returns: True for on and False for off
        :rtype: :obj:`bool`
        """
        return self.__imagewg.rgb()
