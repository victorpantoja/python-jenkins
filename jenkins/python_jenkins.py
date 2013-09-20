# -*- coding: utf-8 -*-
from jenkins import Jenkins, JenkinsException
from optparse import OptionParser

import sys

#TODO - use setup.py
VERSION = "0.2.0"


def validate(options):
    if not options.url:
        raise JenkinsException("Missing Jenkins Server URL")

    if options.create_job:
        if not options.filename:
            print('You must provide a XML file.')

        if not options.filename or not options.job_name:
            raise JenkinsException("Missing job name")


def main(argv):
    parser = OptionParser(version=VERSION)

    parser.add_option("-c", "--create-job", dest="create_job",
                      help="Task to create a new job",
                      action="store_true")

    parser.add_option("-j", "--job-name", dest="job_name",
                      help="Job's name",
                      metavar="CREATE")

    parser.add_option("-f", "--file", dest="filename",
                      help="Path do jenkins config file",
                      metavar="FILE")

    parser.add_option("-u", "--url", dest="url",
                      help="Jenkins server URL",
                      metavar="FILE")

    options, _ = parser.parse_args()

    validate(options)

    ci = Jenkins(url=options.url)

    config = ""
    with open(options.filename, "r") as config_file:
        config = config_file.read()

    config_file.close()

    job_name = options.job_name

    if options.create_job:
        ci.create_job(job_name, config)


if __name__ == "__main__":
    main(sys.argv[1:])
