# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pydata_shiv/prediction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pydata_shiv/prediction.proto',
  package='pydata_shiv',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1cpydata_shiv/prediction.proto\x12\x0bpydata_shiv\"!\n\x11PredictionRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\"h\n\nPrediction\x12,\n\x05label\x18\x01 \x01(\x0e\x32\x1d.pydata_shiv.Prediction.Label\x12\x12\n\nconfidence\x18\x02 \x01(\x02\"\x18\n\x05Label\x12\x07\n\x03YES\x10\x00\x12\x06\n\x02NO\x10\x01\x32Y\n\x11PredictionService\x12\x44\n\x07Predict\x12\x1e.pydata_shiv.PredictionRequest\x1a\x17.pydata_shiv.Prediction\"\x00\x62\x06proto3')
)



_PREDICTION_LABEL = _descriptor.EnumDescriptor(
  name='Label',
  full_name='pydata_shiv.Prediction.Label',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='YES', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=160,
  serialized_end=184,
)
_sym_db.RegisterEnumDescriptor(_PREDICTION_LABEL)


_PREDICTIONREQUEST = _descriptor.Descriptor(
  name='PredictionRequest',
  full_name='pydata_shiv.PredictionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='pydata_shiv.PredictionRequest.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=78,
)


_PREDICTION = _descriptor.Descriptor(
  name='Prediction',
  full_name='pydata_shiv.Prediction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='pydata_shiv.Prediction.label', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='pydata_shiv.Prediction.confidence', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREDICTION_LABEL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=184,
)

_PREDICTION.fields_by_name['label'].enum_type = _PREDICTION_LABEL
_PREDICTION_LABEL.containing_type = _PREDICTION
DESCRIPTOR.message_types_by_name['PredictionRequest'] = _PREDICTIONREQUEST
DESCRIPTOR.message_types_by_name['Prediction'] = _PREDICTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PredictionRequest = _reflection.GeneratedProtocolMessageType('PredictionRequest', (_message.Message,), dict(
  DESCRIPTOR = _PREDICTIONREQUEST,
  __module__ = 'pydata_shiv.prediction_pb2'
  # @@protoc_insertion_point(class_scope:pydata_shiv.PredictionRequest)
  ))
_sym_db.RegisterMessage(PredictionRequest)

Prediction = _reflection.GeneratedProtocolMessageType('Prediction', (_message.Message,), dict(
  DESCRIPTOR = _PREDICTION,
  __module__ = 'pydata_shiv.prediction_pb2'
  # @@protoc_insertion_point(class_scope:pydata_shiv.Prediction)
  ))
_sym_db.RegisterMessage(Prediction)



_PREDICTIONSERVICE = _descriptor.ServiceDescriptor(
  name='PredictionService',
  full_name='pydata_shiv.PredictionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=186,
  serialized_end=275,
  methods=[
  _descriptor.MethodDescriptor(
    name='Predict',
    full_name='pydata_shiv.PredictionService.Predict',
    index=0,
    containing_service=None,
    input_type=_PREDICTIONREQUEST,
    output_type=_PREDICTION,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PREDICTIONSERVICE)

DESCRIPTOR.services_by_name['PredictionService'] = _PREDICTIONSERVICE

# @@protoc_insertion_point(module_scope)