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

""" image display widget """

import pyqtgraph as _pg
from pyqtgraph import QtCore, QtGui
import math
import types

from . import axesDialog
from . import memoExportDialog


_VMAJOR, _VMINOR, _VPATCH = _pg.__version__.split(".")[:3] \
    if _pg.__version__ else ("0", "9", "0")


class SafeImageItem(_pg.ImageItem):

    """ Image item which caught exceptions in paint"""

    def __init__(self, *args, **kargs):
        """ constructor

        :param args: ImageItem parameters list
        :type args: :obj:`list` < :obj:`any`>
        :param kargs:  ImageItem parameter dictionary
        :type kargs: :obj:`dict` < :obj:`str`, :obj:`any`>
        """
        _pg.ImageItem.__init__(self, *args, **kargs)

    def paint(self, p, *args):
        """ safe paint method

        :param p: painter
        :type p: :class:`PyQt5.QtGui.QPainter`
        :param args: ImageItem parameters list
        :type args: :obj:`list` < :obj:`any`>
        """
        try:
            _pg.ImageItem.paint(self, p, *args)
        except ValueError as e:
            print(str(e))
            # print("Shape mismatch: skip painting")


class AxesParameters(object):
    """ axes parameters
    """

    def __init__(self):
        """ constructor
        """

        #: (:obj:`bool`) enabled flag
        self.enabled = False
        #: (:obj:`tuple` <:obj:`float`, :obj:`float`> ) image scale (x,y)
        self.scale = None
        #: (:obj:`tuple` <:obj:`float`, :obj:`float`> )
        #    position of the first pixel
        self.position = None
        #: (:obj:`str`) label of x-axis
        self.xtext = None
        #: (:obj:`str`) label of y-axis
        self.ytext = None
        #: (:obj:`str`) units of x-axis
        self.xunits = None
        #: (:obj:`str`) units of y-axis
        self.yunits = None


class IntensityParameters(object):
    """ intensity parameters
    """

    def __init__(self):
        """ constructor
        """
        #: (:obj:`bool`) do background substraction
        self.dobkgsubtraction = False
        #: (:obj:`bool`) calculate statistics without scaling
        self.statswoscaling = True
        #: (:obj:`str`) intensity scaling
        self.scaling = "sqrt"


class TransformationParameters(object):
    """ transformation parameters
    """

    def __init__(self):
        """ constructor
        """
        #: (:obj:`bool`) transpose coordinates flag
        self.transpose = False
        #: (:obj:`bool`) left-right flip coordinates flag
        self.leftrightflip = False
        #: (:obj:`bool`)  up-down flip coordinates flag
        self.updownflip = False


class ImageDisplayWidget(_pg.GraphicsLayoutWidget):

    #: (:class:`pyqtgraph.QtCore.pyqtSignal`) aspect locked toggled signal
    aspectLockedToggled = QtCore.pyqtSignal(bool)
    #: (:class:`pyqtgraph.QtCore.pyqtSignal`) mouse position changed signal
    mouseImagePositionChanged = QtCore.pyqtSignal()
    #: (:class:`pyqtgraph.QtCore.pyqtSignal`) mouse double clicked
    mouseImageDoubleClicked = QtCore.pyqtSignal(float, float)
    #: (:class:`pyqtgraph.QtCore.pyqtSignal`) mouse single clicked
    mouseImageSingleClicked = QtCore.pyqtSignal(float, float)

    def __init__(self, parent=None):
        """ constructor

        :param parent: parent object
        :type parent: :class:`pyqtgraph.QtCore.QObject`
        """
        _pg.GraphicsLayoutWidget.__init__(self, parent)
        #: (:class:`PyQt5.QtGui.QLayout`) the main layout
        self.__layout = self.ci

        #: (:class:`lavuelib.imageDisplayWidget.AxesParameters`)
        #:            axes parameters
        self.__axes = AxesParameters()
        #: (:class:`lavuelib.imageDisplayWidget.AxesParameters`)
        #:            polar axes parameters
        self.__polaraxes = AxesParameters()

        #: (:class:`lavuelib.imageDisplayWidget.IntensityParameters`)
        #:                  intensity parameters
        self.__intensity = IntensityParameters()
        #: (:class:`lavuelib.imageDisplayWidget.TransformationParameters`)
        #:                  intensity parameters
        self.__transformations = TransformationParameters()

        #: (:class:`numpy.ndarray`) data to displayed in 2d widget
        self.__data = None
        #: (:class:`numpy.ndarray`) raw data to cut plots
        self.__rawdata = None

        #: (:class:`pyqtgraph.ImageItem`) image item
        self.__image = SafeImageItem()

        #: (:class:`pyqtgraph.ViewBox`) viewbox item
        self.__viewbox = self.__layout.addViewBox(row=0, col=1)

        self.__viewbox.addItem(self.__image)
        #: (:obj:`float`) current floar x-position
        self.__xfdata = 0
        #: (:obj:`float`) current floar y-position
        self.__yfdata = 0
        #: (:obj:`float`) current x-position
        self.__xdata = 0
        #: (:obj:`float`) current y-position
        self.__ydata = 0
        #: (:obj:`bool`) auto display level flag
        self.__autodisplaylevels = 2
        #: (:obj:`bool`) auto down sample
        self.__autodownsample = True
        #: ([:obj:`float`, :obj:`float`]) minimum and maximum intensity levels
        self.__displaylevels = [None, None]
        #: (:obj:`bool`) lock for double click
        self.__doubleclicklock = False
        #: (:obj:`bool`) rgb on flag
        self.__rgb = False
        #: (:obj:`dict` < :obj:`str`, :obj:`DisplayExtension` >)
        #          extension dictionary with name keys
        self.__extensions = {}
        #: (:class:`PyQt5.QtGui.QAction`) set aspect ration locked action
        self.__setaspectlocked = QtGui.QAction(
            "Set Aspect Locked", self.__viewbox.menu)
        self.__setaspectlocked.setCheckable(True)
        if _VMAJOR == '0' and int(_VMINOR) < 10 and int(_VPATCH) < 9:
            self.__viewbox.menu.axes.insert(0, self.__setaspectlocked)
        self.__viewbox.menu.addAction(self.__setaspectlocked)

        #: (:class:`PyQt5.QtGui.QAction`) view one to one pixel action
        self.__viewonetoone = QtGui.QAction(
            "View 1:1 pixels", self.__viewbox.menu)
        self.__viewonetoone.triggered.connect(self._oneToOneRange)
        if _VMAJOR == '0' and int(_VMINOR) < 10 and int(_VPATCH) < 9:
            self.__viewbox.menu.axes.insert(0, self.__viewonetoone)
        self.__viewbox.menu.addAction(self.__viewonetoone)

        #: (:class:`pyqtgraph.AxisItem`) left axis
        self.__leftaxis = _pg.AxisItem('left')

        #: (:class:`pyqtgraph.AxisItem`) bottom axis
        self.__bottomaxis = _pg.AxisItem('bottom')

        self.__leftaxis.linkToView(self.__viewbox)
        self.__layout.addItem(self.__leftaxis, row=0, col=0)
        self.__bottomaxis.linkToView(self.__viewbox)
        self.__layout.addItem(self.__bottomaxis, row=1, col=1)

        self.__layout.scene().sigMouseMoved.connect(self.mouse_position)
        self.__layout.scene().sigMouseClicked.connect(self.mouse_click)

        self.__setaspectlocked.triggered.connect(self.emitAspectLockedToggled)

        sc = self.__layout.scene()
        sc.contextMenu[0].triggered.disconnect(sc.showExportDialog)
        sc.showExportDialog = types.MethodType(
            memoExportDialog.GraphicsScene_showExportDialog, sc)
        sc.contextMenu[0].triggered.connect(sc.showExportDialog)

    def viewbox(self):
        """provides viewbox
        :rtype: :class:`pyqtgraph.ViewBox`
        :returns: viewbox
        """
        return self.__viewbox

    def addExtensions(self, extlist):
        """provides viewbox
        :param extlist: extension list
        :type extlist: :obj:`list` < :class:`DisplayExtension` >
        """
        for excls in extlist:
            ext = excls(self)
            self.__extensions[ext.name] = ext

    def extension(self, name):
        """provides viewbox
        :param name: extension name
        :type name: :obj:`str`
        :rtype: :class:`DisplayExtension`
        :returns: display extension
        """
        return self.__extensions[name]

    def setAspectLocked(self, flag):
        """sets aspectLocked

        :param status: state to set
        :type status: :obj:`bool`
        :returns: old state
        :rtype: :obj:`bool`
        """
        if flag != self.__setaspectlocked.isChecked():
            self.__setaspectlocked.setChecked(flag)
        oldflag = self.__viewbox.state["aspectLocked"]
        self.__viewbox.setAspectLocked(flag)
        return oldflag

    def _oneToOneRange(self):
        """ set one to one range
        """
        ps = self.__image.pixelSize()
        currange = self.__viewbox.viewRange()
        xrg = currange[0][1] - currange[0][0]
        yrg = currange[1][1] - currange[1][0]
        if self.__axes.position is not None and self.__axes.enabled:
            self.__viewbox.setRange(
                QtCore.QRectF(
                    self.__axes.position[0], self.__axes.position[1],
                    xrg * ps[0], yrg * ps[1]),
                padding=0)
        else:
            self.__viewbox.setRange(
                QtCore.QRectF(0, 0, xrg * ps[0], yrg * ps[1]),
                padding=0)
        if self.__setaspectlocked.isChecked():
            self.__setaspectlocked.setChecked(False)
            self.__setaspectlocked.triggered.emit(False)

    def setViewRange(self, rangelist):
        """ set view range values

        :param rangelist: xmin,ymin,xsize,ysize
        :type rangelist: :obj:`str`
        """
        lims = rangelist.split(",")
        if lims and len(lims) == 4:
            fl = [float(lm.replace("m", "-")) for lm in lims]
            self.__viewbox.setRange(QtCore.QRectF(*fl), padding=0)

    def viewRange(self):
        """ get view range values

        :returns: xmin,ymin,xsize,ysize
        :rtype rangelist: :obj:`str`
        """
        vr = self.__viewbox.viewRange()
        vr0 = vr[0]
        vr1 = vr[1]
        return "%s,%s,%s,%s" % (
            vr0[0], vr1[0], vr0[1] - vr0[0], vr1[1] - vr1[0])

    def __setScale(self, position=None, scale=None, update=True, polar=False,
                   force=False):
        """ set axes scales

        :param position: start position of axes
        :type position: [:obj:`float`, :obj:`float`]
        :param scale: scale axes
        :type scale: [:obj:`float`, :obj:`float`]
        :param update: update scales on image
        :type update: :obj:`bool`
        :param polar: update polar scale
        :type polar: :obj:`bool`
        :param force: force rescaling
        :type force: :obj:`bool`
        """
        axes = self.__polaraxes if polar else self.__axes

        if update:
            self.__setLabels(axes.xtext, axes.ytext,
                             axes.xunits, axes.yunits)

        if not force:
            if axes.position == position and axes.scale == scale and \
               position is None and scale is None:
                return
        axes.position = position
        axes.scale = scale
        self.__image.resetTransform()
        if axes.scale is not None and update:
            if not self.__transformations.transpose:
                self.__image.scale(*axes.scale)
            else:
                self.__image.scale(
                    axes.scale[1], axes.scale[0])
        else:
            self.__image.scale(1, 1)
        if axes.position is not None and update:
            if not self.__transformations.transpose:
                self.__image.setPos(*axes.position)
            else:
                self.__image.setPos(
                    axes.position[1], axes.position[0])
        else:
            self.__image.setPos(0, 0)
        if self.__rawdata is not None and update:
            self.autoRange()

    def setPolarScale(self, position=None, scale=None):
        """ set axes scales

        :param position: start position of axes
        :type position: [:obj:`float`, :obj:`float`]
        :param scale: scale axes
        :type scale: [:obj:`float`, :obj:`float`]
        :param update: update scales on image
        :type updatescale: :obj:`bool`
        """
        self.__polaraxes.position = position
        self.__polaraxes.scale = scale

    def scale(self):
        """ provides scale and position of the axes
        :rtype: [int, int, int, int]
        :returns: [posx, posy, scalex, scaley]
        """
        position = None, None
        scale = None, None
        if self.__axes.scale is not None and \
           self.__axes.enabled is True:
            position = [0, 0] \
                if self.__axes.position is None \
                else self.__axes.position
            scale = self.__axes.scale
        return position[0], position[1], scale[0], scale[1]

    def __resetScale(self, polar=False):
        """ reset axes scales

        :param polar: update polar scale
        :type polar: :obj:`bool`
        """
        axes = self.__polaraxes if polar else self.__axes

        if axes.scale is not None or axes.position is not None:
            self.__image.resetTransform()
        if axes.scale is not None:
            self.__image.scale(1, 1)
        if axes.position is not None:
            self.__image.setPos(0, 0)
        if axes.scale is not None or axes.position is not None:
            if self.__rawdata is not None:
                self.autoRange()
            self.__setLabels()

    def updateImage(self, img=None, rawimg=None):
        """ updates the image to display

        :param img: 2d image array
        :type img: :class:`numpy.ndarray`
        :param rawimg: 2d raw image array
        :type rawimg: :class:`numpy.ndarray`
        """
        try:
            # if self.__rgb:
            if len(img.shape) == 3:
                self.__image.setLookupTable(None)
                self.__image.setImage(
                    img, lut=None,
                    # levels=[[0,255], [0, 255], [0, 255]],
                    autoLevels=False)
            elif (self.__autodisplaylevels
                  or self.__displaylevels[0] is None
                  or self.__displaylevels[1] is None):
                self.__image.setImage(
                    img, autoLevels=False,
                    autoDownsample=self.__autodownsample)
            else:
                self.__image.setImage(
                    img, autoLevels=False,
                    levels=self.__displaylevels,
                    autoDownsample=self.__autodownsample)
        except Exception as e:
            print(str(e))
        self.__data = img
        self.__rawdata = rawimg
        self.mouse_position()

    def currentIntensity(self):
        """ provides intensity for current mouse position

        :returns: (x position, y position, pixel intensity,
                   x position, y position)
        :rtype: (float, float, float, float, float)
        """
        xfdata = None
        yfdata = None
        for ext in self.__extensions.values():
            if ext.enabled():
                coords = ext.coordinates()
                xfdata = coords[0]
                yfdata = coords[1]
        if xfdata is None or yfdata is None:
            xfdata = self.__xfdata
            yfdata = self.__yfdata
        if self.__rawdata is not None:
            try:
                if not self.__transformations.transpose:
                    xf = int(xfdata)
                    yf = int(yfdata)
                else:
                    yf = int(xfdata)
                    xf = int(yfdata)
                if xf >= 0 and yf >= 0 and xf < self.__rawdata.shape[0] \
                   and yf < self.__rawdata.shape[1]:
                    intensity = self.__rawdata[xf, yf]
                else:
                    intensity = 0.
            except Exception:
                intensity = 0.
        else:
            intensity = 0.
        return (xfdata, yfdata, intensity,
                self.__xdata, self.__ydata)

    def scalingLabel(self):
        """ provides scaling label

        :returns:  scaling label
        :rtype: str
        """
        ilabel = None
        for ext in self.__extensions.values():
            if ext.enabled():
                ilabel = ext.scalingLabel()
        if ilabel is None:
            scaling = self.__intensity.scaling \
                if not self.__intensity.statswoscaling else "linear"
            if self.__intensity.dobkgsubtraction:
                ilabel = "%s(intensity-background)" % (
                    scaling if scaling != "linear" else "")
            else:
                if scaling == "linear":
                    ilabel = "intensity"
                else:
                    ilabel = "%s(intensity)" % scaling
        return ilabel

    def scaling(self):
        """ provides scaling type

        :returns:  scaling type
        :rtype: str
        """
        return self.__intensity.scaling

    def axesunits(self):
        """ return axes units
        :returns: x,y units
        :rtype: (:obj:`str`, :obj:`str`)
        """
        return (self.__axes.xunits, self.__axes.yunits)

    def scaledxy(self, x, y):
        """ provides scaled x,y positions

        :param x: x pixel coordinate
        :type x: float
        :param y: y pixel coordinate
        :type y: float
        :returns: scaled x,y position
        :rtype: (float, float)
        """
        txdata = None
        tydata = None
        if self.__axes.scale is not None:
            txdata = x * self.__axes.scale[0]
            tydata = y * self.__axes.scale[1]
            if self.__axes.position is not None:
                txdata = txdata + self.__axes.position[0]
                tydata = tydata + self.__axes.position[1]
        elif self.__axes.position is not None:
            txdata = x + self.__axes.position[0]
            tydata = y + self.__axes.position[1]
        return (txdata, tydata)

    @QtCore.pyqtSlot(object)
    def mouse_position(self, event=None):
        """ updates image widget after mouse position change

        :param event: mouse move event
        :type event: :class:`pyqtgraph.QtCore.QEvent`
        """
        try:
            if event is not None:
                mousePoint = self.__image.mapFromScene(event)
                if not self.__transformations.transpose:
                    self.__xdata = mousePoint.x()
                    self.__ydata = mousePoint.y()
                else:
                    self.__ydata = mousePoint.x()
                    self.__xdata = mousePoint.y()
                self.__xfdata = math.floor(self.__xdata)
                self.__yfdata = math.floor(self.__ydata)
            for ext in self.__extensions.values():
                if ext.enabled():
                    ext.mouse_position(self.__xdata, self.__ydata)
            self.mouseImagePositionChanged.emit()
        except Exception:
            # print("Warning: %s" % str(e))
            pass

    def __setLabels(self, xtext=None, ytext=None, xunits=None, yunits=None):
        """ sets labels and units

        :param xtext: x-label text
        :param type: :obj:`str`
        :param ytext: y-label text
        :param type: :obj:`str`
        :param xunits: x-units text
        :param type: :obj:`str`
        :param yunits: y-units text
        :param type: :obj:`str`
        """
        self.__bottomaxis.autoSIPrefix = False
        self.__leftaxis.autoSIPrefix = False
        if not self.__transformations.transpose:
            self.__bottomaxis.setLabel(text=xtext, units=xunits)
            self.__leftaxis.setLabel(text=ytext, units=yunits)
            if xunits is None:
                self.__bottomaxis.labelUnits = ''
            if yunits is None:
                self.__leftaxis.labelUnits = ''
            if xtext is None:
                self.__bottomaxis.label.setVisible(False)
            if ytext is None:
                self.__leftaxis.label.setVisible(False)
        else:
            self.__bottomaxis.setLabel(text=ytext, units=yunits)
            self.__leftaxis.setLabel(text=xtext, units=xunits)
            if yunits is None:
                self.__bottomaxis.labelUnits = ''
            if xunits is None:
                self.__leftaxis.labelUnits = ''
            if ytext is None:
                self.__bottomaxis.label.setVisible(False)
            if xtext is None:
                self.__leftaxis.label.setVisible(False)

    @QtCore.pyqtSlot(object)
    def mouse_click(self, event):
        """ updates image widget after mouse click

        :param event: mouse click event
        :type event: :class:`pyqtgraph.QtCore.QEvent`
        """

        mousePoint = self.__image.mapFromScene(event.scenePos())

        if not self.__transformations.transpose:
            xdata = mousePoint.x()
            ydata = mousePoint.y()
        else:
            ydata = mousePoint.x()
            xdata = mousePoint.y()

        # if double click: fix mouse crosshair
        # another double click releases the crosshair again
        if event.double():
            for ext in self.__extensions.values():
                if ext.enabled():
                    ext.mouse_doubleclick(
                        xdata, ydata,
                        self.__doubleclicklock)
            self.mouseImageDoubleClicked.emit(xdata, ydata)
        else:
            for ext in self.__extensions.values():
                if ext.enabled():
                    ext.mouse_click(xdata, ydata)
            self.mouseImageSingleClicked.emit(xdata, ydata)

    def setAutoLevels(self, autolevels):
        """ sets auto levels

        :param autolevels: auto levels enabled
        :type autolevels: :obj:`bool`
        """
        if autolevels == 2:
            self.__autodisplaylevels = True
        else:
            self.__autodisplaylevels = False

    def setAutoDownSample(self, autodownsample):
        """ sets auto levels

        :param autolevels: auto down sample enabled
        :type autolevels: :obj:`bool`
        """
        if autodownsample:
            self.__autodownsample = True
        else:
            self.__autodownsample = False

    def setDisplayMinLevel(self, level=None):
        """ sets minimum intensity level

        :param level: minimum intensity
        :type level: :obj:`float`
        """
        if level is not None:
            self.__displaylevels[0] = level

    def setDisplayMaxLevel(self, level=None):
        """ sets maximum intensity level

        :param level: maximum intensity
        :type level: :obj:`float`
        """
        if level is not None:
            self.__displaylevels[1] = level

    def setDoubleClickLock(self, status=True):
        """ sets double click lock
        :param status: status flag
        :type status: :obj:`bool`
        """
        self.__doubleclicklock = status

    def setSubWidgets(self, parameters):
        """ set subwidget properties

        :param parameters: tool parameters
        :type parameters: :class:`lavuelib.toolWidget.ToolParameters`
        """
        rescale = False
        doreset = False
        if parameters.scale is not None:
            if parameters.scale is False:
                doreset = self.__axes.enabled
            self.__axes.enabled = parameters.scale
        if parameters.polarscale is not None:
            doreset = doreset or parameters.polarscale
            if self.__polaraxes.enabled and not parameters.polarscale:
                doreset = True
                rescale = True
            self.__polaraxes.enabled = parameters.polarscale

        for ext in self.__extensions.values():
            ext.show(parameters)

        if doreset:
            self.__resetScale(polar=parameters.polarscale)
        if parameters.scale is True or rescale:
            self.__setScale(
                self.__axes.position, self.__axes.scale, force=rescale)
        if parameters.polarscale is True:
            self.__setScale(
                self.__polaraxes.position, self.__polaraxes.scale, polar=True)

    @QtCore.pyqtSlot(bool)
    def emitAspectLockedToggled(self, status):
        """ emits aspectLockedToggled

        :param status: aspectLockedToggled status
        :type status: :obj:`bool`
        """
        self.aspectLockedToggled.emit(status)

    def setTicks(self):
        """ launch axes widget

        :returns: apply status
        :rtype: :obj:`bool`
        """
        cnfdlg = axesDialog.AxesDialog()
        if self.__axes.position is None:
            cnfdlg.xposition = None
            cnfdlg.yposition = None
        else:
            cnfdlg.xposition = self.__axes.position[0]
            cnfdlg.yposition = self.__axes.position[1]
        if self.__axes.scale is None:
            cnfdlg.xscale = None
            cnfdlg.yscale = None
        else:
            cnfdlg.xscale = self.__axes.scale[0]
            cnfdlg.yscale = self.__axes.scale[1]

        cnfdlg.xtext = self.__axes.xtext
        cnfdlg.ytext = self.__axes.ytext

        cnfdlg.xunits = self.__axes.xunits
        cnfdlg.yunits = self.__axes.yunits

        cnfdlg.createGUI()
        if cnfdlg.exec_():
            if cnfdlg.xposition is not None and cnfdlg.yposition is not None:
                position = tuple([cnfdlg.xposition, cnfdlg.yposition])
            else:
                position = None
            if cnfdlg.xscale is not None and cnfdlg.yscale is not None:
                scale = tuple([cnfdlg.xscale, cnfdlg.yscale])
            else:
                scale = None
            self.__axes.xtext = cnfdlg.xtext or None
            self.__axes.ytext = cnfdlg.ytext or None

            self.__axes.xunits = cnfdlg.xunits or None
            self.__axes.yunits = cnfdlg.yunits or None
            self.__setScale(position, scale)
            self.updateImage(self.__data, self.__rawdata)

            return True
        return False

    def rawData(self):
        """ provides the raw data

        :returns: current raw data
        :rtype: :class:`numpy.ndarray`
        """
        return self.__rawdata

    def currentData(self):
        """ provides the data

        :returns: current data
        :rtype: :class:`numpy.ndarray`
        """
        return self.__data

    def updateMetaData(self, axisscales=None, axislabels=None):
        """ update Metadata informations

        :param axisscales: [xstart, ystart, xscale, yscale]
        :type axisscales:
                  [:obj:`float`, :obj:`float`, :obj:`float`, :obj:`float`]
        :param axislabels: [xtext, ytext, xunits, yunits]
        :type axislabels:
                  [:obj:`float`, :obj:`float`, :obj:`float`, :obj:`float`]
        """
        if axislabels is not None:
            self.__axes.xtext = str(axislabels[0]) \
                if axislabels[0] is not None else None
            self.__axes.ytext = str(axislabels[1]) \
                if axislabels[0] is not None else None
            self.__axes.xunits = str(axislabels[2]) \
                if axislabels[0] is not None else None
            self.__axes.yunits = str(axislabels[3]) \
                if axislabels[0] is not None else None
        position = None
        scale = None
        if axisscales is not None:
            try:
                position = (float(axisscales[0]), float(axisscales[1]))
            except Exception:
                position = None
            try:
                scale = (float(axisscales[2]), float(axisscales[3]))
            except Exception:
                scale = None
        self.__setScale(position, scale, self.__axes.enabled)

    def setStatsWOScaling(self, status):
        """ sets statistics without scaling flag

        :param status: statistics without scaling flag
        :type status: :obj:`bool`
        :returns: change status
        :rtype: :obj:`bool`
        """
        if self.__intensity.statswoscaling != status:
            self.__intensity.statswoscaling = status
            return True
        return False

    def setScalingType(self, scalingtype):
        """ sets intensity scaling types

        :param scalingtype: intensity scaling type
        :type scalingtype: :obj:`str`
        """
        self.__intensity.scaling = scalingtype

    def setDoBkgSubtraction(self, state):
        """ sets do background subtraction flag

        :param status: do background subtraction flag
        :type status: :obj:`bool`
        """
        self.__intensity.dobkgsubtraction = state

    def image(self):
        """ provides imageItem object

        :returns: image object
        :rtype: :class:`pyqtgraph.imageItem.ImageItem`
        """
        return self.__image

    def setTransformations(self, transpose, leftrightflip, updownflip):
        """ sets coordinate transformations

        :param transpose: transpose coordinates flag
        :type transpose: :obj:`bool`
        :param leftrightflip: left-right flip coordinates flag
        :type leftrightflip: :obj:`bool`
        :param updownflip: up-down flip coordinates flag
        :type updownflip: :obj:`bool`
        """
        if self.__transformations.transpose != transpose:
            self.__transformations.transpose = transpose
            self.__transposeItems()
        if self.__transformations.leftrightflip != leftrightflip:
            self.__transformations.leftrightflip = leftrightflip
            if hasattr(self.__viewbox, "invertX"):
                self.__viewbox.invertX(leftrightflip)
            else:
                """ version 0.9.10 without invertX """
            # workaround for a bug in old pyqtgraph versions: stretch 0.10
            self.__viewbox.sigXRangeChanged.emit(
                self.__viewbox, tuple(self.__viewbox.state['viewRange'][0]))
            self.__viewbox.sigYRangeChanged.emit(
                self.__viewbox, tuple(self.__viewbox.state['viewRange'][1]))
            self.__viewbox.sigRangeChanged.emit(
                self.__viewbox, self.__viewbox.state['viewRange'])

        if self.__transformations.updownflip != updownflip:
            self.__transformations.updownflip = updownflip
            self.__viewbox.invertY(updownflip)
            # workaround for a bug in old pyqtgraph versions: stretch 0.9.10
            self.__viewbox.sigXRangeChanged.emit(
                self.__viewbox, tuple(self.__viewbox.state['viewRange'][0]))
            self.__viewbox.sigYRangeChanged.emit(
                self.__viewbox, tuple(self.__viewbox.state['viewRange'][1]))
            self.__viewbox.sigRangeChanged.emit(
                self.__viewbox, self.__viewbox.state['viewRange'])

    def transformations(self):
        """ povides coordinates transformations

        :returns: transpose, leftrightflip, updownflip flags
        :rtype: (:obj:`bool`, :obj:`bool`, :obj:`bool`)
        """
        return (
            self.__transformations.transpose,
            self.__transformations.leftrightflip,
            self.__transformations.updownflip)

    def __transposeItems(self):
        """ transposes all image items
        """
        for ext in self.__extensions.values():
            ext.transpose()
        self.__transposeAxes()

    def __transposeAxes(self):
        """ transposes axes
        """
        if self.__axes.enabled is True:
            self.__setScale(self.__axes.position, self.__axes.scale)
        if self.__polaraxes.enabled is True:
            self.__setScale(
                self.__polaraxes.position, self.__polaraxes.scale, polar=True)

    def autoRange(self):
        """ sets auto range
        """
        self.__viewbox.autoRange()
        self.__viewbox.enableAutoRange('xy', True)

    def setrgb(self, status=True):
        """ sets RGB on/off

        :param status: True for on and False for off
        :type status: :obj:`bool`
        """
        self.__rgb = status

    def rgb(self):
        """ gets RGB on/off

        :returns: True for on and False for off
        :rtype: :obj:`bool`
        """
        return self.__rgb
