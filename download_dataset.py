import os
import argparse
import requests
import pyunpack

def download_dataset(data_path):
    """Downloads the img dataset.

    Args:
        data_path (str): Defines the path where the dataset will be
                         downloaded and extracted to.

    .. seealso:: The code for downloading files from google drive is based
                 on the solution provided at [https://bit.ly/2JSVgMQ].
    """
    if os.path.isfile("temp.rar")==False:
        url = "https://drive.google.com/uc?id=1Ihjy6yK_hATsQpgrU7a_MnvJXNGExyV5&export=download"
        session = requests.Session()
        response = session.get(url, stream=True)
        token = _get_confirm_token(response)

        if token:
            params = {"confirm": token}
            response = session.get(url, params=params, stream=True)
        _save_response_content(response,"temp.rar")
        
    else:
        print("dataset file exist")
        
    # require pyunpack
    os.makedirs(data_path, exist_ok=True)
    #desination = 
    print("Extracting dataset:...")
    pyunpack.Archive("temp.rar").extractall(data_path)
    print("Done")
    #os.remove("temp.rar")
    
def _save_response_content(response, file_path):
    chunk_size = 32768
    with open(file_path, "wb") as data:
        for chunk in response.iter_content(chunk_size):
            if chunk:
                data.write(chunk)
def _get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith("download_warning"):
            return value

    return None
if __name__=="__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-d", "--datapath",
                        help="Defines the path where the dataset will be \
                         downloaded and extracted to")
    args = parser.parse_args()
    print("Downloading dataset:...")
    download_dataset(args.datapath)