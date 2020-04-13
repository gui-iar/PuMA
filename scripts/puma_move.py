#!/usr/bin/env python2
## puma_reduc

#Author: Santiago del Palacio for PuMA
#Date: April 2020

import os
import sys
import argparse
from pugliS_utils import *

from ConfigParser import SafeConfigParser
import glob
import sigproc
import subprocess


# --------------------------------------------------------
#                        IDEAS
# --------------------------------------------------------
# 07/02/2020
# Treat each observation data as a python class such as:
# raw-data, mask, pfd, observation-data for glitches and
# more.
# Advantages: easy to access once its created and store in
# different formats (hdf5)
# --------------------------------------------------------


def set_argparse():
    # add arguments
    parser = argparse.ArgumentParser(prog='puma_move.py',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            description='moving observations to reduction folder')
    parser.add_argument('--obs_folder', default=os.environ['PWD'], type=str,
            help='ABSOLUTE PATH to folder containing all the folders for each specific observation')
    parser.add_argument('--dest_path', default='/home/jovyan/work/shared/', type=str,
            help='path to directory containing all the observations for reduction')

    return parser.parse_args()


def check_cli_arguments(args):

    ierr = 0

    if os.path.isabs(args.obs_folder) is False:
        print('\n FATAL ERROR: observation folder path is not absolute\n')
        ierr = -1
        return ierr

    if os.path.isabs(args.dest_path) is False:
        print('\n FATAL ERROR: destination folder path is not absolute\n')
        ierr = -1
        return ierr


    return ierr


if __name__ == '__main__':

    # get cli-arguments
    args = set_argparse()

    # check arguments
    ierr = check_cli_arguments(args)
    if ierr != 0: sys.exit(1)
    
    print('\n Start moving folders')

    ierr = move_observations(obs_folder=args.obs_folder, dest_path=args.dest_path)

    if ierr != 0: sys.exit(1)
	
    print('\n Finished moving folders')
