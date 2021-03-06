"""autogenerated by genpy from vector_slam_msgs/CobotStatusMsg.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class CobotStatusMsg(genpy.Message):
  _md5sum = "4e8dff9d792649b915399841b6e125a2"
  _type = "vector_slam_msgs/CobotStatusMsg"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header

float64 timestamp

float32 loc_x
float32 loc_y
float32 orientation

float32[] particles_x
float32[] particles_y
float32[] particles_weight
float32[] locations_weight

uint16 currentNavCommand
float32 obsAvDir_x
float32 obsAvDir_y
bool pathBlocked

float32 batteryVoltage
bool emergencyStop

# Cobot Operation modes:
# 0 = JoystickMode
# 1 = JoystickObstAvMode
# 2 = MotionPrimitiveMode
# 3 = MotionPrimitiveObstAvMode
# 4 = TeleOpMode
# 5 = TestMode
# 6 = AllStopMode
int16 cobotMode

# Cobot Commands:
# 0 = NavCmdNone
# 1 = NavCmdGoTo
# 2 = NavCmdMoveStraight
# 3 = NavCmdMoveDownCorridor
# 4 = NavCmdIntegratedTurn
# 5 = NavCmdInPlaceTurn
# 6 = NavCmdTurnAndMoveStraight
# 7 = NavCmdAbort
int16 currentCommand
bool navComplete

int32 currentEdge
float32 edgeProgress
float32 edgeRemaining
float64 edgeNavDuration

float32[] pathPlan_x
float32[] pathPlan_y

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

"""
  __slots__ = ['header','timestamp','loc_x','loc_y','orientation','particles_x','particles_y','particles_weight','locations_weight','currentNavCommand','obsAvDir_x','obsAvDir_y','pathBlocked','batteryVoltage','emergencyStop','cobotMode','currentCommand','navComplete','currentEdge','edgeProgress','edgeRemaining','edgeNavDuration','pathPlan_x','pathPlan_y']
  _slot_types = ['std_msgs/Header','float64','float32','float32','float32','float32[]','float32[]','float32[]','float32[]','uint16','float32','float32','bool','float32','bool','int16','int16','bool','int32','float32','float32','float64','float32[]','float32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,timestamp,loc_x,loc_y,orientation,particles_x,particles_y,particles_weight,locations_weight,currentNavCommand,obsAvDir_x,obsAvDir_y,pathBlocked,batteryVoltage,emergencyStop,cobotMode,currentCommand,navComplete,currentEdge,edgeProgress,edgeRemaining,edgeNavDuration,pathPlan_x,pathPlan_y

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CobotStatusMsg, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.timestamp is None:
        self.timestamp = 0.
      if self.loc_x is None:
        self.loc_x = 0.
      if self.loc_y is None:
        self.loc_y = 0.
      if self.orientation is None:
        self.orientation = 0.
      if self.particles_x is None:
        self.particles_x = []
      if self.particles_y is None:
        self.particles_y = []
      if self.particles_weight is None:
        self.particles_weight = []
      if self.locations_weight is None:
        self.locations_weight = []
      if self.currentNavCommand is None:
        self.currentNavCommand = 0
      if self.obsAvDir_x is None:
        self.obsAvDir_x = 0.
      if self.obsAvDir_y is None:
        self.obsAvDir_y = 0.
      if self.pathBlocked is None:
        self.pathBlocked = False
      if self.batteryVoltage is None:
        self.batteryVoltage = 0.
      if self.emergencyStop is None:
        self.emergencyStop = False
      if self.cobotMode is None:
        self.cobotMode = 0
      if self.currentCommand is None:
        self.currentCommand = 0
      if self.navComplete is None:
        self.navComplete = False
      if self.currentEdge is None:
        self.currentEdge = 0
      if self.edgeProgress is None:
        self.edgeProgress = 0.
      if self.edgeRemaining is None:
        self.edgeRemaining = 0.
      if self.edgeNavDuration is None:
        self.edgeNavDuration = 0.
      if self.pathPlan_x is None:
        self.pathPlan_x = []
      if self.pathPlan_y is None:
        self.pathPlan_y = []
    else:
      self.header = std_msgs.msg.Header()
      self.timestamp = 0.
      self.loc_x = 0.
      self.loc_y = 0.
      self.orientation = 0.
      self.particles_x = []
      self.particles_y = []
      self.particles_weight = []
      self.locations_weight = []
      self.currentNavCommand = 0
      self.obsAvDir_x = 0.
      self.obsAvDir_y = 0.
      self.pathBlocked = False
      self.batteryVoltage = 0.
      self.emergencyStop = False
      self.cobotMode = 0
      self.currentCommand = 0
      self.navComplete = False
      self.currentEdge = 0
      self.edgeProgress = 0.
      self.edgeRemaining = 0.
      self.edgeNavDuration = 0.
      self.pathPlan_x = []
      self.pathPlan_y = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_d3f.pack(_x.timestamp, _x.loc_x, _x.loc_y, _x.orientation))
      length = len(self.particles_x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.particles_x))
      length = len(self.particles_y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.particles_y))
      length = len(self.particles_weight)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.particles_weight))
      length = len(self.locations_weight)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.locations_weight))
      _x = self
      buff.write(_struct_H2fBfB2hBi2fd.pack(_x.currentNavCommand, _x.obsAvDir_x, _x.obsAvDir_y, _x.pathBlocked, _x.batteryVoltage, _x.emergencyStop, _x.cobotMode, _x.currentCommand, _x.navComplete, _x.currentEdge, _x.edgeProgress, _x.edgeRemaining, _x.edgeNavDuration))
      length = len(self.pathPlan_x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.pathPlan_x))
      length = len(self.pathPlan_y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.pathPlan_y))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 20
      (_x.timestamp, _x.loc_x, _x.loc_y, _x.orientation,) = _struct_d3f.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.particles_x = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.particles_y = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.particles_weight = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.locations_weight = struct.unpack(pattern, str[start:end])
      _x = self
      start = end
      end += 41
      (_x.currentNavCommand, _x.obsAvDir_x, _x.obsAvDir_y, _x.pathBlocked, _x.batteryVoltage, _x.emergencyStop, _x.cobotMode, _x.currentCommand, _x.navComplete, _x.currentEdge, _x.edgeProgress, _x.edgeRemaining, _x.edgeNavDuration,) = _struct_H2fBfB2hBi2fd.unpack(str[start:end])
      self.pathBlocked = bool(self.pathBlocked)
      self.emergencyStop = bool(self.emergencyStop)
      self.navComplete = bool(self.navComplete)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.pathPlan_x = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.pathPlan_y = struct.unpack(pattern, str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_d3f.pack(_x.timestamp, _x.loc_x, _x.loc_y, _x.orientation))
      length = len(self.particles_x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.particles_x.tostring())
      length = len(self.particles_y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.particles_y.tostring())
      length = len(self.particles_weight)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.particles_weight.tostring())
      length = len(self.locations_weight)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.locations_weight.tostring())
      _x = self
      buff.write(_struct_H2fBfB2hBi2fd.pack(_x.currentNavCommand, _x.obsAvDir_x, _x.obsAvDir_y, _x.pathBlocked, _x.batteryVoltage, _x.emergencyStop, _x.cobotMode, _x.currentCommand, _x.navComplete, _x.currentEdge, _x.edgeProgress, _x.edgeRemaining, _x.edgeNavDuration))
      length = len(self.pathPlan_x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.pathPlan_x.tostring())
      length = len(self.pathPlan_y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.pathPlan_y.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 20
      (_x.timestamp, _x.loc_x, _x.loc_y, _x.orientation,) = _struct_d3f.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.particles_x = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.particles_y = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.particles_weight = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.locations_weight = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      _x = self
      start = end
      end += 41
      (_x.currentNavCommand, _x.obsAvDir_x, _x.obsAvDir_y, _x.pathBlocked, _x.batteryVoltage, _x.emergencyStop, _x.cobotMode, _x.currentCommand, _x.navComplete, _x.currentEdge, _x.edgeProgress, _x.edgeRemaining, _x.edgeNavDuration,) = _struct_H2fBfB2hBi2fd.unpack(str[start:end])
      self.pathBlocked = bool(self.pathBlocked)
      self.emergencyStop = bool(self.emergencyStop)
      self.navComplete = bool(self.navComplete)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.pathPlan_x = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.pathPlan_y = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_d3f = struct.Struct("<d3f")
_struct_3I = struct.Struct("<3I")
_struct_H2fBfB2hBi2fd = struct.Struct("<H2fBfB2hBi2fd")
