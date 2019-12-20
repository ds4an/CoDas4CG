#!/bin/bash
set -e

CLASSPATH="lib:lib/stanford-parser/stanford-parser.jar:lib/stanford-parser/stanford-parser-3.5.1-models.jar:lib/easyccg/easyccg.jar"
javac -cp $CLASSPATH lib/*.java
