# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: glossary.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'glossary.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eglossary.proto\x12\x08glossary\x1a\x1bgoogle/protobuf/empty.proto\"(\n\x04Term\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"9\n\x19\x43reateOrUpdateTermRequest\x12\x1c\n\x04term\x18\x01 \x01(\x0b\x32\x0e.glossary.Term\",\n\x0cTermResponse\x12\x1c\n\x04term\x18\x01 \x01(\x0b\x32\x0e.glossary.Term\"\x1d\n\x0eTermKeyRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"2\n\x11TermsListResponse\x12\x1d\n\x05terms\x18\x01 \x03(\x0b\x32\x0e.glossary.Term2\xe6\x02\n\x0fGlossaryService\x12I\n\nCreateTerm\x12#.glossary.CreateOrUpdateTermRequest\x1a\x16.glossary.TermResponse\x12;\n\x07GetTerm\x12\x18.glossary.TermKeyRequest\x1a\x16.glossary.TermResponse\x12I\n\nUpdateTerm\x12#.glossary.CreateOrUpdateTermRequest\x1a\x16.glossary.TermResponse\x12>\n\nDeleteTerm\x12\x18.glossary.TermKeyRequest\x1a\x16.google.protobuf.Empty\x12@\n\tListTerms\x12\x16.google.protobuf.Empty\x1a\x1b.glossary.TermsListResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'glossary_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TERM']._serialized_start=57
  _globals['_TERM']._serialized_end=97
  _globals['_CREATEORUPDATETERMREQUEST']._serialized_start=99
  _globals['_CREATEORUPDATETERMREQUEST']._serialized_end=156
  _globals['_TERMRESPONSE']._serialized_start=158
  _globals['_TERMRESPONSE']._serialized_end=202
  _globals['_TERMKEYREQUEST']._serialized_start=204
  _globals['_TERMKEYREQUEST']._serialized_end=233
  _globals['_TERMSLISTRESPONSE']._serialized_start=235
  _globals['_TERMSLISTRESPONSE']._serialized_end=285
  _globals['_GLOSSARYSERVICE']._serialized_start=288
  _globals['_GLOSSARYSERVICE']._serialized_end=646
# @@protoc_insertion_point(module_scope)