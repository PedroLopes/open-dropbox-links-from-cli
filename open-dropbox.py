from urllib import parse as urlparse
import subprocess
import sys

dropbox_home = "https://dropbox.com/home"

dir = sys.argv[1]
dir_parsed = urlparse.quote(dir)
dir_suffix = dir_parsed.split("Dropbox")[1]
final_url = dropbox_home + dir_suffix

print(final_url)
subprocess.call("open " + final_url , shell=True)

