# Uploads

Types:

```python
from autorender.types import Upload, UploadData, UploadGenerateTokenResponse
```

Methods:

- <code title="post /api/v1/uploads">client.uploads.<a href="./src/autorender/resources/uploads/uploads.py">create</a>(\*\*<a href="src/autorender/types/upload_create_params.py">params</a>) -> <a href="./src/autorender/types/upload.py">Upload</a></code>
- <code title="post /api/v1/uploads/remote">client.uploads.<a href="./src/autorender/resources/uploads/uploads.py">create_from_url</a>(\*\*<a href="src/autorender/types/upload_create_from_url_params.py">params</a>) -> <a href="./src/autorender/types/upload.py">Upload</a></code>
- <code title="post /api/v1/uploads/{token}">client.uploads.<a href="./src/autorender/resources/uploads/uploads.py">create_with_token</a>(token, body, \*\*<a href="src/autorender/types/upload_create_with_token_params.py">params</a>) -> <a href="./src/autorender/types/upload.py">Upload</a></code>
- <code title="post /api/v1/generate-token">client.uploads.<a href="./src/autorender/resources/uploads/uploads.py">generate_token</a>(\*\*<a href="src/autorender/types/upload_generate_token_params.py">params</a>) -> <a href="./src/autorender/types/upload_generate_token_response.py">UploadGenerateTokenResponse</a></code>

## Multipart

Types:

```python
from autorender.types.uploads import Session
```

Methods:

- <code title="post /api/v1/multipart/complete">client.uploads.multipart.<a href="./src/autorender/resources/uploads/multipart.py">complete</a>(\*\*<a href="src/autorender/types/uploads/multipart_complete_params.py">params</a>) -> <a href="./src/autorender/types/upload.py">Upload</a></code>
- <code title="post /api/v1/multipart/start">client.uploads.multipart.<a href="./src/autorender/resources/uploads/multipart.py">start</a>(\*\*<a href="src/autorender/types/uploads/multipart_start_params.py">params</a>) -> <a href="./src/autorender/types/uploads/session.py">Session</a></code>
- <code title="put /api/v1/multipart/parts">client.uploads.multipart.<a href="./src/autorender/resources/uploads/multipart.py">upload_part</a>(body, \*\*<a href="src/autorender/types/uploads/multipart_upload_part_params.py">params</a>) -> None</code>

# Files

Types:

```python
from autorender.types import (
    File,
    FileListItem,
    FileUpdateResponse,
    FileListResponse,
    FileDeleteResponse,
    FileRenameResponse,
)
```

Methods:

- <code title="get /api/v1/files/{fileNo}">client.files.<a href="./src/autorender/resources/files.py">retrieve</a>(file_no) -> <a href="./src/autorender/types/file.py">File</a></code>
- <code title="patch /api/v1/files/{fileNo}">client.files.<a href="./src/autorender/resources/files.py">update</a>(file_no, \*\*<a href="src/autorender/types/file_update_params.py">params</a>) -> <a href="./src/autorender/types/file_update_response.py">FileUpdateResponse</a></code>
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
