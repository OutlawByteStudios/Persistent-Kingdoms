if [ -d "Persistent Kingdoms" ]; then
  echo "cleaning previous build"
  rm -R Persistent\ Kingdoms/
fi
mkdir Persistent\ Kingdoms/
python -tt build_module.py -d
rm *.pyc
echo "build complete"
