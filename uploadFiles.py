import dropbox

class TransferData:
    for root,dirs,files in os.walk(fileFrom):
        relative_path=os.path.relpath(local_pah,file_from)
        drapbox_path=os.path.join(file_to,relative_path)

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='GJRwi-2uji8AAAAAAAAAAXeE-2LXN2tTLQzI3J9vAHyPgppR8qj-xWrwXKDdDpbF'
    transferData=TransferData(access_token)
    file_from=input('Enter The File Path TO Transfer-')
    file_to =input('Enter The Full Path To Upload To Dropbox')

    transferData.upload_file(file_from,file_to)
    print('File Has Been Moved')

main()