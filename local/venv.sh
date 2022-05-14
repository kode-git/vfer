DIR="./venv/"
if [ -d "$DIR" ]; then
  ### Take action if $DIR exists ###
  echo "Installing config files in ${DIR}..."
  source venv/bin/activate
else
  ###  Control will jump here if $DIR does NOT exists ###
  python3 -m venv venv
  source venv/bin/activate
fi

case "$OSTYPE" in
  solaris*) echo "Solaris system detected" ;;
  darwin*)  echo "OSX system detected" ;; 
  linux*)   echo "Linux system detected" ;;
  bsd*)     echo "BSD system detected" ;;
  msys*)    echo "Windows system detected" ;;
  cygwin*)  echo "Windows system detected" ;;
  *)        echo "unknown: $OSTYPE" ;;
esac

if [[ "$OSTYPE" == "msys" ]];
then
    ./venv/bin/activate
else 
    source venv/bin/activate
fi

pip install -r requirements.txt

