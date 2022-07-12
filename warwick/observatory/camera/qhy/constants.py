#
# This file is part of qhy-camd
#
# qhy-camd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qhy-camd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qhy-camd.  If not, see <http://www.gnu.org/licenses/>.

"""Constants and status codes used by qhy-camd"""

# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

from warwick.observatory.common import TFmt


class CommandStatus:
    """Numeric return codes"""
    # General error codes
    Succeeded = 0
    Failed = 1
    Blocked = 2
    InvalidControlIP = 3

    CameraNotFound = 5

    # Command-specific codes
    CameraNotInitialized = 10
    CameraNotIdle = 11
    CameraNotUninitialized = 14
    CameraNotAcquiring = 15

    TemperatureOutsideLimits = 20
    WindowOutsideCCD = 32

    _messages = {
        # General error codes
        1: 'error: command failed',
        2: 'error: another command is already running',
        3: 'error: command not accepted from this IP',
        5: 'error: camera hardware not found',

        # Command-specific codes
        10: 'error: camera has not been initialized',
        11: 'error: camera is not idle',
        14: 'error: camera has already been initialized',
        15: 'error: camera is not acquiring',

        20: 'error: requested temperature is outside the supported limits',
        32: 'error: window extends outside the bounds of the ccd',

        -100: 'error: terminated by user',
        -101: 'error: unable to communicate with camera daemon',
    }

    @classmethod
    def message(cls, error_code):
        """Returns a human readable string describing an error code"""
        if error_code in cls._messages:
            return cls._messages[error_code]
        return 'error: Unknown error code {}'.format(error_code)


class CameraStatus:
    """Status of the camera hardware"""
    # Note that the Reading status is assumed at status-query time
    # and is never assigned to CameraDaemon._status
    Disabled, Initializing, Idle, Waiting, Acquiring, Reading, Aborting = range(7)

    _labels = {
        0: 'OFFLINE',
        1: 'INITIALIZING',
        2: 'IDLE',
        3: 'WAITING',
        4: 'EXPOSING',
        5: 'READING',
        6: 'ABORTING'
    }

    _formats = {
        0: TFmt.Red + TFmt.Bold,
        1: TFmt.Red + TFmt.Bold,
        2: TFmt.Bold,
        3: TFmt.Yellow + TFmt.Bold,
        4: TFmt.Green + TFmt.Bold,
        5: TFmt.Yellow + TFmt.Bold,
        6: TFmt.Red + TFmt.Bold
    }

    @classmethod
    def label(cls, status, formatting=False):
        """
        Returns a human readable string describing a status
        Set formatting=true to enable terminal formatting characters
        """
        if formatting:
            if status in cls._formats and status in cls._formats:
                return cls._formats[status] + cls._labels[status] + TFmt.Clear
            return TFmt.Red + TFmt.Bold + 'UNKNOWN STATUS' + TFmt.Clear

        if status in cls._labels:
            return cls._labels[status]
        return 'UNKNOWN STATUS'


class CoolerMode:
    """Camera temperature control mode"""
    Unknown, Warm, Warming, Cooling, Locking, Locked, UVLOError = range(7)

    _labels = {
        0: 'UNKNOWN',
        1: 'WARM',
        2: 'WARMING',
        3: 'COOLING',
        4: 'LOCKING',
        5: 'LOCKED',
        6: 'UVLO ERROR'
    }

    _formats = {
        0: TFmt.Red + TFmt.Bold,
        1: TFmt.Red + TFmt.Bold,
        2: TFmt.Yellow + TFmt.Bold,
        3: TFmt.Cyan + TFmt.Bold,
        4: TFmt.Yellow + TFmt.Bold,
        5: TFmt.Green + TFmt.Bold,
        6: TFmt.Red + TFmt.Bold
    }

    @classmethod
    def label(cls, status, formatting=False):
        """
        Returns a human readable string describing a status
        Set formatting=true to enable terminal formatting characters
        """
        if formatting:
            if status in cls._formats and status in cls._formats:
                return cls._formats[status] + cls._labels[status] + TFmt.Clear
            return TFmt.Red + TFmt.Bold + 'UNKNOWN' + TFmt.Clear

        if status in cls._labels:
            return cls._labels[status]
        return 'UNKNOWN'
