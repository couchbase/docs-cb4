#/bin/bash -e

echo "building draft documentation"

# get full directory name of the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# set up input directory
INDIR="$DIR"

echo "build directory = $DIR"
echo "input directory = $INDIR"

# set up output directory and DITA-OT path
if [ "$1" == "local" ]; then
	echo "setting up for local build"
	OUTDIR="/Library/WebServer/Documents"
	DITAOT="/Applications/DITA-OT2.0.1"
else
	echo "setting up for draft server build"
	OUTDIR=/home/docs/public_html/draft
	# get name of parent directory 
	PARENT="$(dirname "$DIR")"
	# append name of dita-ot directory to parent directory
	DITAOT="$PARENT/DITA-OT2.0.1"
fi

echo "output directory = $OUTDIR"
echo "dita ot directory = $DITAOT"

# delete previously built documentation
echo "deleting old output files"
rm -rf $OUTDIR/*

# Pull latest docs
echo "getting latest files from GitHub"
cd $INDIR
git pull

# copy home page over
echo "copying home page & assets"
cp index.html $OUTDIR
cp draft.css $OUTDIR

# Pull latest dita plugin from GitHub repo
echo "updating DITA plug-in"
cd $DITAOT/plugins/com.couchbase.docs.html-draft
git pull

# go back to the dita-ot directory
echo "starting DITA build"
cd $DITAOT

# Hack to startcmd without losing shell
SHELL="echo" . startcmd.sh

# Integrate any plugin updates
ant -f integrator.xml

# build server guide
echo "building server guide"
./bin/dita -f com.couchbase.docs.html-draft -i $INDIR/content/cb4.ditamap -o $OUTDIR/4.0

echo "draft documentation build complete"

 