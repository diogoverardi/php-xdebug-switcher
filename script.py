import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[0;32m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

action 	= int(sys.argv[1]) 
files 	= [
  '/Applications/MAMP/bin/php/php7.1.32/conf/php.ini',
  '/Applications/MAMP/conf/php7.1.32/php.ini'
]
xdebug_lines_to_add = [
  '[xdebug]',
  'zend_extension="/Applications/MAMP/bin/php/php7.1.32/lib/php/extensions/no-debug-non-zts-20160303/xdebug.so"',
  'xdebug.coverage_enable=1',
  'xdebug.default_enable=1',
  'xdebug.profiler_enable=1',
  'xdebug.profiler_output_dir="/tmp"',
  'xdebug.remote_autostart=1',
  'xdebug.remote_enable=1',
  'xdebug.remote_host=localhost',
  'xdebug.remote_port=9000'
]

if action==0:
  print(f"{bcolors.BOLD}----------DISABLE MODE----------{bcolors.ENDC}")
elif action==1:
  print(f"{bcolors.BOLD}----------ENABLE MODE----------{bcolors.ENDC}")
    
for file in files:
  with open(file, "r") as f:
    lines = f.readlines()

  if action==0:

    already_disabled=True
    
    with open(file, "w") as f:
      for line in lines:
        if line.strip("\n") == "[xdebug]":
          already_disabled=False
          break
        f.write(line)
        
    if already_disabled:        
        print(f"{bcolors.FAIL}XDebug already disabled, nothing was modified! {bcolors.ENDC}")
    else:
      print(f"{bcolors.OKGREEN}Removing all XDebug references on file: '%s' {bcolors.ENDC}" % file)
      print(f"{bcolors.BOLD}Restart PHP so changes take effect{bcolors.ENDC}")
        
  elif action==1:

    with open(file, "r") as f:
      lines = f.readlines()
      for line in lines:
          if line.strip("\n") == "[xdebug]":
            print(f"{bcolors.FAIL}XDebug reference found on this file: '%s' {bcolors.ENDC}" % file)
            print(f"{bcolors.FAIL}Nothing was modified!{bcolors.ENDC}")
            sys.exit()
            
    print(f"{bcolors.OKGREEN}Enabling XDebug on file: '%s' {bcolors.ENDC}" % file)
    print(f"{bcolors.BOLD}Restart PHP so changes take effect{bcolors.ENDC}")
    with open(file, "a") as f:  
      for line_to_add in xdebug_lines_to_add:
        f.write(line_to_add + '\n')

  else:
    print(f"{bcolors.FAIL}Nothing was modified! argument should be either 1 or 0{bcolors.ENDC}")
