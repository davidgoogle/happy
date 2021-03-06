#!/usr/bin/env python

#
#    Copyright (c) 2016-2017 Nest Labs, Inc.
#    All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

##
#    @file
#       A Happy command line utility through which a virtual node run tcpkill.
#
#       The command is executed by instantiating and running HappyNodeTcpReset class.
#

import getopt
import sys

import happy.HappyNodeTcpReset
from happy.Utils import *

if __name__ == "__main__":
    options = happy.HappyNodeTcpReset.option()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:qfp:P:s:d:",
                                   ["help", "id=", "quiet", "interface=", "isp=", "dstPort=", "start=", "duration="])

    except getopt.GetoptError as err:
        print happy.HappyNodeTcpReset.HappyNodeTcpReset.__doc__
        print hred(str(err))
        sys.exit(hred("%s: Failed to parse arguments." % (__file__)))

    for o, a in opts:
        if o in ("-h", "--help"):
            print happy.HappyNodeTcpReset.HappyNodeTcpReset.__doc__
            sys.exit(0)

        elif o in ("-q", "--quiet"):
            options["quiet"] = True

        elif o in ("-i", "--id"):
            options["node_id"] = a

        elif o in ("-f", "--interface"):
            options["interface"] = a

        elif o in ("-p", "--isp"):
            options["isp"] = a

        elif o in ("-P", "--dstPort"):
            options["dstPort"] = int(a)

        elif o in ("-s", "--start"):
            options["start"] = int(a)

        elif o in ("-d", "--duration"):
            options["duration"] = int(a)

        else:
            assert False, "unhandled option"

    cmd = happy.HappyNodeTcpReset.HappyNodeTcpReset(options)
    cmd.start()
