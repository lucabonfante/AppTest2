Flask on OpenShift
==================

This git repository helps you get up and running quickly w/ a Flask installation
on OpenShift.


Running on OpenShift
----------------------------

Create an account at https://www.openshift.com

### Via Openshift web console

[![Launch on OpenShift](http://launch-shifter.rhcloud.com/launch/light/Click to install.svg)](https://openshift.redhat.com/app/console/application_type/custom?&cartridges[]=python-2.6&initial_git_url=https://github.com/openshift/flask-example.git&name=flask)

### Via rhc & git

Create a python application

    rhc app create flask python-2.6

Add this upstream flask repo

    cd flask
    git remote add upstream -m master https://github.com/openshift/flask-example.git
    git pull -s recursive -X theirs upstream master
    
Then push the repo upstream

    git push

That's it, you can now checkout your application at:

    http://flask-$yournamespace.rhcloud.com

------------------------------

To get more log messages in your OpenShift logs please add the following line to your code

    app.config['PROPAGATE_EXCEPTIONS'] = True

To read more about logging in Flask please see this email

http://librelist.com/browser//flask/2012/1/27/catching-exceptions-from-flask/
