#!/bin/bash

terraform fmt -diff -write=true -list=true $@
