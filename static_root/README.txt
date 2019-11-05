This directory is where django's collectstatic command will deposit all the static files
for this app.

This file must exist otherwise the directory would be empty, and git doesn't recognize
empty directories. Only files committed to the git repo will be recognized by heroku
in deployment.