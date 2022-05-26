from ast import Bytes
from io import BytesIO
from .file_fetch import File_Fetch


class String_Fetch(File_Fetch):
    '''Fetches data from string'''
    def __init__(self, source:str, content_type:str=None, encoding='utf8', **kwargs):
        '''source - sequence of characters(string)\n
        content_type - content type for data in string\n
        **kwargs - optional keywords args to pass to base class(File_Fetch)
        '''
        bytes_file = BytesIO(source.encode(encoding=encoding))
        super().__init__(bytes_file, content_type, **kwargs)


if __name__ == "__main__":
    fetch_obj = String_Fetch("This is string", content_type=" .txt")
    print(fetch_obj.read())
    # b'This is string'
    print(fetch_obj.get_content_type())
    # text/plain

