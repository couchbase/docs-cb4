#!/bin/bash

DOC_PROJECT=$1 # should be <REPO_ROOT>/analytics/cbas/doc

[ -f $DOC_PROJECT/pom.xml ] || {
  echo "$DOC_PROJECT not valid (does not contain a pom.xml)"
  exit 1
}

for FILE in Gemfile _config.yml
do
  [ -f $FILE ] || {
    echo required file $FILE missing
    exit 1
  }
done

MD_DIR=$DOC_PROJECT/target/markdown/

echo '*** copy files from' $MD_DIR

rsync -r $MD_DIR .

echo '*** clean _site'

rm -rf _site/*

echo '*** run jekyll'

bundle exec jekyll b

echo '*** fix HTML ***'

for FILE in $(find . -name "*.html")
do
  # remove the first <h1> tag in the body
  awk 'NR==1,/<h1.*\/h1>/{sub(/<h1.*\/h1>/, "<!-- 1st <h1> removed -->")} 1' $FILE > tmp
  #echo "******** $FILE"
  mv tmp $FILE
done

echo '*** move generated files'

rsync -r _site/* ..

git st
