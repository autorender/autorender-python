# Uploads

Types:

```python
from autorender.types import Upload, UploadData
```

Methods:

- <code title="post /api/v1/uploads">client.uploads.<a href="./src/autorender/resources/uploads.py">create</a>(\*\*<a href="src/autorender/types/upload_create_params.py">params</a>) -> <a href="./src/autorender/types/upload.py">Upload</a></code>

# Files

Types:

```python
from autorender.types import (
    FileListItem,
    FileObject,
    FileListResponse,
    FileDeleteResponse,
    FileRenameResponse,
)
```

Methods:

- <code title="get /api/v1/files/{fileNo}">client.files.<a href="./src/autorender/resources/files.py">retrieve</a>(file_no) -> <a href="./src/autorender/types/file_object.py">FileObject</a></code>
- <code title="get /api/v1/files">client.files.<a href="./src/autorender/resources/files.py">list</a>(\*\*<a href="src/autorender/types/file_list_params.py">params</a>) -> <a href="./src/autorender/types/file_list_response.py">FileListResponse</a></code>
- <code title="delete /api/v1/files/{fileNo}">client.files.<a href="./src/autorender/resources/files.py">delete</a>(file_no) -> <a href="./src/autorender/types/file_delete_response.py">FileDeleteResponse</a></code>
- <code title="patch /api/v1/files/{fileNo}/rename">client.files.<a href="./src/autorender/resources/files.py">rename</a>(file_no, \*\*<a href="src/autorender/types/file_rename_params.py">params</a>) -> <a href="./src/autorender/types/file_rename_response.py">FileRenameResponse</a></code>

# Folders

Types:

```python
from autorender.types import (
    Folder,
    FolderListItem,
    FolderCreateResponse,
    FolderListResponse,
    FolderDeleteResponse,
)
```

Methods:

- <code title="post /api/v1/folders">client.folders.<a href="./src/autorender/resources/folders.py">create</a>(\*\*<a href="src/autorender/types/folder_create_params.py">params</a>) -> <a href="./src/autorender/types/folder_create_response.py">FolderCreateResponse</a></code>
- <code title="get /api/v1/folders">client.folders.<a href="./src/autorender/resources/folders.py">list</a>(\*\*<a href="src/autorender/types/folder_list_params.py">params</a>) -> <a href="./src/autorender/types/folder_list_response.py">FolderListResponse</a></code>
- <code title="delete /api/v1/folders/{folderNo}">client.folders.<a href="./src/autorender/resources/folders.py">delete</a>(folder_no) -> <a href="./src/autorender/types/folder_delete_response.py">FolderDeleteResponse</a></code>
- <code title="post /api/v1/folders/rename/{folderNo}">client.folders.<a href="./src/autorender/resources/folders.py">rename</a>(folder_no, \*\*<a href="src/autorender/types/folder_rename_params.py">params</a>) -> <a href="./src/autorender/types/folder.py">Folder</a></code>
