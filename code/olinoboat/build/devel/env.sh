#!/usr/bin/env sh
# generated from catkin/cmake/templates/env.sh.in

if [ $# -eq 0 ] ; then
  /bin/echo "Entering environment at '/home/bradpowers/groovy_workspace/sandbox/olinoboat/code/olinoboat/build/devel', type 'exit' to leave"
  . "/home/bradpowers/groovy_workspace/sandbox/olinoboat/code/olinoboat/build/devel/setup.sh"
  "$SHELL" -i
  /bin/echo "Exiting environment at '/home/bradpowers/groovy_workspace/sandbox/olinoboat/code/olinoboat/build/devel'"
else
  . "/home/bradpowers/groovy_workspace/sandbox/olinoboat/code/olinoboat/build/devel/setup.sh"
  exec "$@"
fi
