# Simple SSTable class that stores int in sorted order
import struct

class SSTable:
    def __init__(self):
        self._file = None
        self._content = []
        self._pack_fmt = ">I"
        self._pack_fmt_len = struct.calcsize(self._pack_fmt)

    def load_file(self, file_name):
        assert file_name is not None
        assert self._file is None

        self._file = file_name
        with open(self._file, "rb") as fp:
            while True:
                key_pack = fp.read(self._pack_fmt_len)
                if not key_pack:
                    break
                key = struct.unpack(self._pack_fmt, key_pack)[0]
                if len(self._content) > 0:
                    assert key >= self._content[-1]
                self._content.append(key)

    def append(self, key=None):
        if len(self._content) > 0:
            assert key >= self._content[-1]
        self._content.append(key)

    def flush(self, file_name=None):
        if file_name:
            assert self._file is None
            self._file = file_name

        with open(self._file, "wb") as fp:
            for key in self._content:
                key_pack = struct.pack(self._pack_fmt, key)
                fp.write(key_pack)

    def __iter__(self):
        self._iter_idx = 0
        return self

    def next(self):
        assert self._iter_idx <= len(self._content)
        if self._iter_idx == len(self._content):
            raise StopIteration

        key = self._content[self._iter_idx]
        self._iter_idx += 1
        return key

