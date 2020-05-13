import os

def get_mp3_files(dirname):
    mp3_files = []
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            if filename[-4:] == ".mp3":
                mp3_files.append(os.path.join(root, filename))
    return mp3_files


get_mp3_files(dirname='.')



def check_duplicates(list_files):
    checksum_dict = {}

    for a_file in list_files:
        checksum = os.open('md5sum ' + a_file)
        res = checksum.read()
        checksum.close()

        if res in checksum_dict:
            print ("There's a duplicate!")
            print (a_file + " \ " + checksum_dict[res])
        else:
            checksum_dict[res] = a_file