# Uploads

Types:

```python
from autorender.types import UploadCreateResponse, UploadCreateFromURLResponse
```

Methods:

- <code title="post /api/v1/uploads">client.uploads.<a href="./src/autorender/resources/uploads.py">create</a>(\*\*<a href="src/autorender/types/upload_create_params.py">params</a>) -> <a href="./src/autorender/types/upload_create_response.py">UploadCreateResponse</a></code>
- <code title="post /api/v1/uploads/remote">client.uploads.<a href="./src/autorender/resources/uploads.py">create_from_url</a>(\*\*<a href="src/autorender/types/upload_create_from_url_params.py">params</a>) -> <a href="./src/autorender/types/upload_create_from_url_response.py">UploadCreateFromURLResponse</a></code>

# Files

Types:

```python
from autorender.types import FileRetrieveResponse, FileListResponse, FileRenameResponse
```

Methods:

- <code title="get /api/v1/files/{fileNo}">client.files.<a href="./src/autorender/resources/files.py">retrieve</a>(file_no) -> <a href="./src/autorender/types/file_retrieve_response.py">FileRetrieveResponse</a></code>
- <code title="get /api/v1/files">client.files.<a href="./src/autorender/resources/files.py">list</a>(\*\*<a href="src/autorender/types/file_list_params.py">params</a>) -> <a href="./src/autorender/types/file_list_response.py">SyncPagePagination[FileListResponse]</a></code>
- <code title="delete /api/v1/files/{fileNo}">client.files.<a href="./src/autorender/resources/files.py">delete</a>(file_no) -> None</code>
- <code title="patch /api/v1/files/{fileNo}/rename">client.files.<a href="./src/autorender/resources/files.py">rename</a>(file_no, \*\*<a href="src/autorender/types/file_rename_params.py">params</a>) -> <a href="./src/autorender/types/file_rename_response.py">FileRenameResponse</a></code>

# Folders

Types:

```python
from autorender.types import FolderCreateResponse, FolderListResponse, FolderRenameResponse
```

Methods:

- <code title="post /api/v1/folders">client.folders.<a href="./src/autorender/resources/folders.py">create</a>(\*\*<a href="src/autorender/types/folder_create_params.py">params</a>) -> <a href="./src/autorender/types/folder_create_response.py">FolderCreateResponse</a></code>
- <code title="get /api/v1/folders">client.folders.<a href="./src/autorender/resources/folders.py">list</a>(\*\*<a href="src/autorender/types/folder_list_params.py">params</a>) -> <a href="./src/autorender/types/folder_list_response.py">FolderListResponse</a></code>
- <code title="delete /api/v1/folders/{folderNo}">client.folders.<a href="./src/autorender/resources/folders.py">delete</a>(folder_no) -> None</code>
- <code title="post /api/v1/folders/rename/{folderNo}">client.folders.<a href="./src/autorender/resources/folders.py">rename</a>(folder_no, \*\*<a href="src/autorender/types/folder_rename_params.py">params</a>) -> <a href="./src/autorender/types/folder_rename_response.py">FolderRenameResponse</a></code>

# MultipartUploads

Types:

```python
from autorender.types import MultipartUploadCompleteResponse, MultipartUploadStartResponse
```

Methods:

- <code title="post /api/v1/multipart/complete">client.multipart_uploads.<a href="./src/autorender/resources/multipart_uploads.py">complete</a>(\*\*<a href="src/autorender/types/multipart_upload_complete_params.py">params</a>) -> <a href="./src/autorender/types/multipart_upload_complete_response.py">MultipartUploadCompleteResponse</a></code>
- <code title="post /api/v1/multipart/start">client.multipart_uploads.<a href="./src/autorender/resources/multipart_uploads.py">start</a>(\*\*<a href="src/autorender/types/multipart_upload_start_params.py">params</a>) -> <a href="./src/autorender/types/multipart_upload_start_response.py">MultipartUploadStartResponse</a></code>
