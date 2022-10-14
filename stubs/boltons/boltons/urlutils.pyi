import ctypes
from _typeshed import Incomplete

from boltons.dictutils import OrderedMultiDict

unicode: Incomplete
unichr = chr
SCHEME_PORT_MAP: Incomplete
NO_NETLOC_SCHEMES: Incomplete

class URLParseError(ValueError): ...

DEFAULT_ENCODING: str

def to_unicode(obj): ...
def find_all_links(text, with_text: bool = ..., default_scheme: str = ..., schemes=...): ...
def quote_path_part(text, full_quote: bool = ...): ...
def quote_query_part(text, full_quote: bool = ...): ...
def quote_fragment_part(text, full_quote: bool = ...): ...
def quote_userinfo_part(text, full_quote: bool = ...): ...
def unquote(string, encoding: str = ..., errors: str = ...): ...
def unquote_to_bytes(string): ...
def register_scheme(text, uses_netloc: Incomplete | None = ..., default_port: Incomplete | None = ...) -> None: ...
def resolve_path_parts(path_parts): ...

class cachedproperty:
    __doc__: Incomplete
    func: Incomplete
    def __init__(self, func) -> None: ...
    def __get__(self, obj, objtype: Incomplete | None = ...): ...

class URL:
    scheme: Incomplete
    username: Incomplete
    password: Incomplete
    family: Incomplete
    host: Incomplete
    port: Incomplete
    path_parts: Incomplete
    fragment: Incomplete
    def __init__(self, url: str = ...) -> None: ...
    @classmethod
    def from_parts(
        cls,
        scheme: Incomplete | None = ...,
        host: Incomplete | None = ...,
        path_parts=...,
        query_params=...,
        fragment: str = ...,
        port: Incomplete | None = ...,
        username: Incomplete | None = ...,
        password: Incomplete | None = ...,
    ): ...
    def query_params(self): ...
    qp: Incomplete
    @property
    def path(self): ...
    @path.setter
    def path(self, path_text) -> None: ...
    @property
    def uses_netloc(self): ...
    @property
    def default_port(self): ...
    def normalize(self, with_case: bool = ...) -> None: ...
    def navigate(self, dest): ...
    def get_authority(self, full_quote: bool = ..., with_userinfo: bool = ...): ...
    def to_text(self, full_quote: bool = ...): ...
    def __unicode__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class _sockaddr(ctypes.Structure): ...

WSAStringToAddressA: Incomplete
WSAAddressToStringA: Incomplete

def parse_host(host): ...
def parse_url(url_text): ...

DEFAULT_PARSED_URL: Incomplete

def parse_qsl(qs, keep_blank_values: bool = ..., encoding=...): ...

PREV: Incomplete
NEXT: Incomplete
KEY: Incomplete
VALUE: Incomplete
SPREV: Incomplete
SNEXT: Incomplete

OMD = OrderedMultiDict

class QueryParamDict(OrderedMultiDict):
    @classmethod
    def from_text(cls, query_string): ...
    def to_text(self, full_quote: bool = ...): ...
