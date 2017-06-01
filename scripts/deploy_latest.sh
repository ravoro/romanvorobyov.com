#!/bin/bash
# Script for deploying the latest code in the repo.

# Date variable used for distinguishing files by time between different deploys
DATE="$(date +%Y%m%d-%s)"

# Base project directory
BASE_DIR="/var/www"

# Directory with website content (the directory that will be renewed)
SITE_DIR="${BASE_DIR}/public_html"

# Directory that will store backup of current version of the site
BACKUP_DIR="${BASE_DIR}/backups"

# Directory that will store (trash) the old version of site after deploy
TRASH_DIR="/tmp/site-deploy-trash/${DATE}"

# Directory that will temporarily store the new website content as it is being built
TMP_DIR="${BASE_DIR}/public_html_tmp"

# Git repo containing code that will be deployed
GIT_REPO="https://github.com/ravoro/romanvorobyov.com.git"


if [ ! -d ${BASE_DIR} ]; then
    echo "The specified project directory (${BASE_DIR}) does not exist."
    exit
fi
cd ${BASE_DIR}


echo -e "\nFetching latest code from repo ..."
git clone ${GIT_REPO} --depth 1 ${TMP_DIR}
/bin/rm -rf ${TMP_DIR}/.git


echo -e "\nSetting up virtualenv and fetching requirements ..."
virtualenv -p python3 ${TMP_DIR}/venv
source ${TMP_DIR}/venv/bin/activate
pip install -r ${TMP_DIR}/requirements.txt
deactivate


echo -e "\nCreating tgz backup of current version of site ..."
tar czf "${BACKUP_DIR}/public_html-${DATE}.tgz" ${SITE_DIR}


echo -e "\nTrashing current version of the site ..."
mkdir -p ${TRASH_DIR}
mv ${SITE_DIR} ${TRASH_DIR}


echo -e "\nEnabling new version of the website ..."
mv ${TMP_DIR} ${SITE_DIR}


echo -e "\nDeployment done!"
