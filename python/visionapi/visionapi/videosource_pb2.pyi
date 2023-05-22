from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoFrame(_message.Message):
    __slots__ = ["source_id", "timestamp_utc_ms", "shape", "frame_data"]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_UTC_MS_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    FRAME_DATA_FIELD_NUMBER: _ClassVar[int]
    source_id: bytes
    timestamp_utc_ms: int
    shape: Shape
    frame_data: bytes
    def __init__(self, source_id: _Optional[bytes] = ..., timestamp_utc_ms: _Optional[int] = ..., shape: _Optional[_Union[Shape, _Mapping]] = ..., frame_data: _Optional[bytes] = ...) -> None: ...

class Shape(_message.Message):
    __slots__ = ["height", "width", "channels"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    height: int
    width: int
    channels: int
    def __init__(self, height: _Optional[int] = ..., width: _Optional[int] = ..., channels: _Optional[int] = ...) -> None: ...
